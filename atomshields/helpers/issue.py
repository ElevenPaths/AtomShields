#!/usr/bin/env python
# -*- coding:utf8 -*-


class Issue(object):

	SEVERITY_INFO = "Info"
	SEVERITY_LOW = "Low"
	SEVERITY_MEDIUM = "Medium"
	SEVERITY_HIGH = "High"
	SEVERITY_CRITICAL = "Critical"


	def __init__(self):
		self._name = None
		self._file = None
		self._details = None
		self._severity = None
		self._potential = False
		self._checker_name = None


	@property
	def name(self):
		"""
		Getter for 'name' property
	
		Returns:
			string: Issue's name
		"""
		return self._name


	@name.setter
	def name(self, value):
		"""
		Setter for 'name' property

		Args:
			value (str): Issue's name

		"""
		self._name = value


	@property
	def file(self):
		"""
		Getter for 'file' property
	
		Returns:
			string: Issue's file
		"""
		return self._file


	@file.setter
	def file(self, value):
		"""
		Setter for 'path' property

		Args:
			value (str): Issue's file

		"""
		self._file = value


	@property
	def severity(self):
		"""
		Getter for 'severity' property
	
		Returns:
			string: Issue's severity
		"""
		return self._severity


	@severity.setter
	def severity(self, value):
		"""
		Setter for 'path' property

		Args:
			value (str): Issue's severity

		"""
		self._severity = value


	@property
	def potential(self):
		"""
		Getter for 'potential' property
	
		Returns:
			bool: potential is required?
		"""
		if self._potential is not None and self._potential:
			return True
		else:
			return False

	@potential.setter
	def potential(self, value):
		"""
		Setter for 'potential' property

		Args:
			value (bool): True if a potential is required. False else

		"""
		if value:
			self._potential = True
		else:
			self._potential = False


	@property
	def details(self):
		"""
		Getter for 'details' property
	
		Returns:
			string: Issue's details
		"""
		return self._details


	@details.setter
	def details(self, value):
		"""
		Setter for 'details' property

		Args:
			value (str): Issue's details

		"""
		self._details = value

	@property
	def checker(self):
		"""
		Getter for 'checker' property
	
		Returns:
			string: Issue's checker
		"""
		return self._checker_name


	@checker.setter
	def checker(self, value):
		"""
		Setter for 'checker' property

		Args:
			value (str): Issue's checker

		"""
		self._checker_name = value

