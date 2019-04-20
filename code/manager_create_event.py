# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '27manager_create_event.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem
from PyQt5.QtCore import Qt


app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 661, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        self.msr = QtWidgets.QLabel(self.gridLayoutWidget)
        self.msr.setObjectName("msr")
        self.gridLayout.addWidget(self.msr, 2, 8, 1, 1)
        self.createEvent = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.createEvent.setFont(font)
        self.createEvent.setAlignment(QtCore.Qt.AlignCenter)
        self.createEvent.setObjectName("createEvent")
        self.gridLayout.addWidget(self.createEvent, 0, 0, 1, 10)
        self.capacity = QtWidgets.QLabel(self.gridLayoutWidget)
        self.capacity.setObjectName("capacity")
        self.gridLayout.addWidget(self.capacity, 2, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 7, 1, 1)
        self.price = QtWidgets.QLabel(self.gridLayoutWidget)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 2, 0, 1, 1)
        self.capacityEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.capacityEdit.setObjectName("capacityEdit")
        self.gridLayout.addWidget(self.capacityEdit, 2, 6, 1, 1)
        self.name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 1, 1, 1, 9)
        self.priceEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.priceEdit.setObjectName("priceEdit")
        self.gridLayout.addWidget(self.priceEdit, 2, 3, 1, 1)
        self.msrEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.msrEdit.setObjectName("msrEdit")
        self.gridLayout.addWidget(self.msrEdit, 2, 9, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 119, 661, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.eDate = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.eDate.setObjectName("eDate")
        self.gridLayout_2.addWidget(self.eDate, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout_2.addWidget(self.sdateEdit, 0, 1, 1, 1)
        self.sDate = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.sDate.setObjectName("sDate")
        self.gridLayout_2.addWidget(self.sDate, 0, 0, 1, 1)
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.edateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout_2.addWidget(self.edateEdit, 0, 4, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 180, 651, 281))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.assignStaff = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.assignStaff.setObjectName("assignStaff")
        self.gridLayout_3.addWidget(self.assignStaff, 1, 0, 1, 1)
        self.description = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.description.setObjectName("description")
        self.gridLayout_3.addWidget(self.description, 0, 0, 1, 1)
        self.descriptionContent = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
        self.descriptionContent.setObjectName("descriptionContent")
        self.gridLayout_3.addWidget(self.descriptionContent, 0, 1, 1, 1)
        self.staffList = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.staffList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.staffList.setObjectName("staffList")
        self.gridLayout_3.addWidget(self.staffList, 1, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 470, 651, 61))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.createbtn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.createbtn.setObjectName("create")
        self.gridLayout_4.addWidget(self.createbtn, 0, 2, 1, 1)
        self.back = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.back.setObjectName("back")
        self.gridLayout_4.addWidget(self.back, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 1, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Create Event"))
        self.msr.setText(_translate("MainWindow", "Minimum Staff Required"))
        self.createEvent.setText(_translate("MainWindow", "Create Event"))
        self.capacity.setText(_translate("MainWindow", "Capacity"))
        self.price.setText(_translate("MainWindow", "Price"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.label_5.setText(_translate("MainWindow", "$"))
        self.eDate.setText(_translate("MainWindow", "End Date"))
        self.sDate.setText(_translate("MainWindow", "Start Date"))
        self.assignStaff.setText(_translate("MainWindow", "Assign Staff"))
        self.description.setText(_translate("MainWindow", "Description"))
        self.createbtn.setText(_translate("MainWindow", "Create"))
        self.back.setText(_translate("MainWindow", "Back"))

        self.staffRetrieved = list()
        self.showStaff()

        self.staffList.clicked.connect(self.selected_row)
        self.back.clicked.connect(lambda: self.func(idx=25))
        self.createbtn.clicked.connect(self.create)
        self.sdateEdit.dateChanged.connect(self.showStaff)
        self.edateEdit.dateChanged.connect(self.showStaff)

        self.newName = None
        self.newPrice = None
        self.newCap = None
        self.newMsr = None
        self.newSDate = None
        self.newEDate = None
        self.newDes = None
        self.newStaff = list()

    def showStaff(self):

        self.staffRetrieved.clear()
        staff = self.retrieveStaff()

        print(staff)
        if len(staff) != 0:
            for item in staff:
                self.staffList.addItem(QListWidgetItem(item))


    def retrieveStaff(self):
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ", db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()

        query1 = "select distinct concat(user.Firstname, \' \', user.Lastname) " \
                 "from user join staff on user.Username = staff.Username " \
                 "where staff.Username not in (select distinct Username from assign_to);"

        print("query1: ", query1)

        cursor.execute(query1)
        result1 = cursor.fetchall()

        print("result1: ", result1)

        query2 = "select distinct concat(user.Firstname,\' \',user.Lastname), " \
                 "assign_to.EventName, assign_to.StartDate, event.EndDate, assign_to.SiteName " \
                 "from user join assign_to join event " \
                 "on user.Username = assign_to.Username and assign_to.EventName = event.Name " \
                 "and assign_to.StartDate = event.StartDate and assign_to.SiteName = event.SiteName;"

        # result2[0] contains: staff name, event name, event sdate, event edate, event site name

        print("query2: ", query2)

        cursor.execute(query2)
        result2 = cursor.fetchall()

        print("result2: ", result2)

        staffname = []

        for item in result1:
            staffname.append(item[0])

        for item2 in result2:
            stime = self.convert_datetime_to_qdate(item2[2])
            etime = self.convert_datetime_to_qdate(item2[3])
            if stime > self.edateEdit.date() or etime < self.sdateEdit.date():
                staffname.append(item2[0])

        staffname = set(staffname)
        staffname = list(staffname)

        print("staffname:", staffname)

        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

        return staffname

    def convert_datetime_to_qdate(self, datetime_val):
        datetime_val = datetime_val.strftime('%Y%m%d')
        datetime_val = str(datetime_val)
        qdate_val = QtCore.QDate(int(datetime_val[:4]), int(datetime_val[4:6]), int(datetime_val[6:8]))
        return qdate_val

    def msgDialog(self, m):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Sorry!")
        msg.setInformativeText("This action is not allowed.")
        msg.setWindowTitle("Not allowed")
        msg.setDetailedText(m)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def create(self):
        # TODO: get all the info on the screen right now and create sql
        # site is the site linked to the manager
        # what if the manager does not have a site? --retrieve from site table

        if self.nameEdit.text() == "" or self.priceEdit.text() == "" or self.capacityEdit.text() == "" \
                or self.msrEdit.text() == "" or self.descriptionContent.toPlainText() == "":
            self.msgDialog("All fields are required!")
            return

        self.newName = self.nameEdit.text()
        if float(self.priceEdit.text()) < 0:
            self.newPrice = 0.0
        else:
            self.newPrice = float(self.priceEdit.text())

        self.newCap = self.capacityEdit.text()

        if not self.is_number(self.newCap):
            self.msgDialog("Capacity needs to be a number!")
            return

        self.newCap = float(self.newCap)

        if not self.newCap.is_integer():
            self.msgDialog("Capacity needs to be an integer!")
            return

        self.newCap = int(self.newCap)

        if self.newCap < 0:
            self.msgDialog("Capacity needs to be positive!")
            return

        self.newMsr = int(self.msrEdit.text())
        self.newSDate = self.sdateEdit.date().toString(Qt.ISODate)
        self.newEDate = self.edateEdit.date().toString(Qt.ISODate)

        if self.sdateEdit.date() > self.edateEdit.date():
            self.msgDialog("Start date cannot be later than end date!")
            return

        self.newDes = self.descriptionContent.toPlainText()

        if self.newStaff is None:
            self.msgDialog("Need to assign staff!")
            return

        if (len(self.newStaff) < self.newMsr):
            self.msgDialog("Number of staff assigned to this event cannot be fewer than the minimum requirement!")
            return

        # TODO: create!!! commit() to database

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def selected_row(self):
        selected_item = self.staffList.selectedItems()
        self.newStaff.clear()
        for item in selected_item:
            self.newStaff.append(str(item.text()))

        print("new staff:", self.newStaff)


    def func(self, idx):
        __main__.screen_number = idx
        app.exit()

def render():
    manager_create_event = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(manager_create_event)
    manager_create_event.show()
    app.exec_()


if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
