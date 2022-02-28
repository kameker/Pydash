import sys

from PyQt5.QtWidgets import QMainWindow
from ui.UIStopGame import Ui_Form


class StopMenu(QMainWindow, Ui_Form):
    def __init__(self, popitka):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.StopGame)
        self.popitka = popitka
        self.label.setText(f"Вы прошли уровень за {self.popitka} попытки!")

    def StopGame(self):
        self.hide()


# чтобы видеть ошибки
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
