# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setIconSize(QtCore.QSize(45, 59))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.GroupedDragging)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(65, 41, 371, 321))
        self.table.setTabKeyNavigation(True)
        self.table.setGridStyle(QtCore.Qt.SolidLine)
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.verticalHeader().setVisible(False)
        self.einfuegen = QtWidgets.QPushButton(self.centralwidget)
        self.einfuegen.setGeometry(QtCore.QRect(70, 360, 181, 23))
        self.einfuegen.setObjectName("einfuegen")
        self.speichern = QtWidgets.QPushButton(self.centralwidget)
        self.speichern.setGeometry(QtCore.QRect(270, 360, 161, 23))
        self.speichern.setObjectName("speichern")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menudatei = QtWidgets.QMenu(self.menubar)
        self.menudatei.setObjectName("menudatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionbar = QtWidgets.QAction(MainWindow)
        self.actionbar.setObjectName("actionbar")
        self.menudatei.addSeparator()
        self.menudatei.addAction(self.actionbar)
        self.menubar.addAction(self.menudatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "name"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "lastname"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "subject"))
        self.einfuegen.setText(_translate("MainWindow", "einfuegen"))
        self.speichern.setText(_translate("MainWindow", "speichern"))
        self.menudatei.setTitle(_translate("MainWindow", "datei"))
        self.actionbar.setText(_translate("MainWindow", "speichern"))
