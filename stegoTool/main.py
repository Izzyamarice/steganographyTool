#Type designer from cmd to open the command prompt
#Type pyuic5 stegoGUI.ui -o stegoGUI.py to create the python file whenever the ui changes

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import sys
import stegoGUI
import stegoExecution as se

class stego(QtWidgets.QMainWindow, stegoGUI.Ui_Stego):
    def __init__(self, parent=None):
        self._fileTab1 = None
        self._fileTab2 = None


        super(stego, self).__init__(parent)
        self.setupUi(self)

        #Methods for when the different buttons are clicked
        self.fileChooserTab1.clicked.connect(lambda:self.fileChooser(1))
        self.fileChooserTab2.clicked.connect(lambda:self.fileChooser(2))
        self.saveEncryption.clicked.connect(self.saveEncryptedFile)


    #Determines which tab to set the chosen image to
    #Also saves the filepath so it can be used to encrypt/decrypt the image
    def fileChooser(self,tab):
        fname = self.getFile()
        if(tab == 1):
            self.imageTab1.setPixmap(QPixmap(fname[0]))
            self._fileTab1 = fname[0]
        else:
            #If we are setting it to the second tab then we should try to decode the image
            #Immediately when the image loads
            self.imageTab2.setPixmap(QPixmap(fname[0]))
            self._fileTab2 = fname[0]
            self.loadEncryptedFile()
        
    #Returns the file that the user has selected
    def getFile(self):
        return QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.png)")
    
    #Initiates the saving of the encrypted file
    def saveEncryptedFile(self):
        self.encryptImage()
        #the file gets saved automatically in the stegoExecution file, so no need to do it here

    #Loads the encrypted message for the picture in tab 2
    def loadEncryptedFile(self):
        message = self.decryptImage()
        if(message != None):
            #we will put the messasge in the label
            self.decryptedText.setText(message)
        else:
            #we will put "No message found in the supplied image"
            self.decryptedText.setText("No message found in the supplied image")

    #Encrypts the selected image by calling the stego file
    def encryptImage(self):
        #If the user hasn't entered a message yet then don't save the file        
        if(self.userTextToInsert.toPlainText() == ''):
            print("No message entered, file not saved")
        else:
            se.encode(self._fileTab1,self.userTextToInsert.toPlainText())

    #Decrypts the selected image by calling the stego file
    def decryptImage(self):
        return se.decode(self._fileTab2)

def settingStyle(app):
    app.setStyleSheet("QMainWindow { background-color: purple }")

def main():
    app = QApplication(sys.argv)
    settingStyle(app)
    form = stego()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()