# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/build/qgis-3.4.10+14stretch/python/plugins/db_manager/ui/DlgSqlWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DbManagerDlgSqlWindow(object):
    def setupUi(self, DbManagerDlgSqlWindow):
        DbManagerDlgSqlWindow.setObjectName("DbManagerDlgSqlWindow")
        DbManagerDlgSqlWindow.resize(679, 525)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DbManagerDlgSqlWindow.sizePolicy().hasHeightForWidth())
        DbManagerDlgSqlWindow.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QtWidgets.QGridLayout(DbManagerDlgSqlWindow)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(DbManagerDlgSqlWindow)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.queryBuilderBtn = QtWidgets.QToolButton(self.widget)
        self.queryBuilderBtn.setText("")
        self.queryBuilderBtn.setObjectName("queryBuilderBtn")
        self.horizontalLayout.addWidget(self.queryBuilderBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.presetCombo = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presetCombo.sizePolicy().hasHeightForWidth())
        self.presetCombo.setSizePolicy(sizePolicy)
        self.presetCombo.setObjectName("presetCombo")
        self.horizontalLayout.addWidget(self.presetCombo)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.presetName = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presetName.sizePolicy().hasHeightForWidth())
        self.presetName.setSizePolicy(sizePolicy)
        self.presetName.setText("")
        self.presetName.setObjectName("presetName")
        self.horizontalLayout.addWidget(self.presetName)
        self.presetStore = QtWidgets.QPushButton(self.widget)
        self.presetStore.setObjectName("presetStore")
        self.horizontalLayout.addWidget(self.presetStore)
        self.presetDelete = QtWidgets.QPushButton(self.widget)
        self.presetDelete.setObjectName("presetDelete")
        self.horizontalLayout.addWidget(self.presetDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.splitterHistory = QtWidgets.QSplitter(self.widget)
        self.splitterHistory.setOrientation(QtCore.Qt.Horizontal)
        self.splitterHistory.setHandleWidth(2)
        self.splitterHistory.setObjectName("splitterHistory")
        self.editSql = QgsCodeEditorSQL(self.splitterHistory)
        self.editSql.setObjectName("editSql")
        self.queryHistoryWidget = QtWidgets.QWidget(self.splitterHistory)
        self.queryHistoryWidget.setObjectName("queryHistoryWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.queryHistoryWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.queryHistoryTableWidget = QtWidgets.QTableWidget(self.queryHistoryWidget)
        self.queryHistoryTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.queryHistoryTableWidget.setAlternatingRowColors(True)
        self.queryHistoryTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.queryHistoryTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.queryHistoryTableWidget.setObjectName("queryHistoryTableWidget")
        self.queryHistoryTableWidget.setColumnCount(3)
        self.queryHistoryTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.queryHistoryTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.queryHistoryTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.queryHistoryTableWidget.setHorizontalHeaderItem(2, item)
        self.queryHistoryTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.queryHistoryTableWidget, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.splitterHistory)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.btnExecute = QtWidgets.QPushButton(self.widget)
        self.btnExecute.setObjectName("btnExecute")
        self.buttonLayout.addWidget(self.btnExecute)
        self.lblResult = QtWidgets.QLabel(self.widget)
        self.lblResult.setText("")
        self.lblResult.setObjectName("lblResult")
        self.buttonLayout.addWidget(self.lblResult)
        self.btnCreateView = QtWidgets.QPushButton(self.widget)
        self.btnCreateView.setObjectName("btnCreateView")
        self.buttonLayout.addWidget(self.btnCreateView)
        self.btnClear = QtWidgets.QPushButton(self.widget)
        self.btnClear.setObjectName("btnClear")
        self.buttonLayout.addWidget(self.btnClear)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem1)
        self.btnQueryHistory = QtWidgets.QPushButton(self.widget)
        self.btnQueryHistory.setCheckable(True)
        self.btnQueryHistory.setObjectName("btnQueryHistory")
        self.buttonLayout.addWidget(self.btnQueryHistory)
        self.verticalLayout_2.addLayout(self.buttonLayout)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.viewResult = QtWidgets.QTableView(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.viewResult.sizePolicy().hasHeightForWidth())
        self.viewResult.setSizePolicy(sizePolicy)
        self.viewResult.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.viewResult.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.viewResult.setObjectName("viewResult")
        self.verticalLayout.addWidget(self.viewResult)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.loadAsLayerGroup = QtWidgets.QGroupBox(DbManagerDlgSqlWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadAsLayerGroup.sizePolicy().hasHeightForWidth())
        self.loadAsLayerGroup.setSizePolicy(sizePolicy)
        self.loadAsLayerGroup.setCheckable(True)
        self.loadAsLayerGroup.setChecked(True)
        self.loadAsLayerGroup.setObjectName("loadAsLayerGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.loadAsLayerGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.loadAsLayerWidget = QtWidgets.QWidget(self.loadAsLayerGroup)
        self.loadAsLayerWidget.setObjectName("loadAsLayerWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.loadAsLayerWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.getColumnsBtn = QtWidgets.QPushButton(self.loadAsLayerWidget)
        self.getColumnsBtn.setObjectName("getColumnsBtn")
        self.gridLayout_3.addWidget(self.getColumnsBtn, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        self.btnSetFilter = QtWidgets.QPushButton(self.loadAsLayerWidget)
        self.btnSetFilter.setAutoDefault(False)
        self.btnSetFilter.setObjectName("btnSetFilter")
        self.gridLayout_3.addWidget(self.btnSetFilter, 1, 3, 1, 1)
        self.loadLayerBtn = QtWidgets.QPushButton(self.loadAsLayerWidget)
        self.loadLayerBtn.setObjectName("loadLayerBtn")
        self.gridLayout_3.addWidget(self.loadLayerBtn, 2, 3, 1, 1)
        self.avoidSelectById = QtWidgets.QCheckBox(self.loadAsLayerWidget)
        self.avoidSelectById.setObjectName("avoidSelectById")
        self.gridLayout_3.addWidget(self.avoidSelectById, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.loadAsLayerWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.layerNameEdit = QtWidgets.QLineEdit(self.loadAsLayerWidget)
        self.layerNameEdit.setEnabled(True)
        self.layerNameEdit.setText("")
        self.layerNameEdit.setObjectName("layerNameEdit")
        self.horizontalLayout_7.addWidget(self.layerNameEdit)
        self.layerTypeWidget = QtWidgets.QWidget(self.loadAsLayerWidget)
        self.layerTypeWidget.setObjectName("layerTypeWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layerTypeWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layerTypeWidget)
        self.label_6.setIndent(40)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.vectorRadio = QtWidgets.QRadioButton(self.layerTypeWidget)
        self.vectorRadio.setChecked(True)
        self.vectorRadio.setObjectName("vectorRadio")
        self.horizontalLayout_3.addWidget(self.vectorRadio)
        self.rasterRadio = QtWidgets.QRadioButton(self.layerTypeWidget)
        self.rasterRadio.setObjectName("rasterRadio")
        self.horizontalLayout_3.addWidget(self.rasterRadio)
        self.horizontalLayout_7.addWidget(self.layerTypeWidget)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.uniqueColumnCheck = QtWidgets.QCheckBox(self.loadAsLayerWidget)
        self.uniqueColumnCheck.setObjectName("uniqueColumnCheck")
        self.horizontalLayout_6.addWidget(self.uniqueColumnCheck)
        self.uniqueCombo = QtWidgets.QComboBox(self.loadAsLayerWidget)
        self.uniqueCombo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uniqueCombo.sizePolicy().hasHeightForWidth())
        self.uniqueCombo.setSizePolicy(sizePolicy)
        self.uniqueCombo.setEditable(True)
        self.uniqueCombo.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.uniqueCombo.setObjectName("uniqueCombo")
        self.horizontalLayout_6.addWidget(self.uniqueCombo)
        self.hasGeometryCol = QtWidgets.QCheckBox(self.loadAsLayerWidget)
        self.hasGeometryCol.setChecked(True)
        self.hasGeometryCol.setTristate(False)
        self.hasGeometryCol.setObjectName("hasGeometryCol")
        self.horizontalLayout_6.addWidget(self.hasGeometryCol)
        self.geomCombo = QtWidgets.QComboBox(self.loadAsLayerWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geomCombo.sizePolicy().hasHeightForWidth())
        self.geomCombo.setSizePolicy(sizePolicy)
        self.geomCombo.setEditable(True)
        self.geomCombo.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.geomCombo.setObjectName("geomCombo")
        self.horizontalLayout_6.addWidget(self.geomCombo)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.loadAsLayerWidget, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.loadAsLayerGroup, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.progressBar = QtWidgets.QProgressBar(DbManagerDlgSqlWindow)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.btnCancel = QtWidgets.QPushButton(DbManagerDlgSqlWindow)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_4.addWidget(self.btnCancel)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.retranslateUi(DbManagerDlgSqlWindow)
        self.loadAsLayerGroup.toggled['bool'].connect(self.avoidSelectById.setVisible)
        self.hasGeometryCol.toggled['bool'].connect(self.geomCombo.setEnabled)
        self.uniqueColumnCheck.toggled['bool'].connect(self.uniqueCombo.setEnabled)
        self.loadAsLayerGroup.toggled['bool'].connect(self.loadAsLayerWidget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgSqlWindow)
        DbManagerDlgSqlWindow.setTabOrder(self.queryBuilderBtn, self.presetCombo)
        DbManagerDlgSqlWindow.setTabOrder(self.presetCombo, self.presetName)
        DbManagerDlgSqlWindow.setTabOrder(self.presetName, self.presetStore)
        DbManagerDlgSqlWindow.setTabOrder(self.presetStore, self.presetDelete)
        DbManagerDlgSqlWindow.setTabOrder(self.presetDelete, self.editSql)
        DbManagerDlgSqlWindow.setTabOrder(self.editSql, self.btnExecute)
        DbManagerDlgSqlWindow.setTabOrder(self.btnExecute, self.btnCreateView)
        DbManagerDlgSqlWindow.setTabOrder(self.btnCreateView, self.btnClear)
        DbManagerDlgSqlWindow.setTabOrder(self.btnClear, self.viewResult)
        DbManagerDlgSqlWindow.setTabOrder(self.viewResult, self.loadAsLayerGroup)
        DbManagerDlgSqlWindow.setTabOrder(self.loadAsLayerGroup, self.uniqueColumnCheck)
        DbManagerDlgSqlWindow.setTabOrder(self.uniqueColumnCheck, self.uniqueCombo)
        DbManagerDlgSqlWindow.setTabOrder(self.uniqueCombo, self.hasGeometryCol)
        DbManagerDlgSqlWindow.setTabOrder(self.hasGeometryCol, self.geomCombo)
        DbManagerDlgSqlWindow.setTabOrder(self.geomCombo, self.getColumnsBtn)
        DbManagerDlgSqlWindow.setTabOrder(self.getColumnsBtn, self.layerNameEdit)
        DbManagerDlgSqlWindow.setTabOrder(self.layerNameEdit, self.vectorRadio)
        DbManagerDlgSqlWindow.setTabOrder(self.vectorRadio, self.rasterRadio)
        DbManagerDlgSqlWindow.setTabOrder(self.rasterRadio, self.btnSetFilter)
        DbManagerDlgSqlWindow.setTabOrder(self.btnSetFilter, self.avoidSelectById)
        DbManagerDlgSqlWindow.setTabOrder(self.avoidSelectById, self.loadLayerBtn)

    def retranslateUi(self, DbManagerDlgSqlWindow):
        _translate = QtCore.QCoreApplication.translate
        DbManagerDlgSqlWindow.setWindowTitle(_translate("DbManagerDlgSqlWindow", "SQL Window"))
        self.label.setText(_translate("DbManagerDlgSqlWindow", "Saved query"))
        self.label_2.setText(_translate("DbManagerDlgSqlWindow", "Name"))
        self.presetStore.setText(_translate("DbManagerDlgSqlWindow", "Save"))
        self.presetDelete.setText(_translate("DbManagerDlgSqlWindow", "Delete"))
        item = self.queryHistoryTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DbManagerDlgSqlWindow", "Query"))
        item = self.queryHistoryTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DbManagerDlgSqlWindow", "Rows affected"))
        item = self.queryHistoryTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DbManagerDlgSqlWindow", "Duration (secs)"))
        self.btnExecute.setToolTip(_translate("DbManagerDlgSqlWindow", "Execute query (Ctrl+R)"))
        self.btnExecute.setText(_translate("DbManagerDlgSqlWindow", "Execute"))
        self.btnExecute.setShortcut(_translate("DbManagerDlgSqlWindow", "Ctrl+R"))
        self.btnCreateView.setText(_translate("DbManagerDlgSqlWindow", "Create a view"))
        self.btnClear.setText(_translate("DbManagerDlgSqlWindow", "&Clear"))
        self.btnQueryHistory.setText(_translate("DbManagerDlgSqlWindow", "Query History"))
        self.loadAsLayerGroup.setTitle(_translate("DbManagerDlgSqlWindow", "Load as new layer"))
        self.getColumnsBtn.setText(_translate("DbManagerDlgSqlWindow", "Retrieve \n"
"columns"))
        self.btnSetFilter.setText(_translate("DbManagerDlgSqlWindow", "Set filter"))
        self.loadLayerBtn.setText(_translate("DbManagerDlgSqlWindow", "Load"))
        self.avoidSelectById.setToolTip(_translate("DbManagerDlgSqlWindow", "<html><head/><body><p>Avoid selecting feature by id. Sometimes - especially when running expensive queries/views - fetching the data sequentially instead of fetching features by id can be much quicker.</p></body></html>"))
        self.avoidSelectById.setText(_translate("DbManagerDlgSqlWindow", "Avoid selecting by feature id"))
        self.label_5.setText(_translate("DbManagerDlgSqlWindow", "Layer name (prefix)"))
        self.label_6.setText(_translate("DbManagerDlgSqlWindow", "Type"))
        self.vectorRadio.setText(_translate("DbManagerDlgSqlWindow", "Vector"))
        self.rasterRadio.setText(_translate("DbManagerDlgSqlWindow", "Raster"))
        self.uniqueColumnCheck.setText(_translate("DbManagerDlgSqlWindow", "Column(s) with \n"
"unique values"))
        self.hasGeometryCol.setText(_translate("DbManagerDlgSqlWindow", "Geometry column"))
        self.btnCancel.setToolTip(_translate("DbManagerDlgSqlWindow", "Cancel query (ESC)"))
        self.btnCancel.setText(_translate("DbManagerDlgSqlWindow", "Cancel"))

from qgis.gui import QgsCodeEditorSQL
