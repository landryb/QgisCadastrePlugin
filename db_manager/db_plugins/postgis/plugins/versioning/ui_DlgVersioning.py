# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/build/qgis-3.4.10+14stretch/python/plugins/db_manager/db_plugins/postgis/plugins/versioning/DlgVersioning.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgVersioning(object):
    def setupUi(self, DlgVersioning):
        DlgVersioning.setObjectName("DlgVersioning")
        DlgVersioning.resize(774, 395)
        self.gridLayout_3 = QtWidgets.QGridLayout(DlgVersioning)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(DlgVersioning)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cboSchema = QtWidgets.QComboBox(DlgVersioning)
        self.cboSchema.setObjectName("cboSchema")
        self.gridLayout.addWidget(self.cboSchema, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(DlgVersioning)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(DlgVersioning)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.cboTable = QtWidgets.QComboBox(DlgVersioning)
        self.cboTable.setObjectName("cboTable")
        self.gridLayout.addWidget(self.cboTable, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.chkCreateCurrent = QtWidgets.QCheckBox(DlgVersioning)
        self.chkCreateCurrent.setChecked(True)
        self.chkCreateCurrent.setObjectName("chkCreateCurrent")
        self.verticalLayout.addWidget(self.chkCreateCurrent)
        self.groupBox_2 = QtWidgets.QGroupBox(DlgVersioning)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.editPkey = QtWidgets.QLineEdit(self.groupBox_2)
        self.editPkey.setObjectName("editPkey")
        self.gridLayout_2.addWidget(self.editPkey, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.editStart = QtWidgets.QLineEdit(self.groupBox_2)
        self.editStart.setObjectName("editStart")
        self.gridLayout_2.addWidget(self.editStart, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.editEnd = QtWidgets.QLineEdit(self.groupBox_2)
        self.editEnd.setObjectName("editEnd")
        self.gridLayout_2.addWidget(self.editEnd, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.editUser = QtWidgets.QLineEdit(self.groupBox_2)
        self.editUser.setObjectName("editUser")
        self.gridLayout_2.addWidget(self.editUser, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.label_5 = QtWidgets.QLabel(DlgVersioning)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.txtSql = QtWidgets.QTextBrowser(DlgVersioning)
        self.txtSql.setObjectName("txtSql")
        self.gridLayout_3.addWidget(self.txtSql, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgVersioning)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(DlgVersioning)
        self.buttonBox.rejected.connect(DlgVersioning.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgVersioning)
        DlgVersioning.setTabOrder(self.cboSchema, self.cboTable)
        DlgVersioning.setTabOrder(self.cboTable, self.chkCreateCurrent)
        DlgVersioning.setTabOrder(self.chkCreateCurrent, self.editPkey)
        DlgVersioning.setTabOrder(self.editPkey, self.editStart)
        DlgVersioning.setTabOrder(self.editStart, self.editEnd)
        DlgVersioning.setTabOrder(self.editEnd, self.txtSql)
        DlgVersioning.setTabOrder(self.txtSql, self.buttonBox)

    def retranslateUi(self, DlgVersioning):
        _translate = QtCore.QCoreApplication.translate
        DlgVersioning.setWindowTitle(_translate("DlgVersioning", "Add Change Logging Support to a Table"))
        self.label_4.setText(_translate("DlgVersioning", "Table should be empty, with a primary key"))
        self.label_2.setText(_translate("DlgVersioning", "Schema"))
        self.label_3.setText(_translate("DlgVersioning", "Table"))
        self.chkCreateCurrent.setText(_translate("DlgVersioning", "Create a view with current content (<TABLE>_current)"))
        self.groupBox_2.setTitle(_translate("DlgVersioning", "New columns"))
        self.label_6.setText(_translate("DlgVersioning", "Primary key"))
        self.editPkey.setText(_translate("DlgVersioning", "id_hist"))
        self.label_7.setText(_translate("DlgVersioning", "Start time"))
        self.editStart.setText(_translate("DlgVersioning", "time_start"))
        self.label_8.setText(_translate("DlgVersioning", "End time"))
        self.editEnd.setText(_translate("DlgVersioning", "time_end"))
        self.label_9.setText(_translate("DlgVersioning", "User role"))
        self.editUser.setText(_translate("DlgVersioning", "user_role"))
        self.label_5.setText(_translate("DlgVersioning", "SQL to be executed"))

