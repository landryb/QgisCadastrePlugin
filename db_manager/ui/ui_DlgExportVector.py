# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/usr/obj/qgis-2.6.1/qgis-2.6.1/python/plugins/db_manager/ui/DlgExportVector.ui'
#
# Created: Thu Mar  5 05:56:31 2015
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

class Ui_DbManagerDlgExportVector(object):
    def setupUi(self, DbManagerDlgExportVector):
        DbManagerDlgExportVector.setObjectName(_fromUtf8("DbManagerDlgExportVector"))
        DbManagerDlgExportVector.resize(514, 185)
        self.gridLayout_2 = QtGui.QGridLayout(DbManagerDlgExportVector)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(DbManagerDlgExportVector)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.editOutputFile = QtGui.QLineEdit(DbManagerDlgExportVector)
        self.editOutputFile.setText(_fromUtf8(""))
        self.editOutputFile.setObjectName(_fromUtf8("editOutputFile"))
        self.gridLayout_2.addWidget(self.editOutputFile, 0, 1, 1, 1)
        self.btnChooseOutputFile = QtGui.QToolButton(DbManagerDlgExportVector)
        self.btnChooseOutputFile.setObjectName(_fromUtf8("btnChooseOutputFile"))
        self.gridLayout_2.addWidget(self.btnChooseOutputFile, 0, 2, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(DbManagerDlgExportVector)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.chkSourceSrid = QtGui.QCheckBox(self.groupBox_2)
        self.chkSourceSrid.setObjectName(_fromUtf8("chkSourceSrid"))
        self.horizontalLayout.addWidget(self.chkSourceSrid)
        self.editSourceSrid = QtGui.QLineEdit(self.groupBox_2)
        self.editSourceSrid.setEnabled(False)
        self.editSourceSrid.setText(_fromUtf8(""))
        self.editSourceSrid.setObjectName(_fromUtf8("editSourceSrid"))
        self.horizontalLayout.addWidget(self.editSourceSrid)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.chkTargetSrid = QtGui.QCheckBox(self.groupBox_2)
        self.chkTargetSrid.setObjectName(_fromUtf8("chkTargetSrid"))
        self.horizontalLayout.addWidget(self.chkTargetSrid)
        self.editTargetSrid = QtGui.QLineEdit(self.groupBox_2)
        self.editTargetSrid.setEnabled(False)
        self.editTargetSrid.setText(_fromUtf8(""))
        self.editTargetSrid.setObjectName(_fromUtf8("editTargetSrid"))
        self.horizontalLayout.addWidget(self.editTargetSrid)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.chkEncoding = QtGui.QCheckBox(self.groupBox_2)
        self.chkEncoding.setObjectName(_fromUtf8("chkEncoding"))
        self.gridLayout.addWidget(self.chkEncoding, 1, 0, 1, 1)
        self.cboEncoding = QtGui.QComboBox(self.groupBox_2)
        self.cboEncoding.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboEncoding.sizePolicy().hasHeightForWidth())
        self.cboEncoding.setSizePolicy(sizePolicy)
        self.cboEncoding.setEditable(False)
        self.cboEncoding.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.cboEncoding.setObjectName(_fromUtf8("cboEncoding"))
        self.gridLayout.addWidget(self.cboEncoding, 1, 1, 1, 1)
        self.chkDropTable = QtGui.QCheckBox(self.groupBox_2)
        self.chkDropTable.setObjectName(_fromUtf8("chkDropTable"))
        self.gridLayout.addWidget(self.chkDropTable, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(DbManagerDlgExportVector)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 3)

        self.retranslateUi(DbManagerDlgExportVector)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DbManagerDlgExportVector.reject)
        QtCore.QObject.connect(self.chkSourceSrid, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.editSourceSrid.setEnabled)
        QtCore.QObject.connect(self.chkTargetSrid, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.editTargetSrid.setEnabled)
        QtCore.QObject.connect(self.chkEncoding, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cboEncoding.setEnabled)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DbManagerDlgExportVector.accept)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgExportVector)
        DbManagerDlgExportVector.setTabOrder(self.chkSourceSrid, self.editSourceSrid)
        DbManagerDlgExportVector.setTabOrder(self.editSourceSrid, self.chkEncoding)
        DbManagerDlgExportVector.setTabOrder(self.chkEncoding, self.cboEncoding)
        DbManagerDlgExportVector.setTabOrder(self.cboEncoding, self.buttonBox)

    def retranslateUi(self, DbManagerDlgExportVector):
        DbManagerDlgExportVector.setWindowTitle(_translate("DbManagerDlgExportVector", "Export to vector file", None))
        self.label_5.setText(_translate("DbManagerDlgExportVector", "Output file", None))
        self.btnChooseOutputFile.setText(_translate("DbManagerDlgExportVector", "...", None))
        self.groupBox_2.setTitle(_translate("DbManagerDlgExportVector", "Options", None))
        self.chkSourceSrid.setText(_translate("DbManagerDlgExportVector", "Source SRID", None))
        self.chkTargetSrid.setText(_translate("DbManagerDlgExportVector", "Target SRID", None))
        self.chkEncoding.setText(_translate("DbManagerDlgExportVector", "Encoding", None))
        self.chkDropTable.setText(_translate("DbManagerDlgExportVector", "Drop existing one", None))

