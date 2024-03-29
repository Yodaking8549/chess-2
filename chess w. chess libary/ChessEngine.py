import chess
from random import randint
def GetAIMove(inputBoard):
    board = chess.Board(inputBoard)
    NumLegalMoves = board.legal_moves.count()
    if board.is_game_over() == False:
        MoveNum = randint(0, NumLegalMoves - 1)
        Move = list(board.legal_moves)[MoveNum]
        return Move.uci()
    else:
        return "Game Over"
    