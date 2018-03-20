# -*- coding: utf8 -*-
from subprocess import Popen, PIPE

class CommandHelper(object):
	"""
	Class used to execute commands in shell, an d get the output and the errors.
	"""

	def __init__(self, command):
		"""
		Class constructor. 

		Args:
			command (str): Command to execute
		"""
		self._output = None
		self._errors = None
		self._command = None
		self.command = command


	@property
	def command(self):
		"""
		Getter for 'command' property

		Returns:
			str: Command to execute
		"""
		return self._command

	@command.setter
	def command(self, value):
		"""
		Setter for 'command' property

		Args:
			value (str): Command to execute

		"""
		self._command = value

	@property
	def output(self):
		"""
		Getter for 'output' property

		Returns:
			str: Stdout content
		"""
		return self._output

	@output.setter
	def output(self, value):
		"""
		Setter for 'output' property

		Args:
			value (str): Stdout content

		"""
		self._output = value

	@property
	def errors(self):
		"""
		Getter for 'errors' property

		Returns:
			str: Stderr content
		"""
		return self._errors

	@errors.setter
	def errors(self, value):
		"""
		Setter for 'errors' property

		Args:
			value (str): Stderr content

		"""
		self._errors = value


	def execute(self, shell = True):
		"""
		Executes the command setted into class

		Args:
			shell (boolean): Set True if command is a shell command. Default: True
		"""
		process = Popen(self.command, stdout=PIPE, stderr=PIPE, shell=shell)
		self.output, self.errors = process.communicate()
