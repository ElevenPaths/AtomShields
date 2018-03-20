# -*- coding:utf8 -*-

import ast

from atomshields import CommandHelper

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
			atomshield.helpers.DAO: Instance of DAO class
		"""
		return self._dao

	@dao.setter
	def dao(self, value):
		"""
		Setter for 'dao' property

		Args:
			value (atomshield.helpers.DAO): Instance of DAO class

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
		if not value.endswith('/'):
			self._path = '{v}/'.format(v=value)
		else:
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
			list<atomshields.helpers.Issue>: List of instances of Issue class
		"""
		return self._issues

	@issues.setter
	def issues(self, value):
		"""
		Setter for 'issues' property

		Args:
			value (list<atomshields.helpers.Issue>): List of Issue objects

		"""
		self._issues = value

	@property
	def config(self):
		"""
		Getter for 'config' property

		Returns:
			dict: Dictionary which contains the current values for this report config
		"""
		return self._config

	@config.setter
	def config(self, value):
		"""
		Setter for 'config' property

		Args:
			value (dict): Dictionary which contains the current values for this report config

		"""

		self._config = self.parseConfig(value)

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
			issue (atomshields.helpers.Issue): Issue instance
		"""

		self.issues.append(issue)

	@classmethod
	def parseConfig(cls, value):
		"""
		Parse the config values

		Args:
			value (dict): Dictionary which contains the checker config

		Returns:
			dict: The checker config with parsed values
		"""
		if 'enabled' in value:
			value['enabled'] = bool(value['enabled'])

		if 'exclude_paths' in value:
			value['exclude_paths'] = [n.strip() for n in ast.literal_eval(value['exclude_paths'])]

		return value

	@staticmethod
	def isInstalled(value):
		"""
		Check if a software is installed into machine.

		Args:
			value (str): Software's name

		Returns:
			bool: True if the software is installed. False else
		"""

		function = """
		function is_installed {
		  # set to 1 initially
		  local return_=1
		  # set to 0 if not found
		  type $1 >/dev/null 2>&1 || { local return_=0; }
		  # return value
		  echo "$return_"
		}"""
		cmd = CommandHelper(function)
		cmd.execute()

		cmd.command = 'echo $(is_installed \"{arg}\")'.format(arg=value)
		cmd.execute()
		return "1" in cmd.output


def checker(func):
	"""
	Decorator for method run. This method will be execute before the execution
	from the method with this decorator.
	"""
	def execute(self, *args, **kwargs):
		try:
			print "[>] Executing {n} checker. . . ".format(n=self.__class__.NAME)
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
