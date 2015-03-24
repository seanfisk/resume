<!-- -*- coding: utf-8; -*- -->

My Résumé
=========

This is the source code for my résumé, written in LaTeX. The only dependency is [tucv][], a résumé template. First install that dependency:

    tlmgr install tucv

Install the Python requirements:

    pip install -r requirements.txt

Build and open with [Waf][]:

    ./waf configure open

And also upload to [GitHub Pages][] easily with:

    ./waf upload

[tucv]: http://www.ctan.org/pkg/tucv
[Waf]: https://code.google.com/p/waf/
[GitHub Pages]: https://pages.github.com/
