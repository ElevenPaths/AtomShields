
Getting started
===============

.. badges-section

|Build| |Codacy| |Docs| |Version|

.. |Docs| image:: https://readthedocs.org/projects/atomshields/badge/?version=latest
   :target: http://atomshields.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs
.. |Version| image:: http://img.shields.io/pypi/v/atomshields.svg?style=flat
   :target: https://pypi.python.org/pypi/atomshields/
   :alt: Version
.. |Build| image:: https://travis-ci.org/ElevenPaths/AtomShields.svg?branch=master
  :target: https://travis-ci.org/ElevenPaths/AtomShields
  :alt: Build
.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/46c76e50709e4079828d5fecafa60473
   :target: https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ElevenPaths/AtomShields&amp;utm_campaign=Badge_Grade
   :alt: Codacy
.. |Coverage| image:: https://api.codacy.com/project/badge/Coverage/46c76e50709e4079828d5fecafa60473
   :target: https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ElevenPaths/AtomShields&amp;utm_campaign=Badge_Coverage
   :alt: Coverage

.. end-badges-section

.. whatis-section

What is AtomShields?
--------------------

Security testing framework for repositories and source code.

This system has different modules that detect different vulnerabilities or files that may
expose a risk, and the results obtained can be obtained or sent thanks to the reporting modules.

*For developers*: There is also the possibility to develop your own vulnerability detection
(called checkers) or reporting modules. This tool offers certain facilities for those who
want to implement their own modules, publish them and integrate them into the official ElevenPaths tool.

.. end-whatis-section

------------------------------------------------------------------------------------------

.. installation-section


Installation
------------

.. code-block:: shell

  pip install atomshields


.. end-installation-section

------------------------------------------------------------------------------------------

.. usage-section

Basic usage
-----------

.. code-block:: python

  import atomshields

  atoms = atomshields.AtomShieldsScanner('./MyRepo/')
  atoms.project = "MyRepoName"

  issues = atoms.executeCheckers()


.. end-usage-section

------------------------------------------------------------------------------------------

.. tests-section

Run tests
---------

.. code-block:: python

  # If you are in AtomShields directory
  pip install -r requirements-dev.txt
  py.test tests/

.. end-tests-section

------------------------------------------------------------------------------------------

.. docs-section

Generate docs
-------------

.. code-block:: shell

  # If you are in AtomShields directory
  pip install -r requirements-dev.txt
  cd docs
  make html

.. end-docs-section

------------------------------------------------------------------------------------------
