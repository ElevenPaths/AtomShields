#!/usr/bin/env python
# -*- coding:utf8 -*-

from base import GenericChecker

class DSStoreChecker(GenericChecker):

	NAME = "dsstore"
	DESCRIPTION = """Busca y elimina los ficheros .DS_Store"""
	CONFIG = {
		"enabled": True,
		"remove": True,
		"exclude_paths": []
	}

	def __init__(self):
		pass