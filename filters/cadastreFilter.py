# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Cadastre - Export method class
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
# import shutil
from qgis.server import QgsServerFilter

from PyQt4.QtCore import (
    QFileInfo,
    QByteArray
)
from PyQt4.QtXml import QDomDocument

from qgis.core import (
    QgsProject,
    QgsMessageLog,
    QgsLogger,
    QgsMapLayer,
    QgsVectorLayer,
    QgsMapLayerRegistry,
    QgsFeatureRequest
)
from qgis.gui import (
    QgsMapCanvas,
    QgsLayerTreeMapCanvasBridge,
    QgsLayerTreeView
)
from cadastre.cadastre_dialogs import cadastre_common
from cadastre.cadastre_export import (
    cadastreExport
)
try:
    from cadastre_export import cadastrePrintProgress
except:
    pass

import os.path, json, time
from uuid import uuid4
import tempfile

class cadastreFilter(QgsServerFilter):

    def __init__(self, serverIface):
        super(cadastreFilter, self).__init__(serverIface)
        self.serverIface = serverIface
        self.request = None
        self.project = None
        self.projectPath = None
        self.layer = None
        self.connectionParams = None
        self.connector = None
        self.debugMode = True

    def setJsonResponse(self, status, body):
        '''
        Set response with given parameters
        '''
        self.request.clearHeaders()
        self.request.setInfoFormat('text/json')
        self.request.setHeader('Content-type', 'text/json')
        self.request.setHeader('Status', status)
        self.request.clearBody()
        self.request.appendBody( json.dumps( body ) )

    def responseComplete(self):
        self.request = self.serverIface.requestHandler()
        params = self.request.parameterMap( )

        # Check if needed params are passed
        # If not, do not change QGIS Server response
        if params['SERVICE'].lower() != 'cadastre':
            return

        # Check if request is passed
        if 'REQUEST' not in params:
            body = {
                'status': 'fail',
                'message': 'Missing parameters REQUEST: must be CreatePdf or GetPdf ',
            }
            self.setJsonResponse( '200', body)
            return

        prequest = params['REQUEST']
        if prequest.lower() not in ('createpdf', 'getpdf'):
            body = {
                'status': 'fail',
                'message': 'Missing parameters REQUEST: must be CreatePdf or GetPdf ',
            }
            self.setJsonResponse( '200', body)
            return

        # Conditionnal response based on request
        if prequest.lower() == 'createpdf':
            self.createPdf()
            return

        if prequest.lower() == 'getpdf':
            self.getPdf()
            return

    def createPdf(self):
        '''
        Create a PDF from cadastre data
        '''
        params = self.request.parameterMap( )

        # Check if needed params are set
        if 'LAYER' not in params or 'PARCELLE' not in params or 'TYPE' not in params or 'MAP' not in params:
            body = {
                'status': 'fail',
                'message': 'Missing parameters: MAP, LAYER, PARCELLE, TYPE are required '
            }
            self.setJsonResponse( '200', body)
            return

        # Get layer and expression
        pmap = params['MAP']
        player = params['LAYER']
        pparcelle = params['PARCELLE']
        ptype = params['TYPE']

        # Check type
        if ptype.lower() not in ('parcelle', 'proprietaire'):
            QgsMessageLog.logMessage( "Cadastre - Parameter TYPE must be parcelle or proprietaire")
            body = {
                'status': 'fail',
                'message': 'Parameter TYPE must be parcelle or proprietaire'
            }
            self.setJsonResponse( '200', body)
            return

        # Open project
        self.projectPath = pmap
        pfile = QFileInfo( pmap )
        p = QgsProject.instance()
        p.read(pfile)

        # Find layer
        lr = QgsMapLayerRegistry.instance()
        layerList = [ layer for lname,layer in lr.mapLayers().items() if layer.name() == player ]
        if len(layerList ) != 1:
            QgsMessageLog.logMessage( "Cadastre - layer %s not in project" % player)
            body = {
                'status': 'fail',
                'message': 'The source layer cannot be found in the project'
            }
            self.setJsonResponse( '200', body)
            return
        layer = layerList[0]

        # Get feature
        import re
        pattern = re.compile("^([A-Z0-9]+)*$")
        if not pattern.match(pparcelle):
            QgsMessageLog.logMessage( "Cadastre - PARCELLE has not the correct format")
            body = {
                'status': 'fail',
                'message': 'PARCELLE has not the correct format'
            }
            self.setJsonResponse('200', body)
            return

        if self.debugMode:
            QgsMessageLog.logMessage( "cadastre debug - layer = %s  - geo_parcelle = %s" % ( layer.name(), pparcelle ))

        req = QgsFeatureRequest()
        req.setFilterExpression(' "geo_parcelle" = \'%s\' ' % pparcelle)

        it = layer.getFeatures(req)
        feat = None
        for f in it:
            feat = f
            break
        if not feat:
            QgsMessageLog.logMessage( "CADASTRE - No feature found for layer %s and parcelle %s" % (player, pparcelle))
            body = {
                'status': 'fail',
                'message': 'No feature found for layer %s and parcelle %s' % (player, pparcelle)
            }
            self.setJsonResponse('200', body)
            return

        if self.debugMode:
            QgsMessageLog.logMessage( "cadastre debug - feature geo_parcelle = %s" % feat['geo_parcelle'])


        # Get layer connection parameters
        self.connectionParams = cadastre_common.getConnectionParameterFromDbLayer(layer)
        if self.debugMode:
            QgsMessageLog.logMessage( "cadastre debug - connection params = %s" % self.connectionParams )

        self.connector = cadastre_common.getConnectorFromUri( self.connectionParams )
        if self.debugMode:
            QgsMessageLog.logMessage( "cadastre debug - after getting connector" )

        # Get compte communal
        comptecommunal = cadastre_common.getCompteCommunalFromParcelleId(
            feat['geo_parcelle'],
            self.connectionParams,
            self.connector
        )
        pmulti = 1
        if ptype == 'proprietaire' and pmulti == 1:
            comptecommunal = cadastre_common.getProprietaireComptesCommunaux(
                comptecommunal,
                self.connectionParams,
                self.connector
            )
        if self.debugMode:
            QgsMessageLog.logMessage( "cadastre debug - comptecommunal = %s" % comptecommunal )

        # Export PDF
        qex = cadastreExport(
            layer,
            ptype,
            comptecommunal,
            feat['geo_parcelle']
        )
        if self.debugMode:
            QgsMessageLog.logMessage( "cadastre debug - after instanciating cadastreExport" )

        paths = qex.exportAsPDF()
        if self.debugMode:
            QgsMessageLog.logMessage( "cadastre debug - after exportAsPDF(), path: %s" % paths )

        if paths:
            tokens = []
            for path in paths:
                uid = uuid4()

                if self.debugMode:
                    QgsMessageLog.logMessage( "cadastre debug - item path: %s" % path )
                newpath = os.path.join(
                    # '/srv/qgis/temp/',
                    tempfile.gettempdir(),
                    '%s.pdf' % uid
                )
                if self.debugMode:
                    QgsMessageLog.logMessage( "cadastre debug - item newpath: %s" % newpath )

                # shutil.copy(path,newpath)
                os.rename(path,newpath)
                tokens.append( str(uid) )

            body = {
                'status': 'success',
                'message': 'PDF generated',
                'data': {
                    'url': {
                        'request': 'getPdf',
                        'service': 'cadastre',
                        'token': None
                    },
                    'tokens': tokens
                }
            }

            self.setJsonResponse( '200', body)
            return
        else:
            QgsMessageLog.logMessage( "CADASTRE - Error during export: no PDF output")
            body = {
                'status': 'fail',
                'message': 'An error occured while generating the PDF'
            }
            self.setJsonResponse( '200', body)
            return



    def getPdf(self):
        '''
        Get PDF files previously exported
        '''
        params = self.request.parameterMap( )

        # Check if needed params are set
        if 'TOKEN' not in params:
            body = {
                'status': 'fail',
                'message': 'Missing parameter: token',
            }
            self.setJsonResponse( '200', body)
            return

        ptoken = params['TOKEN']
        path = os.path.join(
            # '/srv/qgis/temp/',
            tempfile.gettempdir(),
            '%s.pdf' % ptoken
        )
        if self.debugMode:
            QgsMessageLog.logMessage( "cadastre debug - GetPDF = path is %s" % path )
        if not os.path.exists(path):
            body = {
                'status': 'fail',
                'message': 'PDF does not exists',
            }
            self.setJsonResponse( '200', body)
            return

        if self.debugMode:
            QgsMessageLog.logMessage( "cadastre debug - GetPDF = path exists %s" % path )

        # Send PDF
        self.request.clearHeaders()
        self.request.setInfoFormat('application/pdf')
        self.request.setHeader('Content-type', 'application/pdf')
        self.request.setHeader('Status', '200')
        self.request.clearBody()
        try:
            with open(path, 'rb') as f:
                loads = f.readlines()
                ba = QByteArray(b''.join(loads))
                self.request.appendBody(ba)
            return
        except:
            body = {
                'status': 'fail',
                'message': 'Error occured while reading PDF file',
            }
            self.setJsonResponse( '200', body)
            return
        finally:
            # print("path to remove : %s" % path)
            os.remove(path)
        return
