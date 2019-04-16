# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_functionality.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 70, 261, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.take_transit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.take_transit_btn.setFont(font)
        self.take_transit_btn.setObjectName("take_transit_btn")
        self.verticalLayout.addWidget(self.take_transit_btn)
        self.view_transit_history_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_transit_history_btn.setFont(font)
        self.view_transit_history_btn.setObjectName("view_transit_history_btn")
        self.verticalLayout.addWidget(self.view_transit_history_btn)
        self.back_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout.addWidget(self.back_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "user_functionality"))
        self.label.setText(_translate("Dialog", "User Functionality"))
        self.take_transit_btn.setText(_translate("Dialog", "Take Transit"))
        self.view_transit_history_btn.setText(_translate("Dialog", "View Transit History"))
        self.back_btn.setText(_translate("Dialog", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

