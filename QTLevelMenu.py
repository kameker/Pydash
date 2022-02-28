# импорт библиотек
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from ui.UILevelMenu import Ui_Form
from FirstAssembly import StartLevel
from QTStopGame import StopMenu
from Square import player


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
        self.win = StopMenu(player.deaths)

    def leftClick(self):
        f = open('data/levels.txt', 'r')
        a = f.read()
        self.levels = a.split('\n')
        if self.levelID - 1 >= 0:
            self.levelID -= 1
            self.NameLevelLabel.setText(self.levels[self.levelID][:-4])

    def rightClick(self):
        f = open('data/levels.txt', 'r')
        a = f.read()
        self.levels = a.split('\n')
        if self.levelID + 1 <= len(self.levels) - 1:
            self.levelID += 1
            self.NameLevelLabel.setText(self.levels[self.levelID][:-4])

    def startLevel(self):
        self.showMinimized()
        StartLevel(self.levels[self.levelID], True)
        self.hide()
        self.win = StopMenu(player.deaths)
        self.win.show()
        player.deaths = 1





# чтобы видеть ошибки
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
