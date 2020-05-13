import  sys
from qtpy import QtWidgets
import csv

from untitled.mainwindow import Ui_MainWindow

app=QtWidgets.QApplication(sys.argv)
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Studierendenverwaltung")
        self.datenimportieren()
        self.ui.einfuegen.clicked.connect(self.eifuegen)
        self.ui.speichern.clicked.connect(self.speichern)
        self.ui.actionbar.triggered.connect(self.speichern)
    def speichern(self):
        with open('alaa.csv','w',newline='',encoding="utf-8") as file:
            row=csv.writer(file,delimiter=';',quotechar='"')
            for i in range(0,self.ui.table.rowCount()):
                row.writerow([self.ui.table.item(i,0).text(),self.ui.table.item(i,1).text(),self.ui.table.item(i,2).text()])
    def eifuegen(self):
        row=self.ui.table.rowCount()
        self.ui.table.insertRow(row)
    def datenimportieren(self):
        with open('alaa.csv','r',newline='',encoding="utf-8") as file:
            reader=csv.reader(file,delimiter=";",quotechar='"')
            counter=0
            for row in reader:
                self.ui.table.insertRow(counter)
                for i in range(0,3):
                    self.ui.table.setItem(counter,i,QtWidgets.QTableWidgetItem(row[i]))
                counter+=1


window = MainWindow()

window.show()

sys.exit(app.exec_())

#self.ui.button.clicked.connect(self.f)
      #  self.ui.table.cellChanged.connect(self.g)
   # def g(self,row,col):
       # print(row)
      #  print(col)

   # def f(self):
      #  row=self.ui.table.rowCount()
       # print(row)
       # self.ui.table.insertRow(row)
       # self.ui.table.setItem(row,0,QtWidgets.QTableWidgetItem("Stuttgart"))
       # self.ui.table.setItem(row,1,QtWidgets.QTableWidgetItem("2394923"))

       # print("geklicked")*/*
