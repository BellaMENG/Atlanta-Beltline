# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administrator_manage_transit.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_administrator_manage_transit(object):
    def setupUi(self, administrator_manage_transit):
        administrator_manage_transit.setObjectName("administrator_manage_transit")
        administrator_manage_transit.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(administrator_manage_transit)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.route_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.route_lineEdit.setGeometry(QtCore.QRect(500, 100, 171, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.route_lineEdit.setFont(font)
        self.route_lineEdit.setObjectName("route_lineEdit")
        self.transport_type_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.transport_type_comboBox.setGeometry(QtCore.QRect(210, 100, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.transport_type_comboBox.setFont(font)
        self.transport_type_comboBox.setObjectName("transport_type_comboBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.contain_site_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.contain_site_comboBox.setGeometry(QtCore.QRect(210, 160, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.contain_site_comboBox.setFont(font)
        self.contain_site_comboBox.setObjectName("contain_site_comboBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.min_price_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.min_price_lineEdit.setGeometry(QtCore.QRect(560, 160, 61, 31))
        self.min_price_lineEdit.setObjectName("min_price_lineEdit")
        self.max_price_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.max_price_lineEdit.setGeometry(QtCore.QRect(660, 160, 61, 31))
        self.max_price_lineEdit.setObjectName("max_price_lineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(630, 170, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filter_btn.setGeometry(QtCore.QRect(80, 220, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.filter_btn.setFont(font)
        self.filter_btn.setObjectName("filter_btn")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(430, 220, 301, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_btn.setFont(font)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout.addWidget(self.create_btn)
        self.edit_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edit_btn.setFont(font)
        self.edit_btn.setObjectName("edit_btn")
        self.horizontalLayout.addWidget(self.edit_btn)
        self.delete_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(330, 550, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(609, 280, 181, 80))
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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 280, 551, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        administrator_manage_transit.setCentralWidget(self.centralwidget)

        self.retranslateUi(administrator_manage_transit)
        QtCore.QMetaObject.connectSlotsByName(administrator_manage_transit)

    def retranslateUi(self, administrator_manage_transit):
        _translate = QtCore.QCoreApplication.translate
        administrator_manage_transit.setWindowTitle(_translate("administrator_manage_transit", "Administrator Manage Transit"))
        self.label.setText(_translate("administrator_manage_transit", "Manage Transit"))
        self.label_2.setText(_translate("administrator_manage_transit", "Transport Type"))
        self.label_3.setText(_translate("administrator_manage_transit", "Route"))
        self.label_4.setText(_translate("administrator_manage_transit", "Contain Site"))
        self.label_5.setText(_translate("administrator_manage_transit", "Price Range"))
        self.label_6.setText(_translate("administrator_manage_transit", "--"))
        self.filter_btn.setText(_translate("administrator_manage_transit", "Filter"))
        self.create_btn.setText(_translate("administrator_manage_transit", "Create"))
        self.edit_btn.setText(_translate("administrator_manage_transit", "Edit"))
        self.delete_btn.setText(_translate("administrator_manage_transit", "Delete"))
        self.back_btn.setText(_translate("administrator_manage_transit", "Back"))
        self.sortByLabel.setText(_translate("administrator_manage_transit", "SortBy"))
        self.orderLabel.setText(_translate("administrator_manage_transit", "Order"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    administrator_manage_transit = QtWidgets.QMainWindow()
    ui = Ui_administrator_manage_transit()
    ui.setupUi(administrator_manage_transit)
    administrator_manage_transit.show()
    sys.exit(app.exec_())

