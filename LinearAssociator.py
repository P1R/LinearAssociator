#!/usr/bin/env   python2.7
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created: Tue Mar  4 10:03:33 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Str2Bin as s2b
import numpy as np


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def __init__(self):
        self.L=0
        self.Matrix=[[]]
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(808, 306)
        Form.setMinimumSize(QtCore.QSize(808, 306))
        Form.setMaximumSize(QtCore.QSize(808, 306))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 270, 256, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 788, 249))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.tableWidget = QtGui.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.codifica)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.decodifica)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit_2.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tableWidget.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "LinearAssociator", None))
        self.pushButton_3.setText(_translate("Form", "Limpiar", None))
        self.label.setText(_translate("Form", "Mensaje:", None))
        self.pushButton.setText(_translate("Form", "Codificar", None))
        self.label_3.setText(_translate("Form", "Mensaje Cifrado:", None))
        self.label_2.setText(_translate("Form", "Mensaje Recuperado:", None))
        self.pushButton_2.setText(_translate("Form", "Recuperar", None))
    def codifica(self):
	###se lee texto, se codifica a binario con libreria Str2Bin
	Message=str(_fromUtf8(self.textEdit.toPlainText()))
	self.L = len(Message)
	BinMessage=s2b.Str2Bin(Message)
        self.Matrix=BinMessage
	###se agrega a objeto numpy como arreglo y se aplica transpuesta
	n = np.array(BinMessage)
	ns = np.transpose(n)
	self.tableWidget.setColumnCount(self.L)
        self.tableWidget.setRowCount(7)
	print ns
        for i in range(7):
            for j in range(self.L):
                self.tableWidget.setItem(i,j,QtGui.QTableWidgetItem("%d" % int(ns[i][j])))
    def decodifica(self):
        print self.Matrix
        Message=''
        for i in range(self.L):
            Message+=s2b.Bin2Str(self.Matrix[i])
	self.textEdit_2.setText(Message)
if __name__ == "__main__":
    import sys;
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

