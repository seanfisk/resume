# -*- mode: python -*-
# SCons build file

import os
import subprocess
from tempfile import TemporaryFile
import shutil

RESUME_PDF_NAME = 'sean-fisk-resume.pdf'


def git_current_branch():
    git_branch_output = subprocess.Popen(
        ['git', 'branch'],
        stdout=subprocess.PIPE).communicate()[0]
    branches = git_branch_output.splitlines()
    current_branch = filter(lambda b: b.startswith('*'),
                            branches)[0].split(' ')[1]
    return current_branch


def upload_to_gh_pages(target, source, env):
    current_branch = git_current_branch()
    with TemporaryFile() as temp_file:
        with open(RESUME_PDF_NAME) as pdf_file:
            shutil.copyfileobj(pdf_file, temp_file)
        subprocess.check_call(['git', 'checkout', 'gh-pages'])
        temp_file.seek(0)
        with open(RESUME_PDF_NAME, 'w') as pdf_file:
            shutil.copyfileobj(temp_file, pdf_file)
    subprocess.check_call(['git', 'add', RESUME_PDF_NAME])
    subprocess.check_call(['git', 'commit', '-m', 'Updated resume.'])
    subprocess.check_call(['git', 'push', 'origin', 'gh-pages'])
    subprocess.check_call(['git', 'checkout', current_branch])
    return 0

env = Environment()

# Use LuaTeX instead of pdfTeX.
env.Replace(PDFLATEX='lualatex')

# Enable SyncTeX. This is personal, but I use it, and I would
# recommend it to everybody.
env.AppendUnique(PDFLATEXFLAGS='-synctex=1')

# Look in standard directory ~/texmf for .sty files
env['ENV']['TEXMFHOME'] = os.path.join(os.environ['HOME'], 'texmf')

resume_pdf = env.PDF(target=RESUME_PDF_NAME, source='sean-fisk-resume.tex')
Default(resume_pdf)

env.Command('upload', [resume_pdf], upload_to_gh_pages)
