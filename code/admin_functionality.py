# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administrator_functionality.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import __main__
import sys

app = QtWidgets.QApplication(sys.argv)

class Ui_admin_functionality(object):
    def setupUi(self, admin_functionality):
        admin_functionality.setObjectName("admin_functionality")
        admin_functionality.resize(528, 522)
        self.label = QtWidgets.QLabel(admin_functionality)
        self.label.setGeometry(QtCore.QRect(20, 10, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(admin_functionality)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 251, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.manag_profile_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manag_profile_btn.setFont(font)
        self.manag_profile_btn.setObjectName("manag_profile_btn")
        self.verticalLayout.addWidget(self.manag_profile_btn)
        self.manage_user_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manage_user_btn.setFont(font)
        self.manage_user_btn.setObjectName("manage_user_btn")
        self.verticalLayout.addWidget(self.manage_user_btn)
        self.manage_transit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manage_transit_btn.setFont(font)
        self.manage_transit_btn.setObjectName("manage_transit_btn")
        self.verticalLayout.addWidget(self.manage_transit_btn)
        self.manag_site_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manag_site_btn.setFont(font)
        self.manag_site_btn.setObjectName("manag_site_btn")
        self.verticalLayout.addWidget(self.manag_site_btn)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(admin_functionality)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(290, 80, 211, 371))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.take_transit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.take_transit_btn.setFont(font)
        self.take_transit_btn.setObjectName("take_transit_btn")
        self.verticalLayout_2.addWidget(self.take_transit_btn)
        self.view_transit_history_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_transit_history_btn.setFont(font)
        self.view_transit_history_btn.setObjectName("view_transit_history_btn")
        self.verticalLayout_2.addWidget(self.view_transit_history_btn)
        self.back_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout_2.addWidget(self.back_btn)

        self.retranslateUi(admin_functionality)
        QtCore.QMetaObject.connectSlotsByName(admin_functionality)

    def retranslateUi(self, admin_functionality):
        _translate = QtCore.QCoreApplication.translate
        admin_functionality.setWindowTitle(_translate("admin_functionality", "Administrator Functionality"))
        self.label.setText(_translate("admin_functionality", "Administrator Functionality"))
        self.manag_profile_btn.setText(_translate("admin_functionality", "Manage Profile"))
        self.manage_user_btn.setText(_translate("admin_functionality", "Manage User"))
        self.manage_transit_btn.setText(_translate("admin_functionality", "Manage Transit"))
        self.manag_site_btn.setText(_translate("admin_functionality", "Manage Site"))
        self.take_transit_btn.setText(_translate("admin_functionality", "Take Transit"))
        self.view_transit_history_btn.setText(_translate("admin_functionality", "View Transit History"))
        self.back_btn.setText(_translate("admin_functionality", "Back"))
        self.manage_profile_btn.clicked.connect(lambda:self.func(17))
        self.manage_user_btn.clicked.connect(lambda:self.func(18))
        self.manage_transit_btn.clicked.connect(lambda:self.func(22))
        self.manage_site_btn.clicked.connect(lambda:self.func(19))
        self.take_transit_btn.clicked.connect(lambda:self.func(15))
        self.view_transit_history_btn.clicked.connect(lambda:self.func(16))
        self.back_btn.clicked.connect(lambda:self.func(9))
        
    def func(self,idx):
        __main__.screen_number = idx
        app.exit()

def render():
    admin_functionality = QtWidgets.QMainWindow()
    ui = Ui_admin_functionality()
    ui.setupUi(admin_functionality)
    admin_functionality.show()
    app.exec_()
    admin_functionality.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    admin_functionality = QtWidgets.QMainWindow()
    ui = Ui_admin_functionality()
    ui.setupUi(admin_functionality)
    admin_functionality.show()
    sys.exit(app.exec_())
