# -*- coding: utf-8 -*-
class QgsDataSourceURI:

    def __init__(self):
        self._host = ''

    def setConnection(self, host, port, database, username, password, sslmode):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._database = database

    def host(self):
        return self._host

    def port(self):
        return self._port

    def username(self):
        return self._username

    def password(self):
        return self._password

    def database(self):
        return self._database

    def connectionInfo(self):
        return "dbname='%s' host=%s port=%s user='%s' password='%s'" % ( self._database, self._host, self._port, self._username, self._password)
