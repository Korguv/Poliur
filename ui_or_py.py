from PyQt5 import QtWidgets, uic
import sys
 
app = QtWidgets.QApplication([])
win = uic.loadUi("mydesign.ui") # расположение вашего файла .ui

win.show()
sys.exit(app.exec())




from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())