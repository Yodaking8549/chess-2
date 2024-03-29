import pygame
import chess
pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
StartFEN = "8/pppppppp/8/8/8/8/PPPPPPPP/8"
lightColor = 240, 216, 192
darkColor = 168, 121, 101
MoveSquareHighlightColor = 217, 162, 13, 120
PossibleSquareHighlightColor = 0, 255, 0, 120
turn = "w"
    
if SCREEN_WIDTH <= SCREEN_HEIGHT:
    SmallestValue = SCREEN_WIDTH
else:
    SmallestValue = SCREEN_HEIGHT

square_height = SmallestValue // 8
square_width = SmallestValue // 8

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
transparent = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

def CreateGraphicalBoard():
    rank = 0
    for i in range(64):
        file = i % 8
        square_x = file * square_width
        square_y = rank * square_height

        if (file + rank) % 2 == 0:
            SquareColor = lightColor
        else:
            SquareColor = darkColor

        square = pygame.Rect((square_x, square_y, square_width, square_height))
        pygame.draw.rect(screen, SquareColor, square)

        if file == 7:
            rank += 1

def BoardFENToDisplayingBoard(FEN):
    rank = 0
    file = 0
    for i in range(len(FEN)):
        if FEN[i] == " ":
            break
        elif FEN[i] == "/":
            rank += 1
            file = 0
        elif FEN[i].isdigit():
            for j in range(int(FEN[i])):
                displayingboard[rank * 8 + file] = Empty
                file += 1
        else:
            displayingboard[rank * 8 + file] = FEN[i]
            file += 1

def DrawPieces():
    for i in range(64):
        file = i % 8
        rank = i // 8
        piece_x = file * square_width
        piece_y = rank * square_height
        SummonPieceFromBoardArray(i, piece_x, piece_y)
        
def SummonPieceFromBoardArray(n, piece_x, piece_y):
    if displayingboard[n] == "K":
        screen.blit(WhiteKing_png, (piece_x, piece_y))
    elif displayingboard[n] == "k":
        screen.blit(BlackKing_png, (piece_x, piece_y))
    elif displayingboard[n] == "P":
        screen.blit(WhitePawn_png, (piece_x, piece_y))
    elif displayingboard[n] == "p":
        screen.blit(BlackPawn_png, (piece_x, piece_y))
    elif displayingboard[n] == "N":
        screen.blit(WhiteKnight_png, (piece_x, piece_y))
    elif displayingboard[n] == "n":
        screen.blit(BlackKnight_png, (piece_x, piece_y))
    elif displayingboard[n] == "B":
        screen.blit(WhiteBishop_png, (piece_x, piece_y))
    elif displayingboard[n] == "b":
        screen.blit(BlackBishop_png, (piece_x, piece_y))
    elif displayingboard[n] == "R":
        screen.blit(WhiteRook_png, (piece_x, piece_y))
    elif displayingboard[n] == "r":
        screen.blit(BlackRook_png, (piece_x, piece_y))
    elif displayingboard[n] == "Q":
        screen.blit(WhiteQueen_png, (piece_x, piece_y))
    elif displayingboard[n] == "q":
        screen.blit(BlackQueen_png, (piece_x, piece_y))
    
def GetSquareUnderMouse():
    x, y = pygame.mouse.get_pos()
    file = x // square_width
    rank = y // square_height
    return rank * 8 + file

def RemovePieceFromClickedSquare():
    global ClickedSquare
    global Dragmode
    global DraggedPiece
    ClickedSquare = GetSquareUnderMouse()
    transparent.fill((0, 0, 0, 0))
    if turn == "w" and board[ClickedSquare][0] == "w" or turn == "b" and board[ClickedSquare][0] == "b":
        if board[ClickedSquare] != Empty:
            file = ClickedSquare % 8
            rank = ClickedSquare // 8
            
            if (file + rank) % 2 == 0:
                SquareColor = lightColor
            else:
                SquareColor = darkColor
            
            square_x = file * square_width
            square_y = rank * square_height

            square = pygame.Rect((square_x, square_y, square_width, square_height))
            pygame.draw.rect(screen, SquareColor, square)
            
            Dragmode = 1
            DraggedPiece = board[ClickedSquare]
            displayingboard[ClickedSquare] = Empty
    elif board[ClickedSquare] != Empty:
        print("Not your turn")
        
def PutPieceUnderMouseCurser():
    pass

def PutPieceOnNewSquare():
    pass

def HighlightSquare(squarenumber, color):
    file = squarenumber % 8
    rank = squarenumber // 8
    square_x = file * square_width
    square_y = rank * square_height
    square = pygame.Rect((square_x, square_y, square_width, square_height))
    pygame.draw.rect(transparent, color, square)
    
def HighlightMoveSquares():
    pass
    
def MarkLegalMoves():
    pass

def ClearVariables():
    pass
            
def DisplayBoard():
    BoardFENToDisplayingBoard(board.fen())
    DrawPieces()

WhiteKing_png = pygame.image.load("chess w. chess libary/images/wK.png")
WhiteKing_png = pygame.transform.scale(WhiteKing_png, (int(square_width), int(square_height)))
BlackKing_png = pygame.image.load("chess w. chess libary/images/bK.png")
BlackKing_png = pygame.transform.scale(BlackKing_png, (int(square_width), int(square_height)))
WhitePawn_png = pygame.image.load("chess w. chess libary/images/wP.png")
WhitePawn_png = pygame.transform.scale(WhitePawn_png, (int(square_width), int(square_height)))
BlackPawn_png = pygame.image.load("chess w. chess libary/images/bP.png")
BlackPawn_png = pygame.transform.scale(BlackPawn_png, (int(square_width), int(square_height)))
WhiteKnight_png = pygame.image.load("chess w. chess libary/images/wN.png")
WhiteKnight_png = pygame.transform.scale(WhiteKnight_png, (int(square_width), int(square_height)))
BlackKnight_png = pygame.image.load("chess w. chess libary/images/bN.png")
BlackKnight_png = pygame.transform.scale(BlackKnight_png, (int(square_width), int(square_height)))
WhiteBishop_png = pygame.image.load("chess w. chess libary/images/wB.png")
WhiteBishop_png = pygame.transform.scale(WhiteBishop_png, (int(square_width), int(square_height)))
BlackBishop_png = pygame.image.load("chess w. chess libary/images/bB.png")
BlackBishop_png = pygame.transform.scale(BlackBishop_png, (int(square_width), int(square_height)))
WhiteRook_png = pygame.image.load("chess w. chess libary/images/wR.png")
WhiteRook_png = pygame.transform.scale(WhiteRook_png, (int(square_width), int(square_height)))
BlackRook_png = pygame.image.load("chess w. chess libary/images/bR.png")
BlackRook_png = pygame.transform.scale(BlackRook_png, (int(square_width), int(square_height)))
WhiteQueen_png = pygame.image.load("chess w. chess libary/images/wQ.png")
WhiteQueen_png = pygame.transform.scale(WhiteQueen_png, (int(square_width), int(square_height)))
BlackQueen_png = pygame.image.load("chess w. chess libary/images/bQ.png")
BlackQueen_png = pygame.transform.scale(BlackQueen_png, (int(square_width), int(square_height)))
            
                        
Empty = "0"
WhiteKing = "wK"
BlackKing = "bK"
WhitePawn = "wP"
BlackPawn = "bP"
WhiteKnight = "wN"
BlackKnight = "bN"
WhiteBishop = "wB"
BlackBishop = "bB"
WhiteRook = "wR"
BlackRook = "bR"
WhiteQueen = "wQ"
BlackQueen = "bQ"

displayingboard = [0 for row in range(64)]

ClearVariables()
CreateGraphicalBoard()
board = chess.Board(StartFEN)
DisplayBoard()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                RemovePieceFromClickedSquare()
            if event.button == 3:
                mousesquare = GetSquareUnderMouse() # Gets the square number under the mouse (For Testing Purposes)
                print(mousesquare)
            
        if event.type == pygame.MOUSEBUTTONUP:
            pass
    
    pygame.display.flip()
pygame.quit()