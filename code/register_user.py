# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import __main__
from __main__ import connection_pool
from PyQt5.QtWidgets import QMessageBox
from helper import isValidEmail

app = QtWidgets.QApplication(sys.argv)

class Ui_register_user(object):
    add_btns = list()
    lineEdits = list()
    def setupUi(self, register_user):
        register_user.setObjectName("register_user")
        register_user.resize(685, 646)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(register_user.sizePolicy().hasHeightForWidth())
        register_user.setSizePolicy(sizePolicy)
        self.formLayoutWidget = QtWidgets.QWidget(register_user)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 100, 291, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.firstNameLabel.setFont(font)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.formLayoutWidget_2 = QtWidgets.QWidget(register_user)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(349, 99, 311, 171))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(90)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lastNameLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lastNameLabel.setFont(font)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.confirmPasswordLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.confirmPasswordLabel.setFont(font)
        self.confirmPasswordLabel.setObjectName("confirmPasswordLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.confirmPasswordLabel)
        self.confirmPasswordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.confirmPasswordLineEdit.setObjectName("confirmPasswordLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.confirmPasswordLineEdit)
        self.label = QtWidgets.QLabel(register_user)
        self.label.setGeometry(QtCore.QRect(20, 310, 57, 15))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(register_user)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 401, 31))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.back_btn = QtWidgets.QPushButton(register_user)
        self.back_btn.setGeometry(QtCore.QRect(40, 510, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.register_btn = QtWidgets.QPushButton(register_user)
        self.register_btn.setGeometry(QtCore.QRect(510, 510, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.register_btn.setFont(font)
        self.register_btn.setObjectName("register_btn")
        self.gridLayoutWidget = QtWidgets.QWidget(register_user)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 320, 271, 25))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        add_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(add_btn.sizePolicy().hasHeightForWidth())
        add_btn.setSizePolicy(sizePolicy)
        add_btn.setMinimumSize(QtCore.QSize(80, 23))
        add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(add_btn, 0, 1, 1, 1)
        lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(lineEdit, 0, 0, 1, 1)
        self.add_btns.append(add_btn)
        self.lineEdits.append(lineEdit)

        self.retranslateUi(register_user)
        QtCore.QMetaObject.connectSlotsByName(register_user)

    def retranslateUi(self, register_user):
        _translate = QtCore.QCoreApplication.translate
        register_user.setWindowTitle(_translate("register_user", "Register User"))
        self.firstNameLabel.setText(_translate("register_user", "First name"))
        self.usernameLabel.setText(_translate("register_user", "Username"))
        self.passwordLabel.setText(_translate("register_user", "Password"))
        self.lastNameLabel.setText(_translate("register_user", "Last  Name"))
        self.confirmPasswordLabel.setText(_translate("register_user", "Confirm Password"))
        self.label.setText(_translate("register_user", "Email"))
        self.label_2.setText(_translate("register_user", "Register User"))
        self.back_btn.setText(_translate("register_user", "Back"))
        self.register_btn.setText(_translate("register_user", "Register"))
        self.register_btn.clicked.connect(self.register)
        for btn in self.add_btns:
            btn.setText(_translate("register_visitor", "Add"))
            btn.clicked.connect(self.add_email_input)

    def add_email_input(self):
        h = len(self.add_btns)*45 + 25
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 320, 271, h))
        add_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        add_btn.setFont(font)
        add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(add_btn, len(self.add_btns), 1, 1, 1)
        lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(lineEdit, len(self.lineEdits), 0, 1, 1)
        self.add_btns.append(add_btn)
        self.lineEdits.append(lineEdit)
        _translate = QtCore.QCoreApplication.translate
        add_btn.setText(_translate("register_visitor", "Add"))
        add_btn.clicked.connect(self.add_email_input)

    def register(self):
        fname = self.firstNameLineEdit.text()
        lname = self.lastNameLineEdit.text()
        user_name = self.usernameLineEdit.text()
        pwd = self.passwordLineEdit.text()
        c_pwd = self.confirmPasswordLineEdit.text()
        if ' ' in fname or len(fname) == 0:
            QMessageBox.warning(self.gridLayoutWidget , 
                                    "Invalid Information", 
                                    "First Name can not be NULL. First Name can not contain empty character", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return

        if ' ' in lname or len(lname) == 0:
            QMessageBox.warning(self.gridLayoutWidget , 
                                    "Invalid Information", 
                                    "Last Name can not be NULL. Last Name can not contain empty character", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return 

        if ' ' in user_name or len(user_name) == 0:
            QMessageBox.warning(self.gridLayoutWidget , 
                                    "Invalid Information", 
                                    "User Name can not be NULL. User Name can not contain empty character", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return
        # TODO: check dupicated user name
        if ' ' in pwd or len(pwd) < 8:
            QMessageBox.warning(self.gridLayoutWidget , 
                                    "Invalid Information", 
                                    "Password should be at least 8 characters. Password can not contain empty character", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return 

        if not pwd == c_pwd:
            QMessageBox.warning(self.gridLayoutWidget , 
                                    "Invalid Information", 
                                    "Password and Confirmed Password don't match", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return

        emails = list()
        for le in self.lineEdits:
            email = le.text()
            if not email:
                continue
            if not isValidEmail(email):
                QMessageBox.warning(self.gridLayoutWidget , 
                                    "Invalid Information", 
                                    "Invalid Email address: %s"%(email), 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
                return
            else:
                emails.append(email)

        # store info to database
        #TODO: SQL query to store the input infomation in the database
        query1 = None
        connection_object = connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        # switch to another screen
        __main__.screen = 1
        app.exit()
    
def render():
    register_user = QtWidgets.QDialog()
    ui = Ui_register_user()
    ui.setupUi(register_user)
    register_user.show()
    app.exec_()
    register_user.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_user = QtWidgets.QDialog()
    ui = Ui_register_user()
    ui.setupUi(register_user)
    register_user.show()
    sys.exit(app.exec_())

