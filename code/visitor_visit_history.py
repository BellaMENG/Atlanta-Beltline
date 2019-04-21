# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '38visitor_visit_history.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt

app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 671, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.edateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout.addWidget(self.edateEdit, 2, 5, 1, 1)
        self.site_content = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.site_content.setObjectName("site_content")
        self.site_content.addItem("")
        self.gridLayout.addWidget(self.site_content, 1, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.event = QtWidgets.QLabel(self.gridLayoutWidget)
        self.event.setObjectName("event")
        self.gridLayout.addWidget(self.event, 1, 0, 1, 1)
        self.event_content = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.event_content.setObjectName("event_content")
        self.gridLayout.addWidget(self.event_content, 1, 1, 1, 1)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout.addWidget(self.sdateEdit, 2, 1, 1, 1)
        self.sdate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sdate.setObjectName("sdate")
        self.gridLayout.addWidget(self.sdate, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 6, 1, 1)
        self.visitHistory = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.visitHistory.setFont(font)
        self.visitHistory.setAlignment(QtCore.Qt.AlignCenter)
        self.visitHistory.setObjectName("visitHistory")
        self.gridLayout.addWidget(self.visitHistory, 0, 0, 1, 7)
        self.site = QtWidgets.QLabel(self.gridLayoutWidget)
        self.site.setObjectName("site")
        self.gridLayout.addWidget(self.site, 1, 3, 1, 2)
        self.edate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.edate.setObjectName("edate")
        self.gridLayout.addWidget(self.edate, 2, 3, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 661, 271))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.filterbtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.filterbtn.setObjectName("filterbtn")
        self.gridLayout_2.addWidget(self.filterbtn, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.backbtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.backbtn.setObjectName("backbtn")
        self.gridLayout_2.addWidget(self.backbtn, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.historyTable = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.historyTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.historyTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.historyTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.historyTable.setObjectName("historyTable")
        self.historyTable.setColumnCount(4)
        self.historyTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.historyTable, 1, 0, 1, 3)
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

        if __main__.user_type == 'Administrator_Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=9))
        elif __main__.user_type == 'Manager_Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=11))
        elif __main__.user_type == 'Staff_Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=13))
        elif __main__.user_type == 'Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=14))
        else:
            self.backbtn.clicked.connect(lambda: self.func(idx=14))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Visit History"))
        self.site_content.setItemText(0, _translate("MainWindow", "--ALL--"))
        self.event.setText(_translate("MainWindow", "Event"))
        self.sdate.setText(_translate("MainWindow", "Start Date"))
        self.visitHistory.setText(_translate("MainWindow", "Visit History"))
        self.site.setText(_translate("MainWindow", "Site"))
        self.edate.setText(_translate("MainWindow", "End Date"))
        self.filterbtn.setText(_translate("MainWindow", "Filter"))
        self.backbtn.setText(_translate("MainWindow", "Back"))
        self.historyTable.setSortingEnabled(True)
        item = self.historyTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.historyTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Event"))
        item = self.historyTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Site"))
        item = self.historyTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))

        # TODO: remember to remove this!!!!
        if __main__.logged_user is None:
            __main__.logged_user = 'visitor1'
        self.user_name = __main__.logged_user

        # TODO: decide which page to go back
        if __main__.user_type == 'Administrator_Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=9))
        elif __main__.user_type == 'Manager_Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=11))
        elif __main__.user_type == 'Staff_Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=13))
        elif __main__.user_type == 'Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=14))
        else:
            self.backbtn.clicked.connect(lambda: self.func(idx=14))

        self.retrieve_info()
        self.filterbtn.clicked.connect(self.filter)

    def filter(self):
        self.historyTable.setRowCount(0)
        event_name = self.event_content.text()
        site_name = self.site_content.currentText()
        if site_name == '--ALL--':
            site_name = ''
        start_date = self.sdateEdit.date().toString(Qt.ISODate)
        end_date = self.edateEdit.date().toString(Qt.ISODate)
        query1 = "select visit_event.EndDate, visit_event.Name, visit_event.SiteName, " \
                 "event.Price from visit_event join event on visit_event.Name = event.Name " \
                 "and visit_event.SiteName = event.SiteName and visit_event.StartDate = event.StartDate " \
                 "where Username = \'" + self.user_name + "\' " \
                 "and visit_event.EndDate " \
                 "between \'" + start_date + "\' and \'" + end_date + "\' " \
                 "and visit_event.Name like \'%" + event_name + "%\' " \
                 "and visit_event.SiteName like \'%" + site_name + "%\';"

        result1 = self.retrieve_from_db(query1)

        for row in result1:
            self.add_lines(row)

        query2 = "select VisitSiteDate, Name from visit_site " \
                 "where Username = \'" + self.user_name + "\' and VisitSiteDate " \
                 "between \'" + start_date + "\' and \'" + end_date + "\' " \
                 "and visit_site.Name like \'%" + site_name + "%\';"
        result2 = self.retrieve_from_db(query2)

        for row in result2:
            date, site = row
            event = ''
            price = 0
            single_row = [date, event, site, price]
            self.add_lines(single_row)


    def retrieve_info(self):
        query = "select Name from site"
        result = self.retrieve_from_db(query)
        site_list = list()
        for row in result:
            site_list.append(row[0])

        self.site_content.addItems(site_list)

    def add_lines(self, row):
        date, event_name, site, price = row
        row_count = self.historyTable.rowCount()
        self.historyTable.setRowCount(row_count + 1)
        self.historyTable.setItem(row_count, 0, QTableWidgetItem(str(date)))
        self.historyTable.setItem(row_count, 1, QTableWidgetItem(str(event_name)))
        self.historyTable.setItem(row_count, 2, QTableWidgetItem(str(site)))
        self.historyTable.setItem(row_count, 3, QTableWidgetItem(str(price)))

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

    def func(self, idx):
        __main__.screen_number = idx
        app.exit()

def render():
    visitor_visit_history = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(visitor_visit_history)
    visitor_visit_history.show()
    app.exec_()

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
