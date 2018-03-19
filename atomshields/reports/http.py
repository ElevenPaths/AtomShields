# -*- coding:utf8 -*-
from reports.base import GenericReport
import requests


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

	def __init__(self, *args, **kwrds):
		"""
		Class constuctor. Must call parent constructor
		"""
		super(HttpReport, self).__init__(*args, **kwrds)

	def run(self):
		"""
		Method executed dynamically by framework. This method will do a http request to
		endpoint setted into config file with the issues and other data.
		"""
		pass
