from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit 
from PyQt5.QtGui import QFont, QDoubleValidator, QIntValidator
from instr import *
from final_win import *


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
#__________________________________________________________________________________________________
    def initUI(self):
        self.hintname_text = QLabel(txt_hintname)
        self.line_name = QLineEdit("П.I.Б.")
        self.hintage = QLabel(txt_hintage)
        self.line_age = QLineEdit('0')
       
        # тест 1
        self.test1 = QLabel(txt_test1)
        self.btn_starttest1 = QPushButton(txt_starttest1)
       
        # тест 2
        self.test2 = QLabel(txt_test2)
        self.btn_starttest2 = QPushButton(txt_starttest2)

        # тест 3
        self.test3 = QLabel(txt_test3)
        self.btn_starttest3 = QPushButton(txt_starttest3)
        self.line_tst31 = QLineEdit('0')
        self.line_tst32 = QLineEdit('0')

        # Надіслати результати
        self.btn_sendresults = QPushButton(txt_sendresults)


        #Таймер
        self.timer_txt = QLabel(timer_text)
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))


        #Лейаути

        self.hor_line = QHBoxLayout()
        self.rig_line = QVBoxLayout()
        self.lef_line = QVBoxLayout()        

        self.lef_line.addWidget(self.hintname_text, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.line_name, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.hintage, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.line_age, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.test1, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.btn_starttest1, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.test2, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.btn_starttest2, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.test3, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.btn_starttest3, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.line_tst31, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.line_tst32, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.btn_sendresults, alignment= Qt.AlignCenter)
        self.rig_line.addWidget(self.timer_txt, alignment= Qt.AlignRight)

        self.hor_line.addLayout(self.lef_line)
        self.hor_line.addLayout(self.rig_line)
        self.setLayout(self.hor_line )


#__________________________________________________________________________________________________

    def next_click(self):
        self.fw = FinalWin()
        self.hide()
    

    def set_appear(self):
        self.setWindowTitle("Здоров'я")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def timer_test(self):
        global time 
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer1Event)
        self.timer.start(1000)

    def Timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString("hh:mm:ss")) 
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))
        self.timer_txt.setStyleSheet("color: rgb(0,0,0)")    
        if time.toString("hh:mm:ss")  == "00:00:00":
            self.timer.stop()


    def timer_sits(self):
        global time 
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer2Event)
        self.timer.start(1500)        

    def Timer2Event(self):    
        global time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString("hh:mm:ss")[6:8])
        self.timer_txt.setStyleSheet("color: rgb(0,0,0)")
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time 
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer3Event)
        self.timer.start(1000) 
 
    def Timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8])>= 45:
            self.timer_txt.setStyleSheet("color: rgb(0,255,0)") 
        elif int(time.toString("hh:mm:ss")[6:8])<= 15:
            self.timer_txt.setStyleSheet("color: rgb(0,255,0)") 
        else:
            self.timer_txt.setStyleSheet("color: rgb(0,0,0)") 
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
           self.timer.stop()
    
    def connects(self):
        self.btn_sendresults.clicked.connect(self.next_click)
        self.btn_starttest1.clicked.connect(self.timer_test)
        self.btn_starttest2.clicked.connect(self.timer_sits)
        self.btn_starttest3.clicked.connect(self.timer_final)
