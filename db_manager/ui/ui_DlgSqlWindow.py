# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/usr/obj/qgis-2.6.1/qgis-2.6.1/python/plugins/db_manager/ui/DlgSqlWindow.ui'
#
# Created: Thu Mar  5 05:56:32 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DbManagerDlgSqlWindow(object):
    def setupUi(self, DbManagerDlgSqlWindow):
        DbManagerDlgSqlWindow.setObjectName(_fromUtf8("DbManagerDlgSqlWindow"))
        DbManagerDlgSqlWindow.resize(747, 525)
        self.gridLayout_2 = QtGui.QGridLayout(DbManagerDlgSqlWindow)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.splitter = QtGui.QSplitter(DbManagerDlgSqlWindow)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.presetName = QtGui.QLineEdit(self.layoutWidget)
        self.presetName.setText(_fromUtf8(""))
        self.presetName.setObjectName(_fromUtf8("presetName"))
        self.horizontalLayout.addWidget(self.presetName)
        self.presetCombo = QtGui.QComboBox(self.layoutWidget)
        self.presetCombo.setObjectName(_fromUtf8("presetCombo"))
        self.horizontalLayout.addWidget(self.presetCombo)
        self.presetStore = QtGui.QPushButton(self.layoutWidget)
        self.presetStore.setObjectName(_fromUtf8("presetStore"))
        self.horizontalLayout.addWidget(self.presetStore)
        self.presetDelete = QtGui.QPushButton(self.layoutWidget)
        self.presetDelete.setObjectName(_fromUtf8("presetDelete"))
        self.horizontalLayout.addWidget(self.presetDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.editSql = SqlEdit(self.layoutWidget)
        self.editSql.setObjectName(_fromUtf8("editSql"))
        self.verticalLayout_2.addWidget(self.editSql)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.btnExecute = QtGui.QPushButton(self.layoutWidget)
        self.btnExecute.setObjectName(_fromUtf8("btnExecute"))
        self.hboxlayout.addWidget(self.btnExecute)
        self.lblResult = QtGui.QLabel(self.layoutWidget)
        self.lblResult.setText(_fromUtf8(""))
        self.lblResult.setObjectName(_fromUtf8("lblResult"))
        self.hboxlayout.addWidget(self.lblResult)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.btnClear = QtGui.QPushButton(self.layoutWidget)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.hboxlayout.addWidget(self.btnClear)
        self.verticalLayout_2.addLayout(self.hboxlayout)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.viewResult = QtGui.QTableView(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.viewResult.sizePolicy().hasHeightForWidth())
        self.viewResult.setSizePolicy(sizePolicy)
        self.viewResult.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.viewResult.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.viewResult.setObjectName(_fromUtf8("viewResult"))
        self.verticalLayout.addWidget(self.viewResult)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DbManagerDlgSqlWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.loadAsLayerGroup = QtGui.QGroupBox(DbManagerDlgSqlWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadAsLayerGroup.sizePolicy().hasHeightForWidth())
        self.loadAsLayerGroup.setSizePolicy(sizePolicy)
        self.loadAsLayerGroup.setCheckable(True)
        self.loadAsLayerGroup.setChecked(True)
        self.loadAsLayerGroup.setObjectName(_fromUtf8("loadAsLayerGroup"))
        self.gridLayout = QtGui.QGridLayout(self.loadAsLayerGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.loadAsLayerWidget = QtGui.QWidget(self.loadAsLayerGroup)
        self.loadAsLayerWidget.setObjectName(_fromUtf8("loadAsLayerWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.loadAsLayerWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.loadAsLayerWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.uniqueCombo = QtGui.QComboBox(self.loadAsLayerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uniqueCombo.sizePolicy().hasHeightForWidth())
        self.uniqueCombo.setSizePolicy(sizePolicy)
        self.uniqueCombo.setEditable(True)
        self.uniqueCombo.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.uniqueCombo.setObjectName(_fromUtf8("uniqueCombo"))
        self.horizontalLayout_6.addWidget(self.uniqueCombo)
        self.label_3 = QtGui.QLabel(self.loadAsLayerWidget)
        self.label_3.setIndent(40)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.geomCombo = QtGui.QComboBox(self.loadAsLayerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geomCombo.sizePolicy().hasHeightForWidth())
        self.geomCombo.setSizePolicy(sizePolicy)
        self.geomCombo.setEditable(True)
        self.geomCombo.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.geomCombo.setObjectName(_fromUtf8("geomCombo"))
        self.horizontalLayout_6.addWidget(self.geomCombo)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.getColumnsBtn = QtGui.QPushButton(self.loadAsLayerWidget)
        self.getColumnsBtn.setObjectName(_fromUtf8("getColumnsBtn"))
        self.horizontalLayout_6.addWidget(self.getColumnsBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_5 = QtGui.QLabel(self.loadAsLayerWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.layerNameEdit = QtGui.QLineEdit(self.loadAsLayerWidget)
        self.layerNameEdit.setEnabled(True)
        self.layerNameEdit.setText(_fromUtf8(""))
        self.layerNameEdit.setObjectName(_fromUtf8("layerNameEdit"))
        self.horizontalLayout_7.addWidget(self.layerNameEdit)
        self.layerTypeWidget = QtGui.QWidget(self.loadAsLayerWidget)
        self.layerTypeWidget.setObjectName(_fromUtf8("layerTypeWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layerTypeWidget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_6 = QtGui.QLabel(self.layerTypeWidget)
        self.label_6.setIndent(40)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.vectorRadio = QtGui.QRadioButton(self.layerTypeWidget)
        self.vectorRadio.setChecked(True)
        self.vectorRadio.setObjectName(_fromUtf8("vectorRadio"))
        self.horizontalLayout_3.addWidget(self.vectorRadio)
        self.rasterRadio = QtGui.QRadioButton(self.layerTypeWidget)
        self.rasterRadio.setObjectName(_fromUtf8("rasterRadio"))
        self.horizontalLayout_3.addWidget(self.rasterRadio)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_7.addWidget(self.layerTypeWidget)
        self.loadLayerBtn = QtGui.QPushButton(self.loadAsLayerWidget)
        self.loadLayerBtn.setObjectName(_fromUtf8("loadLayerBtn"))
        self.horizontalLayout_7.addWidget(self.loadLayerBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.loadAsLayerWidget, 0, 0, 1, 1)
        self.avoidSelectById = QtGui.QCheckBox(self.loadAsLayerGroup)
        self.avoidSelectById.setObjectName(_fromUtf8("avoidSelectById"))
        self.gridLayout.addWidget(self.avoidSelectById, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.loadAsLayerGroup, 1, 0, 1, 1)

        self.retranslateUi(DbManagerDlgSqlWindow)
        QtCore.QObject.connect(self.loadAsLayerGroup, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.avoidSelectById.setVisible)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgSqlWindow)
        DbManagerDlgSqlWindow.setTabOrder(self.btnExecute, self.btnClear)
        DbManagerDlgSqlWindow.setTabOrder(self.btnClear, self.viewResult)

    def retranslateUi(self, DbManagerDlgSqlWindow):
        DbManagerDlgSqlWindow.setWindowTitle(_translate("DbManagerDlgSqlWindow", "SQL window", None))
        self.label.setText(_translate("DbManagerDlgSqlWindow", "SQL query:", None))
        self.presetStore.setText(_translate("DbManagerDlgSqlWindow", "Store", None))
        self.presetDelete.setText(_translate("DbManagerDlgSqlWindow", "Delete", None))
        self.btnExecute.setText(_translate("DbManagerDlgSqlWindow", "&Execute (F5)", None))
        self.btnExecute.setShortcut(_translate("DbManagerDlgSqlWindow", "F5", None))
        self.btnClear.setText(_translate("DbManagerDlgSqlWindow", "&Clear", None))
        self.label_2.setText(_translate("DbManagerDlgSqlWindow", "Result:", None))
        self.loadAsLayerGroup.setTitle(_translate("DbManagerDlgSqlWindow", "Load as new layer", None))
        self.label_4.setText(_translate("DbManagerDlgSqlWindow", "Column with unique \n"
"integer values", None))
        self.label_3.setText(_translate("DbManagerDlgSqlWindow", "Geometry column", None))
        self.getColumnsBtn.setText(_translate("DbManagerDlgSqlWindow", "Retrieve \n"
"columns", None))
        self.label_5.setText(_translate("DbManagerDlgSqlWindow", "Layer name (prefix)", None))
        self.label_6.setText(_translate("DbManagerDlgSqlWindow", "Type", None))
        self.vectorRadio.setText(_translate("DbManagerDlgSqlWindow", "Vector", None))
        self.rasterRadio.setText(_translate("DbManagerDlgSqlWindow", "Raster", None))
        self.loadLayerBtn.setText(_translate("DbManagerDlgSqlWindow", "Load now!", None))
        self.avoidSelectById.setToolTip(_translate("DbManagerDlgSqlWindow", "<html><head/><body><p>Avoid selecting feature by id. Sometimes - especially when running expensive queries/views - fetching the data sequentially instead of fetching features by id can be much quicker.</p></body></html>", None))
        self.avoidSelectById.setText(_translate("DbManagerDlgSqlWindow", "Avoid selecting by feature id", None))

from ..sqledit import SqlEdit
