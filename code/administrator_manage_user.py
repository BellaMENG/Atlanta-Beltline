# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administrator_manage_user.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableWidget,QPushButton,QApplication,QVBoxLayout,QTableWidgetItem,QCheckBox,QAbstractItemView,QHeaderView,QLabel,QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import sys
import __main__

app = QtWidgets.QApplication(sys.argv)

class Ui_administrator_manage_user(object):
    def setupUi(self, administrator_manage_user):
        administrator_manage_user.setObjectName("administrator_manage_user")
        administrator_manage_user.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(administrator_manage_user)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 70, 721, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.user_name_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_name_lineEdit.setFont(font)
        self.user_name_lineEdit.setObjectName("user_name_lineEdit")
        self.horizontalLayout.addWidget(self.user_name_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.type_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.type_comboBox.setFont(font)
        self.type_comboBox.setObjectName("type_comboBox")
        self.horizontalLayout.addWidget(self.type_comboBox)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.status_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status_comboBox.setFont(font)
        self.status_comboBox.setObjectName("status_comboBox")
        self.horizontalLayout.addWidget(self.status_comboBox)
        self.filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filter_btn.setGeometry(QtCore.QRect(50, 180, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filter_btn.setFont(font)
        self.filter_btn.setObjectName("filter_btn")
        self.approve_btn = QtWidgets.QPushButton(self.centralwidget)
        self.approve_btn.setGeometry(QtCore.QRect(490, 180, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.approve_btn.setFont(font)
        self.approve_btn.setObjectName("approve_btn")
        self.decline_btn = QtWidgets.QPushButton(self.centralwidget)
        self.decline_btn.setGeometry(QtCore.QRect(620, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.decline_btn.setFont(font)
        self.decline_btn.setObjectName("decline_btn")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 520, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 240, 531, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(590, 240, 160, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.sortByLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sortByLabel.setObjectName("sortByLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sortByLabel)
        self.sortByComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sortByComboBox.setObjectName("sortByComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sortByComboBox)
        self.orderLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.orderLabel.setObjectName("orderLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.orderLabel)
        self.orderComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.orderComboBox.setObjectName("orderComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.orderComboBox)
        administrator_manage_user.setCentralWidget(self.centralwidget)

        self.retranslateUi(administrator_manage_user)
        QtCore.QMetaObject.connectSlotsByName(administrator_manage_user)


    def retranslateUi(self, administrator_manage_user):
        _translate = QtCore.QCoreApplication.translate
        administrator_manage_user.setWindowTitle(_translate("administrator_manage_user", "Administrator Manage User"))
        self.label.setText(_translate("administrator_manage_user", "Manager User"))
        self.label_2.setText(_translate("administrator_manage_user", "User Name"))
        self.label_3.setText(_translate("administrator_manage_user", "Type"))
        self.label_4.setText(_translate("administrator_manage_user", "Status"))
        self.filter_btn.setText(_translate("administrator_manage_user", "Filter"))
        self.approve_btn.setText(_translate("administrator_manage_user", "Approve"))
        self.decline_btn.setText(_translate("administrator_manage_user", "Decline"))
        self.pushButton.setText(_translate("administrator\_manage_user", "Back"))
        self.sortByLabel.setText(_translate("administrator_manage_user", "SortBy "))
        self.orderLabel.setText(_translate("administrator_manage_user", "Order"))

        user_type_list = ['User','Manager','Staff','Visitor']
        self.type_comboBox.addItems(user_type_list)

        status_list = ['','Approved','Pending','Declined']
        self.status_comboBox.addItems(status_list)

        order_list = ['ASC','DESC']
        self.orderComboBox.addItems(order_list)

        col_list = ["user.Username","\'Email Count\'", "user.UserType", "user.UserType"]
        self.sortByComboBox.addItems(col_list)

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['    Selected    ','    User Name    ','    Email Count    ','    User Type    ','    Status    '])
        self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4,QHeaderView.ResizeToContents)
       
        self.check_box_list = list()
        self.filter_btn.clicked.connect(self.filter)
        self.approve_btn.clicked.connect(lambda:self.modify_users(op=1))
        self.decline_btn.clicked.connect(lambda:self.modify_users(op=2))
        self.pushButton.clicked.connect(self.back)

    def filter(self):
        self.tableWidget.setRowCount(0)
        self.check_box_list = list()
        user_name = self.user_name_lineEdit.text()
        user_type = self.type_comboBox.currentText()
        status = self.status_comboBox.currentText()
        order_col = self.sortByComboBox.currentText()
        order = self.orderComboBox.currentText()
        if order_col == "\'Email Count\'":
            order_col = "COUNT(*)"

        
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        if user_name:
            sql = "select emails.Username, count(*) as 'Email Count', user.UserType, user.Status \
from emails join user on emails.Username = user.Username \
where user.UserType like concat(\'%\',\'"+user_type +"\',\'%\') and Status like concat(\'%\',\'"+status +"\',\'%\') and user.Username like \'"+user_name +"\' \
 group by emails.Username \
order by " + order_col + " " + order + ";"
        else:
            sql = "select emails.Username, count(*) as 'Email Count', user.UserType, user.Status \
from emails join user on emails.Username = user.Username \
where user.UserType like concat(\'%\',\'"+user_type +"\',\'%\') and Status like concat(\'%\',\'"+status +"\',\'%\') \
 group by emails.Username \
order by " + order_col + " " + order + ";"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)
            self.add_line(row)
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def add_line(self,row):
        user_name,email_count,user_type,status = row
        email_count = str(email_count)
        row_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_count + 1)
        ck = QCheckBox()
        h = QHBoxLayout()
        h.setAlignment(Qt.AlignCenter)
        h.addWidget(ck)
        w = QWidget()
        w.setLayout(h)
        self.tableWidget.setCellWidget(row_count,0,w)
        self.tableWidget.setItem(row_count,1,QTableWidgetItem(user_name))
        self.tableWidget.setItem(row_count,2,QTableWidgetItem(email_count))
        self.tableWidget.setItem(row_count,3,QTableWidgetItem(user_type))
        self.tableWidget.setItem(row_count,4,QTableWidgetItem(status))
        self.check_box_list.append(ck)

    def modify_users(self,op):
        idx = -1
        for i in range(len(self.check_box_list)):
            if self.check_box_list[i].isChecked():
                if idx != -1:
                    QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                    "Only ONE user can be selected", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
                else:
                    idx = i
        if idx == -1:
            return
        user_name = self.tableWidget.item(idx,1).text()
        status = self.tableWidget.item(idx,4).text()
        if op == 1:
            if status == "Pending" or status == "Declined":
                connection_object = __main__.connection_pool.get_connection()
                if connection_object.is_connected():
                    db_Info = connection_object.get_server_info()
                    print("user_login.py login() Connected to MySQL server: ",db_Info)
                else:
                    print("user_login.py login() Not Connected ")
                cursor = connection_object.cursor()
                sql = "Update user set Status = \'Approved\' where Username= \'" +  user_name + "\'"
                cursor.execute(sql)
                connection_object.commit()
                if(connection_object.is_connected()):
                    cursor.close()
                    connection_object.close()
                    print("MySQL connection is closed")
        if op == 2:
            if status == "Pending":
                connection_object = __main__.connection_pool.get_connection()
                if connection_object.is_connected():
                    db_Info = connection_object.get_server_info()
                    print("user_login.py login() Connected to MySQL server: ",db_Info)
                else:
                    print("user_login.py login() Not Connected ")
                cursor = connection_object.cursor()
                sql = "Update user set Status = \'Declined\' where Username= \'" +  user_name + "\'"
                cursor.execute(sql)
                connection_object.commit()
                if(connection_object.is_connected()):
                    cursor.close()
                    connection_object.close()
                    print("MySQL connection is closed")
        
    def back(self):
        function_screens = {
                            "Administrator": 8,
                            "Administrator_Visitor":9,
                            }
        __main__.screen_number = function_screens[__main__.user_type]
        app.exit()


def render():
    administrator_manage_user = QtWidgets.QMainWindow()
    ui = Ui_administrator_manage_user()
    ui.setupUi(administrator_manage_user)
    administrator_manage_user.show()
    app.exec_()
    administrator_manage_user.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    administrator_manage_user = QtWidgets.QMainWindow()
    ui = Ui_administrator_manage_user()
    ui.setupUi(administrator_manage_user)
    administrator_manage_user.show()
    sys.exit(app.exec_())

