Checkers
========


DS_STORE
--------
DS_STORE is a Mac OS X file containing information about the system that created it.
These files are rarely filtered in. gitignore, providing information about the system of the
author of the repository.

.. autosummary::
  atomshields.checkers.dsstore.DSStoreChecker


----------------------------------------------------------------------------------------------------


RetireJS
--------
The goal of Retire.js is to help you detect use of version of JavaScript libraries with
known vulnerabilities. This checker finds js files with vulnerabilities.
Also, the checker finds and download JS files linked via URL.

.. autosummary::
  atomshields.checkers.retirejs.RetireJSChecker


----------------------------------------------------------------------------------------------------


Target-blank
------------

This checker helps you to detect the *target blank* vulnerability in your code files.
For more details about the vulnerability please see
`this link <https://dev.to/ben/the-targetblank-vulnerability-by-example>`_.

.. autosummary::
  atomshields.checkers.targetblank.TargetBlankChecker
