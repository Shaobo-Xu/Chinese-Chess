from PyQt5.QtWidgets import QFrame, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QPainter, QColor


class UI(QWidget):

    def __init__(self, parent, controller=None, start=None, first=True):
        super().__init__(parent)
        self.first = first
        self.length = 68
        self.x_offset = 60
        self.y_offset = 20
        self.start = start
        if first:
            self.player_color = 'r'
        else:
            self.player_color = 'b'
        self.Controller = controller
        self.Controller.UI = self
        self.piece_dict = {}
        self.show_board()

    def show_board(self):
        self.setFixedSize(1025, 725)
        uos_logo = QLabel(self)
        uos_logo.setPixmap(QPixmap("img/uos.jpg"))
        uos_logo.move(715, 10)
        bg = QLabel(self)
        bg.setPixmap(QPixmap("img/bg.png"))
        bg.move(10, 10)

        comboBox = QComboBox(self)
        comboBox.addItem("choose endgame")
        comboBox.addItem("Endgame1")
        comboBox.addItem("Endgame2")
        comboBox.addItem("Endgame3")
        comboBox.addItem("Endgame4")
        comboBox.addItem("Endgame5")
        comboBox.addItem("Endgame6")
        comboBox.addItem("Endgame7")
        comboBox.addItem("Endgame8")
        comboBox.addItem("Endgame9")
        comboBox.addItem("Endgame10")
        comboBox.activated[str].connect(self.EndgameChoice)
        comboBox.move(820, 200)

        # two buttons
        offensive_restart = QPushButton("Offensive Restart", self)
        offensive_restart.setFont(QFont('SansSerif', 12))
        offensive_restart.resize(150, 70)
        offensive_restart.move(800, 250)
        offensive_restart.clicked.connect(self.OffensiveRestart)

        defensive_restart = QPushButton("Defensive Restart", self)
        defensive_restart.setFont(QFont('SansSerif', 12))
        defensive_restart.resize(150, 70)
        defensive_restart.move(800, 350)
        defensive_restart.clicked.connect(self.DeffensiveRestart)

        # take back
        offensive_restart = QPushButton("take back", self)
        offensive_restart.setFont(QFont('SansSerif', 12))
        offensive_restart.resize(150, 70)
        offensive_restart.move(800, 450)
        offensive_restart.clicked.connect(self.OffensiveRestart)

        shadow = QLabel(self)
        shadow.setPixmap(QPixmap('img/shadow.png'))
        self.Controller.shadow = shadow
        self.update_shadow()
        mark = QLabel(self)
        mark.setPixmap(QPixmap('img/mark.png'))
        self.Controller.mark = mark
        self.update_mark()

        for row in range(10):
            for col in range(9):
                if self.Controller.board[row][col] != 0:
                    if self.player_color == 'r':
                        if self.Controller.board[row][col][0] == 'd':
                            piece = QLabel(self)
                            piece_name = 'r' + self.Controller.board[row][col][1]
                            piece.setPixmap(QPixmap('img/' + piece_name + '.png'))
                            piece.move(col * self.length + self.x_offset, row * self.length + self.y_offset)
                        else:
                            piece = QLabel(self)
                            piece_name = 'b' + self.Controller.board[row][col][1]
                            piece.setPixmap(QPixmap('img/' + piece_name + '.png'))
                            piece.move(col * self.length + self.x_offset, row * self.length + self.y_offset)
                    else:
                        if self.Controller.board[row][col][0] == 'u':
                            piece = QLabel(self)
                            piece_name = 'r' + self.Controller.board[row][col][1]
                            piece.setPixmap(QPixmap('img/' + piece_name + '.png'))
                            piece.move(col * self.length + self.x_offset, row * self.length + self.y_offset)
                        else:
                            piece = QLabel(self)
                            piece_name = 'b' + self.Controller.board[row][col][1]
                            piece.setPixmap(QPixmap('img/' + piece_name + '.png'))
                            piece.move(col * self.length + self.x_offset, row * self.length + self.y_offset)
                    self.piece_dict[self.Controller.board[row][col]] = piece

    def mousePressEvent(self, QMouseEvent):
        if self.Controller.CurrentPlayer == 'd':
            col = round((QMouseEvent.x() - 96) / 68)
            row = round((QMouseEvent.y() - 53) / 68)
            self.simple_ui_control(row=row, col=col)

    def simple_ui_control(self, row=None, col=None):
        if row >= 0 and row <= 9 and col >= 0 and col <= 8:
            if self.Controller.last_clicked is None:
                if self.Controller.board[row][col] != 0:
                    if self.Controller.board[row][col][0] == 'd':
                        self.update_mark((row, col))
                        self.Controller.last_clicked = (row, col)
            # have clicked some piece before
            else:
                # if click the board
                if self.Controller.board[row][col] == 0:
                    self.Controller.act(self.Controller.last_clicked, (row, col))
                else:
                    # if two clicks are of the same side
                    if self.Controller.board[self.Controller.last_clicked[0]][self.Controller.last_clicked[1]][0] == \
                            self.Controller.board[row][col][0]:
                        # if click the same piece
                        if (row, col) == self.Controller.last_clicked:
                            self.Controller.last_clicked = None
                            self.update_mark((-50, -50))
                        else:
                            self.update_mark((row, col))
                            self.Controller.last_clicked = (row, col)
                    else:
                        self.Controller.act(self.Controller.last_clicked, (row, col))

    def update_shadow(self, current_move=(-200, -200)):
        self.Controller.shadow.move(current_move[1] * self.length + self.x_offset,
                                    current_move[0] * self.length + self.y_offset)

    def update_mark(self, current_move=(-200, -200)):
        self.Controller.mark.move(current_move[1] * self.length + self.x_offset,
                                  current_move[0] * self.length + self.y_offset)

    def eat_piece(self, predator=None, prey=None):
        predator_name = self.Controller.board[predator[0]][predator[1]]
        prey_name = self.Controller.board[prey[0]][prey[1]]
        self.piece_dict[prey_name].setVisible(False)
        self.piece_dict[predator_name].move(prey[1] * self.length + self.x_offset,
                                            prey[0] * self.length + self.y_offset)
        self.Controller.last_clicked = None
        self.update_shadow(current_move=predator)
        self.update_mark()

    def move_piece(self, old_position=None, new_position=None):
        piece_name = self.Controller.board[old_position[0]][old_position[1]]
        self.piece_dict[piece_name].move(new_position[1] * self.length + self.x_offset,
                                         new_position[0] * self.length + self.y_offset)
        self.Controller.last_clicked = None
        self.update_shadow(current_move=old_position)
        self.update_mark()

    def EndgameChoice(self, text):
<<<<<<< HEAD
        if self.Controller.CurrentPlayer == 'd':
            if text != "choose endgame":
                self.start.init_new_game(board_name=text)
=======
        if text != "choose initial game":
            self.start.init_new_game(board_name=text)
>>>>>>> parent of 0edd06c... 基本完工

    # restart button function
    def OffensiveRestart(self):
        if self.Controller.CurrentPlayer == 'd':
            self.start.init_new_game()

    def DeffensiveRestart(self):
<<<<<<< HEAD
        if self.Controller.CurrentPlayer == 'd':
            self.start.init_new_game(first=False)

    def takeback(self):
        if self.Controller.CurrentPlayer == 'd':
            self.Controller.take_back()

    def put_piece_back(self, name=None):
        self.piece_dict[name].setVisible(True)
=======
        self.start.init_new_game(first=False)
>>>>>>> parent of 0edd06c... 基本完工
