from PyQt5 import QtWidgets, QtGui, QtCore
from qlabel import Ui_MainWindow
import sys


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.label.setFont(
            QtGui.QFont('Roboto', 30)
        ) # Изменение шрифта и размера
        self.ui.label.setGeometry(
        QtCore.QRect(10, 10, 200, 200)
        ) # изменить геометрию ярлыка
        self.ui.label.setText("No-no-no")



app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())