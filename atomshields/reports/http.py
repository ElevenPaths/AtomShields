# -*- coding:utf8 -*-
from base import GenericReport


class HttpReport(GenericReport):
	"""
	This module sends all information about vulnerabilities to an endpoint via an http request.

    Attributes:
        NAME (str): Name of the module.
        DESCRIPTION (str): Description of the functionality of the module.
        CONFIG (dict): Default values of the module configuration.
	"""

	NAME = "http"
	DESCRIPTION = """Envia los datos de las vulnerabilidades a un endpoint HTTP"""
	CONFIG = {
		"enabled": False,
		"url": "<your_endpoint>",
		"method": "post"
	}
	def __init__(self):
		pass

	def run(self, issues):
		print "Enviando por http"
