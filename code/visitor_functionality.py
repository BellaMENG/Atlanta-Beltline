# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitor_functionality.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import __main__

app = QtWidgets.QApplication(sys.argv)

class Ui_visitor_functionality(object):
    def setupUi(self, visitor_functionality):
        visitor_functionality.setObjectName("visitor_functionality")
        visitor_functionality.resize(553, 628)
        self.label = QtWidgets.QLabel(visitor_functionality)
        self.label.setGeometry(QtCore.QRect(100, 20, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(visitor_functionality)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 90, 421, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.explore_event_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.explore_event_btn.setFont(font)
        self.explore_event_btn.setObjectName("explore_event_btn")
        self.verticalLayout.addWidget(self.explore_event_btn)
        self.explore_site_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.explore_site_btn.setFont(font)
        self.explore_site_btn.setObjectName("explore_site_btn")
        self.verticalLayout.addWidget(self.explore_site_btn)
        self.view_visit_history_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view_visit_history_btn.setFont(font)
        self.view_visit_history_btn.setObjectName("view_visit_history_btn")
        self.verticalLayout.addWidget(self.view_visit_history_btn)
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

        self.retranslateUi(visitor_functionality)
        QtCore.QMetaObject.connectSlotsByName(visitor_functionality)

    def retranslateUi(self, visitor_functionality):
        _translate = QtCore.QCoreApplication.translate
        visitor_functionality.setWindowTitle(_translate("visitor_functionality", "Visitor Functionality"))
        self.label.setText(_translate("visitor_functionality", "Visitor Functionality"))
        self.explore_event_btn.setText(_translate("visitor_functionality", "Explore Event"))
        self.explore_site_btn.setText(_translate("visitor_functionality", "Explore Site"))
        self.view_visit_history_btn.setText(_translate("visitor_functionality", "View Visit History"))
        self.take_transit_btn.setText(_translate("visitor_functionality", "Take Transit"))
        self.view_transit_history_btn.setText(_translate("visitor_functionality", "View Transit History"))
        self.back_btn.setText(_translate("visitor_functionality", "Back"))

        self.explore_event_btn.clicked.connect(lambda:self.func(17))
        self.explore_site_btn.clicked.connect(lambda:self.func(17))
        self.view_visit_history_btn.clicked.connect(lambda:self.func(17))
        self.take_transit_btn.clicked.connect(lambda:self.func(17))
        self.view_transit_history_btn.clicked.connect(lambda:self.func(17))
        self.back_btn.clicked.connect(lambda:self.func(17))

def render():
    visitor_functionality = QtWidgets.QMainWindow()
    ui = Ui_visitor_functionality()
    ui.setupUi(visitor_functionality)
    visitor_functionality.show()
    app.exec_()
    visitor_functionality.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    visitor_functionality = QtWidgets.QMainWindow()
    ui = Ui_visitor_functionality()
    ui.setupUi(visitor_functionality)
    visitor_functionality.show()
    sys.exit(app.exec_())

