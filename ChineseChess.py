from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from UI import UI
from Controller import Controller


class ChineseChess(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chinese chess')
        self.setWindowIcon(QIcon('img/icon.png'))
        self.setFixedSize(1025, 725)
        self.center()
        self.init_new_game()

    def init_new_game(self):
        self.Controller = Controller()
        self.Controller.main_window = self
        UI(self, controller=self.Controller)
        self.show()

    # make the window on the center of the screen
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ChineseChess = ChineseChess()
    sys.exit(app.exec_())
