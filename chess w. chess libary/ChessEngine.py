import chess
from random import randint

def GetAIMove(inputBoard, AIDifficulty):
    global board
    global Capture
    Capture = False
    board = chess.Board(inputBoard)
    if AIDifficulty == 0:
        GetRandomMove()
    if AIDifficulty == 1:
        GetDepthOneMove()
    if AIDifficulty == 2:
        GetMinimaxMove()
    return Move.uci()
    
def GetRandomMove():
    global board
    global Move
    NumLegalMoves = board.legal_moves.count()
    MoveNum = randint(0, NumLegalMoves - 1)
    Move = list(board.legal_moves)[MoveNum]
    
def GetDepthOneMove():
    print("Difficulty 1 not implemented yet")
    exit()

def GetMinimaxMove():
    print("Difficulty 2 not implemented yet")
    exit()