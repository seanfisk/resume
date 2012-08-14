# -*- mode: python -*-
# SCons build file

import os
from subprocess import check_call, check_output
from tempfile import TemporaryFile
import shutil

RESUME_PDF_NAME = 'resume.pdf'


def git_current_branch():
    git_branch_output = check_output(['git', 'branch'])
    branches = git_branch_output.splitlines()
    current_branch = filter(lambda b: b.startswith('*'),
                            branches)[0].split(' ')[1]
    return current_branch


def upload_to_gh_pages(target, source, env):
    current_branch = git_current_branch()
    with TemporaryFile() as temp_file:
        with open(RESUME_PDF_NAME) as pdf_file:
            shutil.copyfileobj(pdf_file, temp_file)
        check_call(['git', 'checkout', 'gh-pages'])
        temp_file.seek(0)
        with open(RESUME_PDF_NAME, 'w') as pdf_file:
            shutil.copyfileobj(temp_file, pdf_file)
    check_call(['git', 'add', RESUME_PDF_NAME])
    check_call(['git', 'commit', '-m', 'Updated resume.'])
    check_call(['git', 'push', 'origin', 'gh-pages'])
    check_call(['git', 'checkout', current_branch])
    return 0

env = Environment()

# Look in standard directory ~/texmf for .sty files
env['ENV']['TEXMFHOME'] = os.path.join(os.environ['HOME'], 'texmf')

resume_pdf = env.PDF(target=RESUME_PDF_NAME, source='resume.tex')
Default(resume_pdf)

env.Command('upload', [resume_pdf], upload_to_gh_pages)
