# импорт библиотек
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.UIMainMenu import Ui_Form
from QTLevelMenu import QTLevelM
from SecondAssembly import StartCreation


# Создание главного стартового окна
class MainWindow(QMainWindow, Ui_Form):
    # инициальзация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setIcon(QIcon('textures/play_button.png'))
        self.pushButton.setIconSize(QSize(150, 200))
        self.NewLevelButton.setIcon(QIcon('textures/newlevelbutton.png'))
        self.NewLevelButton.setIconSize(QSize(150, 200))
        self.pushButton.clicked.connect(self.levelMenu)
        self.NewLevelButton.clicked.connect(self.NewLevel)

    def levelMenu(self):
        self.win = QTLevelM()
        self.win.setObjectName("MainWindow")
        self.win.setStyleSheet("#MainWindow{border-image:url(textures/background.jpg)}")
        self.win.show()
        ex.hide()

    def NewLevel(self):
        self.showMinimized()
        StartCreation()


# чтобы видеть ошибки
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# запуск
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setObjectName("MainWindow")
    ex.setStyleSheet("#MainWindow{border-image:url(textures/background.jpg)}")
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
