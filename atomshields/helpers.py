# -*- coding: utf8 -*-
from subprocess import Popen, PIPE

class CommandHelper(object):

	def __init__(self, command):
		self._output = None
		self._errors = None
		self._command = None
		self.command = command


	@property
	def command(self):
		return self._command

	@command.setter
	def command(self, value):
		self._command = value

	@property
	def output(self):
		return self._output

	@output.setter
	def output(self, value):
		self._output = value

	@property
	def errors(self):
		return self._errors

	@errors.setter
	def errors(self, value):
		self._errors = value


	def execute(self, shell = True):
		process = Popen(self.command, stdout=PIPE, stderr=PIPE, shell=shell)
		self.output, self.errors = process.communicate()
