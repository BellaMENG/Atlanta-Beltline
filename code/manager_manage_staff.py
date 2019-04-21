# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '28manager_manage_staff.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 671, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.fname = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fname.setObjectName("fname")
        self.gridLayout.addWidget(self.fname, 2, 0, 1, 1)
        self.manageStaff = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.manageStaff.setFont(font)
        self.manageStaff.setAlignment(QtCore.Qt.AlignCenter)
        self.manageStaff.setObjectName("manageStaff")
        self.gridLayout.addWidget(self.manageStaff, 0, 0, 1, 5)
        self.lname = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lname.setObjectName("lname")
        self.gridLayout.addWidget(self.lname, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.sDate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sDate.setObjectName("sDate")
        self.gridLayout.addWidget(self.sDate, 3, 0, 1, 1)
        self.eDate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.eDate.setObjectName("eDate")
        self.gridLayout.addWidget(self.eDate, 3, 3, 1, 1)
        self.fnameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.fnameEdit.setObjectName("fnameEdit")
        self.gridLayout.addWidget(self.fnameEdit, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        self.lnameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lnameEdit.setObjectName("lnameEdit")
        self.gridLayout.addWidget(self.lnameEdit, 2, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        self.site = QtWidgets.QLabel(self.gridLayoutWidget)
        self.site.setObjectName("site")
        self.gridLayout.addWidget(self.site, 1, 1, 1, 1)
        self.siteBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.siteBox.setObjectName("siteBox")
        self.gridLayout.addWidget(self.siteBox, 1, 2, 1, 1)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout.addWidget(self.sdateEdit, 3, 1, 1, 1)
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.edateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout.addWidget(self.edateEdit, 3, 4, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(160, 160, 371, 211))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        self.filterBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.filterBtn.setObjectName("filterBtn")
        self.gridLayout_2.addWidget(self.filterBtn, 0, 1, 1, 1)
        self.backBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.backBtn.setObjectName("backBtn")
        self.gridLayout_2.addWidget(self.backBtn, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 2, 1, 1)
        self.staffTable = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.staffTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.staffTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.staffTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.staffTable.setObjectName("staffTable")
        self.staffTable.setColumnCount(2)
        self.staffTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.staffTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.staffTable.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.staffTable, 1, 0, 1, 3)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Staff"))
        self.fname.setText(_translate("MainWindow", "First Name"))
        self.manageStaff.setText(_translate("MainWindow", "Manage Staff"))
        self.lname.setText(_translate("MainWindow", "Last Name"))
        self.sDate.setText(_translate("MainWindow", "Start Date"))
        self.eDate.setText(_translate("MainWindow", "End Date"))
        self.site.setText(_translate("MainWindow", "Site"))
        self.filterBtn.setText(_translate("MainWindow", "Filter"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.staffTable.setSortingEnabled(True)
        item = self.staffTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.staffTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "# Event Shifts"))

        if __main__.user_type == 'Manager':
            self.backBtn.clicked.connect(lambda: self.func(idx=10))
        elif __main__.user_type == "Manager_Visitor":
            self.backBtn.clicked.connect(lambda: self.func(idx=11))
        else:
            self.backBtn.clicked.connect(lambda: self.func(idx=10))

        self.site_list = list()
        self.get_sites()
        self.siteBox.addItems(self.site_list)

        self.filterBtn.clicked.connect(self.filter)

    def get_sites(self):
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")

        query1 = "select distinct SiteName from assign_to"
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        for row in result:
            self.site_list.append(row[0])
        print(self.site_list)
        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")


    def filter(self):
        self.staffTable.setRowCount(0)  # clean the table first
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ", db_Info)
        else:
            print("user_login.py login() Not Connected ")

        current_site = self.siteBox.currentText()
        fname = self.fnameEdit.text()
        lname = self.lnameEdit.text()
        sdate = self.sdateEdit.date().toString(Qt.ISODate)
        edate = self.edateEdit.date().toString(Qt.ISODate)

        query1 = "select concat(user.Firstname,\' \',user.Lastname), count(EventName) " \
                 "from assign_to join event join user " \
                 "on assign_to.EventName = event.Name and assign_to.StartDate = event.StartDate " \
                 "and assign_to.SiteName = event.SiteName and assign_to.Username = user.Username " \
                 "where assign_to.Username in (select distinct Username " \
                 "from assign_to where SiteName = \'" \
                 + current_site \
                 + "\') and event.StartDate between \'" + sdate + "\' and \'" + edate + "\' " \
                   "and user.Firstname like \'%" + fname + "%\' " \
                   "and user.Lastname like \'%" + lname + "%\' group by assign_to.Username;"

        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        for row in result:
            self.add_line(row)

        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")


    def add_line(self, row):
        name, event_shifts = row
        row_count = self.staffTable.rowCount()
        self.staffTable.setRowCount(row_count + 1)
        self.staffTable.setItem(row_count, 0, QTableWidgetItem(str(name)))
        self.staffTable.setItem(row_count, 1, QTableWidgetItem(str(event_shifts)))

    def func(self, idx):
        __main__.screen_number = idx
        app.exit()

def render():
    manager_manage_staff = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(manager_manage_staff)
    manager_manage_staff.show()
    app.exec_()
    manager_manage_staff.close()

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
