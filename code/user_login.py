# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import __main__
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import pooling
from helper import isValidEmail,decodeStr,verify_password
from PyQt5.QtWidgets import QMessageBox


#from __main__ import connection_pool

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
        if not isValidEmail(email):
            QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                    "Invalid email!", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return
        #TODO: SQL query to search for the user with email and password in the database
        query1 = "SELECT Username FROM emails WHERE Email = \'" + email + "\';"
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        ############################
        if len(result) == 0:
            QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                    "Email Does Not Exist!", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
            print("MySQL connection is closed")
            return
        user_name = result[0][0]
        query1 = "SELECT Password,UserType,Status FROM user WHERE Username = \'" + user_name + "\';"
        cursor.execute(query1)
        result = cursor.fetchall()
        password = result[0][0]
        user_type = result[0][1]
        status = result[0][2]
        exist = False

        if verify_password(password,pwd):
            print("wrong passwd")
            exist = True
        if status == "Declined":
            exist = False
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        ############################
        function_screens = { "User": 7,
                            "Administrator": 8,
                            "Administrator_Visitor":9,
                            "Manager":10,
                            "Manager_Visitor":11,
                            "Staff":12,
                            "Staff_Visitor":13,
                            "Visitor":14}
        if exist:
            if user_type == "User":
                __main__.user_type = "User"
            elif self.isVisitor(user_name):
                if self.isManager(user_name):
                    __main__.user_type = "Manager_Visitor"
                elif self.isStaff(user_name):
                    __main__.user_type = "Staff_Visitor"
                elif self.isAdmin(user_name):
                    __main__.user_type = "Administrator_Visitor"
                else:
                    __main__.user_type = "Visitor"
            else:
                if self.isManager(user_name):
                    __main__.user_type = "Manager"
                elif self.isStaff(user_name):
                    __main__.user_type = "Staff"
                elif self.isAdmin(user_name):
                    __main__.user_type = "Administrator"
            
            __main__.logged_user = user_name
            __main__.screen_number = function_screens[__main__.user_type]
            app.exit()
        else:
            QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                    "Invalid email or password or Declined Status! ", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)

    def isVisitor(self,user_name):
        query1 = "SELECT count(*) FROM visitor WHERE Username = \'" + user_name + "\';"
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        if result[0][0] == 0:
            return False
        else:
            return True

    def isManager(self,user_name):
        query1 = "SELECT count(*) FROM manager WHERE Username = \'" + user_name + "\';"
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        if result[0][0] == 0:
            return False
        else:
            return True
    
    def isAdmin(self,user_name):
        query1 = "SELECT count(*) FROM administrator WHERE Username = \'" + user_name + "\';"
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        if result[0][0] == 0:
            return False
        else:
            return True
    
    def isStaff(self,user_name):
        query1 = "SELECT count(*) FROM staff WHERE Username = \'" + user_name + "\';"
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        if result[0][0] == 0:
            return False
        else:
            return True
     

    def register(self):
        __main__.screen_number = 2
        app.exit()
    
def render():
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

