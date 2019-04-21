# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '29manager_site_report.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
__main__.selected_date29 = None
__main__.site_name29 = None
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from datetime import date, timedelta, datetime
app = QtWidgets.QApplication(sys.argv)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 671, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.sdate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sdate.setObjectName("sdate")
        self.gridLayout.addWidget(self.sdate, 1, 0, 1, 1)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout.addWidget(self.sdateEdit, 1, 1, 1, 1)
        self.siteReport = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.siteReport.setFont(font)
        self.siteReport.setAlignment(QtCore.Qt.AlignCenter)
        self.siteReport.setObjectName("siteReport")
        self.gridLayout.addWidget(self.siteReport, 0, 0, 1, 5)
        self.edate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.edate.setObjectName("edate")
        self.gridLayout.addWidget(self.edate, 1, 3, 1, 1)
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.edateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout.addWidget(self.edateEdit, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 671, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scr = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.scr.setObjectName("scr")
        self.gridLayout_2.addWidget(self.scr, 0, 4, 1, 1)
        self.scrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.scrStart.setObjectName("scrStart")
        self.gridLayout_2.addWidget(self.scrStart, 0, 5, 1, 1)
        self.trr = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.trr.setObjectName("trr")
        self.gridLayout_2.addWidget(self.trr, 1, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 6, 1, 1)
        self.tvrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.tvrEnd.setObjectName("tvrEnd")
        self.gridLayout_2.addWidget(self.tvrEnd, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        self.ecrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ecrEnd.setObjectName("ecrEnd")
        self.gridLayout_2.addWidget(self.ecrEnd, 0, 3, 1, 1)
        self.tvr = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.tvr.setObjectName("tvr")
        self.gridLayout_2.addWidget(self.tvr, 1, 0, 1, 1)
        self.tvrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.tvrStart.setObjectName("tvrStart")
        self.gridLayout_2.addWidget(self.tvrStart, 1, 1, 1, 1)
        self.trrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.trrStart.setObjectName("trrStart")
        self.gridLayout_2.addWidget(self.trrStart, 1, 5, 1, 1)
        self.ecr = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ecr.setObjectName("ecr")
        self.gridLayout_2.addWidget(self.ecr, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)
        self.ecrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ecrStart.setObjectName("ecrStart")
        self.gridLayout_2.addWidget(self.ecrStart, 0, 1, 1, 1)
        self.scrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.scrEnd.setObjectName("scrEnd")
        self.gridLayout_2.addWidget(self.scrEnd, 0, 7, 1, 1)
        self.trrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.trrEnd.setObjectName("trrEnd")
        self.gridLayout_2.addWidget(self.trrEnd, 1, 7, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 170, 671, 161))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.filterbtn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.filterbtn.setObjectName("filterbtn")
        self.gridLayout_3.addWidget(self.filterbtn, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.dailyDetail = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.dailyDetail.setObjectName("dailyDetail")
        self.gridLayout_3.addWidget(self.dailyDetail, 0, 2, 1, 1)
        self.filterTable = QtWidgets.QTableWidget(self.gridLayoutWidget_3)
        self.filterTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.filterTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.filterTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.filterTable.setObjectName("filterTable")
        self.filterTable.setColumnCount(5)
        self.filterTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(4, item)
        self.gridLayout_3.addWidget(self.filterTable, 1, 0, 1, 3)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(290, 340, 113, 32))
        self.back.setObjectName("back")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Site Report"))
        self.sdate.setText(_translate("MainWindow", "Start Date"))
        self.siteReport.setText(_translate("MainWindow", "Site Report"))
        self.edate.setText(_translate("MainWindow", "End Date"))
        self.scr.setText(_translate("MainWindow", "Staff Count Range"))
        self.trr.setText(_translate("MainWindow", "Total Revenue Range"))
        self.label_10.setText(_translate("MainWindow", "--"))
        self.label_6.setText(_translate("MainWindow", "--"))
        self.tvr.setText(_translate("MainWindow", "Total Visits Range"))
        self.ecr.setText(_translate("MainWindow", "Event Count Range"))
        self.label_11.setText(_translate("MainWindow", "--"))
        self.label_7.setText(_translate("MainWindow", "--"))
        self.filterbtn.setText(_translate("MainWindow", "Filter"))
        self.dailyDetail.setText(_translate("MainWindow", "Daily Detail"))
        self.filterTable.setSortingEnabled(True)
        item = self.filterTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.filterTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Event Count"))
        item = self.filterTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Staff Count"))
        item = self.filterTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Visits"))
        item = self.filterTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total Revenue ($)"))
        self.back.setText(_translate("MainWindow", "Back"))


        if __main__.user_type == 'Manager':
            self.back.clicked.connect(lambda: self.func(idx=10))
        elif __main__.user_type == "Manager_Visitor":
            self.back.clicked.connect(lambda: self.func(idx=11))
        else:
            self.back.clicked.connect(lambda: self.func(idx=10))

        self.filterTable.clicked.connect(self.selected_rows)
        self.filterbtn.clicked.connect(self.filter)

        self.dailyDetail.clicked.connect(self.daily_detail)
        self.site_name = "Inman Park"
        self.dates_list = list()

    def daily_detail(self):
        if __main__.selected_date29 is None:
            self.msgDialog("You didn't select any date!")
            return
        self.func(idx=30)

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
        self.filterTable.setRowCount(0)  # clean the table first
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ", db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()

        user_name = __main__.logged_user
        if user_name is None:
            user_name = 'manager2'

        query1 = "select Name from site where Manager = \'" + user_name + "\';"
        print(query1)
        cursor.execute(query1)
        result = cursor.fetchall()

        if len(result) == 0:
            self.msgDialog("You don't have a linked site!")
            return

        self.site_name = result[0][0]
        __main__.site_name29 = self.site_name
        sdate = self.sdateEdit.date().toString(Qt.ISODate)
        edate = self.edateEdit.date().toString(Qt.ISODate)

        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ", db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor2 = connection_object.cursor()

        query2 = "select Name, StartDate, " \
                 "EndDate, Price " \
                 "from event " \
                 "where (Name, StartDate, SiteName) " \
                 "not in (select Name, StartDate, SiteName " \
                 "from event where StartDate > \'" \
                 + edate + "\' or EndDate < \'" \
                 + sdate + "\') and SiteName = \'" + self.site_name + "\';"

        print(query2)
        cursor2.execute(query2)
        result2 = cursor2.fetchall()

        if len(result2) == 0:
            if (connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")
            return

        names = [row[0] for row in result2]
        sdates = [row[1] for row in result2]
        edates = [row[2] for row in result2]
        prices = [row[3] for row in result2]

        datefirst = min(sdates)
        datelast = max(edates)
        datefirst = max(datefirst, datetime.strptime(sdate, '%Y-%m-%d').date())
        datelast = min(datelast, datetime.strptime(edate, '%Y-%m-%d').date())

        self.dates_list = self.get_dates(datefirst, datelast)

        for date in self.dates_list:
            curr_date = self.convert_datetime_to_str(date)
            event_count = self.query_for_event_count(curr_date)
            staff_count = self.query_for_staff_count(curr_date)
            tv = self.query_for_tv(curr_date)
            tr = self.query_for_tr(curr_date)
            single_row = [curr_date, event_count, staff_count, tv, tr]
            print(single_row)
            self.add_line(single_row)

        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def query_for_event_count(self, date):
        query = "select count(*) from event where SiteName = \'" \
                + self.site_name + "\' and StartDate <= \'" + date + "\' and EndDate >= \'" + date + "\';"
        result = self.retrieve_from_database(query)
        return result[0][0]

    def query_for_events(self, date):
        query = "select Name, StartDate, SiteName from event where StartDate <= \'" \
                + date + "\' and EndDate >= \'" + date + "\';"
        print(query)
        result = self.retrieve_from_database(query)
        return result

    def query_for_staff_count(self, date):
        events = self.query_for_events(date)
        staff_count = 0
        for event in events:
            name, sdate, site_name = event
            sdate = self.convert_datetime_to_str(sdate)
            query = "select count(Username) from assign_to " \
                    "where EventName = \'" + name + "\' and StartDate = \'" \
                    + sdate + "\' and SiteName = \'" + site_name + "\';"
            print(query)
            result = self.retrieve_from_database(query)
            staff_count += int(result[0][0])

        return staff_count

    def query_for_tv(self, date):
        # add up visit_site and visit_event
        tv = 0
        query1 = "select count(*) from visit_site where Name = \'" + self.site_name + "\' and VisitSiteDate = \'" \
                 + date + "\';"
        print(query1)
        site_visits = self.retrieve_from_database(query1)
        tv += site_visits[0][0]

        query2 = "select count(*) from visit_event where SiteName = \'" + self.site_name + "\' and EndDate = \'" \
                 + date + "\';"
        print(query2)
        event_visits = self.retrieve_from_database(query2)
        tv += event_visits[0][0]
        return tv

    def query_for_tr(self, date):
        query = "select count(*), event.Price, visit_event.Name, visit_event.StartDate, " \
                "visit_event.SiteName from visit_event join event " \
                "on visit_event.Name = event.Name and visit_event.StartDate = event.StartDate " \
                "and visit_event.SiteName = event.SiteName " \
                "where visit_event.SiteName = \'" + self.site_name + "\' " \
                "and visit_event.EndDate = \'" + date + "\' " \
                "group by visit_event.Name, visit_event.StartDate, visit_event.SiteName;"
        print(query)
        result = self.retrieve_from_database(query)
        tr = 0
        for row in result:
            tr += int(row[0]) * float(row[1])
        return tr

    def retrieve_from_database(self, query):
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

    def selected_rows(self):
        rowPos = self.filterTable.currentRow()
        __main__.selected_date29 = self.filterTable.item(rowPos, 0).text()
        print("selected_date:", __main__.selected_date29, "type:", type(__main__.selected_date29))

    def get_dates(self, d1, d2):
        dates_list = list()
        delta = d2 - d1
        for i in range(delta.days + 1):
            print(d1 + timedelta(i))
            dates_list.append(d1 + timedelta(i))
        return dates_list

    def convert_datetime_to_str(self, datetime_val):
        return datetime_val.strftime('%Y-%m-%d')

    def convert_datetime_to_qdate(self, datetime_val):
        datetime_val = datetime_val.strftime('%Y%m%d')
        datetime_val = str(datetime_val)
        qdate_val = QtCore.QDate(int(datetime_val[:4]), int(datetime_val[4:6]), int(datetime_val[6:8]))
        return qdate_val

    def add_line(self, row):
        date, event_count, staff_count, total_visits, total_rev = row
        ecr1 = self.checkIntMin(self.ecrStart.text())
        ecr2 = self.checkIntMax(self.ecrEnd.text())
        scr1 = self.checkIntMin(self.scrStart.text())
        scr2 = self.checkIntMax(self.scrEnd.text())
        tvr1 = self.checkIntMin(self.tvrStart.text())
        tvr2 = self.checkIntMax(self.tvrEnd.text())
        trr1 = self.checkFloatMin(self.trrStart.text())
        trr2 = self.checkFloatMax(self.trrEnd.text())
        if (not ecr1 <= event_count <= ecr2) or (not scr1 <= staff_count <= scr2) \
                or (not tvr1 <= total_visits <= tvr2) or (not trr1 <= total_rev <= trr2):
            print("filter not fulfiled")
            return
        print("adding")

        print("ecr2", ecr2)
        print("event_count", event_count)
        row_count = self.filterTable.rowCount()
        self.filterTable.setRowCount(row_count + 1)
        self.filterTable.setItem(row_count, 0, QTableWidgetItem(str(date)))
        self.filterTable.setItem(row_count, 1, QTableWidgetItem(str(event_count)))
        self.filterTable.setItem(row_count, 2, QTableWidgetItem(str(staff_count)))
        self.filterTable.setItem(row_count, 3, QTableWidgetItem(str(total_visits)))
        self.filterTable.setItem(row_count, 4, QTableWidgetItem(str(total_rev)))

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
    __main__.selected_date29 = None
    __main__.site_name29 = None
    manager_site_report = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(manager_site_report)
    manager_site_report.show()
    app.exec_()

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

