# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '33visitor_explore_event.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox

import __main__
app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 671, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.siteName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.siteName.setObjectName("siteName")
        self.gridLayout.addWidget(self.siteName, 2, 0, 1, 1)
        self.descriptionKeyword = QtWidgets.QLabel(self.gridLayoutWidget)
        self.descriptionKeyword.setObjectName("descriptionKeyword")
        self.gridLayout.addWidget(self.descriptionKeyword, 1, 2, 1, 1)
        self.exploreEvent = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.exploreEvent.setFont(font)
        self.exploreEvent.setAlignment(QtCore.Qt.AlignCenter)
        self.exploreEvent.setObjectName("exploreEvent")
        self.gridLayout.addWidget(self.exploreEvent, 0, 0, 1, 4)
        self.descriptionKeywordContent = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.descriptionKeywordContent.setObjectName("descriptionKeywordContent")
        self.gridLayout.addWidget(self.descriptionKeywordContent, 1, 3, 1, 1)
        self.name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 0, 1, 1)
        self.nameContent = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.nameContent.setObjectName("nameContent")
        self.gridLayout.addWidget(self.nameContent, 1, 1, 1, 1)
        self.siteNameList = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.siteNameList.setObjectName("siteNameList")
        self.gridLayout.addWidget(self.siteNameList, 2, 1, 1, 3)
        self.sdate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sdate.setObjectName("sdate")
        self.gridLayout.addWidget(self.sdate, 3, 0, 1, 1)
        self.edate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.edate.setObjectName("edate")
        self.gridLayout.addWidget(self.edate, 3, 2, 1, 1)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout.addWidget(self.sdateEdit, 3, 1, 1, 1)
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.edateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout.addWidget(self.edateEdit, 3, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 160, 671, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tvrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.tvrEnd.setObjectName("tvrEnd")
        self.gridLayout_2.addWidget(self.tvrEnd, 0, 3, 1, 1)
        self.tvrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.tvrStart.setObjectName("tvrStart")
        self.gridLayout_2.addWidget(self.tvrStart, 0, 1, 1, 1)
        self.tprEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.tprEnd.setObjectName("tprEnd")
        self.gridLayout_2.addWidget(self.tprEnd, 0, 7, 1, 1)
        self.tvr = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.tvr.setObjectName("tvr")
        self.gridLayout_2.addWidget(self.tvr, 0, 0, 1, 1)
        self.tprStart = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.tprStart.setObjectName("tprStart")
        self.gridLayout_2.addWidget(self.tprStart, 0, 5, 1, 1)
        self.tpr = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.tpr.setObjectName("tpr")
        self.gridLayout_2.addWidget(self.tpr, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 6, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 210, 671, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.includeVisited = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.includeVisited.setObjectName("includeVisited")
        self.gridLayout_3.addWidget(self.includeVisited, 0, 0, 1, 1)
        self.includeSoldOutEvent = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.includeSoldOutEvent.setObjectName("includeSoldOutEvent")
        self.gridLayout_3.addWidget(self.includeSoldOutEvent, 0, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 260, 671, 271))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.filterbtn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.filterbtn.setObjectName("filterbtn")
        self.gridLayout_4.addWidget(self.filterbtn, 0, 1, 1, 1)
        self.eventDetail = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.eventDetail.setObjectName("eventDetail")
        self.gridLayout_4.addWidget(self.eventDetail, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 2, 1, 1)
        self.eventTable = QtWidgets.QTableWidget(self.gridLayoutWidget_4)
        self.eventTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.eventTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.eventTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.eventTable.setObjectName("eventTable")
        self.eventTable.setColumnCount(7)
        self.eventTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.eventTable.setHorizontalHeaderItem(6, item)
        self.gridLayout_4.addWidget(self.eventTable, 1, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 4, 1, 1)
        self.backbtn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.backbtn.setObjectName("backbtn")
        self.gridLayout_4.addWidget(self.backbtn, 2, 2, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Explore Event"))
        self.siteName.setText(_translate("MainWindow", "Site Name"))
        self.descriptionKeyword.setText(_translate("MainWindow", "Description Keyword"))
        self.exploreEvent.setText(_translate("MainWindow", "Explore Event"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.sdate.setText(_translate("MainWindow", "Start Date"))
        self.edate.setText(_translate("MainWindow", "End Date"))
        self.tvr.setText(_translate("MainWindow", "Total Visits Range"))
        self.tpr.setText(_translate("MainWindow", "Ticket Price Range"))
        self.label_7.setText(_translate("MainWindow", "--"))
        self.label_9.setText(_translate("MainWindow", "--"))
        self.includeVisited.setText(_translate("MainWindow", "Include Visited"))
        self.includeSoldOutEvent.setText(_translate("MainWindow", "Include Sold Out Event"))
        self.filterbtn.setText(_translate("MainWindow", "Filter"))
        self.eventDetail.setText(_translate("MainWindow", "Event Detail"))
        self.eventTable.setSortingEnabled(True)
        item = self.eventTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Event Name"))
        item = self.eventTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Site Name"))
        item = self.eventTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ticket Price"))
        item = self.eventTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ticket Remaining"))
        item = self.eventTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total Visits"))
        item = self.eventTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "My Visits"))
        item = self.eventTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Start Date"))
        self.backbtn.setText(_translate("MainWindow", "Back"))

        # TODO: remember to remove this!!!!
        if __main__.logged_user is None:
            __main__.logged_user = 'staff2'
        self.user_name = __main__.logged_user
        self.add_sites_to_list()

        if __main__.user_type == 'Administrator_Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=9))
        elif __main__.user_type == 'Manager_Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=11))
        elif __main__.user_type == 'Staff_Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=13))
        elif __main__.user_type == 'Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=14))
        else:
            self.backbtn.clicked.connect(lambda: self.func(idx=13))

        self.filterbtn.clicked.connect(self.filter)
        self.eventTable.clicked.connect(self.selected_row)
        self.eventDetail.clicked.connect(self.view_detail)

    def view_detail(self):
        if __main__.selected_event33 is None:
            self.msgDialog("An event must be selected before viewing detail!")
        else:
            self.func(idx=34)

    def checkIntMin(self, minVal):
        if not minVal:
            return -1
        else:
            return int(minVal)

    def checkFloatMin(self, minVal):
        if not minVal:
            return -1
        else:
            return float(minVal)

    def checkIntMax(self, maxVal):
        if not maxVal:
            return 99999999
        else:
            return int(maxVal)

    def checkFloatMax(self, maxVal):
        if not maxVal:
            return 99999999
        else:
            return float(maxVal)

    def add_sites_to_list(self):
        site_list = list()
        site_list.append("--ALL--")
        query1 = "select distinct SiteName from assign_to"
        result = self.retrieve_from_db(query1)
        for row in result:
            site_list.append(row[0])

        self.siteNameList.addItems(site_list)
        return

    def filter(self):
        self.eventTable.setRowCount(0)  # clean the table first
        name_contain = self.nameContent.text()
        des_contain = self.descriptionKeywordContent.text()
        site_name = self.siteNameList.currentText()
        sdate = self.sdateEdit.date().toString(Qt.ISODate)
        edate = self.edateEdit.date().toString(Qt.ISODate)

        if site_name == "--ALL--":
            query = "select Name, StartDate, SiteName, Price, Capacity " \
                    "from event where Name like \'%" + name_contain + "%\' " \
                    "and StartDate >= \'" + sdate + "\' " \
                    "and EndDate <= \'" + edate + "\' " \
                    "and Description like \'%" + des_contain + "%\';"
            print(query)
            result = self.retrieve_from_db(query)
        else:
            query = "select Name, StartDate, SiteName, Price, Capacity " \
                    "from event where Name like \'%" + name_contain + "%\' " \
                    "and StartDate >= \'" + sdate + "\' " \
                    "and EndDate <= \'" + edate + "\' " \
                    "and Description like \'%" + des_contain + "%\' " \
                    "and SiteName = \'" + site_name + "\';"
            print(query)
            result = self.retrieve_from_db(query)

        for row in result:
            name, d1, sname, p, cap = row
            total_visit_query = "select count(*) from visit_event " \
                    "where Name = \'" + name + "\' " \
                    "and StartDate = \'" + str(d1) + "\' " \
                    "and SiteName = \'" + sname + "\';"
            total_visit_result = self.retrieve_from_db(total_visit_query)
            total_visits = int(total_visit_result[0][0])

            my_visit_query = "select count(*) from visit_event " \
                             "where Username = \'" + self.user_name + "\' " \
                             "and Name = \'" + name + "\' " \
                             "and StartDate = \'" + str(d1) + "\' " \
                             "and SiteName = \'" + sname + "\';"
            my_visit_result = self.retrieve_from_db(my_visit_query)
            tickets_re = int(cap) - total_visits
            my_visits = int(my_visit_result[0][0])
            single_row = [name, sname, p, tickets_re, total_visits, my_visits, str(d1)]
            self.add_lines(single_row)

    def selected_row(self):
        rowPos = self.eventTable.currentRow()
        __main__.selected_event33 = [self.eventTable.item(rowPos, 0).text(),
                                     self.eventTable.item(rowPos, 6).text(),
                                     self.eventTable.item(rowPos, 1).text(),
                                     self.eventTable.item(rowPos, 3).text()]
        # name, start date, site name, tickets remaining
        print(__main__.selected_event33)

    def add_lines(self, row):
        name, site_name, price, tickets_r, total_v, my_v, start_date = row
        tvr1 = self.checkIntMin(self.tvrStart.text())
        tvr2 = self.checkIntMax(self.tvrEnd.text())
        tpr1 = self.checkFloatMin(self.tprStart.text())
        tpr2 = self.checkFloatMax(self.tprEnd.text())
        include_visited = self.includeVisited.isChecked()
        include_sold_out = self.includeSoldOutEvent.isChecked()

        if (not tvr1 <= total_v <= tvr2) or (not tpr1 <= price <= tpr2):
            return

        if not include_visited:
            if my_v > 0:
                return

        if not include_sold_out:
            if tickets_r == 0:
                return
        row_count = self.eventTable.rowCount()
        self.eventTable.setRowCount(row_count + 1)
        self.eventTable.setItem(row_count, 0, QTableWidgetItem(str(name)))
        self.eventTable.setItem(row_count, 1, QTableWidgetItem(str(site_name)))
        self.eventTable.setItem(row_count, 2, QTableWidgetItem(str(price)))
        self.eventTable.setItem(row_count, 3, QTableWidgetItem(str(tickets_r)))
        self.eventTable.setItem(row_count, 4, QTableWidgetItem(str(total_v)))
        self.eventTable.setItem(row_count, 5, QTableWidgetItem(str(my_v)))
        self.eventTable.setItem(row_count, 6, QTableWidgetItem(str(start_date)))

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

    def msgDialog(self, m):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Sorry!")
        msg.setInformativeText("This action is not allowed.")
        msg.setWindowTitle("Not allowed")
        msg.setDetailedText(m)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

def render():
    __main__.selected_event33 = None
    visitor_explore_event = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(visitor_explore_event)
    visitor_explore_event.show()
    app.exec_()

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
