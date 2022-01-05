import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtCore import QFile
from w_base import Ui_w_main
from сeh_ui import Ui_w_ceh

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w_main = QtWidgets.QMainWindow()
	ui = Ui_w_main()
	ui.setupUi(w_main)
	w_main.showMaximized()

def opn_w():
	global w_ceh
	w_ceh = QtWidgets.QMainWindow()
	ui = Ui_w_ceh()
	ui.setupUi(w_ceh)
	w_main.hide()
	w_ceh.show()
	

ui.PushButton_test.clicked.connect(opn_w)

sys.exit(app.exec_())