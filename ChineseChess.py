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
        if board_name == 'Endgame1':
            board = [['uk0', 'us1', 0, 0, 0, 0, 0, 0, 0],
                     ['us0', 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['uz0', 0, 0, 0, 0, 0, 'uz1', 0, 'uz2'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['dz0', 0, 0, 'dz1', 0, 0, 0, 0, 'dz2'],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['ds0', 0, 0, 0, 0, 0, 0, 0, 0],
                     ['dk0', 'ds1', 0, 0, 0, 0, 0, 0, 0]]
            return board
        if board_name == 'Endgame2':
            board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 'up0', 0, 0, 0, 0, 0, 'up1', 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 'dp0', 0, 0, 0, 0, 0, 'dp1', 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
            return board
        if board_name == 'Endgame3':
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
        if board_name == 'Endgame4':
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
        if board_name == 'Endgame5':
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
        if board_name == 'Endgame6':
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
        if board_name == 'Endgame7':
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
        if board_name == 'Endgame8':
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
        if board_name == 'Endgame9':
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
        if board_name == 'Endgame10':
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
