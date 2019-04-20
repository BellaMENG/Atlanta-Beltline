# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administrator_manage_site.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableWidget,QPushButton,QApplication,QVBoxLayout,QTableWidgetItem,QCheckBox,QAbstractItemView,QHeaderView,QLabel,QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import __main__
import sys
import administrator_edit_site

app = QtWidgets.QApplication(sys.argv)

class Ui_adniministrator_manage_site(object):
    def setupUi(self, adniministrator_manage_site):
        adniministrator_manage_site.setObjectName("adniministrator_manage_site")
        adniministrator_manage_site.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(adniministrator_manage_site)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 721, 41))
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
        self.site_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.site_comboBox.setFont(font)
        self.site_comboBox.setObjectName("site_comboBox")
        self.horizontalLayout.addWidget(self.site_comboBox)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.manager_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.manager_comboBox.setFont(font)
        self.manager_comboBox.setObjectName("manager_comboBox")
        self.horizontalLayout.addWidget(self.manager_comboBox)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.open_everyday_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.open_everyday_comboBox.setObjectName("open_everyday_comboBox")
        self.horizontalLayout.addWidget(self.open_everyday_comboBox)
        self.filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filter_btn.setGeometry(QtCore.QRect(50, 180, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.filter_btn.setFont(font)
        self.filter_btn.setObjectName("filter_btn")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(350, 160, 391, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_btn.setFont(font)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_2.addWidget(self.create_btn)
        self.edit_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edit_btn.setFont(font)
        self.edit_btn.setObjectName("edit_btn")
        self.horizontalLayout_2.addWidget(self.edit_btn)
        self.delete_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_2.addWidget(self.delete_btn)
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(330, 530, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 260, 451, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(590, 270, 160, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.sortbyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sortbyLabel.setObjectName("sortbyLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sortbyLabel)
        self.sortbyComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sortbyComboBox.setObjectName("sortbyComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sortbyComboBox)
        self.orderLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.orderLabel.setObjectName("orderLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.orderLabel)
        self.orderComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.orderComboBox.setObjectName("orderComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.orderComboBox)
        adniministrator_manage_site.setCentralWidget(self.centralwidget)

        self.retranslateUi(adniministrator_manage_site)
        QtCore.QMetaObject.connectSlotsByName(adniministrator_manage_site)

    def retranslateUi(self, adniministrator_manage_site):
        _translate = QtCore.QCoreApplication.translate
        adniministrator_manage_site.setWindowTitle(_translate("adniministrator_manage_site", "Administrator Manage Site"))
        self.label.setText(_translate("adniministrator_manage_site", "Manage Site"))
        self.label_2.setText(_translate("adniministrator_manage_site", "Site"))
        self.label_3.setText(_translate("adniministrator_manage_site", "Manager"))
        self.label_4.setText(_translate("adniministrator_manage_site", "Open Everyday"))
        self.filter_btn.setText(_translate("adniministrator_manage_site", "Filter"))
        self.create_btn.setText(_translate("adniministrator_manage_site", "Create"))
        self.edit_btn.setText(_translate("adniministrator_manage_site", "Edit"))
        self.delete_btn.setText(_translate("adniministrator_manage_site", "Delete"))
        self.back_btn.setText(_translate("adniministrator_manage_site", "Back"))

        self.open_everyday_comboBox.addItems(['Yes','No'])
        order_list = ['ASC','DESC']
        self.orderComboBox.addItems(order_list)

        col_list = ["site.Name","manager.Name","site.OpenEveryDay"]
        self.sortbyComboBox.addItems(col_list)

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['   Selected   ','   Name    ','    Manager   ','     Open Everyday     '])
        self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        self.check_box_list = list()
        self.manager_list = ['']
        self.site_list = ['']
        self.get_managers()
        self.get_sites()
        self.manager_comboBox.addItems(self.manager_list)
        self.site_comboBox.addItems(self.site_list)
        self.filter_btn.clicked.connect(self.filter)
        self.delete_btn.clicked.connect(self.delete_site)
        self.edit_btn.clicked.connect(self.edit_site)
        self.back_btn.clicked.connect(self.back)
        #self.create_btn.clicked.connect(self.add_line)

    def filter(self):
        self.tableWidget.setRowCount(0)
        self.check_box_list = list()
        site = self.site_comboBox.currentText()
        manager = self.manager_comboBox.currentText()
        open_everyday = self.open_everyday_comboBox.currentText()
        order = self.orderComboBox.currentText()
        order_col = self.sortbyComboBox.currentText()
        if order_col == "manager.Name":
            order_col = "concat(user.Firstname,\' \',user.Lastname)"
        sql = "select site.Name , concat(user.Firstname,\' \',user.Lastname), site.OpenEveryDay from user join site on user.Username = site.Manager where site.Name like concat(\'%\',\'" + site + "\' ,\'%\') and concat(user.Firstname,\' \',user.Lastname) like concat(\'%\',\'" + manager+ "\' ,\'%\') and site.OpenEveryDay like concat(\'%\',\'"+open_everyday+"\' ,\'%\') order by \'" + order_col + "\' \'" + order + "\';"
        print(sql)
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            self.add_line(row)
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
    
    def delete_site(self):
        idx = -1
        for i in range(len(self.check_box_list)):
            if self.check_box_list[i].isChecked():
                if idx != -1:
                    QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                    "Only ONE site can be selected", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
                else:
                    idx = i
        if idx == -1:
            return
        site_name = self.tableWidget.item(idx,1).text()
        manager = self.tableWidget.item(idx,2).text()
        sql = "delete from site where Name = \'" + site_name + "\'"
        print(sql)
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(sql)
        connection_object.commit()
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def edit_site(self):
        idx = -1
        for i in range(len(self.check_box_list)):
            if self.check_box_list[i].isChecked():
                if idx != -1:
                    QMessageBox.warning(self.label, 
                                    "Invalid Information", 
                                    "Only ONE site can be selected", 
                                    QMessageBox.Yes, 
                                    QMessageBox.Yes)
                else:
                    idx = i
        if idx == -1:
            return
        site_name = self.tableWidget.item(idx,1).text()
        manager = self.tableWidget.item(idx,2).text()
        print("edit site:" , site_name)
        __main__.argv1 = site_name
        __main__.argv2 = manager
        __main__.screen_number = 20
        app.exit()
        

    def add_line(self,row):
        name,manager,open_everyday = row
        row_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_count + 1)
        ck = QCheckBox()
        h = QHBoxLayout()
        h.setAlignment(Qt.AlignCenter)
        h.addWidget(ck)
        w = QWidget()
        w.setLayout(h)
        self.tableWidget.setCellWidget(row_count,0,w)
        self.tableWidget.setItem(row_count,1,QTableWidgetItem(name))
        self.tableWidget.setItem(row_count,2,QTableWidgetItem(manager))
        self.tableWidget.setItem(row_count,3,QTableWidgetItem(open_everyday))
        self.check_box_list.append(ck)
    
    def get_sites(self):
        query1 = "SELECT DISTINCT Name FROM connect;" 
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        for row in result:
            self.site_list.append(row[0])
        print(self.site_list)
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
    
    def get_managers(self):
        query1 = "select concat(Firstname, \' \',Lastname) from user where UserType = \'manager\'"; 
        connection_object = __main__.connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("user_login.py login() Connected to MySQL server: ",db_Info)
        else:
            print("user_login.py login() Not Connected ")
        cursor = connection_object.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        for row in result:
            self.manager_list.append(row[0])
        print(self.manager_list)
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def func(self,idx):
        __main__.screen_number = idx
        app.exit()

    def back(self):
        function_screens = {
                            "Administrator": 8,
                            "Administrator_Visitor":9,
                            }
        __main__.screen_number = function_screens[__main__.user_type]
        app.exit()

def render():
    adniministrator_manage_site = QtWidgets.QMainWindow()
    ui = Ui_adniministrator_manage_site()
    ui.setupUi(adniministrator_manage_site)
    adniministrator_manage_site.show()
    app.exec_()
    adniministrator_manage_site.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adniministrator_manage_site = QtWidgets.QMainWindow()
    ui = Ui_adniministrator_manage_site()
    ui.setupUi(adniministrator_manage_site)
    adniministrator_manage_site.show()
    sys.exit(app.exec_())

