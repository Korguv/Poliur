from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from base_test_connect import Ui_main
import sys


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
        
        self.ui.table_in_moove.resizeColumnsToContents()
        self.ui.table_in_moove.horizontalHeader().resize
        #self.ui.tree_moove.header().resizeSection(0,150)
        self.ui.tree_moove.header().setSectionResizeMode(3)
        #QHeaderView::ResizeToContents


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())