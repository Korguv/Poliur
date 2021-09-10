import sys
import socket
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
#import source


class Ui_ChatWindow(object):
    def setupUi(self, ChatWindow):
        ChatWindow.setObjectName("ChatWindow")
        ChatWindow.setEnabled(True)
        ChatWindow.resize(319, 480)
        self.centralwidget = QtWidgets.QWidget(ChatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 321, 480))
        self.background.setAutoFillBackground(False)
#        self.background.setStyleSheet("image: url(:/newPrefix/чат с кнопкой.png);")
        self.background.setStyleSheet("image: url(im.png);")
        
        self.background.setText("")
        self.background.setWordWrap(False)
        self.background.setIndent(1)
        self.background.setObjectName("background")
        self.input_msg = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_msg.setGeometry(QtCore.QRect(7, 414, 249, 54))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_msg.setFont(font)
#        self.input_msg.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""border: 2px green;")
        self.input_msg.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_msg.setCenterOnScroll(False)
        self.input_msg.setObjectName("input_msg")
        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send.setGeometry(QtCore.QRect(263, 416, 51, 51))
        self.btn_send.setMouseTracking(False)
#        self.btn_send.setStyleSheet("image: url(:/newPrefix/кнопка отправить.png);\n""background-color: rgba(255, 255, 255, 0);")
        self.btn_send.setText("")
        self.btn_send.setObjectName("btn_send")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(7, 15, 306, 390))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.plainTextEdit_2.setFont(font)
#        self.plainTextEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""border: 2px green;")
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setOverwriteMode(False)
        self.plainTextEdit_2.setBackgroundVisible(False)
        self.plainTextEdit_2.setCenterOnScroll(False)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        ChatWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChatWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatWindow)

    def retranslateUi(self, ChatWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatWindow.setWindowTitle(_translate("ChatWindow", "Чат"))


class Ui_AuthWindow(object):
    def setupUi(self, AuthWindow):
        AuthWindow.setObjectName("AuthWindow")
        AuthWindow.setEnabled(True)
        AuthWindow.resize(319, 480)
        self.centralwidget = QtWidgets.QWidget(AuthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 321, 480))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("image: url(:/newPrefix/Auth.png);")
        self.background.setText("Label background")
        self.background.setIndent(1)
        self.background.setObjectName("background")
        self.btn_connect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connect.setGeometry(QtCore.QRect(4, 301, 311, 41))
        self.btn_connect.setMouseTracking(False)
#        self.btn_connect.setStyleSheet("image: url(:/newPrefix/кнопка.png);\n""background-color: rgba(255, 255, 255, 0);")
        self.btn_connect.setStyleSheet(
            "image: url(Ok.png); background-color: rgba(255, 255, 255, 0);")

        self.btn_connect.setText("")
        self.btn_connect.setObjectName("btn_connect")
#        self.btn_connect.clicked.connect(self.add_label)

        self.input_nick = QtWidgets.QLineEdit(self.centralwidget)
        self.input_nick.setGeometry(QtCore.QRect(7, 207, 306, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_nick.setFont(font)
#        self.input_nick.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""border: 2px green;")
        self.input_nick.setMaxLength(18)
        self.input_nick.setObjectName("input_nick")
        
        self.input_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ip.setGeometry(QtCore.QRect(7, 269, 186, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_ip.setFont(font)
#        self.input_ip.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""border: 2px green;")
        self.input_ip.setMaxLength(15)
        self.input_ip.setObjectName("input_ip")
        
        self.input_port = QtWidgets.QLineEdit(self.centralwidget)
        self.input_port.setGeometry(QtCore.QRect(201, 269, 112, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_port.setFont(font)
#        self.input_port.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n""border: 2px green;")
        self.input_port.setMaxLength(5)
        self.input_port.setObjectName("input_port")
        
        AuthWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)

    def retranslateUi(self, AuthWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "Авторизация"))
        

class ChatWindow(QtWidgets.QMainWindow, Ui_ChatWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   

        # тут какая-то логика        
            

class MainWindow(QtWidgets.QMainWindow, Ui_AuthWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.input_nick.setPlaceholderText('input_nick')
        self.input_ip.setPlaceholderText('input_ip')
        self.input_port.setPlaceholderText('port')

        self.btn_connect.clicked.connect(self.add_label)   

        self.chatWindow = ChatWindow() 
        
        # тут какая-то логика
        

    def add_label(self):
#        global nickname, ip, port

        nickname = self.input_nick.text()
        ip = self.input_ip.text()
        port = int(self.input_port.text())
        
        if not nickname or not ip or not port:
            msg = QtWidgets.QMessageBox.information(self, 'Внимание', 'Заполните поля ввода.')   
            return            
            
        self.chatWindow.show()
       
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        self.client.connect((ip, port))

'''        
        def receive():
            while True:
                try:
                    message = client.recv(1024).decode('UTF-8')
                    if message == 'NICK':
                        client.send(nickname.encode('UTF-8'))
                    else:
                        print(message)
                except:
                    print("An error occured!")
                    client.close()
                    break
                    
        def write():
            while True:
                message = f'{nickname}: {input("")}'
                client.send(message.encode('UTF-8'))

        receive_thread = threading.Thread(target=receive)
        receive_thread.start()
        write_thread = threading.Thread(target=write)
        write_thread.start()
'''

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
#    AuthWindow = QtWidgets.QMainWindow()
#    ui = Ui_AuthWindow()
#    ui.setupUi(AuthWindow)
#    AuthWindow.show()
    w = MainWindow()  
    w.show()
    
    sys.exit(app.exec_())