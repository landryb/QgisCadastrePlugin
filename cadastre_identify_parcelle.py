# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Cadastre - import main methods
                                 A QGIS plugin
 This plugins helps users to import the french land registry ('cadastre')
 into a database. It is meant to ease the use of the data in QGIs
 by providing search tools and appropriate layer symbology.
                              -------------------
        begin                : 2013-06-11
        copyright            : (C) 2013 by 3liz
        email                : info@3liz.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import (
    Qt,
    pyqtSignal
)
from PyQt4.QtGui import (
    QCursor,
    QPixmap
)
from qgis.core import (
    QgsMapLayer,
    QgsVectorLayer,
    QgsFeature,
    QgsFeatureRequest,
    QgsGeometry,
    QgsRectangle
)
from qgis.gui import (
    QgsMapTool
)
from cadastre_cursor import Cursor

class IdentifyParcelle(QgsMapTool):

    cadastreGeomIdentified = pyqtSignal(QgsVectorLayer, QgsFeature)

    def __init__(self, canvas, layer):

        super(QgsMapTool, self).__init__(canvas)
        self.canvas = canvas
        self.layer = layer
        self.cursor = QCursor(QPixmap(Cursor), 1, 6)

    def activate(self):
        self.canvas.setCursor(self.cursor)

    def canvasReleaseEvent(self, mouseEvent):

        layerData = []
        layer = self.layer

        if not layer:
            return

        if layer.type() != QgsMapLayer.VectorLayer:
            # Ignore this layer as it's not a vector
            return

        if layer.featureCount() == 0:
            # There are no features - skip
            return

        #~ layer.removeSelection()

        # Determine the location of the click in real-world coords
        point = self.toLayerCoordinates( layer, mouseEvent.pos() )
        pntGeom = QgsGeometry.fromPoint( point )
        pntBuff = pntGeom.buffer( ( self.canvas.mapUnitsPerPixel() * 2 ), 0 )
        rect = pntBuff.boundingBox()
        rq = QgsFeatureRequest( rect )
        selectList = []

        # Take first feature
        feature = None
        for feat in layer.getFeatures( rq ):
            if feat.geometry().intersects( pntGeom ):
                selectList.append( feat.id() )
                feature = feat
                break

        #~ layer.setSelectedFeatures( selectList )

        # Send signal
        if not feature:
            return

        self.cadastreGeomIdentified.emit( layer, feature )
