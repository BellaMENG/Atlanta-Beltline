# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '26manager_view_or_edit_event.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTableWidget, QPushButton, QApplication, QVBoxLayout, \
    QTableWidgetItem, QCheckBox, QAbstractItemView, QHeaderView, QLabel, QFrame, QListWidgetItem, QMessageBox


app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 700)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, -1, 651, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.minimumStaffRequired = QtWidgets.QLabel(self.gridLayoutWidget)
        self.minimumStaffRequired.setObjectName("minimumStaffRequired")
        self.gridLayout.addWidget(self.minimumStaffRequired, 4, 0, 1, 1)
        self.price = QtWidgets.QLabel(self.gridLayoutWidget)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 2, 3, 1, 1)
        self.name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 2, 0, 1, 1)
        self.sdate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sdate.setObjectName("sdate")
        self.gridLayout.addWidget(self.sdate, 3, 0, 1, 1)
        self.capacityContent = QtWidgets.QLabel(self.gridLayoutWidget)
        self.capacityContent.setText("")
        self.capacityContent.setObjectName("capacityContent")
        self.gridLayout.addWidget(self.capacityContent, 4, 4, 1, 2)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.sdateEdit.setReadOnly(True)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout.addWidget(self.sdateEdit, 3, 1, 1, 2)
        self.edate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.edate.setObjectName("edate")
        self.gridLayout.addWidget(self.edate, 3, 3, 1, 1)
        self.msr = QtWidgets.QLabel(self.gridLayoutWidget)
        self.msr.setText("")
        self.msr.setObjectName("msr")
        self.gridLayout.addWidget(self.msr, 4, 1, 1, 2)
        self.nameContent = QtWidgets.QLabel(self.gridLayoutWidget)
        self.nameContent.setText("")
        self.nameContent.setObjectName("nameContent")
        self.gridLayout.addWidget(self.nameContent, 2, 1, 1, 2)
        self.priceContent = QtWidgets.QLabel(self.gridLayoutWidget)
        self.priceContent.setText("")
        self.priceContent.setObjectName("priceContent")
        self.gridLayout.addWidget(self.priceContent, 2, 4, 1, 2)
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.edateEdit.setReadOnly(True)
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout.addWidget(self.edateEdit, 3, 4, 1, 2)
        self.capacity = QtWidgets.QLabel(self.gridLayoutWidget)
        self.capacity.setObjectName("capacity")
        self.gridLayout.addWidget(self.capacity, 4, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 6)
        self.viewOrEditEvent = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.viewOrEditEvent.setFont(font)
        self.viewOrEditEvent.setAlignment(QtCore.Qt.AlignCenter)
        self.viewOrEditEvent.setObjectName("viewOrEditEvent")
        self.gridLayout.addWidget(self.viewOrEditEvent, 0, 0, 1, 6)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 651, 160))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.staffAssignedEdit = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.staffAssignedEdit.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.staffAssignedEdit.setObjectName("staffAssignedEdit")
        self.gridLayout_2.addWidget(self.staffAssignedEdit, 0, 1, 1, 1)
        self.staffAssigned = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.staffAssigned.setObjectName("staffAssigned")
        self.gridLayout_2.addWidget(self.staffAssigned, 0, 0, 1, 1)
        self.description = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.description.setObjectName("description")
        self.gridLayout_2.addWidget(self.description, 1, 0, 1, 1)
        self.descriptionEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.descriptionEdit.setPlainText("")
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout_2.addWidget(self.descriptionEdit, 1, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 410, 651, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.drrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.drrStart.setObjectName("drrStart")
        self.gridLayout_3.addWidget(self.drrStart, 0, 6, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 7, 1, 1)
        self.drr = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.drr.setObjectName("drr")
        self.gridLayout_3.addWidget(self.drr, 0, 5, 1, 1)
        self.drrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.drrEnd.setObjectName("drrEnd")
        self.gridLayout_3.addWidget(self.drrEnd, 0, 8, 1, 1)
        self.dvrEnd = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.dvrEnd.setObjectName("dvrEnd")
        self.gridLayout_3.addWidget(self.dvrEnd, 0, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 2, 1, 1)
        self.dvr = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.dvr.setObjectName("dvr")
        self.gridLayout_3.addWidget(self.dvr, 0, 0, 1, 1)
        self.dvrStart = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.dvrStart.setObjectName("dvrStart")
        self.gridLayout_3.addWidget(self.dvrStart, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 4, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 450, 651, 161))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.filterbtn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.filterbtn.setObjectName("filterbtn")
        self.gridLayout_4.addWidget(self.filterbtn, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 1, 1, 1)
        self.updatebtn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.updatebtn.setObjectName("update")
        self.gridLayout_4.addWidget(self.updatebtn, 0, 2, 1, 1)
        self.filterTable = QtWidgets.QTableWidget(self.gridLayoutWidget_4)
        self.filterTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.filterTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filterTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.filterTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.filterTable.setObjectName("filterTable")
        self.filterTable.setColumnCount(3)
        self.filterTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(2, item)
        self.gridLayout_4.addWidget(self.filterTable, 1, 0, 1, 3)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(280, 620, 113, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setObjectName("back")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "View/Edit Event"))
        self.minimumStaffRequired.setText(_translate("MainWindow", "Minimum Staff Required"))
        self.price.setText(_translate("MainWindow", "Price ($)"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.sdate.setText(_translate("MainWindow", "Start Date"))
        self.edate.setText(_translate("MainWindow", "End Date"))
        self.capacity.setText(_translate("MainWindow", "Capacity"))
        self.viewOrEditEvent.setText(_translate("MainWindow", "View/Edit Event"))
        self.staffAssigned.setText(_translate("MainWindow", "staff Assigned"))
        self.description.setText(_translate("MainWindow", "Description"))
        self.label_13.setText(_translate("MainWindow", "--"))
        self.drr.setText(_translate("MainWindow", "Daily Revenue Range"))
        self.label_11.setText(_translate("MainWindow", "--"))
        self.dvr.setText(_translate("MainWindow", "Daily Visits Range"))
        self.filterbtn.setText(_translate("MainWindow", "Filter"))
        self.updatebtn.setText(_translate("MainWindow", "Update"))
        self.filterTable.setSortingEnabled(True)
        item = self.filterTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.filterTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Daily Visits"))
        item = self.filterTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Daily Revenue ($)"))
        self.back.setText(_translate("MainWindow", "Back"))

        result = self.retrieveEvent()

        self.eventName = result[0][0]
        self.eventPrice = result[0][1]
        self.SDate = result[0][2]
        self.EDate = result[0][3]
        self.MSR = result[0][4]
        self.eventCapacity = result[0][5]
        self.eventDes = result[0][6]

        self.SDate = self.SDate.strftime('%Y%m%d')
        self.EDate = self.EDate.strftime('%Y%m%d')
        self.SDate = str(self.SDate)
        self.EDate = str(self.EDate)

        self.nameContent.setText(str(self.eventName))
        self.priceContent.setText(str(self.eventPrice))

        self.sdateEdit.setDate(QtCore.QDate(int(self.SDate[:4]), int(self.SDate[4:6]), int(self.SDate[6:8])))
        self.edateEdit.setDate(QtCore.QDate(int(self.EDate[:4]), int(self.EDate[4:6]), int(self.EDate[6:8])))

        self.msr.setText(str(self.MSR))
        self.capacityContent.setText(str(self.eventCapacity))
        self.descriptionEdit.setPlainText(str(self.eventDes))

        staff = self.retrieveStaff()
        self.staffRetrieved = list()
        for item in staff:
            self.staffRetrieved.append(item[0])
            self.staffAssignedEdit.addItem(QListWidgetItem(item[0]))

        self.newStaff = list()
        self.staffAssignedEdit.clicked.connect(self.selected_rows)

        self.filterbtn.clicked.connect(self.filter)
        self.updatebtn.clicked.connect(self.update)
        self.back.clicked.connect(lambda: self.func(idx=25))

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
            return 1000
        else:
            return int(maxVal)

    def checkFloatMax(self, maxVal):
        if not maxVal:
            return 1000
        else:
            return float(maxVal)

    def fillTable(self):
        eventName, eventSDate, eventSiteName = __main__.selected_event25
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ", db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()

        query1 = "select visit_event.EndDate as \'Date\', " \
                 "count(visit_event.EndDate) as \'Daily Visits\', " \
                 "count(visit_event.EndDate)*Event.Price as \'Daily Revenue\' " \
                 "from event join visit_event on event.Name = visit_event.Name " \
                 "and event.SiteName = visit_event.SiteName " \
                 "and event.StartDate = visit_event.StartDate " \
                 "where event.Name = \'" + eventName \
                 + "\' and event.StartDate = \'" + eventSDate \
                 + "\' and event.SiteName = \'" + eventSiteName \
                 + "\' "\
                 "group by event.Name, event.SiteName, event.StartDate, visit_event.EndDate "

        print("query: ", query1)

        cursor.execute(query1)
        result = cursor.fetchall()

        if result is None:
            return
        print("result: ", result)

        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

        return result

    def retrieveEvent(self):
        eventName, eventSDate, eventSiteName = __main__.selected_event25
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ", db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()

        query1 = "select event.Name, event.Price, event.StartDate, event.EndDate, event.MinStaffReq," \
                 "event.Capacity, event.Description " \
                 "from event " \
                 "where event.Name = \'" \
                 + eventName \
                 + "\' and event.StartDate = \'" \
                 + eventSDate \
                 + "\' and event.SiteName = \'" \
                 + eventSiteName + "\'"

        print("query: ", query1)

        cursor.execute(query1)
        result = cursor.fetchall()

        if result is None:
            return
        print("result: ", result)

        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

        return result

    def retrieveStaff(self):
        eventName, eventSDate, eventSiteName = __main__.selected_event25
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ", db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()

        query1 = "select concat(Firstname, \' \', Lastname) as \'Staff\'" \
                 "from user join assign_to " \
                 "on user.Username = assign_to.Username " \
                 "where assign_to.EventName = \'" + eventName \
                 + "\' and assign_to.StartDate = \'" + eventSDate \
                 + "\' and assign_to.SiteName = \'" + eventSiteName + "\'"

        print("query: ", query1)

        cursor.execute(query1)
        result = cursor.fetchall()

        if result is None:
            return
        print("result: ", result)

        if (connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

        return result

    def selected_rows(self):
        # store information in global var

        selected_item = self.staffAssignedEdit.selectedItems()
        self.newStaff.clear()
        for item in selected_item:
            self.newStaff.append(str(item.text()))

        print(self.newStaff)

    def update(self):
        if len(self.newStaff) < int(self.MSR):
            self.msgDialog("The number of staff assigned need "
                           "to be more than minimum staff requirement for this event.")
            return

        new_description = self.descriptionEdit.toPlainText()
        print(new_description)
        # TODO: commit the change to database


    def filter(self):
        self.filterTable.setRowCount(0)  # clean the table first
        min_dvr = self.dvrStart.text()
        max_dvr = self.dvrEnd.text()
        min_drr = self.drrStart.text()
        max_drr = self.drrEnd.text()

        min_dvr = self.checkIntMin(min_dvr)
        max_dvr = self.checkIntMax(max_dvr)
        min_drr = self.checkFloatMin(min_drr)
        max_drr = self.checkFloatMax(max_drr)

        log_result = self.fillTable()

        for row in log_result:
            if min_dvr < int(row[1]) < max_dvr and min_drr < float(row[2]) < max_drr:
                self.add_line(row)

    def add_line(self, row):
        # TODO: item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
        # TODO: make the cell uneditable
        date, daily_visits, daily_revenue = row
        row_count = self.filterTable.rowCount()
        self.filterTable.setRowCount(row_count + 1)
        self.filterTable.setItem(row_count, 0, QTableWidgetItem(date.strftime('%Y-%m-%d')))
        self.filterTable.setItem(row_count, 1, QTableWidgetItem(str(daily_visits)))
        self.filterTable.setItem(row_count, 2, QTableWidgetItem(str(daily_revenue)))

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
    manager_view_or_edit_event = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(manager_view_or_edit_event)
    manager_view_or_edit_event.show()
    app.exec_()

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
