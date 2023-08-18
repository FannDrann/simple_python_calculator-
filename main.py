from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_Form
import sys

class CalculatorApp:
    def __init__(self, window):
        self.ui = Ui_Form()
        self.ui.setupUi(window)

        self.ui.button_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.button_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.button_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.button_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.button_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.button_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.button_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.button_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.button_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.button_9.clicked.connect(lambda: self.add_digit('9'))
        self.ui.button_clear.clicked.connect(self.clear_all)
        self.ui.button_idk_1.clicked.connect(self.clear)
        self.ui.button_point.clicked.connect(self.add_point)
        self.ui.pushButton.clicked.connect(self.theme)

        self.ui.button_plus.clicked.connect(lambda: self.temp('+'))
        self.ui.button_product.clicked.connect(lambda: self.temp('*'))
        self.ui.button_devide.clicked.connect(lambda: self.temp('/'))
        self.ui.button_minus.clicked.connect(lambda: self.temp('-'))
        self.ui.button_result.clicked.connect(self.calculate)
        self.operation = None

    temps = []
    label_temps = []

    def theme(self):
        pass

    def add_digit(self, button_text: str):
        if self.ui.lineEdit.text() == '0':
            self.ui.lineEdit.setText(button_text)
        else:
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + button_text)

    def clear_all(self):
        self.temps = []
        self.label_temps = []
        self.ui.lineEdit.setText('0')
        self.ui.label.clear()
        self.operation = None

    def clear(self):
        self.ui.lineEdit.setText('0')

    def add_point(self):
        if '.' not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')

    def temp(self, sign):
        if not self.ui.label.text():
            self.ui.label.setText(self.ui.lineEdit.text() + f'{sign} ')
            self.label_temps.append(self.ui.lineEdit.text())
            self.label_temps.append(sign)
            self.temps.append(float(self.ui.lineEdit.text()))

            self.ui.lineEdit.setText('0')
        else:
            self.label_temps = []
            self.temps = []
            self.label_temps.append(self.ui.lineEdit.text())
            self.label_temps.append(sign)
            self.temps.append(float(self.ui.lineEdit.text()))
            self.ui.lineEdit.setText('0')
        self.operation = sign
            
    def calculate(self):
        if self.operation == '+':
            self.temps.append(float(self.ui.lineEdit.text()))
            self.label_temps.append(self.ui.lineEdit.text())
            answer = sum(self.temps)
        elif self.operation == '*':
            self.temps.append(float(self.ui.lineEdit.text()))
            self.label_temps.append(self.ui.lineEdit.text())
            answer = self.temps[0] * self.temps[1]
        elif self.operation == '/':
            self.temps.append(float(self.ui.lineEdit.text()))
            self.label_temps.append(self.ui.lineEdit.text())
            answer = self.temps[0] / self.temps[1]
        elif self.operation == '-':
            self.temps.append(float(self.ui.lineEdit.text()))
            self.label_temps.append(self.ui.lineEdit.text())
            answer = self.temps[0] - self.temps[1]
        else:
            answer = float(self.ui.lineEdit.text())

        self.ui.label.setText(' '.join(self.label_temps) + ' =')
        if answer % 1 == 0:
            self.ui.lineEdit.setText(str(round(answer)))
        else:
            self.ui.lineEdit.setText(str(round(answer, 100)))
        
        self.temps = []
        self.label_temps = []



def run():
    app = QApplication(sys.argv)
    window = QMainWindow()

    calculator = CalculatorApp(window)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
