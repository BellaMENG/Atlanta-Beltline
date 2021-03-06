# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager_functionality_v.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
import __main__

app = QtWidgets.QApplication(sys.argv)

class Ui_manager_functionality_v(object):
    def setupUi(self, manager_functionality_v):
        manager_functionality_v.setObjectName("manager_functionality_v")
        manager_functionality_v.resize(622, 530)
        self.verticalLayoutWidget = QtWidgets.QWidget(manager_functionality_v)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 271, 411))
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
        self.view_staff_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_staff_btn.setFont(font)
        self.view_staff_btn.setObjectName("view_staff_btn")
        self.verticalLayout.addWidget(self.view_staff_btn)
        self.explore_site_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.explore_site_btn.setFont(font)
        self.explore_site_btn.setObjectName("explore_site_btn")
        self.verticalLayout.addWidget(self.explore_site_btn)
        self.take_transit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.take_transit_btn.setFont(font)
        self.take_transit_btn.setObjectName("take_transit_btn")
        self.verticalLayout.addWidget(self.take_transit_btn)
        self.view_visit_history_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_visit_history_btn.setFont(font)
        self.view_visit_history_btn.setObjectName("view_visit_history_btn")
        self.verticalLayout.addWidget(self.view_visit_history_btn)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(manager_functionality_v)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(310, 90, 291, 411))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.manag_event_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manag_event_btn.setFont(font)
        self.manag_event_btn.setObjectName("manag_event_btn")
        self.verticalLayout_2.addWidget(self.manag_event_btn)
        self.view_stie_report_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_stie_report_btn.setFont(font)
        self.view_stie_report_btn.setObjectName("view_stie_report_btn")
        self.verticalLayout_2.addWidget(self.view_stie_report_btn)
        self.explore_event_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.explore_event_btn.setFont(font)
        self.explore_event_btn.setObjectName("explore_event_btn")
        self.verticalLayout_2.addWidget(self.explore_event_btn)
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
        self.label = QtWidgets.QLabel(manager_functionality_v)
        self.label.setGeometry(QtCore.QRect(110, 25, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(manager_functionality_v)
        QtCore.QMetaObject.connectSlotsByName(manager_functionality_v)

    def retranslateUi(self, manager_functionality_v):
        _translate = QtCore.QCoreApplication.translate
        manager_functionality_v.setWindowTitle(_translate("manager_functionality_v", "Manager-Visitor Functionality"))
        self.manage_profile_btn.setText(_translate("manager_functionality_v", "Manage Profile"))
        self.view_staff_btn.setText(_translate("manager_functionality_v", "View Staff"))
        self.explore_site_btn.setText(_translate("manager_functionality_v", "Explore Site"))
        self.take_transit_btn.setText(_translate("manager_functionality_v", "Take Transit"))
        self.view_visit_history_btn.setText(_translate("manager_functionality_v", "View Visit History"))
        self.manag_event_btn.setText(_translate("manager_functionality_v", "Manage Event"))
        self.view_stie_report_btn.setText(_translate("manager_functionality_v", "View Site Report"))
        self.explore_event_btn.setText(_translate("manager_functionality_v", "Explore Event"))
        self.view_transit_history_btn.setText(_translate("manager_functionality_v", "View Transit History"))
        self.back_btn.setText(_translate("manager_functionality_v", "Back"))
        self.label.setText(_translate("manager_functionality_v", "Manager Functionality"))

        self.user_name = __main__.logged_user
        query = "select Name from site where Manager = \'" + self.user_name + "\';"
        self.result = self.retrieve_from_db(query)

        self.manage_profile_btn.clicked.connect(lambda:self.func(17))
        self.view_staff_btn.clicked.connect(self.view_staff)
        self.explore_site_btn.clicked.connect(lambda:self.func(35))
        self.take_transit_btn.clicked.connect(lambda:self.func(15))
        self.view_visit_history_btn.clicked.connect(lambda:self.func(38))
        self.manag_event_btn.clicked.connect(self.manage_event)
        self.view_stie_report_btn.clicked.connect(self.view_site_report)
        self.explore_event_btn.clicked.connect(lambda:self.func(33))
        self.back_btn.clicked.connect(lambda: self.func(idx=1))
        self.view_transit_history_btn.clicked.connect(lambda: self.func(idx=16))

    def manage_event(self):
        if len(self.result) == 0:
            self.msgDialog("You are not managing sites!")
            return
        self.func(idx=25)

    def view_staff(self):
        if len(self.result) == 0:
            self.msgDialog("You are not managing sites!")
            return
        self.func(idx=28)

    def view_site_report(self):
        if len(self.result) == 0:
            self.msgDialog("You are not managing sites!")
            return
        self.func(idx=29)

    def retrieve_from_db(self, query):
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ", db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        return result

    def msgDialog(self, m):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Sorry!")
        msg.setInformativeText("This action is not allowed.")
        msg.setWindowTitle("Not allowed")
        msg.setDetailedText(m)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def func(self,idx):
        __main__.screen_number = idx
        app.exit()

def render():
    manager_functionality_v = QtWidgets.QMainWindow()
    ui = Ui_manager_functionality_v()
    ui.setupUi(manager_functionality_v)
    manager_functionality_v.show()
    app.exec_()
    manager_functionality_v.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    manager_functionality_v = QtWidgets.QMainWindow()
    ui = Ui_manager_functionality_v()
    ui.setupUi(manager_functionality_v)
    manager_functionality_v.show()
    sys.exit(app.exec_())

