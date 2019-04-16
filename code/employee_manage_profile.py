# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee_manage_profile.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from helper import isValidPhone, isValidEmail
from PyQt5.QtWidgets import QMessageBox
import __main__
import sys

app = QtWidgets.QApplication(sys.argv)

class Ui_employee_manage_profile(object):
    lineEdits = list()

    def setupUi(self, employee_manage_profile):
        employee_manage_profile.setObjectName("employee_manage_profile")
        employee_manage_profile.resize(800, 694)
        self.centralwidget = QtWidgets.QWidget(employee_manage_profile)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 220, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.first_name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name_lineEdit.setGeometry(QtCore.QRect(200, 102, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.first_name_lineEdit.setFont(font)
        self.first_name_lineEdit.setObjectName("first_name_lineEdit")
        self.last_name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.last_name_lineEdit.setGeometry(QtCore.QRect(580, 100, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.last_name_lineEdit.setFont(font)
        self.last_name_lineEdit.setObjectName("last_name_lineEdit")
        self.user_name_label = QtWidgets.QLabel(self.centralwidget)
        self.user_name_label.setGeometry(QtCore.QRect(210, 170, 191, 16))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.user_name_label.setFont(font)
        self.user_name_label.setObjectName("user_name_label")
        self.site_name_label = QtWidgets.QLabel(self.centralwidget)
        self.site_name_label.setGeometry(QtCore.QRect(570, 165, 191, 21))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.site_name_label.setFont(font)
        self.site_name_label.setObjectName("site_name_label")
        self.employee_id_label = QtWidgets.QLabel(self.centralwidget)
        self.employee_id_label.setGeometry(QtCore.QRect(220, 220, 171, 20))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.employee_id_label.setFont(font)
        self.employee_id_label.setObjectName("employee_id_label")
        self.phone_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_lineEdit.setGeometry(QtCore.QRect(580, 220, 113, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phone_lineEdit.setFont(font)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 275, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(210, 276, 581, 20))
        font = QtGui.QFont()
        font.setFamily("STIX")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.address_label.setFont(font)
        self.address_label.setObjectName("address_label")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 330, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.visitor_account_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.visitor_account_checkBox.setGeometry(QtCore.QRect(80, 580, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sawasdee")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.visitor_account_checkBox.setFont(font)
        self.visitor_account_checkBox.setObjectName("visitor_account_checkBox")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(80, 630, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.update_btn.setFont(font)
        self.update_btn.setObjectName("update_btn")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(580, 630, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.gridLayoutWidget = QtWidgets.QWidget(employee_manage_profile)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(230, 360, 271, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        # self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit.setGeometry(QtCore.QRect(230, 360, 271, 25))
        # self.lineEdit.setObjectName("lineEdit")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(560, 340, 80, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        employee_manage_profile.setCentralWidget(self.centralwidget)

        self.retranslateUi(employee_manage_profile)
        QtCore.QMetaObject.connectSlotsByName(employee_manage_profile)

    def retranslateUi(self, employee_manage_profile):
        _translate = QtCore.QCoreApplication.translate
        employee_manage_profile.setWindowTitle(_translate("employee_manage_profile", "Employee Manage Profile"))
        self.label.setText(_translate("employee_manage_profile", "Manage Profile"))
        self.label_2.setText(_translate("employee_manage_profile", "First Name"))
        self.label_3.setText(_translate("employee_manage_profile", "Last Name"))
        self.label_4.setText(_translate("employee_manage_profile", "User Name"))
        self.label_5.setText(_translate("employee_manage_profile", "Site Name"))
        self.label_6.setText(_translate("employee_manage_profile", "Employee ID"))
        self.label_7.setText(_translate("employee_manage_profile", "Phone"))
        self.user_name_label.setText(_translate("employee_manage_profile", "TextLabel"))
        self.site_name_label.setText(_translate("employee_manage_profile", "TextLabel"))
        self.employee_id_label.setText(_translate("employee_manage_profile", "TextLabel"))
        self.label_8.setText(_translate("employee_manage_profile", "Address"))
        self.address_label.setText(_translate("employee_manage_profile", "TextLabel"))
        self.label_9.setText(_translate("employee_manage_profile", "Email"))
        self.visitor_account_checkBox.setText(_translate("employee_manage_profile", "Visitor Account"))
        self.update_btn.setText(_translate("employee_manage_profile", "Update"))
        self.back_btn.setText(_translate("employee_manage_profile", "Back"))
        self.add_btn.setText(_translate("employee_manage_profile", "Add"))

        self.user_name = __main__.logged_user
        self.initInfo()
        self.update_btn.clicked.connect(self.update)
        self.add_btn.clicked.connect(self.add_email_input)
        self.back_btn.clicked.connect(lambda:self.func(idx=1))

    def add_email_input(self):
        if len(self.lineEdits) == 0:
            h = 50
        else:
            h = len(self.lineEdits)*45 + 25
        self.gridLayoutWidget.setGeometry(QtCore.QRect(230, 360, 271, h))
        lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(lineEdit, len(self.lineEdits), 0, 1, 1)
        self.lineEdits.append(lineEdit)
        _translate = QtCore.QCoreApplication.translate

    def get_emails(self):
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        sql = "select Email from emails where Username = \'" + self.user_name + "\';"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in range(len(result)):
            self.add_email_input()
            self.lineEdits[i].setText(result[i][0])
        sql = "delete from emails where Username = \'" + self.user_name + "\';"
        cursor.execute(sql)
        connection_object.commit()
        if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")

    def email_exist(self,email):
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        sql = "select Email from emails where Email = \'" + email+ "\';"
        cursor.execute(sql)
        result = cursor.fetchall()
        if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")
        if len(result) == 0:
            return False
        else:
            return True

    def store_emails(self):
        email_count = 0
        email_list = list()
        for lineEdit in self.lineEdits:
            email = lineEdit.text()
            if not email:
                continue
            else:
                if isValidEmail(email) and not self.email_exist(email):
                    email_list.append(email)
                else:
                    QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                    "Email Exists or Invalid!", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)

        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        for e in email_list:
            sql = "insert into emails values (\'" + self.user_name + "\', \'" + e + "\');"
            cursor.execute(sql)
            connection_object.commit()
        if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")

    def initInfo(self):
        #
        _translate = QtCore.QCoreApplication.translate
        query1 = "select e.Username, e.EmployeeID, e.Phone, e.Address, e.City, e.State, e.Zipcode, u.Firstname, u.Lastname from employee as e join user as u on e.Username = u.Username where e.Username = \'"+ self.user_name + "\';"
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        print(query1)
        cursor.execute(query1)
        result = cursor.fetchall()
        user_name,employee_id,phone,address,city,state,zipcode,first_name,last_name = result[0]
        query2 = "select SiteName from assign_to where Username = \'" + user_name + "\';"
        cursor.execute(query2)
        result = cursor.fetchall()
        if len(result) == 0:
            site_name = "None"
        else:
            site_name = result[0][0]
        #first_name,last_name,user_name,site_name,employee_id,phone,address = ['Clara','Wilson','cwison','Inman Park','123456789','123-123-1234','100 East Main Street']
        self.user_name_label.setText(_translate("employee_manage_profile", user_name))
        self.site_name_label.setText(_translate("employee_manage_profile", site_name))
        self.employee_id_label.setText(_translate("employee_manage_profile", employee_id))
        self.address_label.setText(_translate("employee_manage_profile", address + ' , ' + city + ' , ' + state + " "+ zipcode))
        self.first_name_lineEdit.setText(first_name)
        self.last_name_lineEdit.setText(last_name)
        self.phone_lineEdit.setText(phone)
        if self.isVisitor():
            self.visitor_account_checkBox.setChecked(True)
        else:
            self.visitor_account_checkBox.setChecked(False)
        if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")
        self.get_emails()

    def update(self):
        first_name = self.first_name_lineEdit.text()
        last_name = self.last_name_lineEdit.text()
        phone = self.phone_lineEdit.text()
        is_visitor_account = self.visitor_account_checkBox.isChecked()
        query1 = "SELECT count(*) FROM visitor WHERE Username = \'" + self.user_name + "\';"
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        if not isValidPhone(phone):
            QMessageBox.warning(self.centralwidget, 
                                    "Invalid Information", 
                                    "Invalid Phone Number: %s"%(phone), 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")
            return 

        if not first_name or not last_name or not phone:
            QMessageBox.warning(self.centralwidget, 
                                    "Invalid Information", 
                                    "All fileds required!", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")
            return 
        if not is_visitor_account:
            sql = "delete from visitor where Username = \'" + self.user_name + "\';"
            cursor.execute(sql)
            connection_object.commit()
            
        cursor = connection_object.cursor()
        sql = "Update user set Lastname= \'" + last_name + "\', Firstname= \'" + first_name + "\' where Username= \'" + self.user_name + "';"
        sql2 = "Update employee set Phone= \'" + phone +  "\' where Username= \'" + self.user_name + "\';"
        print(sql)
        cursor.execute(sql)
        connection_object.commit()
        cursor.execute(sql2)
        connection_object.commit()

        if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")
        
        self.store_emails()
    
    def isVisitor(self):
        query1 = "SELECT count(*) FROM visitor WHERE Username = \'" + self.user_name + "\';"
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
    
    def func(idx):
        __main__.screen_number = idx
        self.store_emails()        

def render():
    employee_manage_profile = QtWidgets.QMainWindow()
    ui = Ui_employee_manage_profile()
    ui.setupUi(employee_manage_profile)
    employee_manage_profile.show()
    sys.exit(app.exec_())
    employee_manage_profile.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    employee_manage_profile = QtWidgets.QMainWindow()
    ui = Ui_employee_manage_profile()
    ui.setupUi(employee_manage_profile)
    employee_manage_profile.show()
    sys.exit(app.exec_())

