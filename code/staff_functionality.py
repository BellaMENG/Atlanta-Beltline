# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff_functionality.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__

app = QtWidgets.QApplication(sys.argv)

class Ui_staff_functionality(object):
    def setupUi(self, staff_functionality):
        staff_functionality.setObjectName("staff_functionality")
        staff_functionality.resize(445, 508)
        self.label = QtWidgets.QLabel(staff_functionality)
        self.label.setGeometry(QtCore.QRect(60, 10, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(staff_functionality)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(59, 79, 311, 391))
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
        self.back_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout.addWidget(self.back_btn)

        self.retranslateUi(staff_functionality)
        QtCore.QMetaObject.connectSlotsByName(staff_functionality)

    def retranslateUi(self, staff_functionality):
        _translate = QtCore.QCoreApplication.translate
        staff_functionality.setWindowTitle(_translate("staff_functionality", "Staff-Only Functionality"))
        self.label.setText(_translate("staff_functionality", "Staff Functionality"))
        self.manage_profile_btn.setText(_translate("staff_functionality", "Manage Profile"))
        self.view_schedule_btn.setText(_translate("staff_functionality", "View Schedule"))
        self.take_transit_btn.setText(_translate("staff_functionality", "Take Transit"))
        self.view_transit_history_btn.setText(_translate("staff_functionality", "View Transit History"))
        self.back_btn.setText(_translate("staff_functionality", "Back"))

        self.manage_profile_btn.clicked.connect(lambda:self.func(17))
        self.view_schedule_btn.clicked.connect(lambda:self.func(31))
        self.take_transit_btn.clicked.connect(lambda:self.func(15))
        self.view_transit_history_btn.clicked.connect(lambda:self.func(16))
        self.back_btn.clicked.connect(lambda:self.func(1))

    def func(self,idx):
        __main__.screen_number = idx
        app.exit()

    
def render():
    staff_functionality = QtWidgets.QMainWindow()
    ui = Ui_staff_functionality()
    ui.setupUi(staff_functionality)
    staff_functionality.show()
    app.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staff_functionality = QtWidgets.QMainWindow()
    ui = Ui_staff_functionality()
    ui.setupUi(staff_functionality)
    staff_functionality.show()
    sys.exit(app.exec_())

