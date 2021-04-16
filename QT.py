import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Test")
        self.setGeometry(150,250,400,400)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Тестовая надпись")
        self.main_text.move(150,150)
        self.main_text.adjustSize

        self.main_tabel = QtWidgets.QTableWidget

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(90,50)
        self.btn.setText('Кнопка')
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.app_btn)
    def app_btn(self):
        self.new_text.setText('But dont giveup!')
        self.main_text.move(100,100)
        self.main_text.adjustSize
def testapp():
    app = QApplication(sys.argv)
    w1 = Window() 
    w1.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    testapp()
#Тестовое изменен