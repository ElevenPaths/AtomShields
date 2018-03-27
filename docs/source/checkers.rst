
Checkers
========


DS_STORE
--------
DS_STORE is a Mac OS X file containing information about the system that created it.
These files are rarely filtered in. gitignore, providing information about the system of the author of the repository.

.. automodule:: atomshields.checkers.dsstore
    :members:
    :undoc-members:
    :show-inheritance:



RetireJS
--------
The goal of Retire.js is to help you detect use of version of JavaScript libraries with known vulnerabilities.
This checker finds js files with vulnerabilities. Also, the checker finds and download JS files linked via URL.

.. automodule:: atomshields.checkers.retirejs
    :members:
    :undoc-members:
    :show-inheritance:


Target-blank
------------

This checker helps you to detect the *target blank* vulnerability in your code files. For more details about the vulnerability
please see `this link <https://dev.to/ben/the-targetblank-vulnerability-by-example>`_.

 .. automodule:: atomshields.checkers.targetblank
     :members:
     :undoc-members:
     :show-inheritance:
