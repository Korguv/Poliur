   
        #we have connected clicked signal of button with the selec_data method
        self.pushButton.clicked.connect(self.select_data)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
 
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
    #this is the method for selecting data
    def select_data(self):
        try:
            dbname = self.lineEditDb.text()
            tablename = self.lineEditTable.text()
            mydb = mc.connect(
 
                host="localhost",
                user="root",
                password="",
                database=dbname
            )
 
            mycursor = mydb.cursor()
 
            mycursor.execute("SELECT * FROM {} ".format(tablename))
 
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                print(row_number)
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
 
 
 
        except mc.Error as e:
            print("Error")
 
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Enter Db Name:"))
        self.label_2.setText(_translate("Form", "Enter Table Name:"))
        self.pushButton.setText(_translate("Form", "Show Data"))
 
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


    #https://codeloop.org/pyqt5-tutorial-retrieve-data-from-mysql-in-qtablewidget/#more-5279