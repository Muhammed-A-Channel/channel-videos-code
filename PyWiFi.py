import wifimangement_linux

from PyQt5.QtWidgets import QMainWindow,QTextEdit,QPushButton,QApplication

import sys

class A(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1000,700)
        self.te=QTextEdit(self)

        self.te.setStyleSheet('background-color:yellow;color:black;font-size:18pt;border-radius:20px 20px;border-width:20px;border:yellow radius 20px;')
        self.te.setGeometry(100,50,800,500)


        self.btn1=QPushButton("Info List",self)
        self.btn1.setGeometry(890,630,100, 60)
        self.btn1.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')

        self.btn1.clicked.connect(self.click1)

        self.btn2 = QPushButton("Info IP", self)
        self.btn2.setGeometry(760,630,100, 60)
        self.btn2.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')

        self.btn2.clicked.connect(self.click2)

        self.btn3 = QPushButton("Clear", self)
        self.btn3.setGeometry(70, 630,100, 60)
        self.btn3.setStyleSheet(
            'background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')
        self.btn3.clicked.connect(self.clear)


        self.btn4 = QPushButton("Info Interface", self)
        self.btn4.setGeometry(610, 630,120, 60)
        self.btn4.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')

        self.btn4.clicked.connect(self.click3)

        self.btn5 = QPushButton("Info Interface_L", self)
        self.btn5.setGeometry(460, 630,120, 60)
        self.btn5.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:11pt;')

        self.btn5.clicked.connect(self.click4)

        self.btn6 = QPushButton("WiFi On", self)
        self.btn6.setGeometry(330, 630,100, 60)
        self.btn6.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')

        self.btn6.clicked.connect(self.click5)

        self.btn7 = QPushButton("WiFi Off", self)
        self.btn7.setGeometry(200, 630,100, 60)
        self.btn7.setStyleSheet('background-color:rgb(3, 5, 19);color:yellow;border-radius:20px 20px;border-width:20px;border:rgb(3, 5, 19) radius 20px;font-size:12pt;')

        self.btn7.clicked.connect(self.click6)




        self.show()


    def click1(self):

        a=wifimangement_linux.list()

        self.te.setText(a)



    def click2(self):



            b=wifimangement_linux.ip()
            self.te.setText(f'IP ==> {b}')


    def clear(self):
        self.te.clear()

    def click3(self):
        i=wifimangement_linux.interface_status()
        self.te.setText(i)

    def click4(self):
        i=wifimangement_linux.interface_list()
        self.te.setText(str(i))
    def click5(self):
        o=wifimangement_linux.on()

    def click6(self):
        off = wifimangement_linux.off()




app=QApplication(sys.argv)
w=A()
w.show()
sys.exit(app.exec_())
