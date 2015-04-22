# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/usr/obj/qgis-2.6.1/qgis-2.6.1/python/plugins/db_manager/db_plugins/postgis/plugins/versioning/DlgVersioning.ui'
#
# Created: Thu Mar  5 05:56:51 2015
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

class Ui_DlgVersioning(object):
    def setupUi(self, DlgVersioning):
        DlgVersioning.setObjectName(_fromUtf8("DlgVersioning"))
        DlgVersioning.resize(774, 395)
        self.gridLayout_3 = QtGui.QGridLayout(DlgVersioning)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(DlgVersioning)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(DlgVersioning)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.cboSchema = QtGui.QComboBox(DlgVersioning)
        self.cboSchema.setObjectName(_fromUtf8("cboSchema"))
        self.gridLayout.addWidget(self.cboSchema, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(DlgVersioning)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.cboTable = QtGui.QComboBox(DlgVersioning)
        self.cboTable.setObjectName(_fromUtf8("cboTable"))
        self.gridLayout.addWidget(self.cboTable, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 48, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.chkCreateCurrent = QtGui.QCheckBox(DlgVersioning)
        self.chkCreateCurrent.setChecked(True)
        self.chkCreateCurrent.setObjectName(_fromUtf8("chkCreateCurrent"))
        self.verticalLayout.addWidget(self.chkCreateCurrent)
        self.groupBox_2 = QtGui.QGroupBox(DlgVersioning)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.editPkey = QtGui.QLineEdit(self.groupBox_2)
        self.editPkey.setObjectName(_fromUtf8("editPkey"))
        self.gridLayout_2.addWidget(self.editPkey, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.editStart = QtGui.QLineEdit(self.groupBox_2)
        self.editStart.setObjectName(_fromUtf8("editStart"))
        self.gridLayout_2.addWidget(self.editStart, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.editEnd = QtGui.QLineEdit(self.groupBox_2)
        self.editEnd.setObjectName(_fromUtf8("editEnd"))
        self.gridLayout_2.addWidget(self.editEnd, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.label_5 = QtGui.QLabel(DlgVersioning)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.txtSql = QtGui.QTextBrowser(DlgVersioning)
        self.txtSql.setObjectName(_fromUtf8("txtSql"))
        self.gridLayout_3.addWidget(self.txtSql, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DlgVersioning)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(DlgVersioning)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgVersioning.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgVersioning)
        DlgVersioning.setTabOrder(self.cboSchema, self.cboTable)
        DlgVersioning.setTabOrder(self.cboTable, self.chkCreateCurrent)
        DlgVersioning.setTabOrder(self.chkCreateCurrent, self.editPkey)
        DlgVersioning.setTabOrder(self.editPkey, self.editStart)
        DlgVersioning.setTabOrder(self.editStart, self.editEnd)
        DlgVersioning.setTabOrder(self.editEnd, self.txtSql)
        DlgVersioning.setTabOrder(self.txtSql, self.buttonBox)

    def retranslateUi(self, DlgVersioning):
        DlgVersioning.setWindowTitle(_translate("DlgVersioning", "Add versioning support to a table", None))
        self.label_4.setText(_translate("DlgVersioning", "Table is expected to be empty, with a primary key.", None))
        self.label_2.setText(_translate("DlgVersioning", "Schema", None))
        self.label_3.setText(_translate("DlgVersioning", "Table", None))
        self.chkCreateCurrent.setText(_translate("DlgVersioning", "create a view with current content (<TABLE>_current)", None))
        self.groupBox_2.setTitle(_translate("DlgVersioning", "New columns", None))
        self.label_6.setText(_translate("DlgVersioning", "Prim. key", None))
        self.editPkey.setText(_translate("DlgVersioning", "id_hist", None))
        self.label_7.setText(_translate("DlgVersioning", "Start time", None))
        self.editStart.setText(_translate("DlgVersioning", "time_start", None))
        self.label_8.setText(_translate("DlgVersioning", "End time", None))
        self.editEnd.setText(_translate("DlgVersioning", "time_end", None))
        self.label_5.setText(_translate("DlgVersioning", "SQL to be executed:", None))

