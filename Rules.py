class Rules:
    def __init__(self):
        pass

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
            if piece_name[0] == 'd':
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
            if piece_name[0] == 'd':
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
            if piece_name[0] == 'd':
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
            if piece_name[0] == 'd':
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
                        elif board[current_row_position][current_column_position][1] == 'k':
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
                        elif board[current_row_position][current_column_position][1] == 'k':
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            break
        return possible_moves
