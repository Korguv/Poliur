import sys
from PyQt5.Qt import *


class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(300, 200))
        self.myarray = [
            [1, 2, 3, 4], 
            [1.1, 2.1, 3.1, 4.1], 
            [1.24568897565, 2.2, 3.2, 4.2], 
            [1.3, 2.3, 3.3, 4.]
        ]
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        self.tableWidget = QTableWidget()
        grid = QGridLayout(self.centralWidget)
        grid.addWidget(self.tableWidget) 
    
        line = len(self.myarray)
        column = len(self.myarray[0])
        self.tableWidget.setRowCount(line)
        self.tableWidget.setColumnCount(column)
        row_labels = ['A', '222popo', 'Hello World']
        self.tableWidget.setHorizontalHeaderLabels(row_labels) 

        for c, row in enumerate(self.myarray):
            for r, e in enumerate(row):
                item = QTableWidgetItem(str(e))
                self.tableWidget.setItem(r, c, item)

# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )