from random import randrange
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.zachem)
        self.krug = False

    def zachem(self):
        self.krug = True
        self.update()

    def paintEvent(self, event):
        if self.krug:
            qp = QPainter()
            qp.begin(self)
            rad = randrange(1, 301)
            x, y = randrange(1, 401), randrange(1, 401)
            qp.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
            qp.drawEllipse(x, y, rad, rad)
            qp.end()
            self.krug = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())