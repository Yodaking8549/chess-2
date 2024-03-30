import chess
from random import randint

def GetAIMove(inputBoard):
    global board
    global Capture
    Capture = False
    board = chess.Board(inputBoard)
    GetRandomMove()
    return Move.uci()
    
def GetRandomMove():
    global board
    global Move
    NumLegalMoves = board.legal_moves.count()
    MoveNum = randint(0, NumLegalMoves - 1)
    Move = list(board.legal_moves)[MoveNum]