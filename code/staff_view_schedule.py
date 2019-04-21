# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '31staff_view_schedule.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt
app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 671, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.sdate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sdate.setObjectName("sdate")
        self.gridLayout.addWidget(self.sdate, 2, 0, 1, 1)
        self.eventName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.eventName.setObjectName("eventName")
        self.gridLayout.addWidget(self.eventName, 1, 0, 1, 1)
        self.edate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.edate.setObjectName("edate")
        self.gridLayout.addWidget(self.edate, 2, 2, 1, 1)
        self.descriptionKeyword = QtWidgets.QLabel(self.gridLayoutWidget)
        self.descriptionKeyword.setObjectName("descriptionKeyword")
        self.gridLayout.addWidget(self.descriptionKeyword, 1, 2, 1, 1)
        self.event_name_content = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.event_name_content.setObjectName("event_name_content")
        self.gridLayout.addWidget(self.event_name_content, 1, 1, 1, 1)
        self.des_content = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.des_content.setObjectName("des_content")
        self.gridLayout.addWidget(self.des_content, 1, 3, 1, 1)
        self.viewSchedule = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.viewSchedule.setFont(font)
        self.viewSchedule.setAlignment(QtCore.Qt.AlignCenter)
        self.viewSchedule.setObjectName("viewSchedule")
        self.gridLayout.addWidget(self.viewSchedule, 0, 0, 1, 4)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout.addWidget(self.sdateEdit, 2, 1, 1, 1)
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.edateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout.addWidget(self.edateEdit, 2, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 671, 181))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.filterbtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.filterbtn.setObjectName("filterbtn")
        self.gridLayout_2.addWidget(self.filterbtn, 0, 0, 1, 1)
        self.viewEvent = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.viewEvent.setObjectName("viewEvent")
        self.gridLayout_2.addWidget(self.viewEvent, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.scheduleTable = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.scheduleTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scheduleTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.scheduleTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.scheduleTable.setObjectName("scheduleTable")
        self.scheduleTable.setColumnCount(5)
        self.scheduleTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(4, item)
        self.gridLayout_2.addWidget(self.scheduleTable, 1, 0, 1, 3)
        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(290, 330, 113, 32))
        self.backbtn.setObjectName("backbtn")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "View Schedule"))
        self.sdate.setText(_translate("MainWindow", "Start Date"))
        self.eventName.setText(_translate("MainWindow", "Event Name"))
        self.edate.setText(_translate("MainWindow", "End Date"))
        self.descriptionKeyword.setText(_translate("MainWindow", "Description Keyword"))
        self.viewSchedule.setText(_translate("MainWindow", "View Schedule"))
        self.filterbtn.setText(_translate("MainWindow", "Filter"))
        self.viewEvent.setText(_translate("MainWindow", "View Event"))
        self.scheduleTable.setSortingEnabled(True)
        item = self.scheduleTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Event Name"))
        item = self.scheduleTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Site Name"))
        item = self.scheduleTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Start Date"))
        item = self.scheduleTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "End Date"))
        item = self.scheduleTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Staff Count"))
        self.backbtn.setText(_translate("MainWindow", "Back"))

        if __main__.user_type == 'Staff':
            self.backbtn.clicked.connect(lambda: self.func(idx=12))
        elif __main__.user_type == 'Staff_Visitor':
            self.backbtn.clicked.connect(lambda: self.func(idx=13))
        else:
            self.backbtn.clicked.connect(lambda: self.func(idx=12))

        self.filterbtn.clicked.connect(self.filter)
        self.viewEvent.clicked.connect(self.view_event)
        self.scheduleTable.clicked.connect(self.selected_row)

    def view_event(self):
        if __main__.selected_event31 is None:
            self.msgDialog("An event must be selected before viewing its detail!")
            return
        else:
            self.func(idx=32)

    def selected_row(self):
        rowPos = self.scheduleTable.currentRow()
        __main__.selected_event31 = [self.scheduleTable.item(rowPos, 0).text(),
                                     self.scheduleTable.item(rowPos, 2).text(),
                                     self.scheduleTable.item(rowPos, 1).text()]
        print(__main__.selected_event31)
    def filter(self):
        self.scheduleTable.setRowCount(0)  # clean the table first
        staff_username = __main__.logged_user
        if staff_username is None:
            staff_username = 'staff1'
        event_name = self.event_name_content.text()
        des_keyword = self.des_content.text()
        sdate = self.sdateEdit.date().toString(Qt.ISODate)
        edate = self.edateEdit.date().toString(Qt.ISODate)

        query = "select event.Name, event.SiteName, event.StartDate, " \
                "event.EndDate from assign_to join event " \
                "on assign_to.EventName = event.Name " \
                "and assign_to.StartDate = event.StartDate " \
                "and assign_to.SiteName = event.SiteName " \
                "where assign_to.Username = \'" + staff_username + "\' and " \
                "event.Name like \'%" + event_name + "%\' " \
                "and event.Description like '%" + des_keyword+ "%' " \
                "and (event.Name, event.StartDate, event.SiteName) " \
                "not in (select Name, StartDate, SiteName " \
                "from event where StartDate > \'" + edate + "\' " \
                "or EndDate < \'" + sdate + "\');"
        print(query)
        result = self.retrieve_from_db(query)
        for row in result:
            ename, sname, d1, d2, = row
            query = "select count(*) from assign_to " \
                    "where EventName = \'" + ename + "\' " \
                    "and StartDate = \'" + str(d1) + "\' " \
                    "and SiteName = \'" + sname + "\';"
            print(query)
            result = self.retrieve_from_db(query)
            s_count = result[0][0]
            single_line = [ename, sname, d1, d2, s_count]
            self.add_lines(single_line)


    def add_lines(self, row):
        event_name, site_name, sdate, edate, staff_count = row
        row_count = self.scheduleTable.rowCount()
        self.scheduleTable.setRowCount(row_count + 1)
        self.scheduleTable.setItem(row_count, 0, QTableWidgetItem(str(event_name)))
        self.scheduleTable.setItem(row_count, 1, QTableWidgetItem(str(site_name)))
        self.scheduleTable.setItem(row_count, 2, QTableWidgetItem(str(sdate)))
        self.scheduleTable.setItem(row_count, 3, QTableWidgetItem(str(edate)))
        self.scheduleTable.setItem(row_count, 4, QTableWidgetItem(str(staff_count)))

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
    staff_view_schedule = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(staff_view_schedule)
    staff_view_schedule.show()
    app.exec_()
    staff_view_schedule.close()

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
