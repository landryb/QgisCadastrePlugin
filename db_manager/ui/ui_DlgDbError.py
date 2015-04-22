# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/usr/obj/qgis-2.6.1/qgis-2.6.1/python/plugins/db_manager/ui/DlgDbError.ui'
#
# Created: Thu Mar  5 05:56:42 2015
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

class Ui_DbManagerDlgDbError(object):
    def setupUi(self, DbManagerDlgDbError):
        DbManagerDlgDbError.setObjectName(_fromUtf8("DbManagerDlgDbError"))
        DbManagerDlgDbError.resize(400, 314)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DbManagerDlgDbError)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.stackedWidget = QtGui.QStackedWidget(DbManagerDlgDbError)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.page_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.txtErrorMsg = QtGui.QTextBrowser(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.txtErrorMsg.sizePolicy().hasHeightForWidth())
        self.txtErrorMsg.setSizePolicy(sizePolicy)
        self.txtErrorMsg.setObjectName(_fromUtf8("txtErrorMsg"))
        self.verticalLayout_3.addWidget(self.txtErrorMsg)
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout = QtGui.QVBoxLayout(self.page)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.page)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.txtQueryErrorMsg = QtGui.QTextBrowser(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.txtQueryErrorMsg.sizePolicy().hasHeightForWidth())
        self.txtQueryErrorMsg.setSizePolicy(sizePolicy)
        self.txtQueryErrorMsg.setObjectName(_fromUtf8("txtQueryErrorMsg"))
        self.verticalLayout.addWidget(self.txtQueryErrorMsg)
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.txtQuery = QtGui.QTextBrowser(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.txtQuery.sizePolicy().hasHeightForWidth())
        self.txtQuery.setSizePolicy(sizePolicy)
        self.txtQuery.setObjectName(_fromUtf8("txtQuery"))
        self.verticalLayout.addWidget(self.txtQuery)
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.buttonBox = QtGui.QDialogButtonBox(DbManagerDlgDbError)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(DbManagerDlgDbError)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DbManagerDlgDbError.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DbManagerDlgDbError.reject)
        QtCore.QMetaObject.connectSlotsByName(DbManagerDlgDbError)

    def retranslateUi(self, DbManagerDlgDbError):
        DbManagerDlgDbError.setWindowTitle(_translate("DbManagerDlgDbError", "Database Error", None))
        self.label_3.setText(_translate("DbManagerDlgDbError", "An error occured:", None))
        self.label.setText(_translate("DbManagerDlgDbError", "An error occured when executing a query:", None))
        self.label_2.setText(_translate("DbManagerDlgDbError", "Query:", None))

