"""Stage 1 prototype assembler for the GenAI.mil smoke test. Temporary: folded into build_packages.py in Stage 2.

Usage: python scripts/build_prototype.py --output /path/to/temporary/folder
"""
import argparse, re, shutil, sys, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'scripts'))
import build_packages as bp

KIT_VERSION = '0.7.0 prototype'
bp.VERSION = KIT_VERSION  # header label only
GUARD = ('Do not delegate to subagents. Do all of this work yourself in this chat: do not hand any part of it to '
         'another model or agent, launch parallel assistants, or use automatic agent delegation. Looking up '
         'publications in DoW Policies Beta (GAMECHANGER) is allowed; it is evidence retrieval, not delegation. '
         'No specific model is required.')
END = '=== END OF TASK FILE ==='

def task_file(task_src, title):
    core = (REPO / 'packaging/kit/core.md').read_text().strip()
    week = (REPO / 'packaging/kit/week-file.md').read_text().strip()
    task = (REPO / 'packaging/kit/tasks' / task_src).read_text().strip()
    header = ('=== PANTON SCHEDULING ASSISTANT - TASK FILE ===\n'
              f'THIS TASK: {title}\n'
              f'Kit version: {KIT_VERSION}\n'
              'Read this whole file before you reply. It has three parts: Part 1, core instructions that are the same in every '
              'task file; Part 2, this task\'s step-by-step script; Part 3, the WEEK FILE format. It ends with an end marker.')
    return '\n\n'.join([GUARD, header, core, task, week, END]) + '\n'

def squadron_rules():
    profile = (REPO / 'local-profiles/pantons-v0.4.md').read_text()
    body = profile.split('\n', 1)[1].strip()          # drop the profile's own title
    body = re.sub(r'^## ', '### ', body, flags=re.M)  # nest under Section 1
    rules = (REPO / 'packaging/kit/squadron-rules.md').read_text().replace('{{PROFILE}}', body)
    assert '{{' not in rules
    return rules

def main(dest):
    out = dest / 'prototype'
    if out.exists(): shutil.rmtree(out)
    kit = out / 'Panton Scheduling Assistant (PROTOTYPE)'
    practice = out / 'PRACTICE WEEK (fictional)'
    tf = kit / 'TASK FILES'; tf.mkdir(parents=True)
    text = task_file('1-tuesday-plan.md', '1 TUESDAY - Plan next week')
    (tf / '1 TUESDAY - Plan next week.txt').write_text(text, encoding='utf-8')
    bp.write_doc((REPO / 'packaging/kit/start-here.md').read_text(), kit / 'START HERE.docx', checklist=True)
    bp.write_doc(squadron_rules(), kit / 'Squadron Rules.docx', 'Approved local rules - DO approves changes')
    week = kit / 'WEEKS' / '_COPY ME - New week'
    for d in ('Inputs', 'Schedules'): (week / d).mkdir(parents=True)
    bp.write_doc((REPO / 'packaging/kit/input-checklist.md').read_text(), week / 'INPUT CHECKLIST.docx', checklist=True)
    shutil.copytree(REPO / 'packaging/practice-week/Inputs', practice / 'Inputs')
    bp.write_doc((REPO / 'packaging/practice-week/TESTER NOTES - do not upload.md').read_text(),
                 practice / 'TESTER NOTES - do not upload.docx', 'Answer key - never upload to the assistant')
    bp.write_doc((REPO / 'packaging/practice-week/SMOKE TEST - how to run.md').read_text(), out / 'SMOKE TEST - how to run.docx', checklist=True)
    z = dest / 'Prototype_0.7.0_Tuesday.zip'
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zz:
        for p in sorted(out.rglob('*')):
            zz.write(p, p.relative_to(out).as_posix() + ('/' if p.is_dir() else ''))
    print('task file bytes', len(text.encode()))
    print('zip', z, z.stat().st_size)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--output', type=Path, required=True)
    dest = parser.parse_args().output.resolve(); dest.mkdir(parents=True, exist_ok=True)
    main(dest)
