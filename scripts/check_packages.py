"""Static package checks. These do not test ChatGPT Mil model behavior."""
from pathlib import Path, PurePosixPath
from io import BytesIO
import hashlib
import json
import re
import sys
import tempfile
import zipfile
from docx import Document
from docx.oxml.ns import qn

from build_packages import ROOT, VERSION, GUIDES, FORMS, REFERENCES, clean


def text(docx_bytes):
    doc=Document(BytesIO(docx_bytes))
    return '\n'.join(p.text for p in doc.paragraphs)


def normalize(s):
    return re.sub(r'\s+',' ',clean(s).replace('**','').replace('[ ] ','Check: ')).strip()


def source_coverage(source, actual):
    actual=normalize(actual)
    # Every non-table source paragraph/list/heading must survive conversion.
    for raw in source.splitlines():
        s=raw.strip()
        if not s or s.startswith(('```','|')): continue
        s=re.sub(r'^(#{1,6} |[-] |\d+\. )','',s)
        assert normalize(s) in actual, ('Missing source text',s[:100])
    for block in re.findall(r'(?m)^\|.*(?:\n\|.*)*',source):
        rows=block.splitlines()
        headers=[x.strip() for x in rows[0].strip('|').split('|')]
        if len(headers)>2:
            for header in headers:
                assert normalize(header) in actual, ('Missing field label',header)


def check(out):
    manifest=json.loads((out/'downloads/manifest.json').read_text())
    assert manifest['package_version']==VERSION
    contents={}
    for name,entry in manifest['packages'].items():
        p=out/'downloads'/name
        assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256']
        with zipfile.ZipFile(p) as z:
            assert z.testzip() is None
            assert z.namelist()==entry['files']
            assert len(set(z.namelist()))==len(z.namelist())
            contents[name]={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
        for n,data in contents[name].items():
            assert '..' not in PurePosixPath(n).parts and not n.startswith('/')
            assert n.endswith('.docx'),n
            with zipfile.ZipFile(BytesIO(data)) as z:
                assert z.testzip() is None
                assert not any('vbaProject' in x for x in z.namelist())
            d=Document(BytesIO(data));sec=d.sections[0]
            assert sec.page_width.twips==12240 and sec.page_height.twips==15840
            assert all(x.twips==1440 for x in (sec.left_margin,sec.right_margin,sec.top_margin,sec.bottom_margin))
            assert d.styles['Normal'].font.size.pt==11
            assert d.styles['Normal'].paragraph_format.line_spacing==1.25
            assert not d.tables  # Deliberate labeled-record layout, no tiny tables.
            assert '.md' not in text(data), ('Operator Markdown reference',n)
    pantons=contents['Pantons_Setup.zip'];generic=contents['First_Time_Squadron_Setup.zip'];update=contents['Update_Existing_Setup.zip']
    a='Pantons Scheduling Assistant/';b='Squadron Scheduling Assistant/'
    expected={'START HERE.docx','System/UPLOAD THIS TO START.docx'}
    expected.update('System/Instructions/'+n for _,n in GUIDES)
    expected.update('System/Blank Forms/'+n for _,n in FORMS)
    expected.update('System/Reference/'+n for _,n in REFERENCES)
    assert set(update)==expected|{'UPDATE INSTRUCTIONS.docx'}
    local={'Local Guidance/Local Profile.docx','Local Guidance/Stable References.docx','Local Guidance/Playbook.docx'}
    assert {n.removeprefix(a) for n in pantons}==expected|local
    assert {n.removeprefix(b) for n in generic}==expected|local
    for name in expected:
        assert pantons[a+name]==generic[b+name]==update[name],name
    for source,name in FORMS:
        source_coverage((ROOT/'templates/v0.4'/source).read_text(),text(update['System/Blank Forms/'+name]))
    gp=text(generic[b+'Local Guidance/Local Profile.docx'])
    assert 'DRAFT' in gp and 'three countable' not in gp and '8p8x4' not in gp
    source_coverage((ROOT/'local-profiles/pantons-v0.4.md').read_text(),text(pantons[a+'Local Guidance/Local Profile.docx']))
    primer=(ROOT/'docs/v0.4/system-primer.md').read_text().split('## START OF PRIMER',1)[1].split('## END OF PRIMER',1)[0]
    source_coverage(primer,text(update['System/UPLOAD THIS TO START.docx']))
    # Meaningful manual-update simulation: local rules, decisions and schedule
    # bytes survive; replacing the whole System also removes obsolete system files.
    with tempfile.TemporaryDirectory() as temp:
        base=Path(temp)
        with zipfile.ZipFile(out/'downloads/Pantons_Setup.zip') as z:z.extractall(base)
        install=base/'Pantons Scheduling Assistant'
        samples={'Local Guidance/Local Profile.docx':b'LOCAL APPROVED RULES',
                 'Week of 2099-01-04/Schedules/Published.xlsx':b'WEEKLY BASELINE',
                 'Week of 2099-01-04/Working Record/Decisions.docx':b'HUMAN DECISIONS'}
        for name,data in samples.items():
            p=install/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
        (install/'System/obsolete.docx').write_bytes(b'old')
        import shutil
        shutil.rmtree(install/'System')
        for name,data in update.items():
            if name=='UPDATE INSTRUCTIONS.docx':continue
            p=install/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
        assert not (install/'System/obsolete.docx').exists()
        for name,data in samples.items():assert (install/name).read_bytes()==data
        for name in ('Inputs','Schedules','Working Record'):
            assert (install/'COPY THIS FOLDER FOR EACH NEW WEEK'/name).is_dir()
    print('PASS: ZIP contents/integrity; Word geometry; common System; local-policy isolation; primer/profile coverage; manual update preservation.')


if __name__=='__main__':check(Path(sys.argv[1]))
