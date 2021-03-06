# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administrator_create_site.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableWidget,QPushButton,QApplication,QVBoxLayout,QTableWidgetItem,QCheckBox,QAbstractItemView,QHeaderView,QLabel,QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import __main__
import sys
from helper import isValidZipcode


app = QtWidgets.QApplication(sys.argv)

class Ui_administrator_create_site(object):
    def setupUi(self, administrator_create_site):
        administrator_create_site.setObjectName("administrator_create_site")
        administrator_create_site.resize(588, 384)
        self.centralwidget = QtWidgets.QWidget(administrator_create_site)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 70, 461, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.zipcodeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.zipcodeLabel.setFont(font)
        self.zipcodeLabel.setObjectName("zipcodeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.zipcodeLabel)
        self.zipcodeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zipcodeLineEdit.setFont(font)
        self.zipcodeLineEdit.setObjectName("zipcodeLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.zipcodeLineEdit)
        self.addressLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addressLabel.setFont(font)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.addressLineEdit)
        self.managerLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.managerLabel.setFont(font)
        self.managerLabel.setObjectName("managerLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.managerLabel)
        self.managerComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.managerComboBox.setFont(font)
        self.managerComboBox.setObjectName("managerComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.managerComboBox)
        self.openEverydayLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.openEverydayLabel.setFont(font)
        self.openEverydayLabel.setObjectName("openEverydayLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.openEverydayLabel)
        self.openEverydayCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.openEverydayCheckBox.setFont(font)
        self.openEverydayCheckBox.setObjectName("openEverydayCheckBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.openEverydayCheckBox)
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(60, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(390, 320, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.update_btn.setFont(font)
        self.update_btn.setObjectName("update_btn")
        administrator_create_site.setCentralWidget(self.centralwidget)

        self.retranslateUi(administrator_create_site)
        QtCore.QMetaObject.connectSlotsByName(administrator_create_site)

    def retranslateUi(self, administrator_create_site):
        _translate = QtCore.QCoreApplication.translate
        administrator_create_site.setWindowTitle(_translate("administrator_create_site", "Administrator Create Site"))
        self.label.setText(_translate("administrator_create_site", "Create Site"))
        self.nameLabel.setText(_translate("administrator_create_site", "Name"))
        self.zipcodeLabel.setText(_translate("administrator_create_site", "Zipcode"))
        self.addressLabel.setText(_translate("administrator_create_site", "Address"))
        self.managerLabel.setText(_translate("administrator_create_site", "Manager"))
        self.openEverydayLabel.setText(_translate("administrator_create_site", "Open Everyday"))
        self.back_btn.setText(_translate("administrator_create_site", "Bcak"))
        self.update_btn.setText(_translate("administrator_create_site", "Update"))

        self.manager_list = list()
        self.get_managers()
        self.managerComboBox.addItems(self.manager_list)
        self.update_btn.clicked.connect(self.update)
        self.back_btn.clicked.connect(self.back)


    def get_managers(self):
        query1 = "select concat(Firstname, \' \',Lastname),Username from user where Username in ( select Username from manager where Username not in (select Manager from site) );" 
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        for row in result:
            self.manager_list.append(row[0])
        print(self.manager_list)
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
    
    def update(self):
        name = self.nameLineEdit.text()
        zipcode = self.zipcodeLineEdit.text()
        address = self.addressLineEdit.text()
        manager = self.managerComboBox.currentText()
        query1 = "select Username from user where concat(Firstname, \' \',Lastname) like \'"+ manager + "\';" 
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
        manager = result[0][0]
        if self.openEverydayCheckBox.isChecked():
            openeveryday = "Yes"
        else:
            openeveryday = "No"
        if self.site_exist(name):
            QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                   "Site name exists", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return
        if not isValidZipcode(zipcode):
            QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                    "Invalid zipcode: %s"%(zipcode), 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return
        if not address or not name:
            QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                    "All fileds required", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return
        sql = "insert into site values (\'" + name +"\', \'" + address + "\', \'" + zipcode + "\', \'" + openeveryday+ "\', \'" + manager +"\');"
        print(sql)
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(sql)
        connection_object.commit()
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def site_exist(self,site_name):
        sql = "select * from site where Name = \'" + site_name + "\';"
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
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
    
    def back(self):
        function_screens = {
                            "Administrator": 8,
                            "Administrator_Visitor":9,
                            }
        __main__.screen_number = function_screens[__main__.user_type]
        app.exit()

def render():
    administrator_create_site = QtWidgets.QMainWindow()
    ui = Ui_administrator_create_site()
    ui.setupUi(administrator_create_site)
    administrator_create_site.show()
    app.exec_()
    administrator_create_site.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    administrator_create_site = QtWidgets.QMainWindow()
    ui = Ui_administrator_create_site()
    ui.setupUi(administrator_create_site)
    administrator_create_site.show()
    sys.exit(app.exec_())

