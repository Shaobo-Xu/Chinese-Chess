class Rules:
    def __init__(self, PieceArray=None, position=None):
        self.name = None
        self.PieceArray = PieceArray
        self.position = position
        self.PossibleMove = self.getNextStep(name=self.name, PieceArray=self.PieceArray, position=self.position)

    def getNextStep(self, name=None, PieceArray=None, position=None):
        possible_moves = []
        if name[1] == 'j':  # ju rule
            for i in range(10):
                current_row_position = position[0] + i + 1
                current_column_position = position[1]
                if current_row_position > 9:
                    break
                else:
                    if PieceArray[current_row_position][current_column_position] == 0:
                        possible_moves.append((current_row_position, current_column_position))
                    elif PieceArray[current_row_position][current_column_position][0] != name[0]:
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
                    if PieceArray[current_row_position][current_column_position] == 0:
                        possible_moves.append((current_row_position, current_column_position))
                    elif PieceArray[current_row_position][current_column_position][0] != name[0]:
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
                    if PieceArray[current_row_position][current_column_position] == 0:
                        possible_moves.append((current_row_position, current_column_position))
                    elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                        possible_moves.append((current_row_position, current_column_position))
                        break
                    else:
                        break
            for i in range(9):
                current_row_position = PieceDict[name][0]
                current_column_position = PieceDict[name][1] + i + 1
                if current_column_position > 8:
                    break
                else:
                    if PieceArray[current_row_position][current_column_position] == 0:
                        possible_moves.append((current_row_position, current_column_position))
                    elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                        possible_moves.append((current_row_position, current_column_position))
                        break
                    else:
                        break
        elif name[1] == 'm':
            possible_ma_move = [[1, 2], [2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1], [-1, 2], [-2, 1]]
            matui = [[0, 1], [1, 0], [0, -1], [1, 0], [0, -1], [-1, 0], [0, 1], [-1, 0]]
            for i in range(8):
                current_row_position = PieceDict[name][0] + possible_ma_move[i][0]
                current_column_position = PieceDict[name][1] + possible_ma_move[i][1]
                current_row_matui = PieceDict[name][0] + matui[i][0]
                current_column_matui = PieceDict[name][1] + matui[i][1]

                if current_row_position <= 9 and current_row_position >= 0 and current_column_position <= 8 and current_column_position >= 0:
                    if PieceArray[current_row_matui][current_column_matui] == 0:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                            possible_moves.append((current_row_position, current_column_position))
        elif name[1] == 'p':  # pao rule
            paojia = False  # obstacle
            for i in range(10):
                current_row_position = PieceDict[name][0] + i + 1
                current_column_position = PieceDict[name][1]
                if current_row_position > 9:
                    break
                else:
                    if paojia:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            continue
                        elif PieceArray[current_row_position][current_column_position][0] == name[0]:
                            break
                        else:
                            possible_moves.append((current_row_position, current_column_position))
                            break
                    else:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            paojia = True
                            continue
            paojia = False
            for i in range(10):
                current_row_position = PieceDict[name][0] - i - 1
                current_column_position = PieceDict[name][1]
                if current_row_position < 0:
                    break
                else:
                    if paojia:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            continue
                        elif PieceArray[current_row_position][current_column_position][0] == name[0]:
                            break
                        else:
                            possible_moves.append((current_row_position, current_column_position))
                            break
                    else:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            paojia = True
                            continue
            paojia = False
            for i in range(9):
                current_row_position = PieceDict[name][0]
                current_column_position = PieceDict[name][1] + i + 1
                if current_column_position > 8:
                    break
                else:
                    if paojia:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            continue
                        elif PieceArray[current_row_position][current_column_position][0] == name[0]:
                            break
                        else:
                            possible_moves.append((current_row_position, current_column_position))
                            break
                    else:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            paojia = True
                            continue
            paojia = False
            for i in range(9):
                current_row_position = PieceDict[name][0]
                current_column_position = PieceDict[name][1] - i - 1
                if current_column_position < 0:
                    break
                else:
                    if paojia:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            continue
                        elif PieceArray[current_row_position][current_column_position][0] == name[0]:
                            break
                        else:
                            possible_moves.append((current_row_position, current_column_position))
                            break
                    else:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            paojia = True
                            continue
        elif name[1] == 'z':  # zu rule
            if name[0] == 'r':
                possible_zu_move = [[0, 1], [-1, 0], [0, -1]]
                if PieceDict[name][0] > 4:
                    possible_moves.append((PieceDict[name][0] - 1, PieceDict[name][1]))
                else:
                    for i in range(3):
                        current_row_position = PieceDict[name][0] + possible_zu_move[i][0]
                        current_column_position = PieceDict[name][1] + possible_zu_move[i][1]
                        if current_row_position >= 0 and current_row_position <= 9 and current_column_position >= 0 and current_column_position <= 8:
                            if PieceArray[current_row_position][current_column_position] == 0:
                                possible_moves.append((current_row_position, current_column_position))
                            elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                                possible_moves.append((current_row_position, current_column_position))
            else:
                possible_zu_move = [[0, 1], [1, 0], [0, -1]]
                if PieceDict[name][0] < 5:
                    possible_moves.append((PieceDict[name][0] + 1, PieceDict[name][1]))
                else:
                    for i in range(3):
                        current_row_position = PieceDict[name][0] + possible_zu_move[i][0]
                        current_column_position = PieceDict[name][1] + possible_zu_move[i][1]
                        if current_row_position >= 0 and current_row_position <= 9 and current_column_position >= 0 and current_column_position <= 8:
                            if PieceArray[current_row_position][current_column_position] == 0:
                                possible_moves.append((current_row_position, current_column_position))
                            elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                                possible_moves.append((current_row_position, current_column_position))
        elif name[1] == 's':  # shi rule
            possible_shi_move = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
            if name[0] == 'r':
                for i in range(4):
                    current_row_position = PieceDict[name][0] + possible_shi_move[i][0]
                    current_column_position = PieceDict[name][1] + possible_shi_move[i][1]
                    if current_row_position >= 7 and current_row_position <= 9 and current_column_position >= 3 and current_column_position <= 5:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                            possible_moves.append((current_row_position, current_column_position))
            else:
                for i in range(4):
                    current_row_position = PieceDict[name][0] + possible_shi_move[i][0]
                    current_column_position = PieceDict[name][1] + possible_shi_move[i][1]
                    if current_row_position >= 0 and current_row_position <= 2 and current_column_position >= 3 and current_column_position <= 5:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                            possible_moves.append((current_row_position, current_column_position))
        elif name[1] == 'x':  # xiang rule
            possible_xiang_move = [[2, 2], [2, -2], [-2, 2], [-2, -2]]
            xiangtui = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
            if name[0] == 'r':
                for i in range(4):
                    current_row_position = PieceDict[name][0] + possible_xiang_move[i][0]
                    current_column_position = PieceDict[name][1] + possible_xiang_move[i][1]
                    current_row_matui = PieceDict[name][0] + xiangtui[i][0]
                    current_column_matui = PieceDict[name][1] + xiangtui[i][1]

                    if current_row_position >= 5 and current_row_position <= 9 and current_column_position <= 8 and current_column_position >= 0:
                        if PieceArray[current_row_matui][current_column_matui] == 0:
                            if PieceArray[current_row_position][current_column_position] == 0:
                                possible_moves.append((current_row_position, current_column_position))
                            elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                                possible_moves.append((current_row_position, current_column_position))
            else:
                for i in range(4):
                    current_row_position = PieceDict[name][0] + possible_xiang_move[i][0]
                    current_column_position = PieceDict[name][1] + possible_xiang_move[i][1]
                    current_row_matui = PieceDict[name][0] + xiangtui[i][0]
                    current_column_matui = PieceDict[name][1] + xiangtui[i][1]

                    if current_row_position >= 0 and current_row_position <= 4 and current_column_position <= 8 and current_column_position >= 0:
                        if PieceArray[current_row_matui][current_column_matui] == 0:
                            if PieceArray[current_row_position][current_column_position] == 0:
                                possible_moves.append((current_row_position, current_column_position))
                            elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                                possible_moves.append((current_row_position, current_column_position))
        elif name[1] == 'b':  # king rule
            possible_jiang_move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            if name[0] == 'r':
                for i in range(4):
                    current_row_position = PieceDict[name][0] + possible_jiang_move[i][0]
                    current_column_position = PieceDict[name][1] + possible_jiang_move[i][1]

                    if current_row_position >= 7 and current_row_position <= 9 and current_column_position <= 5 and current_column_position >= 3:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                            possible_moves.append((current_row_position, current_column_position))
                for j in range(9):
                    current_row_position = PieceDict[name][0] - j - 1
                    current_column_position = PieceDict[name][1]
                    if current_row_position < 0:
                        break
                    else:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            continue
                        elif PieceArray[current_row_position][current_column_position][1] == 'b':
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            break

            else:
                for i in range(4):
                    current_row_position = PieceDict[name][0] + possible_jiang_move[i][0]
                    current_column_position = PieceDict[name][1] + possible_jiang_move[i][1]

                    if current_row_position >= 0 and current_row_position <= 2 and current_column_position <= 5 and current_column_position >= 3:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            possible_moves.append((current_row_position, current_column_position))
                        elif PieceArray[current_row_position][current_column_position][0] != name[0]:
                            possible_moves.append((current_row_position, current_column_position))

                for j in range(9):
                    current_row_position = PieceDict[name][0] + j + 1
                    current_column_position = PieceDict[name][1]
                    if current_row_position > 9:
                        break
                    else:
                        if PieceArray[current_row_position][current_column_position] == 0:
                            continue
                        elif PieceArray[current_row_position][current_column_position][1] == 'b':
                            possible_moves.append((current_row_position, current_column_position))
                        else:
                            break
        return possible_moves
