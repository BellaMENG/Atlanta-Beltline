# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '37visitor_site_detail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

app = QtWidgets.QApplication(sys.argv)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 671, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.site_content = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.site_content.setFont(font)
        self.site_content.setText("")
        self.site_content.setObjectName("site_content")
        self.gridLayout.addWidget(self.site_content, 1, 1, 1, 1)
        self.open_content = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.open_content.setFont(font)
        self.open_content.setText("")
        self.open_content.setObjectName("open_content")
        self.gridLayout.addWidget(self.open_content, 1, 3, 1, 1)
        self.site = QtWidgets.QLabel(self.gridLayoutWidget)
        self.site.setObjectName("site")
        self.gridLayout.addWidget(self.site, 1, 0, 1, 1)
        self.openEveryday = QtWidgets.QLabel(self.gridLayoutWidget)
        self.openEveryday.setObjectName("openEveryday")
        self.gridLayout.addWidget(self.openEveryday, 1, 2, 1, 1)
        self.siteDetail = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.siteDetail.setFont(font)
        self.siteDetail.setAlignment(QtCore.Qt.AlignCenter)
        self.siteDetail.setObjectName("siteDetail")
        self.gridLayout.addWidget(self.siteDetail, 0, 0, 1, 4)
        self.address = QtWidgets.QLabel(self.gridLayoutWidget)
        self.address.setObjectName("address")
        self.gridLayout.addWidget(self.address, 2, 0, 1, 1)
        self.add_content = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(True)
        self.add_content.setFont(font)
        self.add_content.setText("")
        self.add_content.setObjectName("add_content")
        self.gridLayout.addWidget(self.add_content, 2, 1, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(110, 220, 471, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.visitDate = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.visitDate.setObjectName("visitDate")
        self.gridLayout_2.addWidget(self.visitDate, 0, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 2, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.log_visitbtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.log_visitbtn.setObjectName("log_visitbtn")
        self.gridLayout_2.addWidget(self.log_visitbtn, 0, 2, 1, 1)
        self.backbtn = QtWidgets.QPushButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(290, 300, 113, 32))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Site Detail"))
        self.site.setText(_translate("MainWindow", "Site"))
        self.openEveryday.setText(_translate("MainWindow", "Open Everyday"))
        self.siteDetail.setText(_translate("MainWindow", "Site Detail"))
        self.address.setText(_translate("MainWindow", "Address"))
        self.visitDate.setText(_translate("MainWindow", "Visit Date"))
        self.log_visitbtn.setText(_translate("MainWindow", "Log Visit"))
        self.backbtn.setText(_translate("MainWindow", "Back"))

        if __main__.logged_user is None:
            __main__.logged_user = 'visitor1'
        self.user_name = __main__.logged_user

        self.retrieve_info()
        self.backbtn.clicked.connect(lambda: self.func(idx=35))
        self.log_visitbtn.clicked.connect(self.log_visit)

    def retrieve_info(self):
        site_name = __main__.selected_site35
        query = "select OpenEveryday, Address " \
                "from site where Name = \'" + site_name + "\';"
        result = self.retrieve_from_db(query)
        open_eve = result[0][0]
        add = result[0][1]
        self.site_content.setText(site_name)
        self.open_content.setText(open_eve)
        self.add_content.setText(add)

    def log_visit(self):
        # TODO: insert into db
        site_name = __main__.selected_site35
        user_name = __main__.logged_user
        visit_date = self.dateEdit.date().toString(Qt.ISODate)
        query = "select VisitSiteDate from visit_site " \
                "where Username = \'" + user_name + "\' " \
                "and Name = \'" + site_name + "\';"
        result = self.retrieve_from_db(query)
        date_list = list()
        if len(result) != 0:
            for row in result:
                date_list.append(str(row[0]))
            if visit_date in date_list:
                self.msgDialog("You can visit the same site once a day!")
                return

        query = "insert into visit_site " \
                "VALUES(\'" + user_name + "\', " \
                "\'" + site_name + "\', \'" + visit_date + "\');"
        self.update_db(query)

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
    visitor_site_detail = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(visitor_site_detail)
    visitor_site_detail.show()
    app.exec_()

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
