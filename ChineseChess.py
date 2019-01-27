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
        self.tboard = None
        self.center()
        self.init_new_game()
        self.show()

    def init_new_game(self, first=True, board_name='default'):
        board = self.get_board(board_name=board_name)
        self.Controller = Controller(board=board)
        self.Controller.main_window = self
        self.tboard = UI(self, first=first, controller=self.Controller, start=self)
        self.setCentralWidget(self.tboard)
        self.Controller.new_game(first=first)

    def get_board(self, board_name=None):
        if board_name == 'test':
            board = [[0, 0, 0, 0, 0, 0, 0, 0, 'uk0'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 'up0', 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 'dz0'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 'dp0', 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['dj0', 'dm0', 0, 0, 0, 0, 0, 0, 'dk0']]
            return board
        if board_name == 'default':
            board = [['uj0', 'um0', 'ux0', 'us0', 'uk0', 'us1', 'ux1', 'um1', 'uj1'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 'up0', 0, 0, 0, 0, 0, 'up1', 0],
                     ['uz0', 0, 'uz1', 0, 'uz2', 0, 'uz3', 0, 'uz4'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['dz0', 0, 'dz1', 0, 'dz2', 0, 'dz3', 0, 'dz4'],
                     [0, 'dp0', 0, 0, 0, 0, 0, 'dp1', 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['dj0', 'dm0', 'dx0', 'ds0', 'dk0', 'ds1', 'dx1', 'dm1', 'dj1']]
            return board
        # qi xing ju hui
        if board_name == 'Endgame1':
            board = [[0, 0, 0, 0, 'uj0', 'uk0', 0, 0, 0],
                     [0, 0, 0, 'dz0', 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 'ux0', 'dz4', 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 'dz2'],
                     [0, 'uz3', 0, 0, 'uz2', 0, 0, 'dp0', 0],
                     [0, 0, 0, 'uz0', 0, 'uz1', 0, 0, 0],
                     [0, 0, 0, 0, 'dk0', 0, 'dj1', 'dj0', 0]]
            return board
        # qiu yin xiang long
        if board_name == 'Endgame2':
            board = [[0, 0, 0, 'us0', 'uk0', 0, 0, 0, 0],
                     [0, 0, 0, 0, 'us1', 0, 0, 0, 0],
                     [0, 0, 0, 0, 'ux0', 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 'uz0', 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 'dj0', 0, 0, 'dz0'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 'uz1', 0, 'uz2', 0, 0],
                     [0, 0, 0, 0, 0, 'dk0', 0, 0, 'dj1']]
            return board
        # ye ma cao tian
        if board_name == 'Endgame3':
            board = [[0, 0, 'ux0', 'us0', 'uk0', 0, 0, 0, 0],
                     [0, 0, 0, 0, 'us1', 0, 0, 0, 0],
                     [0, 0, 0, 0, 'ux1', 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 'dm0', 'dj1', 'dj0'],
                     [0, 0, 'dx0', 0, 0, 0, 0, 0, 0],
                     [0, 'uj0', 'dz0', 0, 'dz1', 0, 0, 0, 0],
                     [0, 0, 0, 'uz0', 'dx1', 0, 0, 0, 0],
                     [0, 0, 0, 0, 'uz1', 0, 0, 0, 0],
                     [0, 0, 0, 'dk0', 0, 0, 0, 0, 0]]
            return board
        # qian li du xing
        if board_name == 'Endgame4':
            board = [[0, 0, 0, 0, 'uk0', 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 'us0', 'dz0', 0, 0, 0, 'ux0'],
                     ['uz0', 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 'um0', 0],
                     [0, 0, 'dz1', 0, 0, 0, 0, 'uz1', 0],
                     [0, 0, 0, 0, 'dj0', 0, 0, 0, 0],
                     [0, 0, 0, 'uz2', 0, 'uz3', 0, 0, 0],
                     [0, 0, 0, 0, 'dk0', 0, 0, 0, 0]]
            return board
        # da zheng xi
        if board_name == 'Endgame5':
            board = [[0, 0, 0, 0, 'up0', 'uk0', 0, 0, 0],
                     [0, 0, 'dz0', 0, 'dz1', 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 'uj0', 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 'dp0', 0, 0],
                     [0, 0, 0, 0, 0, 0, 'dp1', 0, 0],
                     [0, 0, 0, 0, 0, 0, 'dj0', 0, 'dj1'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['uz0', 0, 0, 'uz1', 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 'uz2', 0, 0, 0, 0],
                     [0, 0, 0, 'dk0', 0, 0, 'dx0', 0, 0]]
            return board
        # huo shao lian ying
        if board_name == 'Endgame6':
            board = [[0, 0, 0, 'uk0', 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 'dj0', 0, 0, 0, 0],
                     [0, 0, 0, 0, 'ux0', 0, 0, 0, 'dp0'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 'dz0', 0, 0, 0, 0, 'dj1', 'dp1', 'up0'],
                     [0, 0, 0, 0, 0, 0, 'dx0', 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 'uz3', 0, 0, 0, 0],
                     [0, 0, 0, 'uz2', 'uz1', 0, 0, 'uz0', 0],
                     [0, 0, 0, 0, 0, 'dk0', 0, 0, 0]]
            return board
        # pao da liang lang guan
        if board_name == 'Endgame7':
            board = [[0, 'uj0', 0, 'uk0', 0, 'dp0', 'dj0', 0, 0],
                     [0, 'dz0', 0, 0, 0, 'dz1', 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 'dz2', 0, 0],
                     ['up0', 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 'dz4', 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 'uz1', 0, 0],
                     [0, 0, 0, 'uz0', 0, 'uj0', 0, 0, 0],
                     [0, 0, 0, 0, 'dk0', 0, 0, 0, 0]]
            return board
        # da jiu lian huan
        if board_name == 'Endgame8':
            board = [[0, 0, 0, 0, 0, 'uk0', 0, 0, 0],
                     ['dz1', 0, 0, 0, 'dz2', 0, 0, 0, 'dz0'],
                     [0, 0, 0, 0, 0, 'uj0', 0, 0, 'up0'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 'uz0'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 'dz4', 0, 'dz3', 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 'dp0', 0],
                     [0, 0, 'uz2', 'uz1', 0, 0, 0, 'dp1', 0],
                     [0, 0, 0, 0, 'dk0', 0, 0, 'dj0', 0]]
            return board
        # xiao zheng dong
        if board_name == 'Endgame9':
            board = [[0, 0, 0, 0, 'up0', 'uk0', 0, 0, 0],
                     [0, 0, 0, 'dz1', 'dz0', 0, 0, 0, 0],
                     ['ux0', 0, 0, 0, 0, 'uj0', 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 'dp0'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 'dp1'],
                     [0, 0, 0, 0, 0, 0, 0, 'dj1', 0],
                     [0, 0, 0, 0, 0, 0, 'dz2', 0, 'dj0'],
                     [0, 0, 0, 'uz0', 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 'uz1', 0, 0, 0, 0],
                     [0, 0, 0, 'dk0', 0, 0, 0, 0, 0]]
            return board
        # dai zi ru chao
        if board_name == 'Endgame10':
            board = [[0, 'uj0', 'dz0', 'uj1', 'uk0', 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 'dj0', 0],
                     [0, 0, 0, 0, 'ux0', 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 'dz0', 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 'uz0', 0, 0, 0],
                     [0, 0, 0, 0, 'dk0', 'ds0', 0, 0, 0]]
            return board

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
