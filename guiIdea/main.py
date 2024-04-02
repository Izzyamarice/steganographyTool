#Type designer from cmd to open the command prompt
#Type pyuic5 stegoGUI.ui -o stegoGUI.py to create the python file whenever the ui changes

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QFileDialog
from PyQt5.QtGui import QPixmap
import sys
import stegoGUI

class stego(QtWidgets.QMainWindow, stegoGUI.Ui_Stego):
    def __init__(self, parent=None):
        super(stego, self).__init__(parent)
        self.setupUi(self)

        self.fileChooserTab1.clicked.connect(lambda:self.fileChooser(1))
        self.fileChooserTab2.clicked.connect(lambda:self.fileChooser(2))

    def fileChooser(self,tab):
        fname = self.getFile()
        if(tab == 1):
            self.imageTab1.setPixmap(QPixmap(fname[0]))
        else:
            self.imageTab2.setPixmap(QPixmap(fname[0]))
        
    
    def getFile(self):
        return QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")


def main():
    app = QApplication(sys.argv)
    form = stego()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()