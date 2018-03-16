#!/usr/bin/env python
# -*- coding:utf8 -*-


import sys
import inspect
import termcolor

class GenericChecker(object):

	def __init__(self):
		"""
		Creates a new class instance for Generic Checkers
		"""
		self._dao = None
		self._path = None
		self._config = None
		self._issues = []

	@property
	def dao(self):
		"""
		Getter for 'dao' property
	
		Returns:
			DAO: Instance of DAO class
		"""
		return self._dao

	@dao.setter
	def dao(self, value):
		"""
		Setter for 'dao' property

		Args:
			value (DAO): Instance of DAO class

		"""
		self._dao = value


	@property
	def path(self):
		"""
		Getter for 'path' property
	
		Returns:
			str: Absolute path to scan
		"""
		return self._path

	@path.setter
	def path(self, value):
		"""
		Setter for 'path' property

		Args:
			value (str): Absolute path to scan

		"""
		self._path = value

	@property
	def project(self):
		"""
		Getter for 'project' property
	
		Returns:
			str: Project's name
		"""
		return self._project

	@project.setter
	def project(self, value):
		"""
		Setter for 'project' property

		Args:
			value (str): Project's name

		"""
		self._project = value

	@property
	def issues(self):
		"""
		Getter for 'issues' property
	
		Returns:
			list<Issue>: List of instances of Issue class
		"""
		return self._issues

	@issues.setter
	def issues(self, value):
		"""
		Setter for 'issues' property

		Args:
			value (list): List of Issue objects

		"""
		self._issues = value

	def test(self):
		"""
		Check if the checker is OK to run. 

		This method should to run every test (requirements) in order to ensure the excution will not have errors.

		Returns:

			bool: True if the checker has all the requirements installed. False else
		"""
		if self.path is None:
			return False

		return True

	def run(self):
		"""
		Abstract method. This method will be executed for subclass which not implemented his own method
		"""
		pass

	




	def saveIssue(self, issue):
		"""
		Stores an issue in 'issues' property

		Args:
			issue (Issue): Issue instance
		"""
		

		self.issues.append(issue)



def checker(func):
	"""
	Decorator for method run. This method will be execute before the execution 
	from the method with this decorator.
	"""
	def execute(self, *args, **kwargs):
		try:
			if hasattr(self, 'test'):
				if self.test():
					func(self, *args, **kwargs)
					return self.issues
				else:
					print colored("[!] The initial test for class {c} has not been successful".format(c=self.__class__.__name__), "red")
			else:
				func(self, *args, **kwargs)
				return self.issues

		except Exception as e:
			desc = "Error en la ejecución del checker: %s" % e
			print desc 

	return execute



