# -*- coding: utf-8 -*-
  
"""
Created on 01/09/2018
 
@author: Jonathan ANGUISE
 
Comptability soft in python 
 
"""

from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "mainwindow.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.text = QtGui.QTextEdit(self)
        self.text.setText(open(__file__).read())
        self.edit = QtGui.QLineEdit(self)
        self.edit.setText('/tmp/test.pdf')



#Button events
        self.Print_pushButton.clicked.connect(self.Print)
        self.Load_pushButton.clicked.connect(self.LoadFile)
        self.Save_pushButton.clicked.connect(self.SaveFile)
        self.Mail_pushButton.clicked.connect(self.SendMail)
        self.Calculate_pushButton.clicked.connect(self.Calculate)  


#Button Functions
    def PrintFile(self):
        print('Event print file')
	a = self.NameTextEdit.toPlainText()
        print(a)  
    def LoadFile(self):
        print('Event Load File')
    def SaveFile(self):
        print('Event Save File')
    def SendMail(self):
        print('Event Send mail')
    def Calculate(self):
        #catch last used line
        last_line = 0
        while self.tableWidget.item(last_line,0) != None:
            last_line = last_line + 1

        #catch data by line
        line = 0
        for line in range(0,last_line):
            item = str(self.tableWidget.item(line,0).text())
            quantity = int(self.tableWidget.item(line,1).text())
            dutyfree_price = float(self.tableWidget.item(line,2).text())
            print(quantity * dutyfree_price)
            dutyfree_amount =str(quantity * dutyfree_price)
            self.tableWidget.setItem(line, 3, QtGui.QTableWidgetItem(dutyfree_amount))

        #calculatate Dutyfree total amount
        dutyfree_total_amount = 0
        line = 0
        for line in range(0,last_line):
            dutyfree_total_amount =  float(self.tableWidget.item(line,3).text()) + dutyfree_total_amount
        self.DuttyFreePriceLineEdit.setText(str(dutyfree_total_amount)) 

        #calculate TVA ammount
        tva_ratio = float(self.TVARatioLineEdit.text())
        tva_amount = tva_ratio * dutyfree_total_amount / 100
        self.TVAAmountLineEdit.setText(str(tva_amount))

        #calculate TTC total amount
        total_amount = tva_amount + dutyfree_total_amount
        self.TTCPriceLineEdit.setText(str(total_amount))

    def Print(self):
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        printer.setPageSize(QtGui.QPrinter.A6)
        printer.setColorMode(QtGui.QPrinter.Color)
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setOutputFileName(self.edit.text())
        pixmap = QtGui.QPixmap.grabWidget(self).scaled(
            printer.pageRect(QtGui.QPrinter.DevicePixel).size().toSize(),
            QtCore.Qt.KeepAspectRatio)
        painter = QtGui.QPainter(printer)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()


       

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
sys.exit(app.exec_())
