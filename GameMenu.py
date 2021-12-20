# импорт библиотек
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from game_menu import Ui_Form


# Создание главного стартового окна
class Main(QMainWindow, Ui_Form):
    # инициальзация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.levels_button.clicked.connect(self.open_levels)
        self.registration.clicked.connect(self.open_registration)
        self.creation_new_levels.clicked.connect(self.open_creation_new_levels)

    # открытие окна с заданиями
    def open_level(self):
        pass
        # открытие qt окна с уровнями

    def open_registration(self):
        pass
        # открытие окна qt с регистрацией и статистикой

    def open_creation_new_level(self):
        pass
        # открытие pygame окна с созданием уровней


# чтобы видеть ошибки
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# запуск
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    #ex.setObjectName("MainWindow")
    #ex.setStyleSheet("#MainWindow{border-image:url(image.jpg)}")
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
