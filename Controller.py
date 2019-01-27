from Rules import Rules
from AI import SimpleAI
from PyQt5.QtCore import QThread


class Controller:
    def __init__(self, board=None):
        self.UI = None
        self.main_window = None
        self.last_clicked = None
        self.shadow = None
        self.mark = None
        self.CurrentPlayer = 'd'
        self.AI = SimpleAI(controller=self)
        self.board = board
        self.eat_history = []
        self.old_position_history = []
        self.new_position_history = []
        self.new_position_for_thread = None
        self.old_position_for_thread = None
        self.AI_thread = AIThread(controller=self)

    def act(self, old_position=None, new_position=None):
        rules = Rules()
        possible_moves = rules.get_possible_moves(board=self.board, position=old_position)
        if new_position in possible_moves:
            self.new_position_for_thread = new_position
            self.old_position_for_thread = old_position
            # if move
            if self.board[new_position[0]][new_position[1]] == 0:
                self.UI.move_piece(old_position=old_position, new_position=new_position)
            # eat
            else:
                self.UI.eat_piece(predator=old_position, prey=new_position)

            self.AI_thread.start()
            self.change_side()

    def move_piece(self, old_position=None, new_position=None):
        piece_name = self.board[old_position[0]][old_position[1]]
        self.board[old_position[0]][old_position[1]] = 0
        self.board[new_position[0]][new_position[1]] = piece_name

    def eat_piece(self, predator=None, prey=None):
        predator_name = self.board[predator[0]][predator[1]]
        self.board[predator[0]][predator[1]] = 0
        self.board[prey[0]][prey[1]] = predator_name

    def change_side(self):
        if self.CurrentPlayer == 'u':
            self.CurrentPlayer = 'd'
        else:
            self.CurrentPlayer = 'u'

    def AI_move(self):
        new_position = self.new_position_for_thread
        old_position = self.old_position_for_thread

        # if move
        if self.board[new_position[0]][new_position[1]] == 0:
            self.old_position_history.append(old_position)
            self.new_position_history.append(new_position)
            self.eat_history.append(False)
            self.move_piece(old_position=old_position, new_position=new_position)

        # eat
        else:
            self.old_position_history.append(old_position)
            self.new_position_history.append(new_position)
            self.eat_history.append(self.board[new_position[0]][new_position[1]])
            self.eat_piece(predator=old_position, prey=new_position)
        end = self.is_end()
        if not end:
            piece_position, next_position = self.AI.move(board=self.board)
            # eat
            if self.board[next_position[0]][next_position[1]] != 0:
                self.old_position_history.append(piece_position)
                self.new_position_history.append(next_position)
                self.eat_history.append(self.board[next_position[0]][next_position[1]])
                self.UI.eat_piece(predator=piece_position, prey=next_position)
                self.eat_piece(predator=piece_position, prey=next_position)
            # move
            else:
                self.old_position_history.append(piece_position)
                self.new_position_history.append(next_position)
                self.eat_history.append(False)
                self.UI.move_piece(old_position=piece_position, new_position=next_position)
                self.move_piece(old_position=piece_position, new_position=next_position)
            self.change_side()

    def new_game(self, first=True):
        if not first:
            self.change_side()
            self.AI_thread.start()

    def take_back(self):
        if self.CurrentPlayer == 'd':
            if self.eat_history:
                for i in range(2):
                    eat = self.eat_history.pop()
                    old_position = self.old_position_history.pop()
                    new_position = self.new_position_history.pop()
                    # move
                    if not eat:
                        self.UI.move_piece(old_position=new_position, new_position=old_position)
                        self.move_piece(old_position=new_position, new_position=old_position)
                        self.UI.update_shadow()
                    # eat
                    else:
                        self.UI.move_piece(old_position=new_position, new_position=old_position)
                        self.UI.put_piece_back(name=eat)
                        self.UI.update_shadow()
                        self.move_piece(old_position=new_position, new_position=old_position)
                        self.put_piece_back(name=eat, position=new_position)

    def put_piece_back(self, name=None, position=None):
        self.board[position[0]][position[1]] = name

    def is_end(self):
        live_boss = 0
        for i in range(10):
            for j in range(9):
                if self.board[i][j] != 0:
                    if self.board[i][j][1] == 'k':
                        live_boss += 1
        if live_boss != 2:
            return True


class AIThread(QThread):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller

    def run(self):
        # self.ctrl.view.update()
        self.controller.AI_move()
