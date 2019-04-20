# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '35visitor_explore_site.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 671, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name_list = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.name_list.setObjectName("name_list")
        self.gridLayout.addWidget(self.name_list, 1, 1, 1, 1)
        self.sdate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sdate.setObjectName("sdate")
        self.gridLayout.addWidget(self.sdate, 2, 0, 1, 1)
        self.openEveryday = QtWidgets.QLabel(self.gridLayoutWidget)
        self.openEveryday.setObjectName("openEveryday")
        self.gridLayout.addWidget(self.openEveryday, 1, 2, 1, 1)
        self.name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 0, 1, 1)
        self.openEveryday_list = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.openEveryday_list.setObjectName("openEveryday_list")
        self.openEveryday_list.addItem("")
        self.openEveryday_list.addItem("")
        self.openEveryday_list.addItem("")
        self.gridLayout.addWidget(self.openEveryday_list, 1, 3, 1, 1)
        self.edate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.edate.setObjectName("edate")
        self.gridLayout.addWidget(self.edate, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout.addWidget(self.sdateEdit, 2, 1, 1, 1)
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.edateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout.addWidget(self.edateEdit, 2, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 150, 671, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.evr = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.evr.setObjectName("evr")
        self.gridLayout_2.addWidget(self.evr, 0, 4, 1, 1)
        self.tvr = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.tvr.setObjectName("tvr")
        self.gridLayout_2.addWidget(self.tvr, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.evrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.evrStart.setObjectName("evrStart")
        self.gridLayout_2.addWidget(self.evrStart, 0, 5, 1, 1)
        self.tvrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.tvrStart.setObjectName("tvrStart")
        self.gridLayout_2.addWidget(self.tvrStart, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 6, 1, 1)
        self.tvrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.tvrEnd.setObjectName("tvrEnd")
        self.gridLayout_2.addWidget(self.tvrEnd, 0, 3, 1, 1)
        self.evrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.evrEnd.setObjectName("evrEnd")
        self.gridLayout_2.addWidget(self.evrEnd, 0, 7, 1, 1)
        self.includeVisited = QtWidgets.QCheckBox(self.centralwidget)
        self.includeVisited.setGeometry(QtCore.QRect(280, 190, 111, 20))
        self.includeVisited.setObjectName("includeVisited")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 220, 671, 271))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.siteDetail = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.siteDetail.setObjectName("siteDetail")
        self.gridLayout_3.addWidget(self.siteDetail, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.transitDetail = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.transitDetail.setObjectName("transitDetail")
        self.gridLayout_3.addWidget(self.transitDetail, 0, 3, 1, 1)
        self.filterbtn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.filterbtn.setObjectName("filterbtn")
        self.gridLayout_3.addWidget(self.filterbtn, 0, 0, 1, 1)
        self.siteTable = QtWidgets.QTableWidget(self.gridLayoutWidget_3)
        self.siteTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.siteTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.siteTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.siteTable.setObjectName("siteTable")
        self.siteTable.setColumnCount(4)
        self.siteTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.siteTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.siteTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.siteTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.siteTable.setHorizontalHeaderItem(3, item)
        self.gridLayout_3.addWidget(self.siteTable, 1, 0, 1, 4)
        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(290, 500, 113, 32))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Explore Site"))
        self.sdate.setText(_translate("MainWindow", "Start Date"))
        self.openEveryday.setText(_translate("MainWindow", "Open Everyday"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.openEveryday_list.setItemText(0, _translate("MainWindow", "--ALL--"))
        self.openEveryday_list.setItemText(1, _translate("MainWindow", "Yes"))
        self.openEveryday_list.setItemText(2, _translate("MainWindow", "No"))
        self.edate.setText(_translate("MainWindow", "End Date"))
        self.label.setText(_translate("MainWindow", "Explore Site"))
        self.evr.setText(_translate("MainWindow", "Event Count Range"))
        self.tvr.setText(_translate("MainWindow", "Total Visits Range"))
        self.label_7.setText(_translate("MainWindow", "--"))
        self.label_9.setText(_translate("MainWindow", "--"))
        self.includeVisited.setText(_translate("MainWindow", "Include Visited"))
        self.siteDetail.setText(_translate("MainWindow", "Site Detail"))
        self.transitDetail.setText(_translate("MainWindow", "Transit Detail"))
        self.filterbtn.setText(_translate("MainWindow", "Filter"))
        self.siteTable.setSortingEnabled(True)
        item = self.siteTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Site Name"))
        item = self.siteTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Event Count"))
        item = self.siteTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total Visits"))
        item = self.siteTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "My Visits"))
        self.backbtn.setText(_translate("MainWindow", "Back"))

        # TODO: remember to remove this!!!!
        if __main__.logged_user is None:
            __main__.logged_user = 'staff2'
        self.user_name = __main__.logged_user
        self.add_sites_to_list()

        self.siteTable.clicked.connect(self.selected_row)
        self.filterbtn.clicked.connect(self.filter)
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

        self.siteDetail.clicked.connect(lambda: self.view_detail(idx=37))
        self.transitDetail.clicked.connect(lambda: self.view_detail(idx=36))

    def view_detail(self, idx):
        if __main__.selected_site35 is None:
            self.msgDialog("You must select a site before further action!")
        else:
            self.func(idx)

    def msgDialog(self, m):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Sorry!")
        msg.setInformativeText("This action is not allowed.")
        msg.setWindowTitle("Not allowed")
        msg.setDetailedText(m)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

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

        self.name_list.addItems(site_list)
        return

    def filter(self):
        self.siteTable.setRowCount(0)  # clean the table first

        name = self.name_list.currentText()
        if name == '--ALL--':
            name = ''

        open_everyday = self.openEveryday_list.currentText()
        if open_everyday == '--ALL--':
            open_everyday = ''

        print("open everyday?", open_everyday)

        start_date = self.sdateEdit.date().toString(Qt.ISODate)
        end_date = self.edateEdit.date().toString(Qt.ISODate)

        query = "select Name from site where Name like \'%" + name + "%\' " \
                "and openEveryday like \'%" + open_everyday + "%\';"
        site_name_result = self.retrieve_from_db(query)
        site_list = list()

        for row in site_name_result:
            site_list.append(row[0])

        for site_name in site_list:
            query = "select count(*) from event join site " \
                    "where event.SiteName = site.Name " \
                    "and site.Name = \'" + site_name + "\' " \
                    "group by site.Name;"
            result = self.retrieve_from_db(query)
            event_count = int(result[0][0])
            # TODO: find each event and count total visits and my visits
            # TODO: self.add_line to table
            total_visit_sites_query = "select count(*) from visit_site " \
                                "where Name = \'" + site_name + "\' " \
                                "and VisitSiteDate between \'" + start_date + "\' " \
                                "and \'" + end_date + "\';"
            total_visit_sites_result = self.retrieve_from_db(total_visit_sites_query)
            total_visit_sites = int(total_visit_sites_result[0][0])

            total_visit_events_query = "select count(*) from visit_event " \
                                       "where SiteName = \'" + site_name + "\' " \
                                       "and EndDate between \'" + start_date + "\' " \
                                       "and \'" + end_date + "\';"
            total_visit_events_result = self.retrieve_from_db(total_visit_events_query)
            total_visit_events = int(total_visit_events_result[0][0])
            total_visits = total_visit_sites + total_visit_events

            my_site_visits_query = "select count(*) from visit_site " \
                                    "where Name = \'" + site_name + "\' " \
                                    "and VisitSiteDate between \'" + start_date + "\' " \
                                    "and \'" + end_date + "\' " \
                                    "and Username = \'" + self.user_name + "\';"
            my_site_visits_result = self.retrieve_from_db(my_site_visits_query)
            my_site_visits = int(my_site_visits_result[0][0])

            my_event_visits_query = "select count(*) from visit_event " \
                                    "where SiteName = \'" + site_name + "\' " \
                                    "and EndDate between \'" + start_date + "\' " \
                                    "and \'" + end_date + "\' " \
                                    "and Username = \'" + self.user_name + "\';"
            my_event_visits_result = self.retrieve_from_db(my_event_visits_query)
            my_event_visits = int(my_event_visits_result[0][0])
            my_visits = my_site_visits + my_event_visits

            single_row = [site_name, event_count, total_visits, my_visits]
            self.add_lines(single_row)

    def selected_row(self):
        rowPos = self.siteTable.currentRow()
        __main__.selected_site35 = self.siteTable.item(rowPos, 0).text()
        print(__main__.selected_site35)

    def add_lines(self, row):
        name, event_count, total_v, my_v = row
        include_visited_con = self.includeVisited.isChecked()

        tvr1 = self.checkIntMin(self.tvrStart.text())
        tvr2 = self.checkIntMax(self.tvrEnd.text())
        ecr1 = self.checkIntMin(self.evrStart.text())
        ecr2 = self.checkIntMax(self.evrEnd.text())

        if not include_visited_con:
            if my_v > 0:
                return

        if (not tvr1 <= total_v <= tvr2) or (not ecr1 <= event_count <= ecr2):
            return

        row_count = self.siteTable.rowCount()
        self.siteTable.setRowCount(row_count + 1)
        self.siteTable.setItem(row_count, 0, QTableWidgetItem(str(name)))
        self.siteTable.setItem(row_count, 1, QTableWidgetItem(str(event_count)))
        self.siteTable.setItem(row_count, 2, QTableWidgetItem(str(total_v)))
        self.siteTable.setItem(row_count, 3, QTableWidgetItem(str(my_v)))

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
    visitor_explore_site = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(visitor_explore_site)
    visitor_explore_site.show()
    app.exec_()


if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
