# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\GitHub\Poliur\Ui\dialog\worker.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_d_worker(object):
    def setupUi(self, d_worker):
        d_worker.setObjectName("d_worker")
        d_worker.resize(906, 607)
        self.horizontalLayout = QtWidgets.QHBoxLayout(d_worker)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table = QtWidgets.QTableWidget(d_worker)
        self.table.setObjectName("table")
        self.table.setColumnCount(8)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        self.horizontalLayout.addWidget(self.table)
        self.layout_menu = QtWidgets.QVBoxLayout()
        self.layout_menu.setObjectName("layout_menu")
        self.pushbutton_plus_menu = QtWidgets.QPushButton(d_worker)
        self.pushbutton_plus_menu.setObjectName("pushbutton_plus_menu")
        self.layout_menu.addWidget(self.pushbutton_plus_menu)
        self.pushbutton_delete_menu = QtWidgets.QPushButton(d_worker)
        self.pushbutton_delete_menu.setObjectName("pushbutton_delete_menu")
        self.layout_menu.addWidget(self.pushbutton_delete_menu)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_menu.addItem(spacerItem)
        self.pushbutton_end_menu = QtWidgets.QPushButton(d_worker)
        self.pushbutton_end_menu.setObjectName("pushbutton_end_menu")
        self.layout_menu.addWidget(self.pushbutton_end_menu)
        self.horizontalLayout.addLayout(self.layout_menu)

        self.retranslateUi(d_worker)
        QtCore.QMetaObject.connectSlotsByName(d_worker)

    def retranslateUi(self, d_worker):
        _translate = QtCore.QCoreApplication.translate
        d_worker.setWindowTitle(_translate("d_worker", "Список сотрудников"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("d_worker", "ФИО"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("d_worker", "Должность"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("d_worker", "Телефон"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("d_worker", "Почта"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("d_worker", "Пометки"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("d_worker", "Документы"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("d_worker", "Оклад"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("d_worker", "Премия"))
        self.pushbutton_plus_menu.setText(_translate("d_worker", "Добавить"))
        self.pushbutton_delete_menu.setText(_translate("d_worker", "Удалить"))
        self.pushbutton_end_menu.setText(_translate("d_worker", "Закрыть"))
