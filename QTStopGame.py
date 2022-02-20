import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from UIStopGame import Ui_Form


class Main(QMainWindow, Ui_Form):
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


# запуск
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.setObjectName("MainWindow")
    ex.setStyleSheet("#MainWindow{border-image:url(textures/background.jpg)}")
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
