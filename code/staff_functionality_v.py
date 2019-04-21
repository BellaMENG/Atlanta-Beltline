# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff_functionality_v.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__

app = QtWidgets.QApplication(sys.argv)

class Ui_staff_functionality_v(object):
    def setupUi(self, staff_functionality_v):
        staff_functionality_v.setObjectName("staff_functionality_v")
        staff_functionality_v.resize(637, 554)
        self.label = QtWidgets.QLabel(staff_functionality_v)
        self.label.setGeometry(QtCore.QRect(160, 20, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(staff_functionality_v)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 261, 401))
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
        self.view_schedule_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_schedule_btn.setFont(font)
        self.view_schedule_btn.setObjectName("view_schedule_btn")
        self.verticalLayout.addWidget(self.view_schedule_btn)
        self.take_transit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.take_transit_btn.setFont(font)
        self.take_transit_btn.setObjectName("take_transit_btn")
        self.verticalLayout.addWidget(self.take_transit_btn)
        self.view_transit_history_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_transit_history_btn.setFont(font)
        self.view_transit_history_btn.setObjectName("view_transit_history_btn")
        self.verticalLayout.addWidget(self.view_transit_history_btn)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(staff_functionality_v)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 80, 261, 401))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.explore_event_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.explore_event_btn.setFont(font)
        self.explore_event_btn.setObjectName("explore_event_btn")
        self.verticalLayout_2.addWidget(self.explore_event_btn)
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
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout_2.addWidget(self.back_btn)

        self.retranslateUi(staff_functionality_v)
        QtCore.QMetaObject.connectSlotsByName(staff_functionality_v)

    def retranslateUi(self, staff_functionality_v):
        _translate = QtCore.QCoreApplication.translate
        staff_functionality_v.setWindowTitle(_translate("staff_functionality_v", "0"))
        self.label.setText(_translate("staff_functionality_v", "Staff Functionality"))
        self.manage_profile_btn.setText(_translate("staff_functionality_v", "Manage Profile"))
        self.view_schedule_btn.setText(_translate("staff_functionality_v", "View Schedule"))
        self.take_transit_btn.setText(_translate("staff_functionality_v", "Take Transit"))
        self.view_transit_history_btn.setText(_translate("staff_functionality_v", "View Tansit History"))
        self.explore_event_btn.setText(_translate("staff_functionality_v", "Explore Event"))
        self.explore_site_btn.setText(_translate("staff_functionality_v", "Explore Site"))
        self.view_visit_history_btn.setText(_translate("staff_functionality_v", "View Visit History"))
        self.back_btn.setText(_translate("staff_functionality_v", "Back"))

        self.manage_profile_btn.clicked.connect(lambda:self.func(17))
        self.view_schedule_btn.clicked.connect(lambda:self.func(31))
        self.take_transit_btn.clicked.connect(lambda:self.func(15))
        self.view_transit_history_btn.clicked.connect(lambda:self.func(16))
        self.explore_event_btn.clicked.connect(lambda:self.func(33))
        self.explore_site_btn.clicked.connect(lambda:self.func(35))
        self.view_visit_history_btn.clicked.connect(lambda:self.func(16))
        self.back_btn.clicked.connect(lambda:self.func(1))

    def func(self,idx):
        __main__.screen_number = idx
        app.exit()

def render():
    staff_functionality_v = QtWidgets.QMainWindow()
    ui = Ui_staff_functionality_v()
    ui.setupUi(staff_functionality_v)
    staff_functionality_v.show()
    app.exec_()
    staff_functionality_v.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    staff_functionality_v = QtWidgets.QMainWindow()
    ui = Ui_staff_functionality_v()
    ui.setupUi(staff_functionality_v)
    staff_functionality_v.show()
    sys.exit(app.exec_())

