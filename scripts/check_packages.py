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

from build_packages import (
    ROOT, VERSION, GUIDES, FORMS, REFERENCES, PERSISTENT, WEEKLY_DIRS,
    MIGRATION_DOC, actionable_migrations, clean, persistent_migration_source,
    update_instructions_source,
)
from check_persistent_migrations import validate_current as validate_persistent


def text(docx_bytes):
    doc=Document(BytesIO(docx_bytes))
    return '\n'.join(p.text for p in doc.paragraphs)


def normalize(s):
    return re.sub(r'\s+',' ',clean(s).replace('**','').replace('[ ] ','Check: ')).strip()


def _table_row(line):
    return [v.strip().replace('\\|','|') for v in re.split(r'(?<!\\)\|',line.strip().strip('|'))]


def _table_blocks(source):
    lines=source.splitlines();i=0
    while i<len(lines):
        if not lines[i].strip().startswith('|'):
            i+=1;continue
        block=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            block.append(lines[i]);i+=1
        rows=[]
        for line in block:
            cells=_table_row(line)
            if all(re.fullmatch(r'\s*:?-+:?\s*',v) for v in cells):
                continue
            rows.append(cells)
        if rows:
            yield rows


def source_coverage(source, actual):
    """Require maintained prose, prompts, headers and meaningful table content."""
    actual=normalize(actual)
    for raw in source.splitlines():
        s=raw.strip()
        if not s or s.startswith(('```','|')): continue
        s=re.sub(r'^(#{1,6} |[-] |\d+\. )','',s)
        fragment=normalize(s)
        if fragment:
            assert fragment in actual, ('Missing source text',s[:140])
    for prompt in re.findall(r'```[^\n]*\n(.*?)\n```',source,re.S):
        fragment=normalize(prompt)
        if fragment:
            assert fragment in actual, ('Missing prompt content',fragment[:140])
    for rows in _table_blocks(source):
        width=len(rows[0])
        for row_index,row in enumerate(rows):
            assert len(row)==width, ('Ragged source table',row)
            # Two-column Markdown tables are deliberately rendered as definition
            # lists, so generic source headers are omitted. Their data rows must
            # survive. Wider record tables render and therefore verify headers.
            if width==2 and row_index==0:
                continue
            for cell in row:
                # Pure bracket placeholders are entry hints, not source facts. The
                # converter may consolidate repeated blank fields. Headers, row
                # labels and any fixed/meaningful cell text must still survive.
                if re.fullmatch(r'\[[^]]+\]',cell.strip()):
                    continue
                fragment=normalize(cell)
                if fragment:
                    assert fragment in actual, ('Missing source table cell',cell[:140])


def _migration_reference_entries():
    entries={}
    for item in actionable_migrations():
        for artifact in item['artifacts']:
            spec=PERSISTENT['artifacts'][artifact]
            if 'source' in spec:
                entries['Persistent Migration Sources/'+spec['migration_filename']]=spec['source']
    return entries


def check(out):
    validate_persistent()
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
            assert not d.tables
            assert '.md' not in text(data), ('Operator Markdown reference',n)
    pantons=contents['Pantons_Setup.zip'];generic=contents['First_Time_Squadron_Setup.zip'];update=contents['Update_Existing_Setup.zip']
    a='Pantons Scheduling Assistant/';b='Squadron Scheduling Assistant/'
    expected={'START HERE.docx','System/UPLOAD THIS TO START.docx'}
    expected.update('System/Instructions/'+n for _,n in GUIDES)
    expected.update('System/Blank Forms/'+n for _,n in FORMS)
    expected.update('System/Reference/'+n for _,n in REFERENCES)
    update_only={'UPDATE INSTRUCTIONS.docx'}
    migration_refs=_migration_reference_entries()
    if actionable_migrations():
        update_only.add(MIGRATION_DOC)
        update_only.update(migration_refs)
    assert set(update)==expected|update_only
    local={'Local Guidance/Local Profile.docx','Local Guidance/Stable References.docx','Local Guidance/Playbook.docx'}
    assert {n.removeprefix(a) for n in pantons}==expected|local
    assert {n.removeprefix(b) for n in generic}==expected|local
    for name in expected:
        assert pantons[a+name]==generic[b+name]==update[name],name

    source_coverage((ROOT/'packaging/guides/start.md').read_text(),text(update['START HERE.docx']))
    for source,name in GUIDES:
        source_coverage((ROOT/'packaging/guides'/source).read_text(),text(update['System/Instructions/'+name]))
    for source,name in FORMS:
        source_coverage((ROOT/'templates/v0.4'/source).read_text(),text(update['System/Blank Forms/'+name]))
    for source,name in REFERENCES:
        source_coverage((ROOT/source).read_text(),text(update['System/Reference/'+name]))
    source_coverage((ROOT/'templates/setup/local_profile_template.md').read_text(),text(generic[b+'Local Guidance/Local Profile.docx']))
    gp=text(generic[b+'Local Guidance/Local Profile.docx'])
    assert 'DRAFT' in gp and 'three countable' not in gp and '8p8x4' not in gp
    source_coverage((ROOT/'local-profiles/pantons-v0.4.md').read_text(),text(pantons[a+'Local Guidance/Local Profile.docx']))
    primer=(ROOT/'docs/v0.4/system-primer.md').read_text().split('## START OF PRIMER',1)[1].split('## END OF PRIMER',1)[0]
    intro='# Upload this to start\n\nThis is the assistant’s scheduling primer. Upload this document with current local guidance and sources, then paste the activation prompt in 02 Start a week.docx. These instructions are advisory and do not establish approval of a schedule.\n\n'
    source_coverage(intro+primer,text(update['System/UPLOAD THIS TO START.docx']))
    source_coverage(update_instructions_source(),text(update['UPDATE INSTRUCTIONS.docx']))
    if actionable_migrations():
        source_coverage(persistent_migration_source(),text(update[MIGRATION_DOC]))
        for name,source in migration_refs.items():
            source_coverage((ROOT/source).read_text(),text(update[name]))

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
            if name=='START HERE.docx' or name.startswith('System/'):
                p=install/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
        assert not (install/'System/obsolete.docx').exists()
        for name,data in samples.items():assert (install/name).read_bytes()==data
        for name in WEEKLY_DIRS:
            assert (install/'COPY THIS FOLDER FOR EACH NEW WEEK'/name).is_dir()
    print('PASS: ZIP integrity; Word geometry; full source coverage; common System; local-policy isolation; persistent-state declaration; manual update preservation.')


if __name__=='__main__':check(Path(sys.argv[1]))
