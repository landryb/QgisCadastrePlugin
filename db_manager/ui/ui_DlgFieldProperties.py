# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/usr/obj/qgis-2.6.1/qgis-2.6.1/python/plugins/db_manager/ui/DlgFieldProperties.ui'
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

class Ui_DbManagerDlgFieldProperties(object):
    def setupUi(self, DbManagerDlgFieldProperties):
        DbManagerDlgFieldProperties.setObjectName(_fromUtf8("DbManagerDlgFieldProperties"))
        DbManagerDlgFieldProperties.resize(261, 247)
        self.vboxlayout = QtGui.QVBoxLayout(DbManagerDlgFieldProperties)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(DbManagerDlgFieldProperties)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.editName = QtGui.QLineEdit(DbManagerDlgFieldProperties)
        self.editName.setText(_fromUtf8(""))
        self.editName.setObjectName(_fromUtf8("editName"))
        self.gridlayout.addWidget(self.editName, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(DbManagerDlgFieldProperties)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cboType = QtGui.QComboBox(DbManagerDlgFieldProperties)
        self.cboType.setEditable(True)
        self.cboType.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.cboType.setObjectName(_fromUtf8("cboType"))
        self.gridlayout.addWidget(self.cboType, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(DbManagerDlgFieldProperties)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.chkNull = QtGui.QCheckBox(DbManagerDlgFieldProperties)
        self.chkNull.setText(_fromUtf8(""))
        self.chkNull.setChecked(True)
        self.chkNull.setObjectName(_fromUtf8("chkNull"))
        self.gridlayout.addWidget(self.chkNull, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(DbManagerDlgFieldProperties)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridlayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.editDefault = QtGui.QLineEdit(DbManagerDlgFieldProperties)
        self.editDefault.setText(_fromUtf8(""))
        self.editDefault.setObjectName(_fromUtf8("editDefault"))
        self.gridlayout.addWidget(self.editDefault, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(DbManagerDlgFieldProperties)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.editLength = QtGui.QLineEdit(DbManagerDlgFieldProperties)
        self.editLength.setText(_fromUtf8(""))
        self.editLength.setObjectName(_fromUtf8("editLength"))
        self.gridlayout.addWidget(self.editLength, 2, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(DbManagerDlgFieldProperties)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(DbManagerDlgFieldProperties)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DbManagerDlgFieldProperties.reject)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgFieldProperties)
        DbManagerDlgFieldProperties.setTabOrder(self.editName, self.cboType)
        DbManagerDlgFieldProperties.setTabOrder(self.cboType, self.editLength)
        DbManagerDlgFieldProperties.setTabOrder(self.editLength, self.chkNull)
        DbManagerDlgFieldProperties.setTabOrder(self.chkNull, self.editDefault)
        DbManagerDlgFieldProperties.setTabOrder(self.editDefault, self.buttonBox)

    def retranslateUi(self, DbManagerDlgFieldProperties):
        DbManagerDlgFieldProperties.setWindowTitle(_translate("DbManagerDlgFieldProperties", "Field properties", None))
        self.label.setText(_translate("DbManagerDlgFieldProperties", "Name", None))
        self.label_2.setText(_translate("DbManagerDlgFieldProperties", "Type", None))
        self.label_3.setText(_translate("DbManagerDlgFieldProperties", "Can be NULL", None))
        self.label_4.setText(_translate("DbManagerDlgFieldProperties", "Default value", None))
        self.label_5.setText(_translate("DbManagerDlgFieldProperties", "Length", None))

