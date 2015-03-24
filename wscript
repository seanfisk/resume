# -*- mode: python; coding: utf-8; -*-

import waflib

def options(ctx):
    ctx.load('tex')

def configure(ctx):
    ctx.load('tex')
    ctx.load('open', tooldir='waf-tools')
    # The current version of Waf doesn't directly support LuaTeX, but we can
    # override the PDFLATEX variable which works fine.
    ctx.env.PDFLATEX = ctx.find_program('lualatex')
    ctx.find_program('ghp-import', var='GHP_IMPORT')

class OpenContext(waflib.Build.BuildContext):
    """opens the resume PDF"""
    cmd = 'open'

class UploadContext(waflib.Build.BuildContext):
    """uploads the PDF to GitHub pages"""
    cmd = 'upload'

def build(ctx):
    tex_node = ctx.path.find_resource('sean-fisk-resume.tex')
    pdf_node = tex_node.change_ext('.pdf')
    ctx(features='tex',
        type='pdflatex',
        source=tex_node,
        outs='pdf',
        # prompt=0 enables batch mode, which disables the avalanche of output
        # normally produced by LaTeX.
        prompt=0)

    if ctx.cmd == 'open':
        def _open(ctx):
            ctx.open_file(pdf_node)
        ctx.add_post_fun(_open)

    if ctx.cmd == 'upload':
        website_dir = ctx.path.find_or_declare('website')
        website_dir.mkdir()

        # PDF
        ctx(features='subst',
            source=pdf_node,
            target=website_dir.find_or_declare(pdf_node.name),
            is_copy=True)

        # HTML index page
        # TODO: Since we aren't using the automatically-generated GitHub Pages
        # front page anymore, we could make this look a bit better. But it
        # doesn't really matter much.
        ctx(features='subst',
            source='index.html.in',
            target=website_dir.find_or_declare('index.html'),
            REDIRECT_DELAY='5',
            PDF_URL=pdf_node.name)

        def _run_ghp_import(ctx):
            ctx.exec_command(ctx.env.GHP_IMPORT + [
                '-n', # Include a .nojekyll file in the branch
                '-p', # Push the branch after import
                website_dir.abspath(),
            ])
        ctx.add_post_fun(_run_ghp_import)
