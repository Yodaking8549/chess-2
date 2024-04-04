import chess
from random import randint
import math

pawnValue = 100
knightValue = 320
bishopValue = 330
rookValue = 500
queenValue = 900
# kingValue = int(math.inf)

def CountMaterialForTurn(color) -> int:
    OwnMaterial = 0
    EnemieMaterial = 0
    OwnMaterial = CountMaterialOfColor(color)
    EnemieMaterial = CountMaterialOfColor(not color)
    MaterialForTurn = OwnMaterial - EnemieMaterial
    return MaterialForTurn

def CountMaterialOfColor(color):
    Material = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None and piece.color == color:
            if piece.piece_type == chess.PAWN:
                Material += pawnValue
            if piece.piece_type == chess.KNIGHT:
                Material += knightValue
            if piece.piece_type == chess.BISHOP:
                Material += bishopValue
            if piece.piece_type == chess.ROOK:
                Material += rookValue
            if piece.piece_type == chess.QUEEN:
                Material += queenValue
            # if piece.piece_type == chess.KING:
            #     Material += kingValue
            
    return Material

def EvaluateBoard():
    Eval = 0
    Eval += CountMaterialForTurn(board.turn)
    return Eval

def GetAIMove(inputBoard, AIDifficulty):
    global board
    global Capture
    Capture = False
    board = chess.Board(inputBoard)
    if AIDifficulty == 0:
        GetRandomMove()
    if AIDifficulty == 1:
        GetMinimaxMove(1)
    if AIDifficulty == 2:
        GetMinimaxMove(2)
    return Move.uci()
    
def GetRandomMove():
    global board
    global Move
    NumLegalMoves = board.legal_moves.count()
    MoveNum = randint(0, NumLegalMoves - 1)
    Move = list(board.legal_moves)[MoveNum]
    
def GetMinimaxMove(depth):
    global board
    global Move
    global Capture
    global BestEval
    BestEval = -math.inf
    for move in board.legal_moves:
        board.push(move)
        Eval = Minimax(-math.inf, math.inf, board, depth, False)
        board.pop()
        if Eval > BestEval:
            BestEval = Eval
            Move = move

def Minimax(alpha, beta, board, depth, isMaximizing):
    global Capture
    if depth == 0:
        return EvaluateBoard()
    if isMaximizing:
        maxEval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            Eval = Minimax(alpha, beta, board, depth - 1, False)
            board.pop()
            maxEval = max(maxEval, Eval)
            alpha = max(alpha, Eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        for move in board.legal_moves:
            board.push(move)
            Eval = Minimax(alpha, beta, board, depth - 1, True)
            board.pop()
            minEval = min(minEval, Eval)
            beta = min(beta, Eval)
            if beta <= alpha:
                break
        return minEval