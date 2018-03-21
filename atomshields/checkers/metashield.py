# -*- coding:utf8 -*-
from base import GenericChecker


class MetashieldChecker(GenericChecker):

	NAME = "metashield"
	DESCRIPTION = """Analiza y limpia ficheros con metadatos sensibles"""
	CONFIG = {
		"enabled": True,
		"cache": True,
		"cleaner": False,
		"exclude_paths": ["test/", "tests/", "doc/", "docs/"],
		"appId": "<your_metashield_appId>",
		"secret": "<your_metashield_secret_key>"
	}

	def __init__(self):
		super(MetashieldChecker, self).__init__()

	@staticmethod
	def install():
		"""
		To perform the actions in order to install all the requirements to run this checker
		"""
		print "Metodo de instalacion de metashield"

	@staticmethod
	def test():
		return False


	def run(self):
		print "Run Metashield"
