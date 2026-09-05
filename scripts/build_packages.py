"""Build the current Word-only operator ZIPs. Maintainer utility, not runtime software."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import platform
import re
import shutil
import zipfile

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / 'packaging/version.txt').read_text().strip()
PERSISTENT = json.loads((ROOT / 'packaging/persistent-artifacts.json').read_text())
REPRO = json.loads((ROOT / 'packaging/reproducibility.json').read_text())
WEEKLY_DIRS = PERSISTENT['artifacts']['weekly_folder_layout']['directories']
MIGRATION_DOC = 'PERSISTENT MIGRATIONS.docx'
METADATA_SENTINEL = '1980-01-01T00:00:00Z'
METADATA_TIMESTAMP = datetime.fromisoformat(REPRO.get('metadata_timestamp', '').replace('Z','+00:00')) if REPRO.get('metadata_timestamp') else None
ZIP_TIMESTAMP = ((METADATA_TIMESTAMP.year, METADATA_TIMESTAMP.month, METADATA_TIMESTAMP.day,
                  METADATA_TIMESTAMP.hour, METADATA_TIMESTAMP.minute, METADATA_TIMESTAMP.second)
                 if METADATA_TIMESTAMP else None)
GUIDES = [
    ('01-setup.md', '01 First time setup.docx'),
    ('02-start-week.md', '02 Start a week.docx'),
    ('03-phase-1.md', '03 Gather products.docx'),
    ('04-phase-2.md', '04 Review the draft.docx'),
    ('05-phase-3.md', '05 Schedule sell.docx'),
    ('06-phase-4.md', '06 Correct QC buy and publish.docx'),
    ('07-phase-5.md', '07 Execution reflows.docx'),
    ('08-handoff.md', '08 Hand off to another user.docx'),
    ('09-update.md', '09 Update next week.docx'),
    ('10-check.md', '10 Check the setup.docx'),
]
FORMS = [
    ('01_run_control_and_manifest.md','01 Run Control and Product Manifest.docx'),
    ('02_do_weekly_guidance.md','02 DO Weekly Guidance.docx'),
    ('03_flight_commander_input.md','03 Flight Commander Input.docx'),
    ('04_stable_local_rules_and_references.md','04 Stable References.docx'),
    ('05_retrospective_outcomes.md','05 Retrospective Outcomes.docx'),
    ('06_decision_and_release_record.md','06 Decision and Release Record.docx'),
    ('07_execution_update.md','07 Execution Update.docx'),
    ('08_session_handoff.md','08 Session Handoff.docx'),
    ('09_playbook.md','09 Playbook.docx'),
]
REFERENCES = [
    ('docs/v0.4/phase-guide.md', 'Phase Reference.docx'),
    ('docs/v0.4/report-contracts.md', 'Report Reference.docx'),
    ('docs/v0.4/validation-plan.md', 'Validation Plan.docx'),
    ('docs/data-handling.md', 'Data Handling.docx'),
    ('examples/v0.4/SYNTHETIC_weekly_cycle.md', 'SYNTHETIC Weekly Cycle.docx'),
    ('examples/v0.4/SYNTHETIC_leadership_inputs.md', 'SYNTHETIC Leadership Inputs.docx'),
]
LINK_NAMES = {k:v for k,v in FORMS}
LINK_NAMES.update({Path(k).name:v for k,v in REFERENCES})
LINK_NAMES.update({'first-time-setup.md':'01 First time setup.docx',
                   'system-primer.md':'UPLOAD THIS TO START.docx',
                   'local_profile_template.md':'Local Profile.docx',
                   'pantons-v0.4.md':'Local Profile.docx',
                   'README.md':'START HERE.docx'})


def validate_reproducibility_contract():
    if REPRO.get('schema_version') != 1 or REPRO.get('package_format') != 1:
        raise ValueError('Unsupported packaging/reproducibility.json contract')
    running=platform.python_version()
    if running != REPRO.get('python_version'):
        raise ValueError(f'Package build requires Python {REPRO.get("python_version")}; running {running}')
    if REPRO.get('archive_mode') != 'stored':
        raise ValueError('Current package format requires archive_mode=stored')
    if REPRO.get('metadata_timestamp') != METADATA_SENTINEL or ZIP_TIMESTAMP != (1980,1,1,0,0,0):
        raise ValueError('Package format 1 requires the documented 1980-01-01 metadata sentinel')
    requirements=(ROOT/'packaging/requirements.txt').read_bytes()
    if hashlib.sha256(requirements).hexdigest() != REPRO.get('requirements_sha256'):
        raise ValueError('packaging/requirements.txt changed without updating reproducibility.json')


def actionable_migrations():
    return [item for item in PERSISTENT['migrations'] if item['action'] != 'none']


def update_instructions_source():
    change_note=(ROOT/'packaging/update-note.md').read_text().strip()
    if not change_note:
        raise ValueError('packaging/update-note.md must describe this release')
    return '# Update to package '+VERSION+'\n\n'+change_note+'\n\n## Use next week\n\n1. Extract this update into a temporary folder, separate from your squadron scheduling folder.\n2. Before starting next week’s planning, replace the entire System folder in your permanent scheduling folder with the supplied System folder.\n3. Replace START HERE.docx with the supplied copy.\n4. Keep Local Guidance, COPY THIS FOLDER FOR EACH NEW WEEK, and every Week of date folder in place. Never save local guidance or completed work inside System.\n5. If **PERSISTENT MIGRATIONS.docx** is included, read it before deleting the temporary update folder. Review and merge only the explicitly listed persistent changes; reference-only files are never automatic replacements or approvals.\n6. Follow the new System → Instructions → 02 Start a week.docx when starting next week’s chat. Upload the new startup document.\n\nThe package number in generated document headers is the authoritative installed System version. File dates are deterministic packaging metadata, not release/install timestamps.\n\nThis update does not change an existing conversation or any operational approvals. Current-week work and decisions carry forward. Routine updates include no local guidance or weekly folders. A release that deliberately changes persistent local seeds or folder structure must declare that migration and may include clearly marked reference-only copies outside System for human review.\n\n## Rollback\n\nTo restore a prior System release, download that release’s Update_Existing_Setup.zip and follow System → Instructions → 09 Update next week.docx. Replace only System and START HERE. Do not roll back Local Guidance, weekly work or operational decisions automatically.\n\n## Coming from the earlier Markdown kit?\n\nUse the appropriate full setup ZIP once. Copy your existing approved local guidance and weekly work into the new layout; preserve their contents. Future updates use the System replacement above plus any explicitly declared persistent-migration review.\n\nSee System → Instructions → 09 Update next week.docx for details. Downloading an update or rollback grants no new scheduling approval or waiver.\n'


def persistent_migration_source():
    migrations=actionable_migrations()
    if not migrations:
        return ''
    lines=[
        '# Persistent migration review',
        '',
        'This document appears only when a release deliberately changes persistent installed state. Do not overwrite Local Guidance or weekly work. Review each migration, compare any reference-only copy with your current human-maintained file, and merge only changes that the appropriate human authority accepts.',
        ''
    ]
    for item in migrations:
        lines += [f'## {item["id"]} — package {item["introduced_in"]}', '', item['summary'], '', '**Affected persistent artifacts:** '+', '.join(item['artifacts']), '', 'Required actions:']
        lines += [f'{index}. {instruction}' for index,instruction in enumerate(item['instructions'],1)]
        lines += ['', 'Reference-only source copies, when applicable, are provided under **Persistent Migration Sources**. They are comparison material, not installed replacements and not evidence of approval.', '']
    return '\n'.join(lines)


def el(tag, **attrs):
    node = OxmlElement('w:'+tag)
    for k,v in attrs.items(): node.set(qn('w:'+k), str(v))
    return node


def configure(doc):
    """compact_reference_guide preset; compact customer_pack title, no cover page."""
    sec=doc.sections[0]
    sec.page_width=Inches(8.5); sec.page_height=Inches(11)
    sec.top_margin=sec.bottom_margin=sec.left_margin=sec.right_margin=Inches(1)
    sec.header_distance=sec.footer_distance=Inches(.492)
    styles=doc.styles
    tokens={'Normal':(11,0,6,'000000',False), 'Title':(24,0,8,'0B2545',True),
            'Subtitle':(10,0,8,'555555',False), 'Heading 1':(16,18,10,'2E74B5',True),
            'Heading 2':(13,14,7,'2E74B5',True), 'Heading 3':(12,10,5,'1F4D78',True),
            'List Bullet':(11,0,4,'000000',False), 'List Number':(11,0,4,'000000',False),
            'Prompt':(10.5,0,6,'000000',False), 'Record Label':(11,6,4,'1F4D78',True),
            'Header':(9,0,0,'555555',False), 'Footer':(9,0,0,'555555',False)}
    for name,(size,before,after,color,bold) in tokens.items():
        st=styles[name] if name in styles else styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH)
        st.font.name='Calibri';st.font.size=Pt(size);st.font.color.rgb=RGBColor.from_string(color);st.font.bold=bold
        pf=st.paragraph_format;pf.space_before=Pt(before);pf.space_after=Pt(after);pf.line_spacing=1.25
        pf.widow_control=True
        if name.startswith('Heading') or name in ('Title','Subtitle','Record Label'): pf.keep_with_next=True
    styles['Prompt']._element.get_or_add_pPr().append(el('shd',fill='F4F6F9'))
    styles['Prompt'].paragraph_format.keep_together=True
    numbering=doc.part.numbering_part.element
    for abstract_id,fmt,marker in [(70,'bullet','•'),(71,'decimal','%1.')]:
        a=el('abstractNum',abstractNumId=abstract_id);lvl=el('lvl',ilvl=0)
        lvl.extend([el('start',val=1),el('numFmt',val=fmt),el('lvlText',val=marker),el('lvlJc',val='left')])
        pp=el('pPr');tabs=el('tabs');tabs.append(el('tab',val='num',pos=540));pp.append(tabs)
        pp.append(el('ind',left=540,hanging=271));lvl.append(pp);a.append(lvl);numbering.append(a)
    b=el('num',numId=70);b.append(el('abstractNumId',val=70));numbering.append(b)
    sec.header.paragraphs[0].text='SCHEDULING ASSISTANT  |  Package '+VERSION
    foot=sec.footer.paragraphs[0];foot.alignment=2
    foot.add_run('Page ');field=el('fldSimple',instr='PAGE');foot._p.append(field)
    props=doc.core_properties;props.author='';props.last_modified_by='';props.title='Scheduling Assistant'
    props.created=props.modified=METADATA_TIMESTAMP
    props.revision=1


def clean(text):
    def link(m):
        label,target=m.group(1),m.group(2)
        if target.startswith(('http:','https:')): return label+' ('+target+')'
        return LINK_NAMES.get(Path(target.split('#')[0]).name,label)
    text=re.sub(r'\[([^]]+)\]\(([^)]+)\)',link,text)
    text=text.replace('`','')
    return text


def inline(p,text):
    for bit in re.split(r'(\*\*.*?\*\*)',clean(text)):
        if bit.startswith('**') and bit.endswith('**'): p.add_run(bit[2:-2]).bold=True
        else: p.add_run(bit)


def listpara(doc,text,num_id):
    p=doc.add_paragraph(style='List Bullet' if num_id==70 else 'List Number')
    pp=p._p.get_or_add_pPr();num=el('numPr');num.extend([el('ilvl',val=0),el('numId',val=num_id)]);pp.append(num)
    inline(p,text)


def write_doc(source, destination, subtitle=None):
    doc=Document();configure(doc);lines=source.splitlines();i=0;seq=100
    while i<len(lines):
        line=lines[i].strip()
        if not line: i+=1;continue
        if line.startswith('```'):
            i+=1;buf=[]
            while i<len(lines) and not lines[i].startswith('```'): buf.append(lines[i]);i+=1
            prompt=re.sub(r'(?<![.:])\n(?=\S)',' ','\n'.join(buf))
            p=doc.add_paragraph(style='Prompt');p.add_run(prompt);i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=re.split(r'(?<!\\)\|',lines[i].strip().strip('|'))
                if not all(re.fullmatch(r'\s*:?-+:?\s*',v) for v in row): rows.append([v.strip().replace('\\|','|') for v in row])
                i+=1
            headers=rows[0]
            if len(headers)>2 and len(rows)>4 and all(all(re.fullmatch(r'\[.*\]',v) for v in r[1:]) for r in rows[1:]):
                inline(doc.add_paragraph(),'Cover these topics; reference supplied products instead of retyping them:')
                for row in rows[1:]: listpara(doc,row[0],70)
                inline(doc.add_paragraph(style='Record Label'),'Copy this entry for each topic that needs a record')
                for h,v in zip(headers,['[topic]']+rows[1][1:]):
                    inline(doc.add_paragraph(),'**'+h+':** '+v)
                continue
            for row in rows[1:]:
                if len(row)!=len(headers): raise ValueError(('ragged table',destination,row))
                if len(headers)==2:
                    p=doc.add_paragraph();inline(p,'**'+row[0]+':** '+row[1])
                else:
                    p=doc.add_paragraph(style='Record Label');inline(p,headers[0]+': '+row[0])
                    for h,v in zip(headers[1:],row[1:]):
                        p=doc.add_paragraph();inline(p,'**'+h+':** '+v)
            continue
        heading=re.match(r'^(#{1,6}) (.*)',line)
        if heading:
            level=len(heading[1]);title=heading[2]
            if level==1:
                inline(doc.add_paragraph(style='Title'),title)
                inline(doc.add_paragraph(style='Subtitle'),subtitle or 'Package '+VERSION+' · Human-led scheduling')
            else: inline(doc.add_paragraph(style='Heading '+str(min(level-1,3))),title)
            i+=1;continue
        if re.match(r'^\d+\. ',line):
            seq+=1;n=el('num',numId=seq);n.append(el('abstractNumId',val=71));doc.part.numbering_part.element.append(n)
            while i<len(lines) and re.match(r'^\d+\. ',lines[i].strip()):
                listpara(doc,re.sub(r'^\d+\. ','',lines[i].strip()),seq);i+=1
            continue
        if line.startswith('- '): listpara(doc,line[2:].replace('[ ] ','Check: '),70);i+=1;continue
        buf=[line];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||```|- |\d+\. )',lines[i].strip()):
            buf.append(lines[i].strip());i+=1
        inline(doc.add_paragraph(),' '.join(buf))
    destination.parent.mkdir(parents=True,exist_ok=True)
    doc.save(destination)
    with zipfile.ZipFile(destination) as z: contents={n:z.read(n) for n in z.namelist() if not n.startswith('docProps/thumbnail')}
    with zipfile.ZipFile(destination) as z:
        for n in z.namelist():
            if n.startswith('docProps/thumbnail'): contents[n]=z.read(n)
    with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_STORED) as z:
        for n in sorted(contents):
            info=zipfile.ZipInfo(n,ZIP_TIMESTAMP);info.compress_type=zipfile.ZIP_STORED;z.writestr(info,contents[n])


def make_zip(folder,destination):
    destination.parent.mkdir(exist_ok=True,parents=True)
    with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_STORED) as z:
        for p in sorted(folder.rglob('*')):
            name=p.relative_to(folder).as_posix()+('/' if p.is_dir() else '')
            info=zipfile.ZipInfo(name,ZIP_TIMESTAMP);info.compress_type=zipfile.ZIP_STORED
            z.writestr(info,b'' if p.is_dir() else p.read_bytes())


def build(out):
    validate_reproducibility_contract()
    staging=out/'build';downloads=out/'downloads'
    if staging.exists(): shutil.rmtree(staging)
    common=staging/'common';system=common/'System'
    write_doc((ROOT/'packaging/guides/start.md').read_text(),common/'START HERE.docx')
    for source,name in GUIDES:
        write_doc((ROOT/'packaging/guides'/source).read_text(),system/'Instructions'/name)
    primer=(ROOT/'docs/v0.4/system-primer.md').read_text().split('## START OF PRIMER',1)[1].split('## END OF PRIMER',1)[0]
    intro='# Upload this to start\n\nThis is the assistant’s scheduling primer. Upload this document with current local guidance and sources, then paste the activation prompt in 02 Start a week.docx. These instructions are advisory and do not establish approval of a schedule.\n\n'
    write_doc(intro+primer,system/'UPLOAD THIS TO START.docx')
    for source,name in FORMS:
        write_doc((ROOT/'templates/v0.4'/source).read_text(),system/'Blank Forms'/name)
    for source,name in REFERENCES:
        write_doc((ROOT/source).read_text(),system/'Reference'/name)
    release=update_instructions_source()
    write_doc(release,staging/'UPDATE INSTRUCTIONS.docx')
    for variant,label,profile in [('Pantons','Pantons Scheduling Assistant','local-profiles/pantons-v0.4.md'),('First_Time_Squadron','Squadron Scheduling Assistant','templates/setup/local_profile_template.md')]:
        dest=staging/variant/label;shutil.copytree(common,dest)
        local=dest/'Local Guidance';write_doc((ROOT/profile).read_text(),local/'Local Profile.docx', 'Pantons approved local profile' if variant=='Pantons' else 'DRAFT — local rules must be supplied and approved')
        for src,name in [('04 Stable References.docx','Stable References.docx'),('09 Playbook.docx','Playbook.docx')]:
            shutil.copy2(system/'Blank Forms'/src,local/name)
        for directory in WEEKLY_DIRS:
            (dest/'COPY THIS FOLDER FOR EACH NEW WEEK'/directory).mkdir(parents=True)
        make_zip(staging/variant,downloads/(variant+'_Setup.zip'))
    update=staging/'Update';shutil.copytree(common,update)
    shutil.copy2(staging/'UPDATE INSTRUCTIONS.docx',update/'UPDATE INSTRUCTIONS.docx')
    migrations=actionable_migrations()
    if migrations:
        write_doc(persistent_migration_source(),update/MIGRATION_DOC,'Human-reviewed persistent-state migration')
        included=set()
        for item in migrations:
            for artifact in item['artifacts']:
                spec=PERSISTENT['artifacts'][artifact]
                if 'source' not in spec or artifact in included:
                    continue
                included.add(artifact)
                write_doc((ROOT/spec['source']).read_text(),update/'Persistent Migration Sources'/spec['migration_filename'],'REFERENCE ONLY — compare and merge; do not overwrite local guidance')
    make_zip(update,downloads/'Update_Existing_Setup.zip')
    manifests={}
    for p in sorted(downloads.glob('*.zip')):
        with zipfile.ZipFile(p) as z: entries=z.namelist()
        manifests[p.name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'files':entries}
    (downloads/'manifest.json').write_text(json.dumps({'package_version':VERSION,'packages':manifests},indent=2)+'\n')
    print(json.dumps({p.name:p.stat().st_size for p in downloads.iterdir()},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    build(parser.parse_args().output.resolve())
