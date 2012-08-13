===========
 My Resume
===========

This is the source code for my resume, written in LaTeX. First install the dependencies. The only dependency is tucv_, a resume template.

.. code-block:: bash

    tlmgr install tucv

If you use SCons_, you can build it easily:

.. code-block:: bash

    scons

Then you can clean with:

.. code-block:: bash

    scons --clean

If you don't want to bother with SCons, just run:

.. code-block:: bash

    pdflatex resume.tex

.. _tucv: http://www.ctan.org/pkg/tucv
.. _SCons: http://scons.org/
