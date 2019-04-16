# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_functionality_v.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__

app = QtWidgets.QApplication(sys.argv)

class Ui_admin_functionality_v(object):
    def setupUi(self, admin_functionality_v):
        admin_functionality_v.setObjectName("admin_functionality_v")
        admin_functionality_v.resize(652, 457)
        self.verticalLayoutWidget = QtWidgets.QWidget(admin_functionality_v)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 281, 321))
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
        self.manage_transit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manage_transit_btn.setFont(font)
        self.manage_transit_btn.setObjectName("manage_transit_btn")
        self.verticalLayout.addWidget(self.manage_transit_btn)
        self.manage_site_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manage_site_btn.setFont(font)
        self.manage_site_btn.setObjectName("manage_site_btn")
        self.verticalLayout.addWidget(self.manage_site_btn)
        self.explore_event_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.explore_event_btn.setFont(font)
        self.explore_event_btn.setObjectName("explore_event_btn")
        self.verticalLayout.addWidget(self.explore_event_btn)
        self.vie_transit_history_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vie_transit_history_btn.setFont(font)
        self.vie_transit_history_btn.setObjectName("vie_transit_history_btn")
        self.verticalLayout.addWidget(self.vie_transit_history_btn)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(admin_functionality_v)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(330, 90, 291, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.manage_user_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manage_user_btn.setFont(font)
        self.manage_user_btn.setObjectName("manage_user_btn")
        self.verticalLayout_2.addWidget(self.manage_user_btn)
        self.take_transit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.take_transit_btn.setFont(font)
        self.take_transit_btn.setObjectName("take_transit_btn")
        self.verticalLayout_2.addWidget(self.take_transit_btn)
        self.explore_site_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.explore_site_btn.setFont(font)
        self.explore_site_btn.setObjectName("explore_site_btn")
        self.verticalLayout_2.addWidget(self.explore_site_btn)
        self.view_visit_history_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_visit_history_btn.setFont(font)
        self.view_visit_history_btn.setObjectName("view_visit_history_btn")
        self.verticalLayout_2.addWidget(self.view_visit_history_btn)
        self.back_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout_2.addWidget(self.back_btn)
        self.label = QtWidgets.QLabel(admin_functionality_v)
        self.label.setGeometry(QtCore.QRect(100, 20, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(admin_functionality_v)
        QtCore.QMetaObject.connectSlotsByName(admin_functionality_v)

    def retranslateUi(self, admin_functionality_v):
        _translate = QtCore.QCoreApplication.translate
        admin_functionality_v.setWindowTitle(_translate("admin_functionality_v", "Administrator-Visitor Functionality"))
        self.manage_profile_btn.setText(_translate("admin_functionality_v", "Manage Profile"))
        self.manage_transit_btn.setText(_translate("admin_functionality_v", "Manager Transit"))
        self.manage_site_btn.setText(_translate("admin_functionality_v", "Manage Site"))
        self.explore_event_btn.setText(_translate("admin_functionality_v", "Explore Event"))
        self.vie_transit_history_btn.setText(_translate("admin_functionality_v", "View Transit History"))
        self.manage_user_btn.setText(_translate("admin_functionality_v", "Manage User"))
        self.take_transit_btn.setText(_translate("admin_functionality_v", "Take Transit"))
        self.explore_site_btn.setText(_translate("admin_functionality_v", "Explore Site"))
        self.view_visit_history_btn.setText(_translate("admin_functionality_v", "View Visit History"))
        self.back_btn.setText(_translate("admin_functionality_v", "Back"))
        self.label.setText(_translate("admin_functionality_v", "Administrator Functionality"))
        
        self.manage_profile_btn.clicked.connect(lambda:self.func(17))
        self.manage_transit_btn.clicked.connect(lambda:self.func(22))
        self.manage_site_btn.clicked.connect(lambda:self.func(19))
        self.explore_event_btn.clicked.connect(lambda:self.func(33))
        self.vie_transit_history_btn.clicked.connect(lambda:self.func(16))
        self.manage_user_btn.clicked.connect(lambda:self.func(18))
        self.take_transit_btn.clicked.connect(lambda:self.func(15))
        self.explore_site_btn.clicked.connect(lambda:self.func(35))
        self.view_visit_history_btn.clicked.connect(lambda:self.func(38))
        self.back_btn.clicked.connect(lambda:self.func(9))
        

    def func(self,idx):
        __main__.screen_number = idx
        app.exit()

def render():
    admin_functionality_v = QtWidgets.QMainWindow()
    ui = Ui_admin_functionality_v()
    ui.setupUi(admin_functionality_v)
    admin_functionality_v.show()
    app.exec_()
    admin_functionality_v.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    admin_functionality_v = QtWidgets.QMainWindow()
    ui = Ui_admin_functionality_v()
    ui.setupUi(admin_functionality_v)
    admin_functionality_v.show()
    sys.exit(app.exec_())

