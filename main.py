import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtCore import QFile
from test_UI import Ui_MainWindow
from ceh_ui import


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        self.ui = ui_cehwindow()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    

