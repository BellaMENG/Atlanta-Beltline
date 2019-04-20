# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager_functionality.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__

app = QtWidgets.QApplication(sys.argv)

class Ui_manager_functionality(object):
    def setupUi(self, manager_functionality):
        manager_functionality.setObjectName("manager_functionality")
        manager_functionality.resize(651, 544)
        self.verticalLayoutWidget = QtWidgets.QWidget(manager_functionality)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 291, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.manage_profile_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manage_profile_btn.setFont(font)
        self.manage_profile_btn.setObjectName("manage_profile_btn")
        self.verticalLayout.addWidget(self.manage_profile_btn)
        self.manage_event_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manage_event_btn.setFont(font)
        self.manage_event_btn.setObjectName("manage_event_btn")
        self.verticalLayout.addWidget(self.manage_event_btn)
        self.view_staff_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_staff_btn.setFont(font)
        self.view_staff_btn.setObjectName("view_staff_btn")
        self.verticalLayout.addWidget(self.view_staff_btn)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(manager_functionality)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(329, 109, 301, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.view_site_report_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_site_report_btn.setFont(font)
        self.view_site_report_btn.setObjectName("view_site_report_btn")
        self.verticalLayout_2.addWidget(self.view_site_report_btn)
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
        self.label = QtWidgets.QLabel(manager_functionality)
        self.label.setGeometry(QtCore.QRect(120, 30, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.back_btn = QtWidgets.QPushButton(manager_functionality)
        self.back_btn.setGeometry(QtCore.QRect(209, 450, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")

        self.retranslateUi(manager_functionality)
        QtCore.QMetaObject.connectSlotsByName(manager_functionality)

    def retranslateUi(self, manager_functionality):
        _translate = QtCore.QCoreApplication.translate
        manager_functionality.setWindowTitle(_translate("manager_functionality", "Manager-only Functionality"))
        self.manage_profile_btn.setText(_translate("manager_functionality", "Manage Profile"))
        self.manage_event_btn.setText(_translate("manager_functionality", "Manage Event"))
        self.view_staff_btn.setText(_translate("manager_functionality", "View Staff"))
        self.view_site_report_btn.setText(_translate("manager_functionality", "View Site Report"))
        self.take_transit_btn.setText(_translate("manager_functionality", "Take Transit"))
        self.view_transit_history_btn.setText(_translate("manager_functionality", "View Transit History"))
        self.label.setText(_translate("manager_functionality", "Manager Functionality"))
        self.back_btn.setText(_translate("manager_functionality", "Back"))
        
        self.manage_profile_btn.clicked.connect(lambda:self.func(17))
        self.manage_event_btn.clicked.connect(lambda:self.func(25))
        self.view_staff_btn.clicked.connect(lambda:self.func(28))
        self.view_site_report_btn.clicked.connect(lambda:self.func(29))
        self.take_transit_btn.clicked.connect(lambda:self.func(15))
        self.view_transit_history_btn.clicked.connect(lambda:self.func(16))
        self.back_btn.clicked.connect(lambda:self.func(1))

    def func(self,idx):
        __main__.screen_number = idx
        app.exit()

def render():
    manager_functionality = QtWidgets.QMainWindow()
    ui = Ui_manager_functionality()
    ui.setupUi(manager_functionality)
    manager_functionality.show()
    app.exec_()
    manager_functionality.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    manager_functionality = QtWidgets.QMainWindow()
    ui = Ui_manager_functionality()
    ui.setupUi(manager_functionality)
    manager_functionality.show()
    sys.exit(app.exec_())

