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
        Stego.setStyleSheet("background-color:rgb(229, 186, 248);")
        self.centralwidget = QtWidgets.QWidget(Stego)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 80, 691, 431))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.tabWidget.setStyleSheet("background-color: #C19CD1;\n"
"font: 15px;\n"
"color: #443e3d;\n"
"border: #C19CD1;\n"
"QTabBar::tab {\n"
"       background-color: #C19CD1; \n"
"   }")
        self.tabWidget.setObjectName("tabWidget")
        self.Encrypt = QtWidgets.QWidget()
        self.Encrypt.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Encrypt.setObjectName("Encrypt")
        self.userTextToInsert = QtWidgets.QTextEdit(self.Encrypt)
        self.userTextToInsert.setGeometry(QtCore.QRect(20, 40, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.userTextToInsert.setFont(font)
        self.userTextToInsert.setStyleSheet("background-color:rgb(rgb(245, 232, 254));")
        self.userTextToInsert.setMarkdown("")
        self.userTextToInsert.setObjectName("userTextToInsert")
        self.saveEncryption = QtWidgets.QPushButton(self.Encrypt)
        self.saveEncryption.setGeometry(QtCore.QRect(560, 220, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.saveEncryption.setFont(font)
        self.saveEncryption.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.saveEncryption.setStyleSheet("background-color: rgb(241, 206, 249);")
        self.saveEncryption.setObjectName("saveEncryption")
        self.fileChooserTab1 = QtWidgets.QPushButton(self.Encrypt)
        self.fileChooserTab1.setGeometry(QtCore.QRect(540, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fileChooserTab1.setFont(font)
        self.fileChooserTab1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.fileChooserTab1.setStyleSheet("background-color: rgb(241, 206, 249);")
        self.fileChooserTab1.setObjectName("fileChooserTab1")
        self.imageTab1 = QtWidgets.QLabel(self.Encrypt)
        self.imageTab1.setGeometry(QtCore.QRect(80, 160, 381, 161))
        self.imageTab1.setText("")
        self.imageTab1.setObjectName("imageTab1")
        self.tabWidget.addTab(self.Encrypt, "")
        self.Decrypt = QtWidgets.QWidget()
        self.Decrypt.setObjectName("Decrypt")
        self.fileChooserTab2 = QtWidgets.QPushButton(self.Decrypt)
        self.fileChooserTab2.setGeometry(QtCore.QRect(40, 20, 121, 23))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fileChooserTab2.setFont(font)
        self.fileChooserTab2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.fileChooserTab2.setStyleSheet("background-color: rgb(241, 206, 249);")
        self.fileChooserTab2.setObjectName("fileChooserTab2")
        self.label_2 = QtWidgets.QLabel(self.Decrypt)
        self.label_2.setGeometry(QtCore.QRect(360, 60, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.imageTab2 = QtWidgets.QLabel(self.Decrypt)
        self.imageTab2.setGeometry(QtCore.QRect(40, 60, 281, 181))
        self.imageTab2.setText("")
        self.imageTab2.setObjectName("imageTab2")
        self.decryptedText = QtWidgets.QLabel(self.Decrypt)
        self.decryptedText.setGeometry(QtCore.QRect(360, 80, 241, 141))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.decryptedText.setFont(font)
        self.decryptedText.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.decryptedText.setStyleSheet("background-color:rgb(rgb(245, 232, 254));")
        self.decryptedText.setText("")
        self.decryptedText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.decryptedText.setObjectName("decryptedText")
        self.tabWidget.addTab(self.Decrypt, "")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(100, 20, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setAcceptDrops(False)
        self.Title.setStyleSheet("font: 25px;\n"
" color: #443e3d;")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
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
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Stego)

    def retranslateUi(self, Stego):
        _translate = QtCore.QCoreApplication.translate
        Stego.setWindowTitle(_translate("Stego", "Stego"))
        self.userTextToInsert.setHtml(_translate("Stego", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Eras Medium ITC\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.userTextToInsert.setPlaceholderText(_translate("Stego", "Enter message..."))
        self.saveEncryption.setText(_translate("Stego", "Save"))
        self.fileChooserTab1.setText(_translate("Stego", "Choose file.."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Encrypt), _translate("Stego", "Encrypt"))
        self.fileChooserTab2.setText(_translate("Stego", "Choose file.."))
        self.label_2.setText(_translate("Stego", "Hidden message:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Decrypt), _translate("Stego", "Decrypt"))
        self.Title.setText(_translate("Stego", "Stego"))
        self.menuHelp.setTitle(_translate("Stego", "Help"))
