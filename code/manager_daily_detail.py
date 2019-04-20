# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '30manager_daily_detail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
from PyQt5.QtWidgets import QTableWidgetItem
app = QtWidgets.QApplication(sys.argv)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 671, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dailyDetail = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.dailyDetail.setFont(font)
        self.dailyDetail.setAlignment(QtCore.Qt.AlignCenter)
        self.dailyDetail.setObjectName("dailyDetail")
        self.gridLayout.addWidget(self.dailyDetail, 0, 0, 1, 1)
        self.dailyDetailTable = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.dailyDetailTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dailyDetailTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.dailyDetailTable.setObjectName("dailyDetailTable")
        self.dailyDetailTable.setColumnCount(4)
        self.dailyDetailTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dailyDetailTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dailyDetailTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dailyDetailTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dailyDetailTable.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.dailyDetailTable, 1, 0, 1, 1)
        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(290, 310, 113, 32))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Daily Detail"))
        self.dailyDetail.setText(_translate("MainWindow", "Daily Detail"))
        self.dailyDetailTable.setSortingEnabled(True)
        item = self.dailyDetailTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Event Name"))
        item = self.dailyDetailTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Staff Names"))
        item = self.dailyDetailTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Visits"))
        item = self.dailyDetailTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Revenue ($)"))
        self.backbtn.setText(_translate("MainWindow", "Back"))

        self.backbtn.clicked.connect(lambda: self.func(idx=29))
        self.retrieve()

    def retrieve(self):
        query = "select Name, StartDate, Price " \
                "from event where StartDate <= \'" + str(__main__.selected_date29) + "\' " \
                "and EndDate >= \'" + str(__main__.selected_date29) + "\' and SiteName = \'" \
                + str(__main__.site_name29) + "\';"
        print(query)
        result = self.retrieve_from_db(query)
        if len(result) == 0:
            return
        event_names = [row[0] for row in result]
        event_sdates = [row[1] for row in result]
        event_prices = [row[2] for row in result]

        staff_list = list()
        visit_num = list()
        price_list = list()
        for i in range(len(event_names)):
            query = "select concat(user.Firstname, ' ', user.Lastname) " \
                    "from assign_to join user on user.Username = assign_to.Username " \
                    "where EventName = \'" + event_names[i] + "\' " \
                    "and StartDate = \'" + str(event_sdates[i]) + "\' " \
                    "and SiteName = \'" + str(__main__.site_name29) + "\';"
            print(query)
            result = self.retrieve_from_db(query)
            staff_names = ''
            for row in result:
                staff_names += row[0]
                staff_names += '  '
            staff_list.append(staff_names)

            query = "select count(*) from visit_event " \
                    "where Name = \'" + event_names[i] + "\' " \
                    "and StartDate = \'" + str(event_sdates[i]) + "\' " \
                    "and SiteName = \'" + str(__main__.site_name29) + "\' " \
                    "and EndDate = \'" + __main__.selected_date29 + "\';"
            print(query)
            result = self.retrieve_from_db(query)
            visit_num.append(result[0][0])

        for i in range(len(event_names)):
            price_list.append(float(event_prices[i]) * int(visit_num[i]))

        for i in range(len(event_names)):
            row = [event_names[i], staff_names[i], visit_num[i], price_list[i]]
            self.add_lines(row)

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

    def add_lines(self, row):
        event_name, staff_name, visits, rev = row
        row_count = self.dailyDetailTable.rowCount()
        self.dailyDetailTable.setRowCount(row_count + 1)
        self.dailyDetailTable.setItem(row_count, 0, QTableWidgetItem(str(event_name)))
        self.dailyDetailTable.setItem(row_count, 1, QTableWidgetItem(str(staff_name)))
        self.dailyDetailTable.setItem(row_count, 2, QTableWidgetItem(str(visits)))
        self.dailyDetailTable.setItem(row_count, 3, QTableWidgetItem(str(rev)))

    def func(self, idx):
        __main__.screen_number = idx
        app.exit()

def render():
    manager_daily_detail = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(manager_daily_detail)
    manager_daily_detail.show()
    app.exec_()


if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
