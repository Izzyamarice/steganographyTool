#Type designer from cmd to open the command prompt
#Type pyuic5 stegoGUI.ui -o stegoGUI.py to create the python file whenever the ui changes

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import stegoGUI

class stego(QtWidgets.QMainWindow, stegoGUI.Ui_Stego):
    def __init__(self, parent=None):
        super(stego, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = stego()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()