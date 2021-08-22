# Coded by OneParsec
# PySpeedTest main code
# Importing
import os
import sys
import speedtest
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from os.path import expanduser
from PyQt5.QtGui import QIcon
from design import Ui_MainWindow

# Variables
version = "1.0"

# Executable code
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage("Version: " + version + "                                                 Window can be not responding, while testing. Don't close it!")
        self.ui.pushButton.clicked.connect(self.startTest)
    def startTest(self):

        s = speedtest.Speedtest()
        s.get_servers()
        best = s.get_best_server()
        self.ui.lcdNumber.display(best["latency"])
        self.ui.lcdNumber_2.display(s.download() / 1000000)
        self.ui.lcdNumber_3.display(s.upload() / 1000000)
        self.ui.statusbar.showMessage("Thanks for using PySpeedTest!")
    



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    application.setWindowTitle("PySpeedTest")
    app.exec()