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
            self.imageTab2.setPixmap(QPixmap(fname[0]))
            self._fileTab = fname[0]
        
    #Returns the file that the user has selected
    def getFile(self):
        return QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.png)")
    
    #Initiates the saving of the encrypted file
    def saveEncryptedFile(self):
        self.encryptImage()

    #Encrypts the selected image by calling the stego file
    def encryptImage(self):
        #If the user hasn't entered a message yet then don't save the file        
        if(self.userTextToInsert.toPlainText() == ''):
            print("No message entered, file not saved")
        else:
            se.encode(self._fileTab1,self.userTextToInsert.toPlainText())

    #Decrypts the selected image by calling the stego file
    def decryptImage(self):
        se.decode(self._fileTab2)

        


def main():
    app = QApplication(sys.argv)
    form = stego()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()