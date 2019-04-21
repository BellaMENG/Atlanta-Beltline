# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '25manager_manage_event.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTableWidget, QPushButton, QApplication, QVBoxLayout, \
    QTableWidgetItem, QCheckBox, QAbstractItemView, QHeaderView, QLabel, QFrame
from PyQt5.QtWidgets import QMessageBox
import datetime
import sys

app = QtWidgets.QApplication(sys.argv)
import __main__
__main__.selected_event25 = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 681, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.manageEvent = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.manageEvent.setFont(font)
        self.manageEvent.setAlignment(QtCore.Qt.AlignCenter)
        self.manageEvent.setObjectName("manageEvent")
        self.gridLayout.addWidget(self.manageEvent, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 50, 261, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 0, 1, 1)
        self.startDate = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.startDate.setObjectName("startDate")
        self.gridLayout_2.addWidget(self.startDate, 1, 0, 1, 1)
        self.nameLine = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.nameLine.setObjectName("nameLine")
        self.gridLayout_2.addWidget(self.nameLine, 0, 1, 1, 1)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout_2.addWidget(self.sdateEdit, 1, 1, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(330, 50, 311, 161))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.descriptionKeywordEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.descriptionKeywordEdit.setObjectName("descriptionKeywordEdit")
        self.gridLayout_5.addWidget(self.descriptionKeywordEdit, 0, 1, 1, 1)
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_5)
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout_5.addWidget(self.edateEdit, 1, 1, 1, 1)
        self.descriptionKeyword = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.descriptionKeyword.setObjectName("descriptionKeyword")
        self.gridLayout_5.addWidget(self.descriptionKeyword, 0, 0, 1, 1)
        self.endDate = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.endDate.setObjectName("endDate")
        self.gridLayout_5.addWidget(self.endDate, 1, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(30, 220, 611, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 7, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)
        self.drEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.drEnd.setObjectName("drEnd")
        self.gridLayout_3.addWidget(self.drEnd, 0, 3, 1, 1)
        self.tvrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.tvrEnd.setObjectName("tvrEnd")
        self.gridLayout_3.addWidget(self.tvrEnd, 0, 8, 1, 1)
        self.tvrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.tvrStart.setObjectName("tvrStart")
        self.gridLayout_3.addWidget(self.tvrStart, 0, 6, 1, 1)
        self.durationRange = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.durationRange.setObjectName("durationRange")
        self.gridLayout_3.addWidget(self.durationRange, 0, 0, 1, 1)
        self.totalVisitsRange = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.totalVisitsRange.setObjectName("totalVisitsRange")
        self.gridLayout_3.addWidget(self.totalVisitsRange, 0, 5, 1, 1)
        self.drStart = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.drStart.setObjectName("drStart")
        self.gridLayout_3.addWidget(self.drStart, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 4, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(140, 280, 351, 51))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.totalRevenueRange = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.totalRevenueRange.setObjectName("totalRevenueRange")
        self.gridLayout_4.addWidget(self.totalRevenueRange, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 2, 1, 1)
        self.trrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.trrStart.setObjectName("trrStart")
        self.gridLayout_4.addWidget(self.trrStart, 0, 1, 1, 1)
        self.trrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.trrEnd.setObjectName("trrEnd")
        self.gridLayout_4.addWidget(self.trrEnd, 0, 3, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(40, 340, 591, 41))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 1, 1, 1)
        self.createButton = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.createButton.setObjectName("createButton")
        self.gridLayout_6.addWidget(self.createButton, 0, 2, 1, 1)
        self.viewOrEditButton = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.viewOrEditButton.setObjectName("viewOrEditButton")
        self.gridLayout_6.addWidget(self.viewOrEditButton, 0, 3, 1, 1)
        self.filterButton = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.filterButton.setObjectName("filterButton")
        self.gridLayout_6.addWidget(self.filterButton, 0, 0, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout_6.addWidget(self.deleteButton, 0, 4, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(280, 510, 113, 32))
        self.backButton.setObjectName("backButton")
        self.filterResultTable = QtWidgets.QTableWidget(self.centralwidget)
        self.filterResultTable.setGeometry(QtCore.QRect(40, 390, 591, 111))
        self.filterResultTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.filterResultTable.setAutoScrollMargin(18)
        self.filterResultTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.filterResultTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.filterResultTable.setObjectName("filterResultTable")
        self.filterResultTable.setColumnCount(7)
        self.filterResultTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.filterResultTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.filterResultTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.filterResultTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.filterResultTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.filterResultTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.filterResultTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.filterResultTable.setHorizontalHeaderItem(6, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Event"))
        self.manageEvent.setText(_translate("MainWindow", "Manage Event"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.startDate.setText(_translate("MainWindow", "Start Date"))
        self.descriptionKeyword.setText(_translate("MainWindow", "Description Keyword"))
        self.endDate.setText(_translate("MainWindow", "End Date"))
        self.label_9.setText(_translate("MainWindow", "--"))
        self.label_7.setText(_translate("MainWindow", "--"))
        self.durationRange.setText(_translate("MainWindow", "Duration Range"))
        self.totalVisitsRange.setText(_translate("MainWindow", "Total Visits Range"))
        self.totalRevenueRange.setText(_translate("MainWindow", "Total Revenue Range"))
        self.label_11.setText(_translate("MainWindow", "--"))
        self.createButton.setText(_translate("MainWindow", "Create"))
        self.viewOrEditButton.setText(_translate("MainWindow", "View/Edit"))
        self.filterButton.setText(_translate("MainWindow", "Filter"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.filterResultTable.setSortingEnabled(True)
        item = self.filterResultTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.filterResultTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Staff Count"))
        item = self.filterResultTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Duration (days)"))
        item = self.filterResultTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Visits"))
        item = self.filterResultTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total Revenue ($)"))
        item = self.filterResultTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Start Date"))
        item = self.filterResultTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Site Name"))

        self.filterResultTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.filterResultTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.filterResultTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.filterResultTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.filterResultTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.filterResultTable.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.filterResultTable.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)

        self.user_name = __main__.logged_user
        query = "select Name from site where Manager = \'" + self.user_name + "\';"
        self.result = self.retrieve_from_db(query)
        self.site_name = self.result[0][0]

        self.filterButton.clicked.connect(self.filter)
        self.createButton.clicked.connect(lambda: self.func(idx=27))
        self.viewOrEditButton.clicked.connect(self.viewOrEdit)
        if __main__.user_type == 'Manager':
            self.backButton.clicked.connect(lambda: self.func(idx=10))
        elif __main__.user_type == "Manager_Visitor":
            self.backButton.clicked.connect(lambda: self.func(idx=11))
        else:
            self.backButton.clicked.connect(lambda: self.func(idx=10))
        self.filterResultTable.clicked.connect(self.selected_row)
        self.deleteButton.clicked.connect(self.delete)

        self.eventSDate = list()
        self.eventSiteName = list()

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

    def filter(self):

        self.filterResultTable.setRowCount(0)  # clean the table first
        event_name = self.nameLine.text()
        keyword = self.descriptionKeywordEdit.text()
        sdate = self.sdateEdit.date().toString(Qt.ISODate)
        edate = self.edateEdit.date().toString(Qt.ISODate)

        query1 = "select Name, StartDate, SiteName, datediff(EndDate, StartDate) + 1, Price " \
                 "from event where Name like \'%" + event_name + "%\' " \
                 "and Description like \'%" + keyword + "%\' " \
                 "and StartDate >= \'" + sdate + "\' " \
                 "and EndDate <= \'" + edate + "\' and SiteName = \'" + self.site_name + "\';"

        result = self.retrieve_from_db(query1)
        for row in result:
            name, start_date, site_name, duration, price = row
            query = "select count(UserName) from assign_to join event " \
                    "on assign_to.EventName = event.Name and assign_to.StartDate = event.StartDate " \
                    "and assign_to.SiteName = event.SiteName " \
                    "where event.Name = \'" + name + "\' " \
                    "and event.StartDate = \'" + str(start_date) + "\' " \
                    "and event.SiteName = \'" + site_name + "\' " \
                    "group by event.Name, event.StartDate, event.SiteName;"
            result = self.retrieve_from_db(query)
            if len(result) == 0:
                staff_count = 0
            else:
                staff_count = result[0][0]
            query = "select count(*) from visit_event " \
                    "where Name = \'" + name + "\' " \
                    "and StartDate = \'" + str(start_date) + "\' " \
                    "and SiteName = \'" + site_name + "\';"
            result = self.retrieve_from_db(query)
            total_visits = result[0][0]
            total_rev = int(total_visits) * float(price)
            single_row = [name, staff_count, duration, total_visits, total_rev, start_date, site_name]
            self.add_line(single_row)

    def selected_row(self):
        rowPos = self.filterResultTable.currentRow()
        # event.Name, event.StartDate, event.SiteName
        __main__.selected_event25 = [self.filterResultTable.item(rowPos, 0).text(),
                                     self.filterResultTable.item(rowPos, 5).text(),
                                     self.filterResultTable.item(rowPos, 6).text()]
        print("selected_event:", __main__.selected_event25)

    def add_line(self, row):
        min_duration = self.checkIntMin(self.drStart.text())
        max_duration = self.checkIntMax(self.drEnd.text())
        min_tvr = self.checkIntMin(self.tvrStart.text())
        max_tvr = self.checkIntMax(self.tvrEnd.text())
        min_trr = self.checkFloatMin(self.trrStart.text())
        max_trr = self.checkFloatMax(self.trrEnd.text())

        name, staff_count, duration, total_visits, tr, start_date, site_name = row
        if (not min_duration <= duration <= max_duration) \
                or (not min_tvr <= total_visits <= max_tvr) \
                or (not min_trr <= tr <= max_trr):
            return

        tr = float(tr)
        row_count = self.filterResultTable.rowCount()
        self.filterResultTable.setRowCount(row_count + 1)
        self.filterResultTable.setItem(row_count, 0, QTableWidgetItem(name))
        self.filterResultTable.setItem(row_count, 1, QTableWidgetItem(str(staff_count)))
        self.filterResultTable.setItem(row_count, 2, QTableWidgetItem(str(duration)))
        self.filterResultTable.setItem(row_count, 3, QTableWidgetItem(str(total_visits)))
        self.filterResultTable.setItem(row_count, 4, QTableWidgetItem(str(tr)))
        self.filterResultTable.setItem(row_count, 5, QTableWidgetItem(start_date.strftime('%Y-%m-%d')))
        self.filterResultTable.setItem(row_count, 6, QTableWidgetItem(str(site_name)))

    def create(self):
        self.func(27)
        app.exit()

    def delete(self):
        if __main__.selected_event25 is None:
            self.msgDialog("Nothing selected!")
            return
        # TODO: add dialogue: Sure to delete?
        # TODO: remember to commit to db
        name, start_date, site_name = __main__.selected_event25
        query = "DELETE FROM event " \
                "where Name = \'" + name + "\' " \
                "and StartDate = \'" + start_date + "\' and SiteName = \'" + site_name + "\';"
        print(query)
        self.update_db(query)
        self.filter()

    def viewOrEdit(self):
        if __main__.selected_event25 is None:
            self.msgDialog("Nothing selected!")
            return
        self.func(26)

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
    __main__.selected_event25 = None
    manager_manage_event = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(manager_manage_event)
    manager_manage_event.show()
    app.exec_()
    manager_manage_event.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
