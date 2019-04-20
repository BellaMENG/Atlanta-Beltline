# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '36visitor_transit_detail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 671, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.siteContent = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.siteContent.setFont(font)
        self.siteContent.setText("")
        self.siteContent.setObjectName("siteContent")
        self.gridLayout.addWidget(self.siteContent, 1, 1, 1, 1)
        self.transportType = QtWidgets.QLabel(self.gridLayoutWidget)
        self.transportType.setObjectName("transportType")
        self.gridLayout.addWidget(self.transportType, 1, 2, 1, 1)
        self.site = QtWidgets.QLabel(self.gridLayoutWidget)
        self.site.setObjectName("site")
        self.gridLayout.addWidget(self.site, 1, 0, 1, 1)
        self.transportTypeList = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.transportTypeList.setObjectName("transportTypeList")
        self.transportTypeList.addItem("")
        self.transportTypeList.addItem("")
        self.transportTypeList.addItem("")
        self.gridLayout.addWidget(self.transportTypeList, 1, 3, 1, 1)
        self.transitDetail = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.transitDetail.setFont(font)
        self.transitDetail.setAlignment(QtCore.Qt.AlignCenter)
        self.transitDetail.setObjectName("transitDetail")
        self.gridLayout.addWidget(self.transitDetail, 0, 0, 1, 4)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 671, 251))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.transitDate = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.transitDate.setObjectName("transitDate")
        self.gridLayout_2.addWidget(self.transitDate, 1, 1, 1, 1)
        self.logTransit = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.logTransit.setObjectName("logTransit")
        self.gridLayout_2.addWidget(self.logTransit, 1, 3, 1, 1)
        self.transitTable = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.transitTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.transitTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.transitTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.transitTable.setObjectName("transitTable")
        self.transitTable.setColumnCount(4)
        self.transitTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.transitTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.transitTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.transitTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.transitTable.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.transitTable, 0, 0, 1, 4)
        self.backbtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.backbtn.setObjectName("backbtn")
        self.gridLayout_2.addWidget(self.backbtn, 1, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 2, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transit Detail"))
        self.transportType.setText(_translate("MainWindow", "Transport Type"))
        self.site.setText(_translate("MainWindow", "Site"))
        self.transportTypeList.setItemText(0, _translate("MainWindow", "MARTA"))
        self.transportTypeList.setItemText(1, _translate("MainWindow", "Bus"))
        self.transportTypeList.setItemText(2, _translate("MainWindow", "Bike"))
        self.transitDetail.setText(_translate("MainWindow", "Transit Detail"))
        self.transitDate.setText(_translate("MainWindow", "Transit Date"))
        self.logTransit.setText(_translate("MainWindow", "Log Transit"))
        self.transitTable.setSortingEnabled(True)
        item = self.transitTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Route"))
        item = self.transitTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Transport Type"))
        item = self.transitTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.transitTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "# Connected Sites"))
        self.backbtn.setText(_translate("MainWindow", "Back"))

        self.selected = None
        self.retrieve_info()
        self.transitTable.clicked.connect(self.selected_rows)
        if __main__.logged_user is None:
            __main__.logged_user = 'visitor1'
        self.user_name = __main__.logged_user

        self.backbtn.clicked.connect(lambda: self.func(idx=35))
        self.logTransit.clicked.connect(self.log_transit)

    def retrieve_info(self):
        site_name = __main__.selected_site35
        self.siteContent.setText(site_name)
        trans_type = self.transportTypeList.currentText()

        transits_query = "select Route from connect " \
                         "where Name = \'" + site_name + "\' and TransportType = \'" + trans_type + "\';"
        result = self.retrieve_from_db(transits_query)
        # TODO: get transits and get the price and connected sites
        for row in result:
            route = row[0]
            query1 = "select Price from transit " \
                     "where Route = \'" + route + "\' " \
                     "and TransportType = \'" + trans_type + "\';"
            result = self.retrieve_from_db(query1)
            price = result[0][0]
            query2 = "select count(*) from connect " \
                     "where Route = \'" + route + "\' " \
                     "and TransportType = \'" + trans_type + "\';"
            result = self.retrieve_from_db(query2)
            num_con = result[0][0]
            single_row = [route, trans_type, price, num_con]
            self.add_lines(single_row)

    def add_lines(self, row):
        route, trans_type, price, num_sites = row
        row_count = self.transitTable.rowCount()
        self.transitTable.setRowCount(row_count + 1)
        self.transitTable.setItem(row_count, 0, QTableWidgetItem(str(route)))
        self.transitTable.setItem(row_count, 1, QTableWidgetItem(str(trans_type)))
        self.transitTable.setItem(row_count, 2, QTableWidgetItem(str(price)))
        self.transitTable.setItem(row_count, 3, QTableWidgetItem(str(num_sites)))

    def retrieve_from_db(self, query):
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ", db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        return result

    def update_db(self, query):
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ", db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query)
        connection_object.commit()
        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def log_transit(self):
        # TODO: log transit into the db
        if self.selected is None:
            self.msgDialog("You must select a transit before logging the transit!")
            return
        route, trans_type = self.selected
        transit_date = self.dateEdit.date().toString(Qt.ISODate)
        user_name = self.user_name

        query = "select TransitDate from take " \
                "where Route = \'" + route + "\' " \
                "and TransportType = \'" + trans_type + "\' " \
                "and Username = \'" + user_name + "\';"
        result = self.retrieve_from_db(query)
        transit_dates = list()
        if len(result) != 0:
            for row in result:
                transit_dates.append(str(row[0]))
            if transit_date in transit_dates:
                self.msgDialog("You can only take the same transit once a day!")
                return

        query = "insert into take " \
                "VALUES(\'" + user_name + "\', \'" + trans_type + "\', " \
                "\'" + route + "\', \'" + transit_date + "\');"
        print(query)
        self.update_db(query)

    def selected_rows(self):
        # TODO: handle selected rows and put it in global var
        rowPos = self.transitTable.currentRow()
        self.selected = [self.transitTable.item(rowPos, 0).text(), self.transitTable.item(rowPos, 1).text()]

    def msgDialog(self, m):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Sorry!")
        msg.setInformativeText("This action is not allowed.")
        msg.setWindowTitle("Not allowed")
        msg.setDetailedText(m)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def func(self, idx):
        __main__.screen_number = idx
        app.exit()

def render():
    visitor_transit_detail = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(visitor_transit_detail)
    visitor_transit_detail.show()
    app.exec_()

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
