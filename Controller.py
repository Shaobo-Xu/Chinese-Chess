from PyQt5.QtCore import QThread
from UI import UI


class Controller:
    def __init__(self):
        self.UI = None
        self.main_window = None
        self.last_clicked = None
        self.shadow = None
        self.mark = None
        self.UI = None
        # c for computer, p for player
        self.board = [['cj0', 'cm0', 'cx0', 'cs0', 'ck0', 'cs1', 'cx1', 'cm1', 'cj1'],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 'cp0', 0, 0, 0, 0, 0, 'cp1', 0],
                      ['cz0', 0, 'cz1', 0, 'cz2', 0, 'cz3', 0, 'cz4'],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      ['pz0', 0, 'pz1', 0, 'pz2', 0, 'pz3', 0, 'pz4'],
                      [0, 'pp0', 0, 0, 0, 0, 0, 'pp1', 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      ['pj0', 'pm0', 'px0', 'ps0', 'pk0', 'ps1', 'px1', 'pm1', 'pj1']]

    def act(self, old_position=None, new_position=None):
        possible_moves = self.get_possible_moves(self.board, old_position)
        if new_position in possible_moves:
            # if move
            if self.board[new_position[0]][new_position[1]] == 0:
                self.UI.move_piece(old_position=old_position, new_position=new_position)
                self.move_piece(old_position=old_position, new_position=new_position)
            # eat
            else:
                self.UI.eat_piece(predator=old_position, prey=new_position)
                self.eat_piece(predator=old_position, prey=new_position)

    def move_piece(self, old_position=None, new_position=None):
        piece_name = self.board[old_position[0]][old_position[1]]
        self.board[old_position[0]][old_position[1]] = 0
        self.board[new_position[0]][new_position[1]] = piece_name

    def eat_piece(self, predator=None, prey=None):
        predator_name = self.board[predator[0]][predator[1]]
        self.board[predator[0]][predator[1]] = 0
        self.board[prey[0]][prey[1]] = predator_name

    def get_possible_moves(self, board=None, position=None):
        piece_name = board[position[0]][position[1]]
        possible_moves = []
        if piece_name[1] == 'j':  # ju rule
            for i in range(10):
                current_row_position = position[0] + i + 1
                current_column_position = position[1]
                if current_row_position > 9:
                    break
                else:
                    if board[current_row_position][current_column_position] == 0:
                        possible_moves.append((current_row_position, current_column_position))
                    elif board[current_row_position][current_column_position][0] != piece_name[0]:
                        possible_moves.append((current_row_position, current_column_position))
                        break
                    else:
                        break
            for i in range(10):
                current_row_position = position[0] - i - 1
                current_column_position = position[1]
                if current_row_position < 0:
                    break
                else:
                    if board[current_row_position][current_column_position] == 0:
                        possible_moves.append((current_row_position, current_column_position))
                    elif board[current_row_position][current_column_position][0] != piece_name[0]:
                        possible_moves.append((current_row_position, current_column_position))
                        break
                    else:
                        break
            for i in range(9):
                current_row_position = position[0]
                current_column_position = position[1] - i - 1
                if current_column_position < 0:
                    break
                else:
                    if board[current_row_position][current_column_position] == 0:
                        possible_moves.append((current_row_position, current_column_position))
                    elif board[current_row_position][current_column_position][0] != piece_name[0]:
                        possible_moves.append((current_row_position, current_column_position))
                        break
                    else:
                        break
            for i in range(9):
                current_row_position = position[0]
                current_column_position = position[1] + i + 1
                if current_column_position > 8:
                    break
                else:
                    if board[current_row_position][current_column_position] == 0:
                        possible_moves.append((current_row_position, current_column_position))
                    elif board[current_row_position][current_column_position][0] != piece_name[0]:
                        possible_moves.append((current_row_position, current_column_position))
                        break
                    else:
                        break
        elif piece_name[1] == 'm':
            possible_ma_move = [[1, 2], [2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1], [-1, 2], [-2, 1]]
            matui = [[0, 1], [1, 0], [0, -1], [1, 0], [0, -1], [-1, 0], [0, 1], [-1, 0]]
            for i in range(8):
                current_row_position = position[0] + possible_ma_move[i][0]
                current_column_position = position[1] + possible_ma_move[i][1]
                current_row_matui = position[0] + matui[i][0]
                current_column_matui = position[1] + matui[i][1]

                if current_row_position <= 9 and current_row_position >= 0 and current_column_position <= 8 and current_column_position >= 0:
                    if board[current_row_matui][current_column_matui] == 0:
                        if board[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        elif board[current_row_position][current_column_position][0] != piece_name[0]:
                            possible_moves.append((current_row_position, current_column_position))
        elif piece_name[1] == 'p':  # pao rule
            paojia = False  # obstacle
            for i in range(10):
                current_row_position = position[0] + i + 1
                current_column_position = position[1]
                if current_row_position > 9:
                    break
                else:
                    if paojia:
                        if board[current_row_position][current_column_position] == 0:
                            continue
                        elif board[current_row_position][current_column_position][0] == piece_name[0]:
                            break
                        else:
                            possible_moves.append((current_row_position, current_column_position))
                            break
                    else:
                        if board[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            paojia = True
                            continue
            paojia = False
            for i in range(10):
                current_row_position = position[0] - i - 1
                current_column_position = position[1]
                if current_row_position < 0:
                    break
                else:
                    if paojia:
                        if board[current_row_position][current_column_position] == 0:
                            continue
                        elif board[current_row_position][current_column_position][0] == piece_name[0]:
                            break
                        else:
                            possible_moves.append((current_row_position, current_column_position))
                            break
                    else:
                        if board[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            paojia = True
                            continue
            paojia = False
            for i in range(9):
                current_row_position = position[0]
                current_column_position = position[1] + i + 1
                if current_column_position > 8:
                    break
                else:
                    if paojia:
                        if board[current_row_position][current_column_position] == 0:
                            continue
                        elif board[current_row_position][current_column_position][0] == piece_name[0]:
                            break
                        else:
                            possible_moves.append((current_row_position, current_column_position))
                            break
                    else:
                        if board[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            paojia = True
                            continue
            paojia = False
            for i in range(9):
                current_row_position = position[0]
                current_column_position = position[1] - i - 1
                if current_column_position < 0:
                    break
                else:
                    if paojia:
                        if board[current_row_position][current_column_position] == 0:
                            continue
                        elif board[current_row_position][current_column_position][0] == piece_name[0]:
                            break
                        else:
                            possible_moves.append((current_row_position, current_column_position))
                            break
                    else:
                        if board[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            paojia = True
                            continue
        elif piece_name[1] == 'z':  # zu rule
            if piece_name[0] == 'p':
                possible_zu_move = [[0, 1], [-1, 0], [0, -1]]
                if position[0] > 4:
                    possible_moves.append((position[0] - 1, position[1]))
                else:
                    for i in range(3):
                        current_row_position = position[0] + possible_zu_move[i][0]
                        current_column_position = position[1] + possible_zu_move[i][1]
                        if current_row_position >= 0 and current_row_position <= 9 and current_column_position >= 0 and current_column_position <= 8:
                            if board[current_row_position][current_column_position] == 0:
                                possible_moves.append((current_row_position, current_column_position))
                            elif board[current_row_position][current_column_position][0] != piece_name[0]:
                                possible_moves.append((current_row_position, current_column_position))
            else:
                possible_zu_move = [[0, 1], [1, 0], [0, -1]]
                if position[0] < 5:
                    possible_moves.append((position[0] + 1, position[1]))
                else:
                    for i in range(3):
                        current_row_position = position[0] + possible_zu_move[i][0]
                        current_column_position = position[1] + possible_zu_move[i][1]
                        if current_row_position >= 0 and current_row_position <= 9 and current_column_position >= 0 and current_column_position <= 8:
                            if board[current_row_position][current_column_position] == 0:
                                possible_moves.append((current_row_position, current_column_position))
                            elif board[current_row_position][current_column_position][0] != piece_name[0]:
                                possible_moves.append((current_row_position, current_column_position))
        elif piece_name[1] == 's':  # shi rule
            possible_shi_move = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
            if piece_name[0] == 'p':
                for i in range(4):
                    current_row_position = position[0] + possible_shi_move[i][0]
                    current_column_position = position[1] + possible_shi_move[i][1]
                    if current_row_position >= 7 and current_row_position <= 9 and current_column_position >= 3 and current_column_position <= 5:
                        if board[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        elif board[current_row_position][current_column_position][0] != piece_name[0]:
                            possible_moves.append((current_row_position, current_column_position))
            else:
                for i in range(4):
                    current_row_position = position[0] + possible_shi_move[i][0]
                    current_column_position = position[1] + possible_shi_move[i][1]
                    if current_row_position >= 0 and current_row_position <= 2 and current_column_position >= 3 and current_column_position <= 5:
                        if board[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        elif board[current_row_position][current_column_position][0] != piece_name[0]:
                            possible_moves.append((current_row_position, current_column_position))
        elif piece_name[1] == 'x':  # xiang rule
            possible_xiang_move = [[2, 2], [2, -2], [-2, 2], [-2, -2]]
            xiangtui = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
            if piece_name[0] == 'p':
                for i in range(4):
                    current_row_position = position[0] + possible_xiang_move[i][0]
                    current_column_position = position[1] + possible_xiang_move[i][1]
                    current_row_matui = position[0] + xiangtui[i][0]
                    current_column_matui = position[1] + xiangtui[i][1]

                    if current_row_position >= 5 and current_row_position <= 9 and current_column_position <= 8 and current_column_position >= 0:
                        if board[current_row_matui][current_column_matui] == 0:
                            if board[current_row_position][current_column_position] == 0:
                                possible_moves.append((current_row_position, current_column_position))
                            elif board[current_row_position][current_column_position][0] != piece_name[0]:
                                possible_moves.append((current_row_position, current_column_position))
            else:
                for i in range(4):
                    current_row_position = position[0] + possible_xiang_move[i][0]
                    current_column_position = position[1] + possible_xiang_move[i][1]
                    current_row_matui = position[0] + xiangtui[i][0]
                    current_column_matui = position[1] + xiangtui[i][1]

                    if current_row_position >= 0 and current_row_position <= 4 and current_column_position <= 8 and current_column_position >= 0:
                        if board[current_row_matui][current_column_matui] == 0:
                            if board[current_row_position][current_column_position] == 0:
                                possible_moves.append((current_row_position, current_column_position))
                            elif board[current_row_position][current_column_position][0] != piece_name[0]:
                                possible_moves.append((current_row_position, current_column_position))
        elif piece_name[1] == 'k':  # king rule
            possible_jiang_move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            if piece_name[0] == 'p':
                for i in range(4):
                    current_row_position = position[0] + possible_jiang_move[i][0]
                    current_column_position = position[1] + possible_jiang_move[i][1]

                    if current_row_position >= 7 and current_row_position <= 9 and current_column_position <= 5 and current_column_position >= 3:
                        if board[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        elif board[current_row_position][current_column_position][0] != piece_name[0]:
                            possible_moves.append((current_row_position, current_column_position))
                for j in range(9):
                    current_row_position = position[0] - j - 1
                    current_column_position = position[1]
                    if current_row_position < 0:
                        break
                    else:
                        if board[current_row_position][current_column_position] == 0:
                            continue
                        elif board[current_row_position][current_column_position][1] == 'b':
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            break

            else:
                for i in range(4):
                    current_row_position = position[0] + possible_jiang_move[i][0]
                    current_column_position = position[1] + possible_jiang_move[i][1]

                    if current_row_position >= 0 and current_row_position <= 2 and current_column_position <= 5 and current_column_position >= 3:
                        if board[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        elif board[current_row_position][current_column_position][0] != piece_name[0]:
                            possible_moves.append((current_row_position, current_column_position))

                for j in range(9):
                    current_row_position = position[0] + j + 1
                    current_column_position = position[1]
                    if current_row_position > 9:
                        break
                    else:
                        if board[current_row_position][current_column_position] == 0:
                            continue
                        elif board[current_row_position][current_column_position][1] == 'b':
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            break
        return possible_moves
