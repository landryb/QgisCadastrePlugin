# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/usr/obj/qgis-2.6.1/qgis-2.6.1/python/plugins/db_manager/ui/DlgCreateConstraint.ui'
#
# Created: Thu Mar  5 05:56:36 2015
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

class Ui_DbManagerDlgCreateConstraint(object):
    def setupUi(self, DbManagerDlgCreateConstraint):
        DbManagerDlgCreateConstraint.setObjectName(_fromUtf8("DbManagerDlgCreateConstraint"))
        DbManagerDlgCreateConstraint.resize(284, 138)
        self.gridLayout = QtGui.QGridLayout(DbManagerDlgCreateConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(DbManagerDlgCreateConstraint)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cboColumn = QtGui.QComboBox(DbManagerDlgCreateConstraint)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboColumn.sizePolicy().hasHeightForWidth())
        self.cboColumn.setSizePolicy(sizePolicy)
        self.cboColumn.setObjectName(_fromUtf8("cboColumn"))
        self.gridLayout.addWidget(self.cboColumn, 0, 1, 1, 1)
        self.radPrimaryKey = QtGui.QRadioButton(DbManagerDlgCreateConstraint)
        self.radPrimaryKey.setChecked(True)
        self.radPrimaryKey.setObjectName(_fromUtf8("radPrimaryKey"))
        self.gridLayout.addWidget(self.radPrimaryKey, 1, 1, 1, 1)
        self.radUnique = QtGui.QRadioButton(DbManagerDlgCreateConstraint)
        self.radUnique.setObjectName(_fromUtf8("radUnique"))
        self.gridLayout.addWidget(self.radUnique, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DbManagerDlgCreateConstraint)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(DbManagerDlgCreateConstraint)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DbManagerDlgCreateConstraint.reject)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgCreateConstraint)

    def retranslateUi(self, DbManagerDlgCreateConstraint):
        DbManagerDlgCreateConstraint.setWindowTitle(_translate("DbManagerDlgCreateConstraint", "Add constraint", None))
        self.label.setText(_translate("DbManagerDlgCreateConstraint", "Column", None))
        self.radPrimaryKey.setText(_translate("DbManagerDlgCreateConstraint", "Primary key", None))
        self.radUnique.setText(_translate("DbManagerDlgCreateConstraint", "Unique", None))

