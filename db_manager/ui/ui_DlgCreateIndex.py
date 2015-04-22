# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/usr/obj/qgis-2.6.1/qgis-2.6.1/python/plugins/db_manager/ui/DlgCreateIndex.ui'
#
# Created: Thu Mar  5 05:56:33 2015
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

class Ui_DbManagerDlgCreateIndex(object):
    def setupUi(self, DbManagerDlgCreateIndex):
        DbManagerDlgCreateIndex.setObjectName(_fromUtf8("DbManagerDlgCreateIndex"))
        DbManagerDlgCreateIndex.resize(357, 111)
        self.gridlayout = QtGui.QGridLayout(DbManagerDlgCreateIndex)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(DbManagerDlgCreateIndex)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.cboColumn = QtGui.QComboBox(DbManagerDlgCreateIndex)
        self.cboColumn.setObjectName(_fromUtf8("cboColumn"))
        self.gridlayout.addWidget(self.cboColumn, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(DbManagerDlgCreateIndex)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.editName = QtGui.QLineEdit(DbManagerDlgCreateIndex)
        self.editName.setText(_fromUtf8(""))
        self.editName.setObjectName(_fromUtf8("editName"))
        self.gridlayout.addWidget(self.editName, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DbManagerDlgCreateIndex)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(DbManagerDlgCreateIndex)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DbManagerDlgCreateIndex.reject)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgCreateIndex)
        DbManagerDlgCreateIndex.setTabOrder(self.cboColumn, self.editName)
        DbManagerDlgCreateIndex.setTabOrder(self.editName, self.buttonBox)

    def retranslateUi(self, DbManagerDlgCreateIndex):
        DbManagerDlgCreateIndex.setWindowTitle(_translate("DbManagerDlgCreateIndex", "Create index", None))
        self.label.setText(_translate("DbManagerDlgCreateIndex", "Column", None))
        self.label_2.setText(_translate("DbManagerDlgCreateIndex", "Name", None))

