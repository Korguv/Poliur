import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtCore import QFile
from test_UI import Ui_base_window
from сeh_Ui import Ui_ceh_window


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_base_window()
        self.ui.setupUi(self)
    
    def clicked_1(self):
        self.PushButton.hide() # Скрыть интерфейс 1
        self.PushButton.show() # Интерфейс дисплея 2
        

"""class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        self.ui = Ui_CehWindow()
        self.ui.setupUi(self)
"""
   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    

