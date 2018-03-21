# -*- coding: utf8 -*-
from subprocess import Popen, PIPE
import platform

class CommandHelper(object):
	"""
	Class used to execute commands in shell, an d get the output and the errors.
	"""

	OS_UBUNTU = "Ubuntu"
	OS_DEBIAN = "Debian"
	OS_CENTOS = "CentOS"
	OS_REDHAT = "Redhat"

	OS_LINUX = "Linux"
	OS_MAC = "Darwin"
	OS_WINDOWS = "Windows"

	def __init__(self, command = None):
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

	def getOSName(self):
		"""
		Get the OS name. If OS is linux, returns the Linux distribution name

		Returns:
			str: OS name
		"""
		_system = platform.system()
		if _system in [self.__class__.OS_WINDOWS, self.__class__.OS_MAC, self.__class__.OS_LINUX]:
			if _system == self.__class__.OS_LINUX:
				_dist = platform.linux_distribution()[0]
				if _dist.lower() == self.__class__.OS_UBUNTU.lower():
					return self.__class__.OS_UBUNTU
				elif _dist.lower() == self.__class__.OS_DEBIAN.lower():
					return self.__class__.OS_DEBIAN
				elif _dist.lower() == self.__class__.OS_CENTOS.lower():
					return self.__class__.OS_CENTOS
				elif _dist.lower() == self.__class__.OS_REDHAT.lower():
					return self.__class__.OS_REDHAT
			return _system
		else:
			return None


	def install(self, software, uninstall = False):
		if uninstall:
			action = 'uninstall'
		else:
			action = 'install'

		osname = self.getOSName()
		if osname == self.__class__.OS_WINDOWS:
			raise Exception("Windows installs are not supported yet")
		elif osname == self.__class__.OS_MAC:
			command = "brew -y {action} {name}".format(action=action, name=software)
			# raise Exception("MacOS installs are not supported yet")
		elif osname in [self.__class__.OS_UBUNTU, self.__class__.OS_DEBIAN]:
			command = "apt-get -y {action} {name}".format(action=action, name=software)
		elif osname in [self.__class__.OS_CENTOS, self.__class__.OS_REDHAT]:
			command = "yum -y {action} {name}".format(action=action, name=software)
		else:
			raise Exception("Unknown OS: Try to install the packages '{p}' manually".format(p=packages))

		try:
			self.command = command
			self.execute()
		except OSError as e:
			if 'Permission denied' in e:
				raise Exception("Permission denied: Try to install the packages '{p}' manually".format(p=packages))


	def execute(self, shell = True):
		"""
		Executes the command setted into class

		Args:
			shell (boolean): Set True if command is a shell command. Default: True
		"""
		process = Popen(self.command, stdout=PIPE, stderr=PIPE, shell=shell)
		self.output, self.errors = process.communicate()
