===========
 My Résumé
===========

This is the source code for my résumé, written in LaTeX. The only
dependency is tucv_, a résumé template. First install that
dependency::

    tlmgr install tucv

If you use SCons_, you can build it easily::

    scons

Then you can clean with::

    scons --clean

And also upload to GitHub pages easily with::

    scons upload

This uses some ``git`` trickery and I've only tested it on my Mac, so YMMV.

If you don't want to bother with SCons, just run::

    pdflatex resume.tex

.. _tucv: http://www.ctan.org/pkg/tucv
.. _SCons: http://scons.org/
