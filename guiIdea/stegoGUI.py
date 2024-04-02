# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stegoGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stego(object):
    def setupUi(self, Stego):
        Stego.setObjectName("Stego")
        Stego.resize(773, 567)
        Stego.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Stego)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 80, 691, 431))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.Encrypt = QtWidgets.QWidget()
        self.Encrypt.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Encrypt.setObjectName("Encrypt")
        self.textEdit = QtWidgets.QTextEdit(self.Encrypt)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 501, 61))
        self.textEdit.setObjectName("textEdit")
        self.graphicsView = QtWidgets.QGraphicsView(self.Encrypt)
        self.graphicsView.setGeometry(QtCore.QRect(140, 140, 256, 221))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.Encrypt)
        self.pushButton.setGeometry(QtCore.QRect(560, 220, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Encrypt)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 60, 101, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.Encrypt, "")
        self.Decrypt = QtWidgets.QWidget()
        self.Decrypt.setObjectName("Decrypt")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.Decrypt)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 60, 256, 221))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Decrypt)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 20, 101, 23))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.Decrypt)
        self.label_2.setGeometry(QtCore.QRect(360, 60, 241, 101))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.Decrypt, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 20, 41, 41))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        Stego.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Stego)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Stego.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Stego)
        self.statusbar.setObjectName("statusbar")
        Stego.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Stego)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Stego)

    def retranslateUi(self, Stego):
        _translate = QtCore.QCoreApplication.translate
        Stego.setWindowTitle(_translate("Stego", "MainWindow"))
        self.textEdit.setHtml(_translate("Stego", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter message..</p></body></html>"))
        self.pushButton.setText(_translate("Stego", "Save"))
        self.pushButton_2.setText(_translate("Stego", "Choose file.."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Encrypt), _translate("Stego", "Tab 1"))
        self.pushButton_3.setText(_translate("Stego", "Choose file.."))
        self.label_2.setText(_translate("Stego", "Hidden message:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Decrypt), _translate("Stego", "Tab 2"))
        self.label.setText(_translate("Stego", "Stego"))
        self.menuHelp.setTitle(_translate("Stego", "Help"))