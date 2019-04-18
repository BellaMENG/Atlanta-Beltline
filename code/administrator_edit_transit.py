# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administrator_edit_transit.ui'
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

app = QtWidgets.QApplication(sys.argv)

class Ui_administrator_edit_transit(object):
    def __init__(self,route,transport_type,price):
        self.route = route
        self.transport_type = transport_type
        self.price = price

    def setupUi(self, administrator_edit_transit):
        administrator_edit_transit.setObjectName("administrator_edit_transit")
        administrator_edit_transit.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(administrator_edit_transit)
        self.centralwidget.setObjectName("centralwidget")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(559, 520, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.update_btn.setFont(font)
        self.update_btn.setObjectName("update_btn")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(280, 150, 481, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(110, 520, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 220, 241, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.routeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.routeLabel.setFont(font)
        self.routeLabel.setObjectName("routeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.routeLabel)
        self.routeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.routeLineEdit.setFont(font)
        self.routeLineEdit.setObjectName("routeLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.routeLineEdit)
        self.priceLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.priceLabel.setFont(font)
        self.priceLabel.setObjectName("priceLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.priceLabel)
        self.priceLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.priceLineEdit.setFont(font)
        self.priceLineEdit.setObjectName("priceLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.priceLineEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 169, 241, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.transport_type_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("STIXGeneral")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.transport_type_label.setFont(font)
        self.transport_type_label.setObjectName("transport_type_label")
        self.horizontalLayout.addWidget(self.transport_type_label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 120, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        administrator_edit_transit.setCentralWidget(self.centralwidget)

        self.retranslateUi(administrator_edit_transit)
        QtCore.QMetaObject.connectSlotsByName(administrator_edit_transit)

    def retranslateUi(self, administrator_edit_transit):
        _translate = QtCore.QCoreApplication.translate
        administrator_edit_transit.setWindowTitle(_translate("administrator_edit_transit", "Administrator Edit Transit"))
        self.update_btn.setText(_translate("administrator_edit_transit", "Update"))
        self.back_btn.setText(_translate("administrator_edit_transit", "Back"))
        self.label.setText(_translate("administrator_edit_transit", "Edit Transit"))
        self.routeLabel.setText(_translate("administrator_edit_transit", "Route"))
        self.priceLabel.setText(_translate("administrator_edit_transit", "Price"))
        self.label_2.setText(_translate("administrator_edit_transit", "Transport Type"))
        self.transport_type_label.setText(_translate("administrator_edit_transit", "TextLabel"))
        self.label_4.setText(_translate("administrator_edit_transit", "Connected Sites"))
        self.site_list = list()
        self.get_sites()
        self.listWidget.addItems(self.site_list)
        self.listWidget.setSelectionMode(QtWidgets.QListWidget.MultiSelection)
        managed_list = self.get_routed_sites()
        for i in managed_list:
            matching_items = self.listWidget.findItems(i, Qt.MatchExactly)
            for item in matching_items:
                item.setSelected(True)
        self.transport_type_label.setText(_translate("administrator_edit_transit", self.transport_type))
        self.routeLineEdit.setText(self.route)
        self.priceLineEdit.setText(str(self.price))
        self.update_btn.clicked.connect(self.update)
        self.back_btn.clicked.connect(lambda:self.func(idx=1))

    def update(self):
        route = self.routeLineEdit.text()
        price = self.priceLineEdit.text()
        p = float(price)
        items = self.listWidget.selectedItems()
        if len(items) < 2:
            QMessageBox.warning(self.label, 
                                    "Invalid Input", 
                                    "Select at least 2 sites", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return
        if p < 0:
            QMessageBox.warning(self.label, 
                                    "Invalid Input", 
                                    "Price can not less than 0", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return
        if not self.route == route:
            if self.route_exist(route):
                QMessageBox.warning(self.label, 
                                    "Invalid Input", 
                                    "Route Name Exist", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
                return
            if not route:
                if self.route_exist(route):
                    QMessageBox.warning(self.label, 
                                    "Invalid Input", 
                                    "Route Can not be None", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
                    return
            sql = "update transit set Route= \'" + route + "\', Price= " + price +" where route = \'" + self.route + "\' and TransportType = \'" + self.transport_type + "\';"
        else:
            sql = "update transit set Price= " + price +" where route = \'" + self.route + "\' and TransportType = \'" + self.transport_type + "\';"
        
        sql1 = "delete from connect where Route = \'" + self.route + "\' and TransportType = \'" + self.transport_type + "\';"
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(sql1)
        cursor.execute(sql)
        for i in items:
            sql2 = "insert into connect values (\'" + i.text() + "\', \'"+route+"\', \'"+self.transport_type+"\');"
            cursor.execute(sql2)

        connection_object.commit()
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        

    def get_sites(self):
        query1 = "SELECT DISTINCT Name FROM connect;" 
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
            self.site_list.append(row[0])
        print(self.site_list)
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        
    def get_routed_sites(self):
        query1 = "SELECT DISTINCT Name FROM connect where Route = \'" + self.route +"\';" 
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        temp = list()
        for row in result:
            temp.append(row[0])
        print(self.site_list)
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        return temp

    def route_exist(self,route):
        query1 = "SELECT * FROM transit where Route = \'" + route +"\' and TransportType = \'" + self.transport_type + "\';" 
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
        if len(result) == 0:
            return False
        else:
            return True

    def func(self,idx):
            __main__.screen_number = idx
            app.exit()

def render(route,transport_type,price):
    administrator_edit_transit = QtWidgets.QMainWindow()
    ui = Ui_administrator_edit_transit(route,transport_type,price)
    ui.setupUi(administrator_edit_transit)
    administrator_edit_transit.show()
    app.exec_()
    administrator_edit_transit.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    administrator_edit_transit = QtWidgets.QMainWindow()
    ui = Ui_administrator_edit_transit()
    ui.setupUi(administrator_edit_transit)
    administrator_edit_transit.show()
    sys.exit(app.exec_())

