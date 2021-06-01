import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)
        self.sec = SecondWindow()
        self.pushButton.clicked.connect(self.on_click)
        self.sec.login_data[str,str].connect(self.handle_input)
 
    def on_click(self):
        self.sec.show()
 
    def handle_input(self, name, login):
        self.label.setText(name)
        self.label_2.setText(login)
        
 
class SecondWindow(QMainWindow):
    login_data = pyqtSignal(str, str)
 
    def __init__(self):
        super().__init__()
        uic.loadUi("second_window.ui", self)
        self.pushButton.clicked.connect(self.send_data)
 
    def send_data(self):
        self.login_data.emit(self.lineEdit.text(), self.lineEdit_2.text())
        self.close()
    
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())