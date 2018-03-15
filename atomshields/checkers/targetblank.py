#!/usr/bin/env python
# -*- coding:utf8 -*-

from base import GenericChecker

class TargetBlankChecker(GenericChecker):

	NAME = "targetblank"
	DESCRIPTION = """Detecta vulnerabilidades 'Target Blank' en ficheros HTML"""
	CONFIG = {
		"enabled": True,
		"exclude_paths": ["test/", "docs/"]
	}

	def __init__(self):
		pass