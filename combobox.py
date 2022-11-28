from PyQt5.QtWidgets import QTableWidgetItem
from qtable import *
import sys

data = ['Python', 'PHP', 'Java']


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(2)

        row = 0
        for item in data:
            cellinfo = QTableWidgetItem(item)

            combo = QtWidgets.QComboBox()
            combo.addItem("Изучить")
            combo.addItem("Забыть")
            combo.addItem("Удалить")

            self.ui.tableWidget.setItem(row, 0, cellinfo)
            self.ui.tableWidget.setCellWidget(row, 1, combo)
            row += 1


app = QtWidgets.QApplication([])
win = mywindow()
win.show()

sys.exit(app.exec())