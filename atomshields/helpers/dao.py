# -*-coding:utf8 -*-
import sqlite3

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

    def __init__(self, database, debug=False):
		"""
		Inits MySQL connection
		"""
		self.debug = debug
		self._connect(database=database)


    def _connect(self, database):
        """
        Creates connection
        """
        try:
            conn = sqlite3.connect(database)
            if conn.open:
                self.connection = conn
            else:
                raise ValueError('Could not connect to database %s' % database)
        except FileNotFoundError:
            self.debug("Database '%s' not found" % database)


	def _get_cursor(self):
		"""
		Return cursor
		"""
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
