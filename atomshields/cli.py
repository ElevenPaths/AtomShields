#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
import os
import glob
import shutil
import ast
import json
from ConfigParser import ConfigParser

# CONSTANTS
CONTEXT_PLUGINS = ["plugins"]
CONTEXT_REPORTS = ["reports"]
CONTEXT_RUN = ["run"]
CONTEXT_SETUP = ["setup"]
CONTEXT_CONFIG = ["config"]

CMD_SHOW = ["list", "show"]
CMD_INSTALL = ["install"]
CMD_GENERATE = ["gen", "generate"]


CLASSNAME_GENERIC_CHECKER = 'GenericChecker'
CLASSNAME_GENERIC_REPORT = 'GenericReport'

ROOT_DIR = "/usr/local/share/atomshields"
CONFIG_PATH = os.path.expanduser("~/.atomshields/config")
PLUGINS_DIR = os.path.join(ROOT_DIR,"checkers")
REPORTS_DIR = os.path.join(ROOT_DIR,"reports")
CONFIG_FILE = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config", "atomshields.conf"))

def usage():
	print "python cli.py COMMAND [OPTIONS]"
	sys.exit(-1)

def _setup():
	# Create plugins directory
	if not os.path.isdir(PLUGINS_DIR):
		os.makedirs(PLUGINS_DIR)
	if not os.path.isdir(REPORTS_DIR):
		os.makedirs(REPORTS_DIR)

	# Copy all checkers
	for f in getFiles(os.path.join(os.path.dirname(os.path.realpath(__file__)), "checkers"), "*.py"):
		shutil.copy(f, PLUGINS_DIR)
	# Copy all reports
	for f in getFiles(os.path.join(os.path.dirname(os.path.realpath(__file__)), "reports"), "*.py"):
		shutil.copy(f, REPORTS_DIR)

	# Setup plugins
	exclude = ["__init__.py", "base.py"]
	for file in getFiles(PLUGINS_DIR, "*.py", exclude=exclude):
		_class = getClass(file)
		basename = os.path.basename(file).replace(".py", "")
		sys.path.append(ROOT_DIR)
		try:
			mod = __import__("checkers.{b}".format(b=basename), globals(), locals(), [_class.name], -1)
			instance = getattr(mod, _class.name)
			instance.install()
			del instance
			del mod
		except Exception as e:
			pass

	#generateConfig(asume_yes=True, show=False)

def getClass(path):
	with open(path) as file:
		node = ast.parse(file.read())
	return [n for n in node.body if isinstance(n, ast.ClassDef)][0]

def getFiles(path, extension="*.py", exclude=[]):
	_p = os.path.join(path, extension)
	return [fn for fn in glob.glob(_p) if not os.path.basename(fn) in exclude]
	
def showFiles(path, extension="*.py", exclude=[]):
	for f in getFiles(path, extension, exclude=exclude):
		print os.path.basename(f)


def getCheckers():
	checkers = {}
	exclude = ["__init__.py", "base.py"]
	for file in getFiles(PLUGINS_DIR, "*.py", exclude=exclude):
		if checkPlugin(file):
			_class = getClass(file)
			basename = os.path.basename(file).replace(".py", "")
			sys.path.append(ROOT_DIR)
			try:
				mod = __import__("checkers.{b}".format(b=basename), globals(), locals(), [_class.name], -1)
				instance = getattr(mod, _class.name)
				desc = instance.DESCRIPTION
				del instance
				del mod
			except Exception as e:
				desc = None			
			checkers[_class.name] = desc
	return checkers

def getReports():
	reports = {}
	exclude = ["__init__.py", "base.py"]
	for file in getFiles(REPORTS_DIR, "*.py", exclude=exclude):
		if checkReport(file):
			_class = getClass(file)
			basename = os.path.basename(file).replace(".py", "")
			sys.path.append(ROOT_DIR)
			try:
				mod = __import__("reports.{b}".format(b=basename), globals(), locals(), [_class.name], -1)
				instance = getattr(mod, _class.name)
				desc = instance.DESCRIPTION
				del instance
				del mod
			except Exception as e:
				desc = None			
			reports[_class.name] = desc
	return reports

def showCheckers():
	print "CHECKERS"
	print "-------------------"
	checkers = getCheckers()
	for k in checkers.keys():
		print "%-20s\t%-60s" % (k, checkers[k])

def showReports():
	print "REPORTS"
	print "-------------------"
	reports = getReports()
	for k in reports.keys():
		print "%-20s\t%-60s" % (k, reports[k])

def checkPlugin(path):
	if not path.endswith(".py"):
		return False
	if not os.path.isfile(path):
		return False

	with open(path) as file:
		node = ast.parse(file.read())
	classes = [n.bases[0].id for n in node.body if isinstance(n, ast.ClassDef)]
	if CLASSNAME_GENERIC_CHECKER not in classes:
		return False

	return True

def checkReport(path):
	if not path.endswith(".py"):
		return False
	if not os.path.isfile(path):
		return False

	with open(path) as file:
		node = ast.parse(file.read())
	classes = [n.bases[0].id for n in node.body if isinstance(n, ast.ClassDef)]
	if CLASSNAME_GENERIC_REPORT not in classes:
		return False

	return True

def installPlugin(path):
	if checkPlugin(path):
		shutil.copy(path, PLUGINS_DIR)
	else:
		print "[!] Plugin will not be installed. Is not a valid checker"

def installReport(path):
	if checkReport(path):
		shutil.copy(path, REPORTS_DIR)
	else:
		print "[!] Plugin will not be installed. Is not a valid report"

def getConfig(section = None):
	# Read config file
	config = ConfigParser()
	config.read(CONFIG_PATH)

	data = {}

	for s in sorted(config.sections()):
		if '/' in s:
			# Subsection
			parent, _s = s.split('/')
			data[parent][_s] = dict(config.items(s))
		else:
			data[s] = dict(config.items(s))

	if section is not None:
		try:
			return data[section]
		except KeyError:
			if '/' in section:
				parent, _s = section.split('/')
				try:
					return data[parent][_s]
				except KeyError:
					raise Exception("Section '{s}' does not exists".format(s=section))
			else:
				raise Exception("Section '{s}' does not exists".format(s=section))

	else:
		return data

def generateConfig(asume_yes = True, show = True):

	# Setup config file
	target_dir = os.path.dirname(CONFIG_PATH)
	if not os.path.isdir(target_dir):
		os.makedirs(target_dir)


	if os.path.isfile(CONFIG_PATH):
		if not asume_yes:
			answer = raw_input("Config file '{path}' will be overwritten. Are you sure? [y/n] ".format(path=CONFIG_PATH))
			if answer.lower() in ["y", "s"]:
				allow = True
			else:
				allow = False
		else:
			allow = True
	else:
		allow = True

	if allow:

		config = ConfigParser()
		# config.read(CONFIG_PATH)


		# Add Default config
		config.add_section("atomshields")
		config.set("atomshields", "enabled", True)

		config.add_section("checkers")
		config.set("checkers", "enabled", True)

		exclude = ["__init__.py", "base.py"]
		for file in getFiles(PLUGINS_DIR, "*.py", exclude=exclude):
			_class = getClass(file)
			basename = os.path.basename(file).replace(".py", "")
			sys.path.append(ROOT_DIR)
			try:
				mod = __import__("checkers.{b}".format(b=basename), globals(), locals(), [_class.name], -1)
				instance = getattr(mod, _class.name)
				section_name = "checkers/{name}".format(name=instance.NAME)
				config.add_section(section_name)
				for k in instance.CONFIG.keys():
					config.set(section_name, k, instance.CONFIG[k])

				del instance
				del mod
			except Exception as e:
				pass

		config.add_section("reports")
		config.set("reports", "enabled", True)

		exclude = ["__init__.py", "base.py"]
		for file in getFiles(REPORTS_DIR, "*.py", exclude=exclude):
			_class = getClass(file)
			basename = os.path.basename(file).replace(".py", "")
			sys.path.append(ROOT_DIR)
			try:
				mod = __import__("reports.{b}".format(b=basename), globals(), locals(), [_class.name], -1)
				instance = getattr(mod, _class.name)
				section_name = "reports/{name}".format(name=instance.NAME)
				config.add_section(section_name)
				for k in instance.CONFIG.keys():
					config.set(section_name, k, instance.CONFIG[k])

				del instance
				del mod
			except Exception as e:
				pass


		config.add_section("database")
		config.set("database", "host", "127.0.0.1")
		config.set("database", "user", "root")
		config.set("database", "password", "")
		config.set("database", "db", "atomshields")


		config.add_section("proxy")
		config.set("proxy", "enabled", False)
		config.set("proxy", "host", "127.0.0.1")
		config.set("proxy", "port", 8000)


		config.add_section("scm")
		
		config.add_section("scm/gerrit")
		config.set("scm/gerrit", "clone", "git clone ssh://[GERRIT_HOST]/<project> <destination>")
		config.set("scm/gerrit", "clone_last", "git clone -b <branch> --depth 1 ssh://[GERRIT_HOST]/<project> <destination>")
		config.set("scm/gerrit", "fetch", "git pull origin <ref>")


		config.add_section("scm/github")
		config.set("scm/github", "clone", "git clone git@github.com:[COMPANY]/<project> <destination>")
		config.set("scm/github", "fetch", "git checkout -b <branch> <commitId>")

		with open(CONFIG_PATH, 'wb') as configfile:
			config.write(configfile)

		if show:
			os.system("cat {file}".format(file=CONFIG_PATH))


if __name__ == "__main__":

	if len(sys.argv) < 2:
		usage()

	context = sys.argv[1]
	

	if context.lower() in CONTEXT_PLUGINS:
		# Se opera con plugins
		command = sys.argv[2]
		if command.lower() in CMD_SHOW:
			showCheckers()
		elif command.lower() in CMD_INSTALL:
			try:
				plugin_path = sys.argv[3]
				installPlugin(plugin_path)
			except IndexError:
				print "[!] Plugin path is required"
	elif context.lower() in CONTEXT_REPORTS:
		# Se opera con reports
		command = sys.argv[2]
		if command.lower() in CMD_SHOW:
			showReports()
		elif command.lower() in CMD_INSTALL:
			try:
				plugin_path = sys.argv[3]
				installReport(plugin_path)
			except IndexError:
				print "[!] Report path is required"
	elif context.lower() in CONTEXT_SETUP:
		_setup()

	elif context.lower() in CONTEXT_CONFIG:
		command = sys.argv[2]
		if command.lower() in CMD_GENERATE:
			generateConfig(asume_yes=False, show=True)
		elif command.lower() in CMD_SHOW:
			try:
				arg = sys.argv[3]
				print json.dumps(getConfig(arg), indent=4)
			except IndexError:
				print json.dumps(getConfig(), indent=4)




	
	else:
		print "[!] Unknown command '{command}'".format(command=command)
		sys.exit(-9)

