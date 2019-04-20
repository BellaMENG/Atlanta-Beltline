# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '32staff_event_detail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
from PyQt5.QtWidgets import QListWidgetItem
app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, -1, 671, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.evetDetail = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.evetDetail.setFont(font)
        self.evetDetail.setAlignment(QtCore.Qt.AlignCenter)
        self.evetDetail.setObjectName("evetDetail")
        self.gridLayout.addWidget(self.evetDetail, 0, 0, 1, 4)
        self.site = QtWidgets.QLabel(self.gridLayoutWidget)
        self.site.setObjectName("site")
        self.gridLayout.addWidget(self.site, 1, 2, 1, 1)
        self.event = QtWidgets.QLabel(self.gridLayoutWidget)
        self.event.setObjectName("event")
        self.gridLayout.addWidget(self.event, 1, 0, 1, 1)
        self.eventContent = QtWidgets.QLabel(self.gridLayoutWidget)
        self.eventContent.setText("")
        self.eventContent.setObjectName("eventContent")
        self.gridLayout.addWidget(self.eventContent, 1, 1, 1, 1)
        self.siteContent = QtWidgets.QLabel(self.gridLayoutWidget)
        self.siteContent.setText("")
        self.siteContent.setObjectName("siteContent")
        self.gridLayout.addWidget(self.siteContent, 1, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 671, 76))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.edate = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.edate.setObjectName("edate")
        self.gridLayout_2.addWidget(self.edate, 0, 2, 1, 1)
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.edateEdit.setReadOnly(True)
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout_2.addWidget(self.edateEdit, 0, 3, 1, 1)
        self.durationDays = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.durationDays.setObjectName("durationDays")
        self.gridLayout_2.addWidget(self.durationDays, 0, 4, 1, 1)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.sdateEdit.setReadOnly(True)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout_2.addWidget(self.sdateEdit, 0, 1, 1, 1)
        self.sdate = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.sdate.setObjectName("sdate")
        self.gridLayout_2.addWidget(self.sdate, 0, 0, 1, 1)
        self.duration = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.duration.setText("")
        self.duration.setObjectName("duration")
        self.gridLayout_2.addWidget(self.duration, 0, 5, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 220, 671, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.capacity = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.capacity.setObjectName("capacity")
        self.gridLayout_3.addWidget(self.capacity, 0, 2, 1, 1)
        self.staffAssigned = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.staffAssigned.setObjectName("staffAssigned")
        self.gridLayout_3.addWidget(self.staffAssigned, 0, 0, 1, 1)
        self.capacityContent = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.capacityContent.setObjectName("capacityContent")
        self.gridLayout_3.addWidget(self.capacityContent, 0, 3, 1, 1)
        self.price = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.price.setObjectName("price")
        self.gridLayout_3.addWidget(self.price, 0, 4, 1, 1)
        self.staff_list = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.staff_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.staff_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.staff_list.setObjectName("staff_list")
        self.gridLayout_3.addWidget(self.staff_list, 0, 1, 1, 1)
        self.priceContent = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.priceContent.setObjectName("priceContent")
        self.gridLayout_3.addWidget(self.priceContent, 0, 5, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 310, 671, 151))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.description = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.description.setObjectName("description")
        self.gridLayout_4.addWidget(self.description, 0, 0, 1, 1)
        self.description_content = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.description_content.setReadOnly(True)
        self.description_content.setObjectName("description_content")
        self.gridLayout_4.addWidget(self.description_content, 0, 1, 1, 1)
        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(290, 480, 113, 32))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Event Detail"))
        self.evetDetail.setText(_translate("MainWindow", "Event Detail"))
        self.site.setText(_translate("MainWindow", "Site"))
        self.event.setText(_translate("MainWindow", "Event"))
        self.edate.setText(_translate("MainWindow", "End Date"))
        self.durationDays.setText(_translate("MainWindow", "Duration Days"))
        self.sdate.setText(_translate("MainWindow", "Start Date"))
        self.capacity.setText(_translate("MainWindow", "Capacity"))
        self.staffAssigned.setText(_translate("MainWindow", "Staffs Assigned"))
        self.capacityContent.setText(_translate("MainWindow", "                "))
        self.price.setText(_translate("MainWindow", "Price"))
        self.staff_list.setSortingEnabled(True)
        self.priceContent.setText(_translate("MainWindow", "                "))
        self.description.setText(_translate("MainWindow", "Description"))
        self.backbtn.setText(_translate("MainWindow", "Back"))

        self.backbtn.clicked.connect(lambda: self.func(idx=31))
        self.retrieve()

    def retrieve(self):
        if __main__.selected_event31 is None:
            return
        event_name, start_date, site_name = __main__.selected_event31
        query = "select Name, SiteName, StartDate, EndDate, " \
                "datediff(EndDate, StartDate) + 1, Capacity, Price, Description " \
                "from event where Name = \'" + event_name + "\' " \
                "and StartDate = \'" + str(start_date) + "\' " \
                "and SiteName = \'" + site_name + "\';"
        print(query)
        result = self.retrieve_from_db(query)
        end_date = result[0][3]
        duration = result[0][4]
        capacity = result[0][5]
        price = result[0][6]
        description = result[0][7]

        query = "select concat(Firstname, \' \', Lastname) " \
                "from assign_to join user on user.Username = assign_to.Username " \
                "where EventName = \'" + event_name + "\' " \
                "and StartDate = \'" + str(start_date) + "\' " \
                "and SiteName = \'" + site_name + "\';"
        print(query)
        result = self.retrieve_from_db(query)
        staff_names = list()
        for row in result:
            staff_names.append(row[0])

        self.eventContent.setText(event_name)
        self.siteContent.setText(site_name)
        self.sdateEdit.setDate(self.convert_str_to_qdate(start_date))
        self.edateEdit.setDate(self.convert_datetime_to_qdate(end_date))
        self.duration.setText(str(duration))
        self.capacityContent.setText(str(capacity))
        self.priceContent.setText(str(price))
        self.description_content.setPlainText(description)

        if len(staff_names) != 0:
            for item in staff_names:
                self.staff_list.addItem(QListWidgetItem(item))

    def add_line(self):
        return

    def convert_datetime_to_qdate(self, datetime_val):
        datetime_val = datetime_val.strftime('%Y%m%d')
        datetime_val = str(datetime_val)
        qdate_val = QtCore.QDate(int(datetime_val[:4]), int(datetime_val[4:6]), int(datetime_val[6:8]))
        return qdate_val

    def convert_str_to_qdate(self, str_val):
        qdate_val = QtCore.QDate(int(str_val[:4]), int(str_val[5:7]), int(str_val[8:10]))
        return qdate_val

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
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
