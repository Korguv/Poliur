# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Admin_CPU\Desktop\Сode\1\Poliur\dialog_zayav.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_zayav(object):
    def setupUi(self, Dialog_zayav):
        Dialog_zayav.setObjectName("Dialog_zayav")
        Dialog_zayav.resize(275, 114)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_zayav)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtWidgets.QPushButton(Dialog_zayav)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_delete = QtWidgets.QPushButton(Dialog_zayav)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout.addWidget(self.pushButton_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog_zayav)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog_zayav)
        QtCore.QMetaObject.connectSlotsByName(Dialog_zayav)

    def retranslateUi(self, Dialog_zayav):
        _translate = QtCore.QCoreApplication.translate
        Dialog_zayav.setWindowTitle(_translate("Dialog_zayav", "Статус заявки"))
        self.pushButton_save.setText(_translate("Dialog_zayav", "Выполнено"))
        self.pushButton_delete.setText(_translate("Dialog_zayav", "Удалено"))
        self.pushButton_cancel.setText(_translate("Dialog_zayav", "Без изменений"))
