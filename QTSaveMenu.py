import sys

from PyQt5.QtWidgets import QMainWindow
from ui.UISaveMenu import Ui_Form
from CreationOfNewLevel import list_of_obj


# Создание главного стартового окна
class QTSaveM(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton2.clicked.connect(self.saveName)
        self.name = None

    def save_level(self, fname):
        sp = []
        with open('data/levels.txt', encoding="utf8") as f:
            s = f.read()
            for i in s:
                sp.append(i)
        with open('data/levels.txt', encoding="utf8", mode="w") as f:
            for i in sp:
                f.write(i)
            f.write("\n")
            f.write(fname + ".txt")
        if list_of_obj:
            e = open("levelList/" + fname + '.txt', encoding="utf8", mode="w")
            for i in list_of_obj:
                if i != "None":
                    e.write(str(i) + '\n')
            e.close()

    def saveName(self):
        self.save_level(self.lineEdit.text())
        self.hide()


# чтобы видеть ошибки
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
