# -*- coding:utf8 -*-

import json

class Issue(object):
	"""
	Type of object returned by all checkers.

	Este es el modelo genérico que será generado por cada vulnerabilidad encontrada por los
	checkers y tratada por los modulos de reporte.

	Attributes:
		SEVERITY_INFO (str): Name of the incidences of informatic value
		SEVERITY_LOW (str): Name of incidents with low criticality
		SEVERITY_MEDIUM (str): Name of incidents with medium criticality
		SEVERITY_HIGH (str): Name of requests with high criticality
		SEVERITY_CRITICAL (str): Name of the requests with very high criticality
		_name (str) : Name of the request
		_file (str) : File affected by the incident
		_details (str) : Other details about the incident
		_severity (str) : Criticism of the incidence
		_potential (bool) :
		_checker_name (str) : Name of the module that detected the request

	"""

	SEVERITY_INFO = "Info"
	SEVERITY_LOW = "Low"
	SEVERITY_MEDIUM = "Medium"
	SEVERITY_HIGH = "High"
	SEVERITY_CRITICAL = "Critical"

	def __init__(self, name=None, file=None, details=None, severity=None, potential=None, checker_name=None):
		self._name = name
		self._file = file
		self._details = details
		self._severity = severity
		self._potential = potential
		self._checker_name = checker_name


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

	def __todict__(self):
		"""
		Returns a dictionary with the class representation

		Returns:
			dict: class representarion
		"""
		return {
			"name": self.name,
			"file": self.file,
			"details": self.details,
			"severity": self.severity,
			"potential": self.potential,
			"checker": self.checker
		}

	def __str__(self):
		"""
		Return a JSON class representation

		Returns:

			str: JSON class representation
		"""
		return json.dumps(self.__todict__())

	def __unicode__(self):
		"""
		Return a JSON class representation (unicode)

		Returns:

			unicode: JSON class representation
		"""
		return unicode(self.__str__())
