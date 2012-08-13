# -*- mode: python -*-
# SCons build file

import os

env = Environment()

# Look in standard directory ~/texmf for .sty files
env['ENV']['TEXMFHOME'] = os.path.join(os.environ['HOME'], 'texmf')

resume_pdf = env.PDF('resume.tex')
Default(resume_pdf)
