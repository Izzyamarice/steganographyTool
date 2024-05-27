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
        Stego.resize(1073, 756)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Stego.sizePolicy().hasHeightForWidth())
        Stego.setSizePolicy(sizePolicy)
        Stego.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Stego.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Stego.setMouseTracking(False)
        Stego.setStyleSheet("\n"
"background: rgb(237, 221, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Stego)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(60, 120, 961, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QWidget{\n"
"    background: rgb(229, 199, 255);\n"
"    font: 20px;\n"
"    color: #443e3d;\n"
"    margin: rgba(0,0,0,0);\n"
"    border:rgba(0,0,0,0);\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"QTabBar::tab{\n"
"        background:rgb(230, 187, 255);\n"
"        padding-right: 10px;\n"
"        padding-left: 10px;\n"
"        border-radius: 10px;\n"
"}\n"
"QTabBar::tab::selected{\n"
"        background:rgb(191, 134, 255);\n"
"        padding: 5px;\n"
"        padding-right: 10px;\n"
"        padding-left: 10px;\n"
"        border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Encrypt = QtWidgets.QWidget()
        self.Encrypt.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Encrypt.setObjectName("Encrypt")
        self.userTextToInsert = QtWidgets.QTextEdit(self.Encrypt)
        self.userTextToInsert.setGeometry(QtCore.QRect(40, 40, 561, 121))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.userTextToInsert.setFont(font)
        self.userTextToInsert.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.userTextToInsert.setStyleSheet("background-color: rgb(248, 239, 255);")
        self.userTextToInsert.setMarkdown("")
        self.userTextToInsert.setObjectName("userTextToInsert")
        self.saveEncryption = QtWidgets.QPushButton(self.Encrypt)
        self.saveEncryption.setGeometry(QtCore.QRect(740, 300, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.saveEncryption.setFont(font)
        self.saveEncryption.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.saveEncryption.setStyleSheet("background-color: rgb(248, 239, 255);\n"
"")
        self.saveEncryption.setObjectName("saveEncryption")
        self.fileChooserTab1 = QtWidgets.QPushButton(self.Encrypt)
        self.fileChooserTab1.setGeometry(QtCore.QRect(700, 80, 161, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileChooserTab1.sizePolicy().hasHeightForWidth())
        self.fileChooserTab1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fileChooserTab1.setFont(font)
        self.fileChooserTab1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.fileChooserTab1.setAutoFillBackground(False)
        self.fileChooserTab1.setStyleSheet("background-color: rgb(248, 239, 255);\n"
"")
        self.fileChooserTab1.setIconSize(QtCore.QSize(16, 16))
        self.fileChooserTab1.setAutoDefault(False)
        self.fileChooserTab1.setDefault(False)
        self.fileChooserTab1.setFlat(False)
        self.fileChooserTab1.setObjectName("fileChooserTab1")
        self.imageTab1 = QtWidgets.QLabel(self.Encrypt)
        self.imageTab1.setGeometry(QtCore.QRect(40, 200, 561, 301))
        self.imageTab1.setText("")
        self.imageTab1.setObjectName("imageTab1")
        self.tabWidget.addTab(self.Encrypt, "")
        self.Decrypt = QtWidgets.QWidget()
        self.Decrypt.setObjectName("Decrypt")
        self.fileChooserTab2 = QtWidgets.QPushButton(self.Decrypt)
        self.fileChooserTab2.setGeometry(QtCore.QRect(40, 40, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fileChooserTab2.setFont(font)
        self.fileChooserTab2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.fileChooserTab2.setStyleSheet("background-color: rgb(248, 239, 255);\n"
"")
        self.fileChooserTab2.setObjectName("fileChooserTab2")
        self.label_2 = QtWidgets.QLabel(self.Decrypt)
        self.label_2.setGeometry(QtCore.QRect(560, 40, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.imageTab2 = QtWidgets.QLabel(self.Decrypt)
        self.imageTab2.setGeometry(QtCore.QRect(40, 140, 381, 321))
        self.imageTab2.setStyleSheet("\n"
"")
        self.imageTab2.setText("")
        self.imageTab2.setObjectName("imageTab2")
        self.decryptedText = QtWidgets.QLabel(self.Decrypt)
        self.decryptedText.setGeometry(QtCore.QRect(560, 140, 321, 361))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.decryptedText.setFont(font)
        self.decryptedText.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.decryptedText.setStyleSheet("")
        self.decryptedText.setText("")
        self.decryptedText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.decryptedText.setWordWrap(True)
        self.decryptedText.setObjectName("decryptedText")
        self.tabWidget.addTab(self.Decrypt, "")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(300, 40, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setAcceptDrops(False)
        self.Title.setStyleSheet("font: 60px;\n"
" color: #443e3d;")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        Stego.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Stego)
        self.statusbar.setObjectName("statusbar")
        Stego.setStatusBar(self.statusbar)

        self.retranslateUi(Stego)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Stego)

    def retranslateUi(self, Stego):
        _translate = QtCore.QCoreApplication.translate
        Stego.setWindowTitle(_translate("Stego", "Stego"))
        self.userTextToInsert.setHtml(_translate("Stego", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Eras Medium ITC\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.userTextToInsert.setPlaceholderText(_translate("Stego", "Enter message..."))
        self.saveEncryption.setText(_translate("Stego", "Save"))
        self.fileChooserTab1.setText(_translate("Stego", "Choose file.."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Encrypt), _translate("Stego", "Encrypt"))
        self.fileChooserTab2.setText(_translate("Stego", "Choose file.."))
        self.label_2.setText(_translate("Stego", "Hidden message:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Decrypt), _translate("Stego", "Decrypt"))
        self.Title.setText(_translate("Stego", "Stego"))
