Sampling Strategy documentation
===============================

This is the top level build directory for the **Sampling Strategy**
documentation.  
Parts of this documentation is taken from 
`matplotlib documentation <http://matplotlib.org>`_
since it has been used as sphinx example to emulate.
Like the example, all of the documentation is written using sphinx, a
python documentation system built on top of ReST.  

This directory contains:

* _static - used by the sphinx build system

* _templates - used by the sphinx build system

* sphinxext - Sphinx extensions for the mpl docs

* api - placeholders to automatically generate the api documentation

* users - the user documentation, including the aim of the project and tutorials using ipython notebooks

* devel - documentation for matplotlib developers

* MakeFile - the build script to build the html or PDF docs

* index.rst - the top level include document for matplotlib docs

* conf.py - the sphinx configuration


Things to look at
=================


`<http://sphinxcontrib-napoleon.readthedocs.org/en/latest/index.html>`_

`<https://github.com/snide/sphinx_rtd_theme>`_

`<https://github.com/Khan/style-guides/blob/master/style/python.md>`_

`<https://github.com/Khan/style-guides>`_

`<http://sphinx-doc.org/extensions.html>`_

Test
====

.. toctree::
  :maxdepth: 2
  
 devel/coding_guide.rst
  

.. module:: data_class_instance
.. autoclass:: DataClassInstance
   :members:
   :undoc-members:


.. automethod:: DataBase



Test2
=====
uml_generated_code.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

