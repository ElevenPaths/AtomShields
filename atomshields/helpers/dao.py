#!/usr/bin/env python
# -*-coding:utf8 -*-

import MySQLdb


class Singleton(object):
    """
    Restriction for the creation of a single object instance.

    Restriction for the creation of objects belonging to a class or the value of a type to a
    single object. Its intention is to ensure that a class has only one instance and to provide
    a global access point to it.

    Attributes:
        _instance(object): Object already initialized

    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class DAO(Singleton):
    """
    Database access module.

    This module accesses and stores information about checkers who need to make use of it, for example, metashield.

    Attributes:
        debug (bool): Enable to display information about the process.
        connection (sqlite.Connection): Instance of the connection to the database

    """

	def __init__(self, host, username, password, dbname, port = 3306, debug = False):
		"""
		Inits MySQL connection
		"""
		self.debug = debug
		self._connect(host, username, password, dbname, port)


	def _connect(self, host, username, password, dbname, port = 3306):
		"""
		Creates connection
		"""
		self.connection = MySQLdb.connect(host=host, user=username, passwd=password, db=dbname, port=port)

	def _get_cursor(self):
		"""
		Pings connection and returns cursor
		"""
		try:
		    self.connection.ping()
		except:
		    self._connect()
		return self.connection.cursor()


	def get_row(self, query):
		"""
		Fetchs one row
		"""
		cursor = self._get_cursor()
		cursor.execute(query)
		row = cursor.fetchone()
		cursor.close()
		return row


	def get_rows(self, query):
		"""
		Fetchs all rows
		"""
		cursor = self._get_cursor()
		cursor.execute(query)
		rows = cursor.fetchall()
		cursor.close()
		return rows


	def execute(self, query):
		"""
		Executes query for update, delete
		"""
		cursor = self._get_cursor()
		cursor.execute(query)
		cursor.close()
