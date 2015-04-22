# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/usr/obj/qgis-2.6.1/qgis-2.6.1/python/plugins/db_manager/ui/DlgAddGeometryColumn.ui'
#
# Created: Thu Mar  5 05:56:37 2015
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

class Ui_DbManagerDlgAddGeometryColumn(object):
    def setupUi(self, DbManagerDlgAddGeometryColumn):
        DbManagerDlgAddGeometryColumn.setObjectName(_fromUtf8("DbManagerDlgAddGeometryColumn"))
        DbManagerDlgAddGeometryColumn.resize(297, 179)
        self.gridLayout = QtGui.QGridLayout(DbManagerDlgAddGeometryColumn)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(DbManagerDlgAddGeometryColumn)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.editName = QtGui.QLineEdit(DbManagerDlgAddGeometryColumn)
        self.editName.setText(_fromUtf8("geom"))
        self.editName.setObjectName(_fromUtf8("editName"))
        self.gridLayout.addWidget(self.editName, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(DbManagerDlgAddGeometryColumn)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cboType = QtGui.QComboBox(DbManagerDlgAddGeometryColumn)
        self.cboType.setObjectName(_fromUtf8("cboType"))
        self.cboType.addItem(_fromUtf8(""))
        self.cboType.setItemText(0, _fromUtf8("POINT"))
        self.cboType.addItem(_fromUtf8(""))
        self.cboType.setItemText(1, _fromUtf8("LINESTRING"))
        self.cboType.addItem(_fromUtf8(""))
        self.cboType.setItemText(2, _fromUtf8("POLYGON"))
        self.cboType.addItem(_fromUtf8(""))
        self.cboType.setItemText(3, _fromUtf8("MULTIPOINT"))
        self.cboType.addItem(_fromUtf8(""))
        self.cboType.setItemText(4, _fromUtf8("MULTILINESTRING"))
        self.cboType.addItem(_fromUtf8(""))
        self.cboType.setItemText(5, _fromUtf8("MULTIPOLYGON"))
        self.cboType.addItem(_fromUtf8(""))
        self.cboType.setItemText(6, _fromUtf8("GEOMETRYCOLLECTION"))
        self.gridLayout.addWidget(self.cboType, 1, 1, 1, 2)
        self.label_3 = QtGui.QLabel(DbManagerDlgAddGeometryColumn)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinDim = QtGui.QSpinBox(DbManagerDlgAddGeometryColumn)
        self.spinDim.setMinimum(2)
        self.spinDim.setMaximum(4)
        self.spinDim.setObjectName(_fromUtf8("spinDim"))
        self.gridLayout.addWidget(self.spinDim, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 48, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 2, 1)
        self.label_4 = QtGui.QLabel(DbManagerDlgAddGeometryColumn)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.editSrid = QtGui.QLineEdit(DbManagerDlgAddGeometryColumn)
        self.editSrid.setText(_fromUtf8("0"))
        self.editSrid.setObjectName(_fromUtf8("editSrid"))
        self.gridLayout.addWidget(self.editSrid, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DbManagerDlgAddGeometryColumn)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)

        self.retranslateUi(DbManagerDlgAddGeometryColumn)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DbManagerDlgAddGeometryColumn.reject)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgAddGeometryColumn)
        DbManagerDlgAddGeometryColumn.setTabOrder(self.editName, self.cboType)
        DbManagerDlgAddGeometryColumn.setTabOrder(self.cboType, self.spinDim)
        DbManagerDlgAddGeometryColumn.setTabOrder(self.spinDim, self.editSrid)
        DbManagerDlgAddGeometryColumn.setTabOrder(self.editSrid, self.buttonBox)

    def retranslateUi(self, DbManagerDlgAddGeometryColumn):
        DbManagerDlgAddGeometryColumn.setWindowTitle(_translate("DbManagerDlgAddGeometryColumn", "Add geometry column", None))
        self.label.setText(_translate("DbManagerDlgAddGeometryColumn", "Name", None))
        self.label_2.setText(_translate("DbManagerDlgAddGeometryColumn", "Type", None))
        self.label_3.setText(_translate("DbManagerDlgAddGeometryColumn", "Dimensions", None))
        self.label_4.setText(_translate("DbManagerDlgAddGeometryColumn", "SRID", None))

