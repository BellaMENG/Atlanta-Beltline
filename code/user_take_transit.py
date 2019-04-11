# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_take_transit.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableWidget,QPushButton,QApplication,QVBoxLayout,QTableWidgetItem,QCheckBox,QAbstractItemView,QHeaderView,QLabel,QFrame
from PyQt5.QtCore import Qt
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
        self.tableWidget.setHorizontalHeaderLabels(['Selected','Route','Transport Type','Price','# Connected Sites'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
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

        type_list = ['MARTA','Bus','Bike']
        self.transport_type_combobox.addItems(type_list)

        self.filter_btn.clicked.connect(self.add_line)
        self.log_transit_btn.clicked.connect(self.log_transit)
        self.check_box_list = list()

    def filter(self):
        contain_site = self.site_combobox.currentText()
        transport_type = self.transport_type_combobox.currentText()
        min_price = self.min_price_lineEdit.text()
        max_price = self.max_price_lineEdit.text()
        print(contain_site)
        print(transport_type)
        print(min_price)
        print(max_price)

    def add_line(self):
        #route,transport_type,price,connected_sites = ss.split()
        route,transport_type,price,connected_sites = ['816','Bus','2.5','3']
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
        for i in range(len(self.check_box_list)):
            if self.check_box_list[i].isChecked():
                if idx == -1:
                    idx = i
                else:
                    print("Can not register multiple transit in one day")
                    return
        info.append(self.tableWidget.item(idx ,1).text())
        info.append(self.tableWidget.item(idx ,2).text())
        info.append(self.tableWidget.item(idx ,3).text())
        info.append(self.tableWidget.item(idx ,4).text())
                    
        if idx == -1:
            print("Please select a route")
        else:
            print(info)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user_take_transit = QtWidgets.QMainWindow()
    ui = Ui_user_take_transit()
    ui.setupUi(user_take_transit)
    user_take_transit.show()
    sys.exit(app.exec_())

