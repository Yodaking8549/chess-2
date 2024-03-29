import chess
from random import randint

def GetSound():
    if board.is_check == True:
        return "Check"
    elif Capture == True:
        return "Capture"
    elif board.is_check == True:
        return "Check"
    else:
        return "Move"

def GetAIMove(inputBoard):
    global board
    global Capture
    global Check
    Capture = False
    board = chess.Board(inputBoard)
    NumLegalMoves = board.legal_moves.count()
    if board.is_game_over() == False:
        MoveNum = randint(0, NumLegalMoves - 1)
        Move = list(board.legal_moves)[MoveNum]
        if board.is_capture(Move) == True:
            Capture = True
        return Move.uci()
    else:
        return "Game Over"