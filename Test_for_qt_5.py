import sys
import first_window
import double_window

from PyQt5 import QtCore, QtGui, QtWidgets

class TwoWindow(QtWidgets.QMainWindow, double_window.Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            #self.pushButton.clicked.connect(self.check2)

        

class OneWindow(QtWidgets.QMainWindow, first_window.Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.twoWindow = None
        self.pushButton.clicked.connect(self.check)

    def check(self):
        #print (5)
        self.close()
        self.twoWindow = TwoWindow()
        self.twoWindow.show()
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = OneWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()