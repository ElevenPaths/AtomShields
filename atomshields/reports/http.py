#!/usr/bin/env python
# -*- coding:utf8 -*-

from reports.base import GenericReport

class HttpReport(GenericReport):

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