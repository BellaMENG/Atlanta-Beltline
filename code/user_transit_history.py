# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_transit_history.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableWidget,QPushButton,QApplication,QVBoxLayout,QTableWidgetItem,QCheckBox,QAbstractItemView,QHeaderView,QLabel,QFrame
from PyQt5.QtCore import Qt
import __main__
import sys

app = QtWidgets.QApplication(sys.argv)

class Ui_user_transit_history(object):
    def setupUi(self, user_transit_history):
        user_transit_history.setObjectName("user_transit_history")
        user_transit_history.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(user_transit_history)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 80, 321, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.transportTypeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.transportTypeLabel.setFont(font)
        self.transportTypeLabel.setObjectName("transportTypeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.transportTypeLabel)
        self.transportTypeComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.transportTypeComboBox.setFont(font)
        self.transportTypeComboBox.setObjectName("transportTypeComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.transportTypeComboBox)
        self.containSiteLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.containSiteLabel.setFont(font)
        self.containSiteLabel.setObjectName("containSiteLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.containSiteLabel)
        self.containSiteComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.containSiteComboBox.setFont(font)
        self.containSiteComboBox.setObjectName("containSiteComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.containSiteComboBox)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(480, 80, 271, 125))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(30)
        self.formLayout_2.setVerticalSpacing(20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.routeLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.routeLabel.setFont(font)
        self.routeLabel.setObjectName("routeLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.routeLabel)
        self.routeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.routeLineEdit.setFont(font)
        self.routeLineEdit.setObjectName("routeLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.routeLineEdit)
        self.startDateLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startDateLabel.setFont(font)
        self.startDateLabel.setObjectName("startDateLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.startDateLabel)
        self.startDateDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startDateDateEdit.setFont(font)
        self.startDateDateEdit.setObjectName("startDateDateEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.startDateDateEdit)
        self.endDateLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.endDateLabel.setFont(font)
        self.endDateLabel.setObjectName("endDateLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.endDateLabel)
        self.endDateDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.endDateDateEdit.setFont(font)
        self.endDateDateEdit.setObjectName("endDateDateEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.endDateDateEdit)
        self.filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filter_btn.setGeometry(QtCore.QRect(570, 530, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.filter_btn.setFont(font)
        self.filter_btn.setObjectName("filter_btn")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(50, 530, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 240, 551, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        user_transit_history.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(user_transit_history)
        self.statusbar.setObjectName("statusbar")
        user_transit_history.setStatusBar(self.statusbar)

        self.retranslateUi(user_transit_history)
        QtCore.QMetaObject.connectSlotsByName(user_transit_history)

    def retranslateUi(self, user_transit_history):
        _translate = QtCore.QCoreApplication.translate
        user_transit_history.setWindowTitle(_translate("user_transit_history", "User Transit History"))
        self.label.setText(_translate("user_transit_history", "Transit History"))
        self.transportTypeLabel.setText(_translate("user_transit_history", "Transport Type"))
        self.containSiteLabel.setText(_translate("user_transit_history", "Contain Site"))
        self.routeLabel.setText(_translate("user_transit_history", "Route"))
        self.startDateLabel.setText(_translate("user_transit_history", "Start Date"))
        self.endDateLabel.setText(_translate("user_transit_history", "End Date"))
        self.filter_btn.setText(_translate("user_transit_history", "Filter"))
        self.back_btn.setText(_translate("user_transit_history", "Back"))

        type_list = ['--ALL--','MARTA','Bus','Bike']
        self.transportTypeComboBox.addItems(type_list)

        self.site_list = list()
        self.get_sites()
        self.containSiteComboBox.addItems(self.site_list)

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['          Date           ','        Route        ','           Transport Type        ','      Price    '])
        self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)

        self.user_name = __main__.logged_user
        self.filter_btn.clicked.connect(self.filter)
        self.back_btn.clicked.connect(lambda:self.func(idx=1))


    def filter(self):
        self.tableWidget.setRowCount(0)
        contain_site = self.containSiteComboBox.currentText()
        transport_type = self.transportTypeComboBox.currentText()
        route = self.routeLineEdit.text()
        end_date = self.endDateDateEdit.date().toString(Qt.ISODate)
        start_date = self.startDateDateEdit.date().toString( Qt.ISODate)
        if transport_type == "--ALL--":
            transport_type = ''
        sql = "select take.TransitDate,take.Route,take.TransportType,transit.Price from take join transit on take.Route = transit.Route where transit.TransportType like concat(\'%\',\'"+ transport_type + "\',\'%\') and take.Username like \'" + self.user_name + "\' \
                and take.TransitDate >= \'" + start_date + "\' and take.TransitDate <= \'" + end_date + "\' and take.Route in (select Route from connect where connect.Name like \'" + contain_site + "\' and connect.Route =\'"+ route + "\');"
        # print(sql)
        # print(contain_site)
        # print(transport_type)
        # print(start_date)
        # print(end_date)
        # print(route)    
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            self.add_line(row)
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
    
    

    def add_line(self,row):
        date,route,transport_type,price = row
        date = str(date)
        print(date)
        price = str(price)
        row_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_count + 1)
        self.tableWidget.setItem(row_count,0,QTableWidgetItem(date))
        self.tableWidget.setItem(row_count,1,QTableWidgetItem(route))
        self.tableWidget.setItem(row_count,2,QTableWidgetItem(transport_type))
        self.tableWidget.setItem(row_count,3,QTableWidgetItem(price))

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

    def func(self,idx):
        __main__.screen_number = idx
        app.exit()

def render():
    user_transit_history = QtWidgets.QMainWindow()
    ui = Ui_user_transit_history()
    ui.setupUi(user_transit_history)
    user_transit_history.show()
    app.exec_()
    user_transit_history.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user_transit_history = QtWidgets.QMainWindow()
    ui = Ui_user_transit_history()
    ui.setupUi(user_transit_history)
    user_transit_history.show()
    sys.exit(app.exec_())

