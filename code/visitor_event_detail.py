# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '34visitor_event_detail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import __main__

app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 671, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ticketsRemaining = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ticketsRemaining.setObjectName("ticketsRemaining")
        self.gridLayout.addWidget(self.ticketsRemaining, 3, 2, 1, 1)
        self.event = QtWidgets.QLabel(self.gridLayoutWidget)
        self.event.setObjectName("event")
        self.gridLayout.addWidget(self.event, 1, 0, 1, 1)
        self.site = QtWidgets.QLabel(self.gridLayoutWidget)
        self.site.setObjectName("site")
        self.gridLayout.addWidget(self.site, 1, 2, 1, 1)
        self.sdate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.sdate.setObjectName("sdate")
        self.gridLayout.addWidget(self.sdate, 2, 0, 1, 1)
        self.ticketPrice = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ticketPrice.setObjectName("ticketPrice")
        self.gridLayout.addWidget(self.ticketPrice, 3, 0, 1, 1)
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
        self.edate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.edate.setObjectName("edate")
        self.gridLayout.addWidget(self.edate, 2, 2, 1, 1)
        self.eventContent = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.eventContent.setFont(font)
        self.eventContent.setText("")
        self.eventContent.setObjectName("eventContent")
        self.gridLayout.addWidget(self.eventContent, 1, 1, 1, 1)
        self.ticketPriceContent = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.ticketPriceContent.setFont(font)
        self.ticketPriceContent.setText("")
        self.ticketPriceContent.setObjectName("ticketPriceContent")
        self.gridLayout.addWidget(self.ticketPriceContent, 3, 1, 1, 1)
        self.siteContent = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.siteContent.setFont(font)
        self.siteContent.setText("")
        self.siteContent.setObjectName("siteContent")
        self.gridLayout.addWidget(self.siteContent, 1, 3, 1, 1)
        self.ticketsRemainingContent = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.ticketsRemainingContent.setFont(font)
        self.ticketsRemainingContent.setText("")
        self.ticketsRemainingContent.setObjectName("ticketsRemainingContent")
        self.gridLayout.addWidget(self.ticketsRemainingContent, 3, 3, 1, 1)
        self.sdateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.sdateEdit.setReadOnly(True)
        self.sdateEdit.setObjectName("sdateEdit")
        self.gridLayout.addWidget(self.sdateEdit, 2, 1, 1, 1)
        self.edateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.edateEdit.setReadOnly(True)
        self.edateEdit.setObjectName("edateEdit")
        self.gridLayout.addWidget(self.edateEdit, 2, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 150, 671, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.description = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.description.setObjectName("description")
        self.gridLayout_2.addWidget(self.description, 0, 0, 1, 1)
        self.des_content = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.des_content.setFont(font)
        self.des_content.setObjectName("des_content")
        self.gridLayout_2.addWidget(self.des_content, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(90, 280, 521, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.logVisit = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.logVisit.setObjectName("logVisit")
        self.gridLayout_3.addWidget(self.logVisit, 0, 2, 1, 1)
        self.visitDate = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.visitDate.setObjectName("visitDate")
        self.gridLayout_3.addWidget(self.visitDate, 0, 0, 1, 1)
        self.visit_date_content = QtWidgets.QDateEdit(self.gridLayoutWidget_3)
        self.visit_date_content.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 2, 1), QtCore.QTime(0, 0, 0)))
        self.visit_date_content.setObjectName("visit_date_content")
        self.gridLayout_3.addWidget(self.visit_date_content, 0, 1, 1, 1)
        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(290, 340, 113, 32))
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
        self.ticketsRemaining.setText(_translate("MainWindow", "Tickets Remaining"))
        self.event.setText(_translate("MainWindow", "Event"))
        self.site.setText(_translate("MainWindow", "Site"))
        self.sdate.setText(_translate("MainWindow", "Start Date"))
        self.ticketPrice.setText(_translate("MainWindow", "Ticket Price ($)"))
        self.label.setText(_translate("MainWindow", "Event Detail"))
        self.edate.setText(_translate("MainWindow", "End Date"))
        self.description.setText(_translate("MainWindow", "Description"))
        self.logVisit.setText(_translate("MainWindow", "Log Visit"))
        self.visitDate.setText(_translate("MainWindow", "Visit Date"))
        self.backbtn.setText(_translate("MainWindow", "Back"))

        self.retrieve_info()
        if __main__.logged_user is None:
            __main__.logged_user = 'visitor1'
        self.user_name = __main__.logged_user

        self.backbtn.clicked.connect(lambda: self.func(idx=33))
        self.logVisit.clicked.connect(self.log_visit)

    def retrieve_info(self):
        name, start_date, site_name, tickets_re = __main__.selected_event33
        query = "select EndDate, Price, Description " \
                "from event where Name = \'" + name + "\' " \
                "and StartDate = \'" + start_date + "\' " \
                "and SiteName = \'" + site_name + "\';"
        result = self.retrieve_from_db(query)
        end_date, price, description = result[0]
        self.eventContent.setText(name)
        self.siteContent.setText(site_name)
        self.sdateEdit.setDate(self.convert_str_to_qdate(start_date))
        self.edateEdit.setDate(self.convert_datetime_to_qdate(end_date))
        self.ticketPriceContent.setText(str(price))
        self.ticketsRemainingContent.setText(str(tickets_re))
        self.des_content.setPlainText(description)

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

    def log_visit(self):
        name, start_date, site_name, tickets_re = __main__.selected_event33
        # check the status of the create statement
        start_date = self.sdateEdit.date()
        end_date = self.edateEdit.date()
        visit_date = self.visit_date_content.date()
        if not (start_date <= visit_date <= end_date):
            self.msgDialog("The visit date needs to be within the start date and end date!")
            return
        # TODO: log the visit to db!
        visit_date = visit_date.toString(Qt.ISODate)
        start_date = start_date.toString(Qt.ISODate)
        end_date = end_date.toString(Qt.ISODate)

        query = "select EndDate from visit_event " \
                "where Name = \'" + name + "\' " \
                "and StartDate = \'" + str(start_date) + "\' " \
                "and SiteName = \'" + site_name + "\' " \
                "and Username = \'" + self.user_name + "\';"
        result = self.retrieve_from_db(query)
        visit_dates = list()
        if len(result) != 0:
            for row in result:
                visit_dates.append(str(row[0]))
        if visit_date in visit_dates:
            self.msgDialog("You cannot log visit to the same event on the same date!")
            return
        query = "insert into visit_event " \
                "VALUES(\'" + self.user_name + "\', \'" + name + "\', " \
                "\'" + str(start_date) + "\', \'" + site_name + "\', " \
                "\'" + str(visit_date) + "\');"
        self.update_db(query)

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
    visitor_event_detail = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(visitor_event_detail)
    visitor_event_detail.show()
    app.exec_()
    visitor_event_detail.close()

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
