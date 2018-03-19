# -*- coding:utf8 -*-
from base import GenericChecker, checker


class PasswordsCheckers(GenericChecker):

	NAME = "passwords"
	DESCRIPTION = """Identifica patrones que puedan suponer un password hardcodeado"""
	CONFIG = {
		"enabled": True,
		"exclude_paths": ["test/", "docs/", "qa/"]
	}

	def __init__(self):
		pass
