# Chinese-Chess

一个基于python的中国象棋的UI以及AI(Alphabeta pruning)

加入了部分endgame，可供测试及开发AI

原出处是这里(java版)： https://github.com/geeeeeeeeek/IntelligentChineseChessSystem

=================================================================================================

简单说明：

每一次玩家操作以后，controller会给simple AI传一个 board ，这个board是当前的棋盘array

simple AI 进行计算以后会返回两个array： piece_position, next_position ，就是需要操作的棋子的当前位置以及目标位置，如(0，0),(1，0)就是黑棋的车向下走一格