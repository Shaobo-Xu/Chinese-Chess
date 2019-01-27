from Rules import Rules
from copy import deepcopy


class SimpleAI:
    def __init__(self, controller=None):
        self.rules = Rules()
        self.controller = controller

    def move(self, board=None):
        return self.game_tree_search(board=board)

    def game_tree_search(self, board=None):
        pieces_alive = 0
        for i in range(10):
            for j in range(9):
                if board[i][j] != 0:
                    pieces_alive += 1

        # the real depth is SearchDepth+1
        # if pieces_alive < 26:
        #     SearchDepth = 2
        # else:
        #     SearchDepth = 1
        SearchDepth = 1
        max_value = float('-inf')
        piece_position = None
        next_position = None
        for i in range(10):
            for j in range(9):
                if board[i][j] != 0:
                    if board[i][j][0] == 'u':
                        possible_moves = self.rules.get_possible_moves(board=board, position=[i, j])
                        for move in possible_moves:
                            new_board = deepcopy(board)
                            node = Node(board=new_board, current_side=self.controller.CurrentPlayer,
                                        old_position=(i, j), new_position=move)
                            # for each possible move of each piece, do alpha-beta search
                            value = self.alpha_beta_search(node=node, SearchDepth=SearchDepth, maximizingPlayer=False)
                            if value > max_value:
                                max_value = value
                                piece_position = (i, j)
                                next_position = move
        return piece_position, next_position

    # alpha-beta search
    def alpha_beta_search(self, node=None, SearchDepth=None, alpha=float('-inf'), beta=float('inf'),
                          maximizingPlayer=True):
        if SearchDepth == 0:
            value = self.evaluate_score(node=node, score_side='u')
            print('value: ', value)
            print('old position: ', node.old_position)
            print('new position: ', node.new_position)
            print()
            while node.parent:
                print('old position: ', node.parent.old_position)
                print('new position: ', node.parent.new_position)
                node=node.parent
                print()
            print('-----------------------------------')

            return value
        node_has_child = node.has_child()
        if not node_has_child:
            value = self.evaluate_score(node=node, score_side='u')
            return value

        for child in node.child:
            if maximizingPlayer:
                alpha = max(alpha, self.alpha_beta_search(child, SearchDepth - 1, alpha, beta, False))
            else:
                beta = min(beta, self.alpha_beta_search(child, SearchDepth - 1, alpha, beta, True))
            if alpha >= beta:
                break
        if maximizingPlayer:
            return alpha
        else:
            return beta

    # evaluate whole score of each tree node
    def evaluate_score(self, node=None, score_side=None):
        score = 0
        for row in range(10):
            for column in range(9):
                if node.board[row][column] != 0:
                    score += self.piece_score(Name=node.board[row][column], Position=(row, column),
                                              ScoreColor=score_side)
        return score

    # score of a single piece
    def piece_score(self, Name=None, Position=None, ScoreColor=None):
        # position score
        j_position_score = [[14, 14, 12, 18, 16, 18, 12, 14, 14],
                            [16, 20, 18, 24, 26, 24, 18, 20, 16],
                            [12, 12, 12, 18, 18, 18, 12, 12, 12],
                            [12, 18, 16, 22, 22, 22, 16, 18, 12],
                            [12, 14, 12, 18, 18, 18, 12, 14, 12],
                            [12, 16, 14, 20, 20, 20, 14, 16, 12],
                            [6, 10, 8, 14, 14, 14, 8, 10, 6],
                            [4, 8, 6, 14, 12, 14, 6, 8, 4],
                            [8, 4, 8, 16, 8, 16, 8, 4, 8],
                            [-2, 12, 6, 14, 12, 14, 6, 12, -2]]

        m_position_score = [[4, 8, 16, 12, 4, 12, 16, 8, 4],
                            [4, 10, 28, 16, 8, 16, 28, 10, 4],
                            [12, 14, 16, 20, 18, 20, 16, 14, 12],
                            [8, 24, 18, 24, 20, 24, 18, 24, 8],
                            [6, 16, 14, 18, 16, 18, 14, 16, 6],
                            [4, 12, 16, 14, 12, 14, 16, 12, 4],
                            [2, 6, 8, 6, 10, 6, 8, 6, 2],
                            [4, 2, 9, 8, 4, 8, 9, 2, 4],
                            [0, 2, 4, 4, -2, 4, 4, 2, 0],
                            [0, -4, 0, 0, 0, 0, 0, -4, 0]]

        p_position_score = [[6, -8, 0, -10, -12, -10, 0, -8, 6],
                            [2, 2, 0, -4, -14, -4, 0, 2, 2],
                            [2, 2, 0, -10, -8, -10, 0, 2, 2],
                            [0, 0, -2, 4, 10, 4, -2, 0, 0],
                            [0, 0, 0, 2, 8, 2, 0, 0, 0],
                            [-2, 0, 4, 2, 6, 2, 4, 0, -2],
                            [0, 0, 0, 2, 4, 2, 0, 0, 0],
                            [4, 0, 8, 4, 8, 4, 8, 0, 4],
                            [0, 2, 4, 6, 3, 6, 4, 2, 0],
                            [0, 0, 1, 4, 3, 4, 2, 1, 0]]

        z_position_score = [[0, 0, 6, 9, 12, 9, 6, 0, 0],
                            [15, 30, 43, 60, 80, 60, 43, 30, 15],
                            [12, 24, 33, 48, 60, 48, 33, 24, 12],
                            [10, 20, 28, 30, 35, 30, 28, 20, 10],
                            [9, 18, 27, 27, 30, 27, 27, 18, 9],
                            [2, 0, 8, 0, 8, 0, 8, 0, 2],
                            [0, 0, -2, 0, 4, 0, -2, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # piece value
        j_score = 400
        m_score = 180
        p_score = 210
        z_score = 45
        x_score = 90
        s_score = 90
        k_score = 1000000

        if Name[0] == 'd':
            row = Position[0]
        else:
            row = 9 - Position[0]
        column = Position[1]
        if Name[0] == ScoreColor:
            sgn = 1
        else:
            sgn = -1
        if Name[1] == 'j':
            return (j_position_score[row][column] + j_score) * sgn
        if Name[1] == 'm':
            return (m_position_score[row][column] + m_score) * sgn
        if Name[1] == 'p':
            return (p_position_score[row][column] + p_score) * sgn
        if Name[1] == 'z':
            return (z_position_score[row][column] + z_score) * sgn
        if Name[1] == 'x':
            return x_score * sgn
        if Name[1] == 's':
            return s_score * sgn
        if Name[1] == 'k':
            return k_score * sgn


# node structure
class Node:
    def __init__(self, board=None, current_side=None, old_position=None, new_position=None):
        self.board = board
        self.old_position = old_position
        self.new_position = new_position
        self.parent = None
        self.child = []
        self.current_side = current_side
        self.move()
        self.get_next_player()

    # if this node has child, return true and generate the childs
    def has_child(self):
        rules = Rules()

        # if this is the end, then don't do further search
        live_boss = 0
        for i in range(10):
            for j in range(9):
                if self.board[i][j] != 0:
                    if self.board[i][j][1] == 'k':
                        live_boss += 1
        if live_boss != 2:
            return False

        # generate child nodes
        for i in range(10):
            for j in range(9):
                if self.board[i][j] != 0:
                    if self.board[i][j][0] == self.current_side:
                        possible_moves = rules.get_possible_moves(board=self.board, position=(i, j))
                        for move in possible_moves:
                            new_board = deepcopy(self.board)
                            node = Node(board=new_board, current_side=self.current_side, old_position=(i, j),
                                        new_position=move)
                            self.child.append(node)
                            node.parent = self
        return True

    def get_next_player(self):
        if self.current_side == 'd':
            self.current_side = 'u'
        else:
            self.current_side = 'd'

    def move(self):
        piece_name = self.board[self.old_position[0]][self.old_position[1]]
        self.board[self.new_position[0]][self.new_position[1]] = piece_name
        self.board[self.old_position[0]][self.old_position[1]] = 0
