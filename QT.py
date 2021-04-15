import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def testapp():
    app = QApplication(sys.argv)
    w1 = QMainWindow() 

    w1.setWindowTitle("Test")
    w1.setGeometry(150,250,400,400)
    w1.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    testapp()
#Тестовое изменен