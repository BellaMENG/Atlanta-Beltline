# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_take_transit.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableWidget,QPushButton,QApplication,QVBoxLayout,QTableWidgetItem,QCheckBox,QAbstractItemView,QHeaderView,QLabel,QFrame
from PyQt5.QtCore import Qt
import __main__
import sys
import mysql.connector
from PyQt5.QtWidgets import QMessageBox

app = QtWidgets.QApplication(sys.argv)

class Ui_user_take_transit(object):
    def setupUi(self, user_take_transit):
        user_take_transit.setObjectName("user_take_transit")
        user_take_transit.resize(800, 609)
        self.centralwidget = QtWidgets.QWidget(user_take_transit)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.site_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.site_combobox.setGeometry(QtCore.QRect(170, 90, 171, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.site_combobox.setFont(font)
        self.site_combobox.setObjectName("site_combobox")
        self.transport_type_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.transport_type_combobox.setFont(font)
        self.transport_type_combobox.setGeometry(QtCore.QRect(550, 90, 181, 23))
        self.transport_type_combobox.setObjectName("transport_type_combobox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.min_price_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.min_price_lineEdit.setGeometry(QtCore.QRect(170, 160, 61, 23))
        self.min_price_lineEdit.setObjectName("min_price_lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 160, 57, 15))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.max_price_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.max_price_lineEdit.setGeometry(QtCore.QRect(260, 160, 71, 23))
        self.max_price_lineEdit.setObjectName("max_price_lineEdit")
        self.filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filter_btn.setGeometry(QtCore.QRect(520, 160, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.filter_btn.setFont(font)
        self.filter_btn.setObjectName("filter_btn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 220, 691, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(50, 522, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 530, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(360, 530, 131, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.log_transit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.log_transit_btn.setGeometry(QtCore.QRect(580, 520, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.log_transit_btn.setFont(font)
        self.log_transit_btn.setObjectName("log_transit_btn")
        user_take_transit.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(user_take_transit)
        self.statusbar.setObjectName("statusbar")
        user_take_transit.setStatusBar(self.statusbar)

        self.retranslateUi(user_take_transit)
        QtCore.QMetaObject.connectSlotsByName(user_take_transit)

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Selected','        Route        ','        Transport Type        ','        Price        ','        # Connected Sites        '])
        self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4,QHeaderView.ResizeToContents)

        
    def retranslateUi(self, user_take_transit):
        _translate = QtCore.QCoreApplication.translate
        user_take_transit.setWindowTitle(_translate("user_take_transit", "User Take Transit"))
        self.label.setText(_translate("user_take_transit", "Take Transit"))
        self.label_2.setText(_translate("user_take_transit", "Contain Site"))
        self.label_3.setText(_translate("user_take_transit", "Transport Type"))
        self.label_4.setText(_translate("user_take_transit", "Price Range"))
        self.label_5.setText(_translate("user_take_transit", "--"))
        self.filter_btn.setText(_translate("user_take_transit", "Filter"))
        self.back_btn.setText(_translate("user_take_transit", "Bcak"))
        self.label_6.setText(_translate("user_take_transit", "Transit Date"))
        self.log_transit_btn.setText(_translate("user_take_transit", "Log Transit"))

        type_list = ['--ALL--','MARTA','Bus','Bike']
        self.transport_type_combobox.addItems(type_list)

        self.site_list = list()
        self.get_sites()
        self.site_combobox.addItems(self.site_list)

        self.filter_btn.clicked.connect(self.filter)
        self.log_transit_btn.clicked.connect(self.log_transit)
        self.check_box_list = list()
        self.user_name = __main__.logged_user


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

    def filter(self):
        self.check_box_list = list()
        self.tableWidget.setRowCount(0)
        contain_site = self.site_combobox.currentText()
        transport_type = self.transport_type_combobox.currentText()
        min_price = self.min_price_lineEdit.text()
        if not min_price:
            min_price = 0
        else:
            min_price = float(min_price)
        max_price = self.max_price_lineEdit.text()
        if not max_price:
            max_price = 1000
        else:
            max_price = float(max_price)
        if transport_type == "--ALL--":
            transport_type = ''
        print(contain_site)
        print(transport_type)
        print(min_price)
        print(max_price)
        mydb = mysql.connector.connect(
                 host="localhost",       # 数据库主机地址
                user="root",    # 数据库用户名
                passwd='',
                database = 'beltline_version2'
                )
        cursor = mydb.cursor()
        sql = "call get_transit_options(\'"+ contain_site+ "\',\'"+ transport_type+"\',"+str(min_price)+","+str(max_price)+");"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)
            self.add_line(row)
        if(mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")

    def add_line(self,row):
        route,transport_type,price,connected_sites = row
        #route,transport_type,price,connected_sites = ['816','Bus','2.5','3']
        connected_sites = str(connected_sites)
        price = str(price)
        row_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_count + 1)
        ck = QCheckBox()
        h = QHBoxLayout()
        h.setAlignment(Qt.AlignCenter)
        h.addWidget(ck)
        w = QWidget()
        w.setLayout(h)
        self.tableWidget.setCellWidget(row_count,0,w)
        self.tableWidget.setItem(row_count,1,QTableWidgetItem(route))
        self.tableWidget.setItem(row_count,2,QTableWidgetItem(transport_type))
        self.tableWidget.setItem(row_count,3,QTableWidgetItem(price))
        self.tableWidget.setItem(row_count,4,QTableWidgetItem(connected_sites))
        self.check_box_list.append(ck)
    
    def log_transit(self):
        idx = -1
        info = list()
        info.append(self.user_name)
        date = self.dateEdit.date()
        

        for i in range(len(self.check_box_list)):
            if self.check_box_list[i].isChecked():
                if idx == -1:
                    idx = i
                else:
                    QMessageBox.warning(self.label, 
                                    "Invalid Input", 
                                    "Can not register multiple transit in one day", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
                    return
        if idx == -1:
            QMessageBox.warning(self.label, 
                                    "Invalid Input", 
                                    "No Route Selected!", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
            return
        else:
            route = self.tableWidget.item(idx ,1).text()
            transport_type = self.tableWidget.item(idx ,2).text()
            if self.hasTakenTransit(date,route,transport_type):
                QMessageBox.warning(self.label, 
                                    "Log Error", 
                                    "Can not register multiple transit in one day", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
                return
            info.append(self.tableWidget.item(idx ,2).text())
            info.append(self.tableWidget.item(idx ,1).text())
            formatted_date = date.toString(Qt.ISODate)
            info.append(formatted_date)
            connection_object = __main__.connection_pool.get_connection()
            if connection_object.is_connected():
                db_Info = connection_object.get_server_info()
                print("user_login.py login() Connected to MySQL server: ",db_Info)
            else:
                print("user_login.py login() Not Connected ")
            cursor = connection_object.cursor()
            cursor.callproc('log_user_transit',info)
            connection_object.commit()
            if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")
    
    def hasTakenTransit(self,date,route,transport_type):
        formatted_date = date.toString(Qt.ISODate)
        query1 = "SELECT count(*) FROM take WHERE Username = \'" + self.user_name + "\' and TransitDate = \'" + formatted_date + "\' and Route = \'" + route + "\' and TransportType = \'"+ transport_type + "\';" 
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

def render():
    user_take_transit = QtWidgets.QMainWindow()
    ui = Ui_user_take_transit()
    ui.setupUi(user_take_transit)
    user_take_transit.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user_take_transit = QtWidgets.QMainWindow()
    ui = Ui_user_take_transit()
    ui.setupUi(user_take_transit)
    user_take_transit.show()
    sys.exit(app.exec_())

