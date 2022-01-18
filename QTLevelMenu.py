# импорт библиотек
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.UILevelMenu import Ui_Form
from FirstAssembly import StartLevel


# Создание главного стартового окна
class QTLevelM(QMainWindow, Ui_Form):
    # инициальзация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.NameLevelLabel.setText("")
        self.pushButton_3.setText("Играть")
        self.LeftButton.setIcon(QIcon('textures/left120.png'))
        self.LeftButton.setIconSize(QSize(150, 200))
        self.LeftButton.clicked.connect(self.leftClick)
        self.RightButton.setIcon(QIcon('textures/right120.png'))
        self.RightButton.setIconSize(QSize(150, 200))
        self.RightButton.clicked.connect(self.rightClick)
        self.levelID = 0
        f = open('data/levels.txt', 'r')
        a = f.read()
        self.levels = a.split('\n')
        self.NameLevelLabel.setText(self.levels[self.levelID][:-4])
        self.pushButton_3.clicked.connect(self.startLevel)


    def leftClick(self):
        if self.levelID - 1 >= 0:
            self.levelID -= 1
            self.NameLevelLabel.setText(self.levels[self.levelID][:-4])

    def rightClick(self):
        if self.levelID + 1 <= len(self.levels) - 1:
            self.levelID += 1
            self.NameLevelLabel.setText(self.levels[self.levelID][:-4])

    def startLevel(self):
        StartLevel(self.levels[self.levelID], True)

# чтобы видеть ошибки
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# запуск
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QTLevelM()
    ex.setObjectName("MainWindow")
    ex.setStyleSheet("#MainWindow{border-image:url(textures/background.jpg)}")
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
