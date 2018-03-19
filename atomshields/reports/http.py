# -*- coding:utf8 -*-
from reports.base import GenericReport
import requests, json


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
		"method": "post",
		"use_proxy": False,
		"proxy": "http://127.0.0.1:8080"
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
		options = {}
		if bool(self.config['use_proxy']):
			options['proxies'] = {"http": self.config['proxy'], "https": self.config['proxy']}

		options["url"] = self.config['url']
		options["data"] = {"issues": json.dumps(map(lambda x: x.__todict__(), self.issues))}

		if 'get' == self.config['method'].lower():
			requests.get(**options)
		else:
			requests.post(**options)


