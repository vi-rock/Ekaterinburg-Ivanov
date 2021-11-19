import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.circle_size = (10, 10)
        uic.loadUi('des.ui', self)
        self.pushButton.clicked.connect(self.random_size)
        self.setWindowTitle('Yellow')

    def random_size(self):
        n = random.randint(10, 100)
        self.circle_size = (n, n)
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setBrush(QColor(255, 255, 0))
        p.begin(self)
        p.drawEllipse(130, 50, *self.circle_size)
        p.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec())
