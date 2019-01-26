from Rules import Rules
from AI import SimpleAI


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

    def act(self, old_position=None, new_position=None):
        rules = Rules()
        possible_moves = rules.get_possible_moves(board=self.board, position=old_position)
        if new_position in possible_moves:
            # if move
            if self.board[new_position[0]][new_position[1]] == 0:
                self.UI.move_piece(old_position=old_position, new_position=new_position)
                self.move_piece(old_position=old_position, new_position=new_position)
            # eat
            else:
                self.UI.eat_piece(predator=old_position, prey=new_position)
                self.eat_piece(predator=old_position, prey=new_position)
            self.change_side()
            self.AI_move()

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
        piece_position, next_position = self.AI.move(board=self.board)
        if self.board[next_position[0]][next_position[1]] != 0:
            self.UI.eat_piece(predator=piece_position, prey=next_position)
            self.eat_piece(predator=piece_position, prey=next_position)
        else:
            self.UI.move_piece(old_position=piece_position, new_position=next_position)
            self.move_piece(old_position=piece_position, new_position=next_position)
        self.change_side()

    def new_game(self, first=True):
        if not first:
            self.change_side()
            self.AI_move()
