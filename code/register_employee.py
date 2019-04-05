# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_employee.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import __main__
from __main__ import connection_pool
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from helper import isValidEmail
import sys

app = QtWidgets.QApplication(sys.argv)

class Ui_register_employee(object):
    add_btns = list()
    lineEdits = list()

    def setupUi(self, register_employee):
        register_employee.setObjectName("register_employee")
        register_employee.resize(762, 589)
        self.label = QtWidgets.QLabel(register_employee)
        self.label.setGeometry(QtCore.QRect(210, 20, 461, 61))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(register_employee)
        self.formLayoutWidget.setGeometry(QtCore.QRect(29, 89, 331, 220))
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
        self.userNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.userNameLabel.setFont(font)
        self.userNameLabel.setObjectName("userNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.userNameLabel)
        self.userNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.userNameLineEdit.setObjectName("userNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.userNameLineEdit)
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
        self.phoneLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.phoneLabel.setFont(font)
        self.phoneLabel.setObjectName("phoneLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.phoneLabel)
        self.phoneLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.phoneLineEdit.setObjectName("phoneLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.phoneLineEdit)
        self.formLayoutWidget_2 = QtWidgets.QWidget(register_employee)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(379, 89, 341, 220))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setVerticalSpacing(30)
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
        self.userTypeLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.userTypeLabel.setFont(font)
        self.userTypeLabel.setObjectName("userTypeLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.userTypeLabel)
        self.userTypeComboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.userTypeComboBox.setObjectName("userTypeComboBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.userTypeComboBox)
        self.confirmedPasswordLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.confirmedPasswordLabel.setFont(font)
        self.confirmedPasswordLabel.setObjectName("confirmedPasswordLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.confirmedPasswordLabel)
        self.confirmedPasswordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.confirmedPasswordLineEdit.setObjectName("confirmedPasswordLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.confirmedPasswordLineEdit)
        self.addressLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.addressLabel.setFont(font)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.addressLineEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(register_employee)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 330, 691, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.city_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.city_input.setMaximumSize(QtCore.QSize(300, 20))
        self.city_input.setObjectName("city_input")
        self.horizontalLayout.addWidget(self.city_input)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.state_input = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.state_input.setObjectName("state_input")
        self.horizontalLayout.addWidget(self.state_input)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.zipcode_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.zipcode_input.setObjectName("zipcode_input")
        self.horizontalLayout.addWidget(self.zipcode_input)
        self.label_5 = QtWidgets.QLabel(register_employee)
        self.label_5.setGeometry(QtCore.QRect(40, 440, 57, 15))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(register_employee)
        self.pushButton.setGeometry(QtCore.QRect(70, 512, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(register_employee)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 510, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayoutWidget = QtWidgets.QWidget(register_employee)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(210, 450, 321, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        add_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(add_btn, 0, 1, 1, 1)
        lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(lineEdit, 0, 0, 1, 1)
        self.add_btns.append(add_btn)
        self.lineEdits.append(lineEdit)

        self.retranslateUi(register_employee)
        QtCore.QMetaObject.connectSlotsByName(register_employee)

    def retranslateUi(self, register_employee):
        _translate = QtCore.QCoreApplication.translate
        register_employee.setWindowTitle(_translate("register_employee", "Register Employee"))
        self.label.setText(_translate("register_employee", "Register Employee"))
        self.firstNameLabel.setText(_translate("register_employee", "First Name"))
        self.userNameLabel.setText(_translate("register_employee", "User Name"))
        self.passwordLabel.setText(_translate("register_employee", "Password"))
        self.phoneLabel.setText(_translate("register_employee", "Phone"))
        self.lastNameLabel.setText(_translate("register_employee", "Last Name"))
        self.userTypeLabel.setText(_translate("register_employee", "User Type"))
        self.confirmedPasswordLabel.setText(_translate("register_employee", "Confirmed Password"))
        self.addressLabel.setText(_translate("register_employee", "Address"))
        self.label_2.setText(_translate("register_employee", "City"))
        self.label_3.setText(_translate("register_employee", "State"))
        self.label_4.setText(_translate("register_employee", "Zipcode"))
        self.label_5.setText(_translate("register_employee", "Email"))
        self.pushButton.setText(_translate("register_employee", "Back"))
        self.pushButton_2.setText(_translate("register_employee", "Register"))
        state_list = ['other','AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
        self.state_input.addItems(state_list)
        user_type_list = ['Manager','Staff']
        self.userTypeComboBox.addItems(user_type_list)
        for btn in self.add_btns:
            btn.setText(_translate("register_employee", "Add"))
            btn.clicked.connect(self.add_email_input)
        self.pushButton_2.clicked.connect(self.register)

    def add_email_input(self):
        h = len(self.add_btns)*45 + 25
        self.gridLayoutWidget.setGeometry(QtCore.QRect(210, 450, 321, h))
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
        c_pwd = self.confirmedPasswordLineEdit.text()
        user_type = self.userTypeComboBox.currentText()
        phone = self.phoneLineEdit.text()
        address = self.addressLineEdit.text()
        city = self.city_input.text()
        state = self.state_input.currentText()
        zipcode = self.zipcode_input.text()
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

        if not isValidPhone(phone):
                QMessageBox.warning(self.gridLayoutWidget , 
                                    "Invalid Information", 
                                    "Invalid Phone Number: %s"%(phone), 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
                return 

        if not isValidZipcode(zipcode):
                QMessageBox.warning(self.gridLayoutWidget , 
                                    "Invalid Information", 
                                    "Invalid Zipcode: %s"%(zipcode), 
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
    register_employee = QtWidgets.QMainWindow()
    ui = Ui_register_employee()
    ui.setupUi(register_employee)
    register_employee.show()
    sys.exit(app.exec_())
    register_employee.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    register_employee = QtWidgets.QMainWindow()
    ui = Ui_register_employee()
    ui.setupUi(register_employee)
    register_employee.show()
    sys.exit(app.exec_())

