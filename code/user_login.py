# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import __main__
from __main__ import connection_pool

app = QtWidgets.QApplication(sys.argv)

class Ui_UserLogin(object):
    def setupUi(self, UserLogin):
        UserLogin.setObjectName("UserLogin")
        UserLogin.resize(427, 300)
        self.pushButton = QtWidgets.QPushButton(UserLogin)
        self.pushButton.setGeometry(QtCore.QRect(30, 250, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(UserLogin)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 250, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(UserLogin)
        self.lineEdit.setGeometry(QtCore.QRect(140, 130, 251, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(UserLogin)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 180, 251, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(UserLogin)
        self.label.setGeometry(QtCore.QRect(30, 130, 57, 15))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(UserLogin)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 81, 20))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(UserLogin)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 351, 41))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(UserLogin)
        QtCore.QMetaObject.connectSlotsByName(UserLogin)

    def retranslateUi(self, UserLogin):
        _translate = QtCore.QCoreApplication.translate
        UserLogin.setWindowTitle(_translate("UserLogin", "User Login"))
        self.pushButton.setText(_translate("UserLogin", "Login"))
        self.pushButton_2.setText(_translate("UserLogin", "Register"))
        self.label.setText(_translate("UserLogin", "Email"))
        self.label_2.setText(_translate("UserLogin", "Password"))
        self.label_3.setText(_translate("UserLogin", "Atlanta Beltline Login"))

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.register)

    def login(self):
        pwd = self.lineEdit_2.text()
        email = self.lineEdit.text()
        #TODO: SQL query to search for the user with email and password in the database
        query1 = None
        connection_object = connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        ############################
        #TODO: identyfy user

        ############################

        function_screens = { "user": 7,
                            "admin": 8,
                            "admin_visitor":9,
                            "manager":10,
                            "manager_visitor":11,
                            "staff":12,
                            "staff_visitor":13,
                            "visitor":14}
        if exist:
            __main__.logged_user = user_name
            __main__.user_type = user_type
            __main__.screen = function_screens[user_type]
            app.exit()
        else:
            QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                    "Invalid email or password!", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)

    def register(self):
        __main__.screen = 2
        app.exit()
    
def render()
    UserLogin = QtWidgets.QMainWindow()
    ui = Ui_UserLogin()
    ui.setupUi(UserLogin)
    UserLogin.show()
    app.exec_()
    UserLogin.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    UserLogin = QtWidgets.QMainWindow()
    ui = Ui_UserLogin()
    ui.setupUi(UserLogin)
    UserLogin.show()
    sys.exit(app.exec_())

