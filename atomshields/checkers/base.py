#!/usr/bin/env python
# -*- coding:utf8 -*-

class GenericChecker(object):

	def __init__(self):
		"""
		Creates a new class instance for Generic Checkers
		"""
		self._dao = None
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

	@staticmethod
	def test():
		"""
		Check if the checker is OK to run. 

		This method should to run every test (requirements) in order to ensure the excution will not have errors.

		Returns:

			bool: True if the checker has all the requirements installed. False else
		"""
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

