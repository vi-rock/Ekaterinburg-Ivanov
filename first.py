import sys
from random import randint as r

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from des import Ui_Form


class Main(QWidget, Ui_Form):
    def __init__(self):
        super(Main, self).__init__()
        self.circle_size = (10, 10)
        self.circle_color = (255, 255, 0)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.init_circle)
        self.setWindowTitle('Not Yellow')

    def init_circle(self):
        n = r(10, 100)
        self.circle_size = (n, n)
        self.circle_color = (r(0, 255), r(0, 255), r(0, 255))
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setBrush(QColor(*self.circle_color))
        p.begin(self)
        p.drawEllipse(130, 50, *self.circle_size)
        p.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec())
