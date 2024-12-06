import sys
import random

from PyQt6.QtCore import QPoint, Qt, QTimer
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.circles = []  # Список для хранения окружностей

        self.btn.setText('Нарисовать')
        self.btn.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.circles.append((random.randint(100, 500), random.randint(100, 500),
                            random.randint(1, 100)))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        # Задаем кисть
        painter.setBrush(QColor(255, 255, 0))
        # Рисуем круги заданной кистью
        for el in self.circles:
            painter.drawEllipse(QPoint(el[0], el[1]), el[2], el[2])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
