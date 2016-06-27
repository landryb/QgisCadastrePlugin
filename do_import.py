# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Cadastre - Dialog classes
                                                                 A QGIS plugin
 This plugins helps users to import the french land registry ('cadastre')
 into a database. It is meant to ease the use of the data in QGIs
 by providing search tools and appropriate layer symbology.
                                                            -------------------
                begin                                : 2013-06-11
                copyright                        : (C) 2013 by 3liz
                email                                : info@3liz.com
 ***************************************************************************/

/***************************************************************************
 *                                                                                                                                                 *
 *     This program is free software; you can redistribute it and/or modify    *
 *     it under the terms of the GNU General Public License as published by    *
 *     the Free Software Foundation; either version 2 of the License, or         *
 *     (at your option) any later version.                                                                     *
 *                                                                                                                                                 *
 ***************************************************************************/
"""

import csv
import os.path
import operator
import re
import tempfile
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import unicodedata

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/forms")

from db_manager.db_plugins.plugin import DBPlugin, Schema, Table
from db_manager.db_plugins import createDbPlugin
from db_manager.db_plugins.postgis.connector import PostGisDBConnector

from cadastre_import_cli import cadastreImport

from functools import partial

# --------------------------------------------------------
#        import - Import data from EDIGEO and MAJIC files
# --------------------------------------------------------

class cadastre_dialog_cli():
    def __init__(self):

        print "creating instance of dialog_cli"

class cadastre_common():

    def __init__(self, dialog):

        self.dialog = dialog
        # plugin directory path
        self.plugin_dir = '.'

        # default auth id for layers
        self.defaultAuthId = 'EPSG:2154'

    def hasSpatialiteSupport(self):
        '''
        Check whether or not
        spatialite support is ok
        '''
        try:
            from db_manager.db_plugins.spatialite.connector import SpatiaLiteDBConnector
            return True
        except ImportError:
            return False
            pass


    def updateLog(self, msg):
        '''
        Update the log
        '''
        print msg


    def updateProgressBar(self):
        '''
        Update the progress bar
        '''
        print 'progress'

    def updateConnectionList(self):
        '''
        Update the combo box containing the database connection list
        '''

        dbType = unicode(self.dialog.liDbType.currentText()).lower()
        self.dialog.liDbConnection.clear()

        if self.dialog.liDbType.currentIndex() != 0:
            self.dialog.dbType = dbType
            # instance of db_manager plugin class
            dbpluginclass = createDbPlugin( dbType )
            self.dialog.dbpluginclass = dbpluginclass

            # fill the connections combobox
            self.dialog.connectionDbList = []
            for c in dbpluginclass.connections():
                self.dialog.liDbConnection.addItem( unicode(c.connectionName()))
                self.dialog.connectionDbList.append(unicode(c.connectionName()))

            # Show/Hide database specific pannel
            if hasattr(self.dialog, 'databaseSpecificOptions'):
                if dbType == 'postgis':
                    self.dialog.databaseSpecificOptions.setCurrentIndex(0)
                else:
                    self.dialog.databaseSpecificOptions.setCurrentIndex(1)
                    self.toggleSchemaList(False)
        else:
            if hasattr(self.dialog, "inDbCreateSchema"):
                self.dialog.databaseSpecificOptions.setTabEnabled(0, False)
                self.dialog.databaseSpecificOptions.setTabEnabled(1, False)


    def toggleSchemaList(self, t):
        '''
        Toggle Schema list and inputs
        '''
        self.dialog.liDbSchema.setEnabled(t)
        if hasattr(self.dialog, "inDbCreateSchema"):
            self.dialog.inDbCreateSchema.setEnabled(t)
            self.dialog.btDbCreateSchema.setEnabled(t)
            self.dialog.databaseSpecificOptions.setTabEnabled(0, t)
            self.dialog.databaseSpecificOptions.setTabEnabled(1, not t)
            self.dialog.btCreateNewSpatialiteDb.setEnabled(not t)


    def updateSchemaList(self):
        '''
        Update the combo box containing the schema list if relevant
        '''
        self.dialog.liDbSchema.clear()

        connectionName = unicode(self.dialog.liDbConnection.currentText())
        self.dialog.connectionName = connectionName
        dbType = unicode(self.dialog.liDbType.currentText()).lower()

        # Deactivate schema fields
        self.toggleSchemaList(False)

        connection = None
        if connectionName:
            # Get schema list
            dbpluginclass = createDbPlugin( dbType, connectionName )
            self.dialog.dbpluginclass = dbpluginclass
            try:
                connection = dbpluginclass.connect()
            except BaseError as e:

                DlgDbError.showError(e, self.dialog)
                self.dialog.go = False
                self.updateLog(e.msg)
                return

        if connection:
            self.dialog.connection = connection
            db = dbpluginclass.database()
            if db:
                self.dialog.db = db
                self.dialog.schemaList = []

            if dbType == 'postgis':
                # Activate schema fields
                self.toggleSchemaList(True)
                for s in db.schemas():
                    self.dialog.liDbSchema.addItem( unicode(s.name))
                    self.dialog.schemaList.append(unicode(s.name))
            else:
                self.toggleSchemaList(False)
        else:
            self.toggleSchemaList(False)


    def checkDatabaseForExistingStructure(self):
        '''
        Search among a database / schema
        if there are alreaday Cadastre structure tables
        in it
        '''
        hasStructure = False
        hasData = False
        hasMajicData = False
        hasMajicDataProp = False
        hasMajicDataParcelle = False
        hasMajicDataVoie = False

        searchTable = u'geo_commune'
        majicTableParcelle = u'parcelle'
        majicTableProp = u'proprietaire'
        majicTableVoie = u'voie'
        if self.dialog.db:
            if self.dialog.dbType == 'postgis':
                schemaSearch = [s for s in self.dialog.db.schemas() if s.name == self.dialog.schema]
                schemaInst = schemaSearch[0]
                getSearchTable = [a for a in self.dialog.db.tables(schemaInst) if a.name == searchTable]
            if self.dialog.dbType == 'spatialite':
                getSearchTable = [a for a in self.dialog.db.tables() if a.name == searchTable]
            if getSearchTable:
                hasStructure = True

                # Check for data in it
                sql = 'SELECT * FROM "%s" LIMIT 1' % searchTable
                if self.dialog.dbType == 'postgis':
                    sql = self.setSearchPath(sql, self.dialog.schema)
                [header, data, rowCount] = self.fetchDataFromSqlQuery(self.dialog.db.connector, sql)
                if rowCount >= 1:
                    hasData = True

                # Check for Majic data in it
                sql = 'SELECT * FROM "%s" LIMIT 1' % majicTableParcelle
                if self.dialog.dbType == 'postgis':
                    sql = self.setSearchPath(sql, self.dialog.schema)
                [header, data, rowCount] = self.fetchDataFromSqlQuery(self.dialog.db.connector, sql)
                if rowCount >= 1:
                    hasMajicData = True
                    hasMajicDataParcelle = True

                # Check for Majic data in it
                sql = 'SELECT * FROM "%s" LIMIT 1' % majicTableProp
                if self.dialog.dbType == 'postgis':
                    sql = self.setSearchPath(sql, self.dialog.schema)
                [header, data, rowCount] = self.fetchDataFromSqlQuery(self.dialog.db.connector, sql)
                if rowCount >= 1:
                    hasMajicData = True
                    hasMajicDataProp = True

                # Check for Majic data in it
                sql = 'SELECT * FROM "%s" LIMIT 1' % majicTableVoie
                if self.dialog.dbType == 'postgis':
                    sql = self.setSearchPath(sql, self.dialog.schema)
                [header, data, rowCount] = self.fetchDataFromSqlQuery(self.dialog.db.connector, sql)
                if rowCount >= 1:
                    hasMajicData = True
                    hasMajicDataVoie = True

        # Set global properties
        self.dialog.hasStructure = hasStructure
        self.dialog.hasData = hasData
        self.dialog.hasMajicData = hasMajicData
        self.dialog.hasMajicDataParcelle = hasMajicDataParcelle
        self.dialog.hasMajicDataProp = hasMajicDataProp
        self.dialog.hasMajicData = hasMajicDataVoie


    def checkDatabaseForExistingTable(self, tableName, schemaName=''):
        '''
        Check if the given table
        exists in the database
        '''
        tableExists = False
        if not self.dialog.db:
            return False

        if self.dialog.dbType == 'postgis':
            sql = "SELECT * FROM information_schema.tables WHERE table_schema = '%s' AND table_name = '%s'" % (schemaName, tableName)

        if self.dialog.dbType == 'spatialite':
            sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='%s'" % tableName

        [header, data, rowCount] = self.fetchDataFromSqlQuery(self.dialog.db.connector, sql)
        if rowCount >= 1:
            tableExists = True

        return tableExists


    def getLayerFromLegendByTableProps(self, tableName, geomCol='geom', sql=''):
        '''
        Get the layer from QGIS legend
        corresponding to a database
        table name (postgis or sqlite)
        '''

        layer = None
        layers = self.dialog.iface.legendInterface().layers()
        for l in layers:
            if not hasattr(l, 'providerType'):
                continue
            if not l.type() == QgsMapLayer.VectorLayer:
                continue
            if not l.providerType() in (u'postgres', u'spatialite'):
                continue

            connectionParams = self.getConnectionParameterFromDbLayer(l)
            import re

            reg = r'(\.| )?(%s)' % tableName
            if connectionParams and \
                ( \
                    connectionParams['table'] == tableName or \
                    ( re.findall(reg, '%s' % connectionParams['table']) and re.findall(reg, '%s' % connectionParams['table'])[0] ) \
                ) and \
                connectionParams['geocol'] == geomCol and \
                connectionParams['sql'] == sql:
                return l

        return layer

    def getConnectionParameterFromDbLayer(self, layer):
        '''
        Get connection parameters
        from the layer datasource
        '''
        connectionParams = None

        # Get params via regex
        uri = layer.dataProvider().dataSourceUri()
        reg = "dbname='([^']+)' (?:host=([^ ]+) )?(?:port=([0-9]+) )?(?:user='([^ ]+)' )?(?:password='([^ ]+)' )?(?:sslmode=([^ ]+) )?(?:key='([^ ]+)' )?(?:estimatedmetadata=([^ ]+) )?(?:srid=([0-9]+) )?(?:type=([a-zA-Z]+) )?(?:table=\"(.+)\" \()?(?:([^ ]+)\) )?(?:sql=(.*))?"
        result = re.findall(r'%s' % reg, uri)
        if not result:
            return None

        res = result[0]
        if not res:
            return None

        dbname = res[0]
        host = res[1]
        port = res[2]
        user = res[3]
        password = res[4]
        sslmode = res[5]
        key = res[6]
        estimatedmetadata = res[7]
        srid = res[8]
        gtype = res[9]
        table = res[10]
        geocol = res[11]
        sql = res[12]

        schema = ''

        if ' FROM ' not in table:
            if re.search('"\."', table):
                table = '"' + table + '"'
                sp = table.replace('"', '').split('.')
                schema = sp[0]
                table = sp[1]
        else:
            reg = r'\* FROM ([^\)]+)?(\))?'
            f = re.findall(r'%s' % reg, table)

            if f and f[0]:
                sp = f[0][0].replace('"', '').split('.')
                if len(sp) > 1:
                    schema = sp[0].replace('\\', '')
                    table = sp[1]
                else:
                    table = sp[0]
            else:
                return None


        if layer.providerType() == u'postgres':
            dbType = 'postgis'
        else:
            dbType = 'spatialite'

        connectionParams = {
            'dbname' : dbname,
            'host' : host,
            'port': port,
            'user' : user,
            'password': password,
            'sslmode' : sslmode,
            'key': key,
            'estimatedmetadata' : estimatedmetadata,
            'srid' : srid,
            'type': gtype,
            'schema': schema,
            'table' : table,
            'geocol' : geocol,
            'sql' : sql,
            'dbType': dbType
        }

        return connectionParams

    def setSearchPath(self, sql, schema):
        '''
        Set the search_path parameters if postgis database
        '''
        prefix = u'SET search_path = "%s", public, pg_catalog;' % schema
        if re.search('^BEGIN;', sql):
            sql = sql.replace('BEGIN;', 'BEGIN;%s' % prefix)
        else:
            sql = prefix + sql

        return sql


    def fetchDataFromSqlQuery(self, connector, sql, schema=None):
        '''
        Execute a SQL query and
        return [header, data, rowCount]
        '''

        data = []
        header = []
        rowCount = 0
        c = None


        try:
            c = connector._execute(None,unicode(sql))
            data = []
            header = connector._get_cursor_columns(c)

            if header == None:
                header = []

            if len(header) > 0:
                data = connector._fetchall(c)

            rowCount = c.rowcount
            if rowCount == -1:
                rowCount = len(data)

        except BaseError as e:

            DlgDbError.showError(e, self.dialog)
            self.dialog.go = False
            try:
                self.updateLog(e.msg)
            except:
                print e.msg
            return

        finally:
            if c:
                c.close()
                del c

        return [header, data, rowCount]



    def getConnectorFromUri(self, connectionParams):
        '''
        Set connector property
        for the given database type
        and parameters
        '''
        uri = QgsDataSourceURI()
        if connectionParams['dbType'] == 'postgis':
            uri.setConnection(
                connectionParams['host'],
                connectionParams['port'],
                connectionParams['dbname'],
                connectionParams['user'],
                connectionParams['password']
            )
            connector = PostGisDBConnector(uri)

        if connectionParams['dbType'] == 'spatialite':
            uri.setConnection('', '', connectionParams['dbname'], '', '')
            if self.hasSpatialiteSupport():
                from db_manager.db_plugins.spatialite.connector import SpatiaLiteDBConnector
            connector = SpatiaLiteDBConnector(uri)

        return connector


    def chooseDataPath(self, key):
        '''
        Ask the user to select a folder
        and write down the path to appropriate field
        '''
        ipath = QFileDialog.getExistingDirectory(
            None,
            u"Choisir le répertoire contenant les fichiers",
            str(self.dialog.pathSelectors[key]['input'].text().encode('utf-8')).strip(' \t')
        )
        if os.path.exists(unicode(ipath)):
            self.dialog.pathSelectors[key]['input'].setText(unicode(ipath))



    def normalizeString(self, s):
        '''
        Removes all accents from
        the given string and
        replace e dans l'o
        '''
        p = re.compile( '(œ)')
        s = p.sub('oe', s)

        if isinstance(s,str):
            s = unicode(s,"utf8","replace")

        s=unicodedata.normalize('NFD',s)
        s = s.encode('ascii','ignore')
        s = s.upper().strip(' \t\n')
        r = re.compile(r"[^ -~]")
        s = r.sub(' ', s)
        s = s.replace("'", " ")

        return s


    def postgisToSpatialite(self, sql, targetSrid='2154'):
        '''
        Convert postgis SQL statement
        into spatialite compatible
        statements
        '''

        # delete some incompatible options
        # replace other by spatialite syntax
        replaceDict = [
            # delete
            {'in': r'with\(oids=.+\)', 'out': ''},
            {'in': r'comment on [^;]+;', 'out': ''},
            {'in': r'alter table ([^;]+) add primary key( )+\(([^;]+)\);',
            'out': r'create index idx_\1_\3 on \1 (\3);'},
            {'in': r'alter table ([^;]+) add constraint [^;]+ primary key( )+\(([^;]+)\);',
            'out': r'create index idx_\1_\3 on \1 (\3);'},
            {'in': r'alter table [^;]+drop column[^;]+;', 'out': ''},
            {'in': r'alter table [^;]+drop constraint[^;]+;', 'out': ''},
            #~ {'in': r'^analyse [^;]+;', 'out': ''},
            # replace
            {'in': r'truncate (bati|fanr|lloc|nbat|pdll|prop)',
            'out': r'drop table \1;create table \1 (tmp text)'},
            {'in': r'truncate ', 'out': 'delete from '},
            {'in': r'distinct on *\([a-z, ]+\)', 'out': 'distinct'},
            {'in': r'serial', 'out': 'INTEGER PRIMARY KEY AUTOINCREMENT'},
            {'in': r'current_schema::text, ', 'out': ''},
            {'in': r'substring', 'out': 'SUBSTR'},
            {'in': r"(to_char\()([^']+) *, *'[09]+' *\)", 'out': r"CAST(\2 AS TEXT)"},
            {'in': r"(to_number\()([^']+) *, *'[09]+' *\)", 'out': r"CAST(\2 AS float)"},
            {'in': r"(to_date\()([^']+) *, *'DDMMYYYY' *\)",
            'out': r"date(substr(\2, 5, 4) || '-' || substr(\2, 3, 2) || '-' || substr(\2, 1, 2))"},
            {'in': r"(to_date\()([^']+) *, *'DD/MM/YYYY' *\)",
            'out': r"date(substr(\2, 7, 4) || '-' || substr(\2, 4, 2) || '-' || substr(\2, 1, 2))"},
            {'in': r"(to_date\()([^']+) *, *'YYYYMMDD' *\)",
            'out': r"date(substr(\2, 1, 4) || '-' || substr(\2, 5, 2) || '-' || substr(\2, 7, 2))"},
            {'in': r"(to_char\()([^']+) *, *'dd/mm/YYYY' *\)",
            'out': r"strftime('%d/%m/%Y', \2)"},
            {'in': r"ST_MakeValid\(geom\)",
             'out': r"CASE WHEN ST_IsValid(geom) THEN geom ELSE ST_Buffer(geom,0) END"},
            {'in': r"ST_MakeValid\(p\.geom\)",
             'out': r"CASE WHEN ST_IsValid(p.geom) THEN p.geom ELSE ST_Buffer(p.geom,0) END"}
        ]

        for a in replaceDict:
            r = re.compile(a['in'], re.IGNORECASE|re.MULTILINE)
            sql = r.sub(a['out'], sql)
            #~ self.updateLog(sql)

        # index spatiaux
        r = re.compile(r'(create index [^;]+ ON )([^;]+)( USING +)(gist +)?\(([^;]+)\);',  re.IGNORECASE|re.MULTILINE)
        sql = r.sub(r"SELECT createSpatialIndex('\2', '\5');", sql)

        # replace postgresql "update from" statement
        r = re.compile(r'(update [^;=]+)(=)([^;=]+ FROM [^;]+)(;)', re.IGNORECASE|re.MULTILINE)
        sql = r.sub(r'\1=(SELECT \3);', sql)

        # majic formatage : replace multiple column update for loca10
        r = re.compile(r'update local10 set[^;]+;',  re.IGNORECASE|re.MULTILINE)
        res = r.findall(sql)
        replaceBy = ''
        for statement in res:
            replaceBy = '''
            CREATE TABLE ll AS
            SELECT DISTINCT l.invar, l.ccopre , l.ccosec, l.dnupla, l.ccoriv, l.ccovoi, l.dnvoiri, l10.annee || l10.invar AS local00, REPLACE(l10.annee||l10.ccodep || l10.ccodir || l10.ccocom || l.ccopre || l.ccosec || l.dnupla,' ', '0') AS parcelle, REPLACE(l10.annee || l10.ccodep ||  l10.ccodir || l10.ccocom || l.ccovoi,' ', '0') AS voie
            FROM local00 l
            INNER JOIN local10 AS l10 ON l.invar = l10.invar AND l.annee = l10.annee
            WHERE l10.annee='?';
            CREATE INDEX  idx_ll_invar ON ll (invar);
            UPDATE local10 SET ccopre = (SELECT DISTINCT ll.ccopre FROM ll WHERE ll.invar = local10.invar)
            WHERE local10.annee = '?';
            UPDATE local10 SET ccosec = (SELECT DISTINCT ll.ccosec FROM ll WHERE ll.invar = local10.invar)
            WHERE local10.annee = '?';
            UPDATE local10 SET dnupla = (SELECT DISTINCT ll.dnupla FROM ll WHERE ll.invar = local10.invar)
            WHERE local10.annee = '?';
            UPDATE local10 SET ccoriv = (SELECT DISTINCT ll.ccoriv FROM ll WHERE ll.invar = local10.invar)
            WHERE local10.annee = '?';
            UPDATE local10 SET ccovoi = (SELECT DISTINCT ll.ccovoi FROM ll WHERE ll.invar = local10.invar)
            WHERE local10.annee = '?';
            UPDATE local10 SET dnvoiri = (SELECT DISTINCT ll.dnvoiri FROM ll WHERE ll.invar = local10.invar)
            WHERE local10.annee = '?';
            UPDATE local10 SET local00 = (SELECT DISTINCT ll.local00 FROM ll WHERE ll.invar = local10.invar)
            WHERE local10.annee = '?';
            UPDATE local10 SET parcelle = (SELECT DISTINCT ll.parcelle FROM ll WHERE ll.invar = local10.invar)
            WHERE local10.annee = '?';
            UPDATE local10 SET voie = (SELECT DISTINCT ll.voie FROM ll WHERE ll.invar = local10.invar)
            WHERE local10.annee = '?';
            DROP TABLE ll;
            '''
            replaceBy = replaceBy.replace('?', self.dialog.dataYear)
            sql = sql.replace(statement, replaceBy)

        #~ self.updateLog(sql)
        return sql


    def createNewSpatialiteDatabase(self):
        '''
        Choose a file path to save
        create the sqlite database with
        spatial tools and create QGIS connection
        '''
        # Let the user choose new file path
        ipath = QFileDialog.getSaveFileName (
            None,
            u"Choisir l'emplacement du nouveau fichier",
            str(os.path.expanduser("~").encode('utf-8')).strip(' \t'),
            "Sqlite database (*.sqlite)"
        )
        if not ipath:
            self.updateLog(u"Aucune base de données créée (annulation)")
            return None

        # Delete file if exists (question already asked above)
        if os.path.exists(unicode(ipath)):
            os.remove(unicode(ipath))

        # Create the spatialite database
        try:
            from pyspatialite import dbapi2 as db

            # Create a connection (which will create the file automatically)
            conn=db.connect(unicode(ipath))
            c=conn.cursor()

            # Get spatialite version
            cursor = conn.execute('SELECT spatialite_version()')
            rep = cursor.fetchall()
            v = [int(a) for a in rep[0][0].split('.')]
            vv = v[0] * 100000 + v[1] * 1000 + v[2] * 10

            # Add spatialite support
            if vv >= 401000:
                # 4.1 and above
                sql = "SELECT initspatialmetadata(1)"
            else:
                # Under 4.1
                sql = "SELECT initspatialmetadata()"
            c.execute(sql)
        except:
            self.updateLog(u"Échec lors de la création du fichier Spatialite !")
            return None
        finally:
            conn.close()
            del conn

        # Create QGIS connexion
        baseKey = "/SpatiaLite/connections/"
        settings = QSettings()
        myName = os.path.basename(ipath);
        baseKey+= myName;
        myFi = QFileInfo(ipath)
        settings.setValue( baseKey + "/sqlitepath", myFi.canonicalFilePath());

        # Update connections combo box and set new db selected
        self.updateConnectionList()
        listDic = { self.dialog.connectionDbList[i]:i for i in range(0, len(self.dialog.connectionDbList)) }
        self.dialog.liDbConnection.setCurrentIndex(listDic[myName])


    def getCompteCommunalFromParcelleId(self, parcelleId, connectionParams, connector):

        comptecommunal = None

        sql = "SELECT comptecommunal FROM parcelle WHERE parcelle = '%s'" % parcelleId
        if connectionParams['dbType'] == 'postgis':
            sql = self.setSearchPath(sql, connectionParams['schema'])
        [header, data, rowCount] = self.fetchDataFromSqlQuery(connector, sql)
        for line in data:
            comptecommunal = line[0]

        return comptecommunal

class cadastre_import_cli(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.iface = None

        self.connectionDbList = []
        # common cadastre methods
        self.qc = cadastre_common(self)

        # Set initial values
        self.doMajicImport = False
        self.doEdigeoImport = False
        self.dataVersion = None
        self.dataYear = None
        self.dbType = None
        self.dbpluginclass = None
        self.connectionName = None
        self.connection = None
        self.db = None
        self.schema = None
        self.schemaList = None
        self.hasStructure = None
        self.hasData = None
        self.hasMajicData = None
        self.hasMajicDataParcelle = None
        self.hasMajicDataVoie = None
        self.hasMajicDataProp = None
        self.edigeoSourceProj = None
        self.edigeoTargetProj = None
        self.edigeoDepartement = None
        self.edigeoDirection = None
        self.edigeoLot = None
        self.majicSourceDir = None
        self.edigeoSourceDir = None
        self.edigeoMakeValid = False

        # set input values from settings

        cfg = os.getenv('QADASTRECFG','config.ini')
        s = QSettings(cfg, QSettings.IniFormat)
        print "Using this config file for import parameters: "+cfg

    def onClose(self):
        '''
        Close dialog
        '''
        if self.db:
            self.db.connector.__del__()

        self.close()


    def getValuesFromSettings(self):
        '''
        get values from QGIS settings
        and set input fields appropriately
        '''
        s = QSettings()
        for k,v in self.sList.items():
            value = s.value("cadastre/%s" % k, '', type=str)
            if value and value != 'None' and v['widget']:
                if v['wType'] == 'text':
                    v['widget'].setText(value)
                if v['wType'] == 'spinbox':
                    v['widget'].setValue(int(value))
                if v['wType'] == 'combobox':
                    listDic = {v['list'][i]:i for i in range(0, len(v['list']))}
                    v['widget'].setCurrentIndex(listDic[value])


    def createSchema(self):
        if self.db == None:
            print "No database selected or you are not connected to it."
            return
        schema = self.inDbCreateSchema.text()

        if schema:
            try:
                self.db.createSchema(schema)

            except BaseError as e:

                DlgDbError.showError(e, self)
                self.qc.updateLog(e.msg)
                return

            finally:
                self.qc.updateSchemaList()
                listDic = { self.schemaList[i]:i for i in range(0, len(self.schemaList)) }
                self.liDbSchema.setCurrentIndex(listDic[schema])
                self.inDbCreateSchema.clear()


    def chooseProjection(self, key):
        '''
        Let the user choose a SCR
        '''
        header = u"Choisir la projection"
        sentence = self.projSelectors[key]['sentence']
        projSelector = QgsGenericProjectionSelector(self)
        projSelector.setMessage( "<h2>%s</h2>%s" % (header.encode('UTF8'), sentence.encode('UTF8')) )
        projSelector.setSelectedAuthId(self.qc.defaultAuthId)
        if projSelector.exec_():
            self.crs = QgsCoordinateReferenceSystem( projSelector.selectedCrsId(), QgsCoordinateReferenceSystem.InternalCrsId )
            if len(projSelector.selectedAuthId()) == 0:
                print self.tr(u"Aucun système de coordonnée de référence valide n'a été sélectionné")
                return
            else:
                self.projSelectors[key]['input'].clear()
                self.projSelectors[key]['input'].setText(self.crs.authid() + " - " + self.crs.description())
        else:
            return

    def checkImportInputData(self):
        '''
        Check the user defined inpu data
        '''

        s = QSettings(os.getenv('QADASTRECFG','config.ini'), QSettings.IniFormat)
        self.dataVersion = str(s.value('cadastre/dataVersion', '2014', type=str))
        self.dataYear = str(s.value('cadastre/dataYear','2014', type=str))
        self.majicSourceDir = str(s.value('cadastre/majicSourceDir','/tmp/qadastre/majic', type=str))
        self.edigeoSourceDir = str(s.value('cadastre/edigeoSourceDir','/tmp/qadastre/edigeo', type=str))
        self.edigeoDepartement = str(s.value('cadastre/edigeoDepartement','xx', type=str))
        self.edigeoDirection = str(s.value('cadastre/edigeoDirection','0', type=str))
        self.edigeoLot = str(s.value('cadastre/edigeoLot','0', type=str))
        self.edigeoSourceProj = str(s.value('cadastre/edigeoSourceProj','EPSG:2154', type=str))
        self.edigeoTargetProj = str(s.value('cadastre/edigeoTargetProj','EPSG:2154', type=str))
        self.connectionName = str(s.value('PostgreSQL/connections/selected','qadastre', type=str))
        self.schema = str(s.value('PostgreSQL/connections/%s/schema' % self.connectionName,'public', type=str))
        self.dbType = u'postgis'

        # defined properties
        self.doMajicImport = os.path.exists(self.majicSourceDir)
        self.doEdigeoImport =  os.path.exists(self.edigeoSourceDir)

#        if self.cbMakeValid.isChecked():
#            self.edigeoMakeValid = True

        msg = ''
        if not self.connectionName:
            msg+= u'Veuillez sélectionner une base de données\n'

        if not self.doMajicImport and not self.doEdigeoImport:
            msg+= u'Veuillez sélectionner le chemin vers les fichiers à importer !\n'

        if self.edigeoSourceDir and not self.doEdigeoImport:
            msg+= u"Le chemin spécifié pour les fichiers EDIGEO n'existe pas\n"

        if self.majicSourceDir and not self.doMajicImport:
            msg+= u"Le chemin spécifié pour les fichiers MAJIC n'existe pas\n"

        if self.doEdigeoImport and not self.edigeoSourceProj:
            msg+= u'La projection source doit être renseignée !\n'
        if self.doEdigeoImport and not self.edigeoTargetProj:
            msg+= u'La projection cible doit être renseignée !\n'
        if len(self.edigeoDepartement) != 2 :
            msg+= u'Le département ne doit pas être vide !\n'
        if not self.edigeoDirection:
            msg+= u'La direction doit être un entier (0 par défaut) !\n'
        if not self.edigeoLot:
            msg+= u'Merci de renseigner un lot pour cet import (code commune, date d\'import, etc.)\n'

        self.qc.updateLog(msg.replace('\n','<br/>'))
        return msg

    def processImport(self):
        '''
        Lancement du processus d'import
        '''

        msg = self.checkImportInputData()
        if msg:
            print "critical:"+msg
            return

        dbpluginclass = createDbPlugin( self.dbType, self.connectionName )
        connection = dbpluginclass.connect()
        self.db = dbpluginclass.database()


        # cadastreImport instance
        qi = cadastreImport(self)

        # Check if structure already exists in the database/schema
        self.qc.checkDatabaseForExistingStructure()

        #~ # Run Script for creating tables
        if not self.hasStructure:
            qi.installOpencadastreStructure()

        # Run MAJIC import
        if self.doMajicImport:
            qi.importMajic()

        # Run Edigeo import
        if self.doEdigeoImport:
                qi.importEdigeo()

        qi.endImport()


cii = cadastre_import_cli()
cii.processImport()
