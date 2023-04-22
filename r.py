from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont
class Mainwin(QWidget):
    def __init__(self): 
        super().__init__()
        self.set_appear() 
        self.initUI() 
        self.connects() 
        self.show()
    def initUI(self):
        self.btn_next=QPushButton('3')
        self.hello_text = QLabel('2')
        self.instructions = QLabel('1')
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft) 
        self.layout_line.addWidget(self.instructions, alignment = Qt.AlignLeft) 
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.hide()
        self.tw=RufieTest()
    def connects (self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear (self):
        self.setWindowTitle('4')
        self.resize(700, 700)
        self.move(0,0)
class RufieTest(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() 
        self.initUI() 
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle("Тест Руф'є")
        self.resize(900, 675)
        self.move(0,0)
    def initUI(self):
        self.name_label = QLabel('Введіть П.І.Б:', self)
        self.name_label.move(50, 50)
        self.name_input = QLineEdit(self)
        self.name_input.move(200, 50)
        
        self.age_label = QLabel('Повних років:', self)
        self.age_label.move(50, 100)
        self.age_input = QLineEdit(self)
        self.age_input.move(200, 100)
        
        self.first_test_label = QLabel('Лягте на спину, заміряйте пульс на 15 секунд. Натисніть кнопку "Почати перший тест", щоб запустити таймер', self)
        self.first_test_label.setGeometry(50, 150, 1000, 32)
        self.start_first_test_button = QPushButton('Почати перший тест', self)
        self.start_first_test_button.setGeometry(50, 200, 200, 32)


        self.first_test_input = QLineEdit(self)
        self.first_test_input.move(300, 200)
        
        self.second_test_label = QLabel('Виконайте 30 присідань', self)
        self.second_test_label.setGeometry(50, 250, 1000, 32)
        self.start_second_test_button = QPushButton('Почати робити присідання', self)
        self.start_second_test_button.setGeometry(50, 300, 220, 32)
        

        self.third_test_label = QLabel('Лягти на спину', self)
        self.third_test_label.setGeometry(50, 350, 900, 32)
        self.start_third_test_button = QPushButton('Почати фінальний тест', self)
        self.start_third_test_button.setGeometry(50, 400, 200, 32)


        self.third_test_input1 = QLineEdit(self)
        self.third_test_input1.move(50, 450)
        self.third_test_input2 = QLineEdit(self)
        self.third_test_input2.move(50, 500)
        
        self.send_result_button = QPushButton('Надіслати результат', self)
        self.send_result_button.setGeometry(370, 600, 190, 32)

        self.text_timer = QLabel(QTime(0, 0, 15).toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.move(700, 700)
    def timer_test(self):
        global time
        time = QTime(0, 0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000) 
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet ("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet ("color: rgb(0, 0, 0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
           self.timer.stop()
    def connects(self):
        self.start_first_test_button.clicked.connect(self.timer_test)
        self.start_second_test_button.clicked.connect(self.timer_sits)
        self.start_third_test_button.clicked.connect(self.timer_final)


app = QApplication([])
a = Mainwin()
app.exec_()
