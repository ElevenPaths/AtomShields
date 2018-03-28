Reports
========


Echo
----
This reports prints on screen a summary of all issues found. The fields printed are Name,
Severity and File affected.

.. autosummary::
  atomshields.reports.echo.EchoReport


----------------------------------------------------------------------------------------------------


Http Request
------------
Sends hte full information of issues via HTTP. The endpoint must be setted into the config file in
the directory *.atomshields* into your home path.

.. autosummary::
  atomshields.reports.http.HttpReport
