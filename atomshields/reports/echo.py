# -*- coding:utf8 -*-
from atomshields.reports.base import *


class EchoReport(GenericReport):
	"""
	This module shows all the information about the vulnerabilities per screen (echo).

    Attributes:
        NAME (str): Name of the module.
        DESCRIPTION (str): Description of the functionality of the module.
        CONFIG (dict): Default values of the module configuration..
	"""

	NAME = "echo"
	DESCRIPTION = """Muestra las vulnerabilidades por pantalla"""
	CONFIG = {
		"enabled": True,
	}

	def __init__(self, *args, **kwargs):
		super(EchoReport, self).__init__(*args, **kwargs)

	@report
	def run(self):

		format_str = '{:<40}  {:<20} {:<40}'

		# Header
		print ""
		print format_str.format("Vulnerability", "Severity", "File affected")
		print "-"*80

		for issue in self.issues:
			if issue.potential:
				severity = "{s} [POTENTIAL]".format(s=issue.severity.upper())
			else:
				severity = issue.severity.upper()
			print format_str.format(issue.name, severity, issue.file)
