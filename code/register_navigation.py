# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_navigation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
class Ui_Regster_Navigation(object):
    def setupUi(self, Regster_Navigation):
        Regster_Navigation.setObjectName("Regster_Navigation")
        Regster_Navigation.resize(431, 444)
        self.verticalLayoutWidget = QtWidgets.QWidget(Regster_Navigation)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 120, 271, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.user_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.user_btn.setObjectName("user_btn")
        self.verticalLayout.addWidget(self.user_btn)
        self.visitor_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.visitor_btn.setObjectName("visitor_btn")
        self.verticalLayout.addWidget(self.visitor_btn)
        self.employee_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.employee_btn.setObjectName("employee_btn")
        self.verticalLayout.addWidget(self.employee_btn)
        self.employee_visitor_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.employee_visitor_btn.setObjectName("employee_visitor_btn")
        self.verticalLayout.addWidget(self.employee_visitor_btn)
        self.back_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout.addWidget(self.back_btn)
        self.label = QtWidgets.QLabel(Regster_Navigation)
        self.label.setGeometry(QtCore.QRect(70, 40, 331, 51))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Regster_Navigation)
        QtCore.QMetaObject.connectSlotsByName(Regster_Navigation)

    def retranslateUi(self, Regster_Navigation):
        _translate = QtCore.QCoreApplication.translate
        Regster_Navigation.setWindowTitle(_translate("Regster_Navigation", "Register Navigation"))
        self.user_btn.setText(_translate("Regster_Navigation", "User Only"))
        self.visitor_btn.setText(_translate("Regster_Navigation", "Visitor Only"))
        self.employee_btn.setText(_translate("Regster_Navigation", "Employee Only"))
        self.employee_visitor_btn.setText(_translate("Regster_Navigation", "Employee-Visitor"))
        self.back_btn.setText(_translate("Regster_Navigation", "Back"))
        self.label.setText(_translate("Regster_Navigation", "Register Navigation"))
        self.user_btn.clicked.connect(lambda:self.func(idx=3))
        self.visitor_btn.clicked.connect(lambda:self.func(idx=4))
        self.employee_btn.clicked.connect(lambda:self.func(idx=5))
        self.employee_visitor_btn.clicked.connect(lambda:self.func(idx=6))


    def func(self,idx):
        __main__.screen = idx
        app.exit()
    
def render():
    Regster_Navigation = QtWidgets.QMainWindow()
    ui = Ui_Regster_Navigation()
    ui.setupUi(Regster_Navigation)
    Regster_Navigation.show()
    app.exec_()
    Regster_Navigation.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Regster_Navigation = QtWidgets.QDialog()
    ui = Ui_Regster_Navigation()
    ui.setupUi(Regster_Navigation)
    Regster_Navigation.show()
    sys.exit(app.exec_())

