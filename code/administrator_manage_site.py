# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administrator_manage_site.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableWidget,QPushButton,QApplication,QVBoxLayout,QTableWidgetItem,QCheckBox,QAbstractItemView,QHeaderView,QLabel,QFrame
from PyQt5.QtCore import Qt

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
        self.tableWidget.setGeometry(QtCore.QRect(160, 260, 451, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
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

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['    Selected     ','     Name      ','      Manager     ','     Open Everyday     '])
        self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        self.check_box_list = list()

        #self.create_btn.clicked.connect(self.add_line)

    def add_line(self):
        #route,transport_type,price,connected_sites = ss.split()
        name,manager,open_everyday = ['lcb','jimmy','Yes']
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adniministrator_manage_site = QtWidgets.QMainWindow()
    ui = Ui_adniministrator_manage_site()
    ui.setupUi(adniministrator_manage_site)
    adniministrator_manage_site.show()
    sys.exit(app.exec_())

