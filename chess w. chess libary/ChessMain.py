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
PossibleMovesSquareHighlightColor = 0, 255, 0, 120
HighlightPossibleMoves = 0
    
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
            
def MakeBoardListUsable(listname):
    for i in range(len(listname)):
        if listname[i] == "0":
            listname[i] = "0"
        elif listname[i] == "K":
            listname[i] = WhiteKing
        elif listname[i] == "k":
            listname[i] = BlackKing
        elif listname[i] == "P":
            listname[i] = WhitePawn
        elif listname[i] == "p":
            listname[i] = BlackPawn
        elif listname[i] == "N":
            listname[i] = WhiteKnight
        elif listname[i] == "n":
            listname[i] = BlackKnight
        elif listname[i] == "B":
            listname[i] = WhiteBishop
        elif listname[i] == "b":
            listname[i] = BlackBishop
        elif listname[i] == "R":
            listname[i] = WhiteRook
        elif listname[i] == "r":
            listname[i] = BlackRook
        elif listname[i] == "Q":
            listname[i] = WhiteQueen
        elif listname[i] == "q":
            listname[i] = BlackQueen

def DrawPieces():
    for i in range(64):
        file = i % 8
        rank = i // 8
        piece_x = file * square_width
        piece_y = rank * square_height
        SummonPieceFromBoardArray(i, piece_x, piece_y)
        
def SummonPieceFromBoardArray(n, piece_x, piece_y):
    if displayingboard[n] == WhiteKing:
        screen.blit(WhiteKing_png, (piece_x, piece_y))
    elif displayingboard[n] == BlackKing:
        screen.blit(BlackKing_png, (piece_x, piece_y))
    elif displayingboard[n] == WhitePawn:
        screen.blit(WhitePawn_png, (piece_x, piece_y))
    elif displayingboard[n] == BlackPawn:
        screen.blit(BlackPawn_png, (piece_x, piece_y))
    elif displayingboard[n] == WhiteKnight:
        screen.blit(WhiteKnight_png, (piece_x, piece_y))
    elif displayingboard[n] == BlackKnight:
        screen.blit(BlackKnight_png, (piece_x, piece_y))
    elif displayingboard[n] == WhiteBishop:
        screen.blit(WhiteBishop_png, (piece_x, piece_y))
    elif displayingboard[n] == BlackBishop:
        screen.blit(BlackBishop_png, (piece_x, piece_y))
    elif displayingboard[n] == WhiteRook:
        screen.blit(WhiteRook_png, (piece_x, piece_y))
    elif displayingboard[n] == BlackRook:
        screen.blit(BlackRook_png, (piece_x, piece_y))
    elif displayingboard[n] == WhiteQueen:
        screen.blit(WhiteQueen_png, (piece_x, piece_y))
    elif displayingboard[n] == BlackQueen:
        screen.blit(BlackQueen_png, (piece_x, piece_y))
        
def SummonPieceFromName(name, piece_x, piece_y):
    if name == WhiteKing:
        screen.blit(WhiteKing_png, (piece_x, piece_y))
    elif name == BlackKing:
        screen.blit(BlackKing_png, (piece_x, piece_y))
    elif name == WhitePawn:
        screen.blit(WhitePawn_png, (piece_x, piece_y))
    elif name == BlackPawn:
        screen.blit(BlackPawn_png, (piece_x, piece_y))
    elif name == WhiteKnight:
        screen.blit(WhiteKnight_png, (piece_x, piece_y))
    elif name == BlackKnight:
        screen.blit(BlackKnight_png, (piece_x, piece_y))
    elif name == WhiteBishop:
        screen.blit(WhiteBishop_png, (piece_x, piece_y))
    elif name == BlackBishop:
        screen.blit(BlackBishop_png, (piece_x, piece_y))
    elif name == WhiteRook:
        screen.blit(WhiteRook_png, (piece_x, piece_y))
    elif name == BlackRook:
        screen.blit(BlackRook_png, (piece_x, piece_y))
    elif name == WhiteQueen:
        screen.blit(WhiteQueen_png, (piece_x, piece_y))
    elif name == BlackQueen:
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
    if turn == chess.WHITE and displayingboard[ClickedSquare][0] == "w" or turn == chess.BLACK and displayingboard[ClickedSquare][0] == "b":
        if displayingboard[ClickedSquare] != Empty:
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
            DraggedPiece = displayingboard[ClickedSquare]
            displayingboard[ClickedSquare] = Empty
    elif displayingboard[ClickedSquare] != Empty:
        print("Not your turn")
        
def PutPieceUnderMouseCurser():
    piece_x = pygame.mouse.get_pos()[0] - square_width / 2
    piece_y = pygame.mouse.get_pos()[1] - square_height / 2
    SummonPieceFromName(DraggedPiece, piece_x, piece_y)

def PutPieceOnNewSquare():
    global Dragmode
    global OldSquare
    global NewSquare
    global Move
    global legal_move
    global turn
    SquareDict = {
        0: "a8", 1: "b8", 2: "c8", 3: "d8", 4: "e8", 5: "f8", 6: "g8", 7: "h8",
        8: "a7", 9: "b7", 10: "c7", 11: "d7", 12: "e7", 13: "f7", 14: "g7", 15: "h7",
        16: "a6", 17: "b6", 18: "c6", 19: "d6", 20: "e6", 21: "f6", 22: "g6", 23: "h6",
        24: "a5", 25: "b5", 26: "c5", 27: "d5", 28: "e5", 29: "f5", 30: "g5", 31: "h5",
        32: "a4", 33: "b4", 34: "c4", 35: "d4", 36: "e4", 37: "f4", 38: "g4", 39: "h4",
        40: "a3", 41: "b3", 42: "c3", 43: "d3", 44: "e3", 45: "f3", 46: "g3", 47: "h3",
        48: "a2", 49: "b2", 50: "c2", 51: "d2", 52: "e2", 53: "f2", 54: "g2", 55: "h2",
        56: "a1", 57: "b1", 58: "c1", 59: "d1", 60: "e1", 61: "f1", 62: "g1", 63: "h1"
    }
    OldSquare = ClickedSquare
    NewSquare = GetSquareUnderMouse()
    DynamicOldSquare = SquareDict[OldSquare]
    DynamicNewSquare = SquareDict[NewSquare]
    if OldSquare != NewSquare:
        Move = chess.Move.from_uci(DynamicOldSquare + DynamicNewSquare)
        if Move in board.legal_moves:
            legal_move = 1
            if IsCapture() == False:
                pygame.mixer.music.load("chess w. chess libary/sounds/move.mp3")
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.load("chess w. chess libary/sounds/capture.mp3")
                pygame.mixer.music.play()
            board.push(Move)
            turn = not turn
            Dragmode = 0
        else:
            if Dragmode == 1:
                displayingboard[OldSquare] = DraggedPiece
                Dragmode = 0
                if OldSquare != NewSquare:
                    pygame.mixer.music.load("chess w. chess libary/sounds/illegal.mp3")
                    pygame.mixer.music.play()
            legal_move = 0
    else:
        displayingboard[OldSquare] = DraggedPiece
        OldSquare = -1
        NewSquare = -1
        Dragmode = 0

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
    if HighlightPossibleMoves == 1:
        for move in board.legal_moves:
            HighlightSquare(int(move.to_square), PossibleMovesSquareHighlightColor)

def IsCapture() -> bool:
    if displayingboard[NewSquare] != Empty:
        return True
    # elif has_legal_en_passant() == True:
    #     if ep_squre == NewSquare:
    #         return True
    else:    
        return False

def ClearVariables():
    global Dragmode
    Dragmode = 0
    global EnPassantSquare
    EnPassantSquare = -1
            
def ReloadDisplayingBoardlistFromFEN():
    BoardFENToDisplayingBoard(board.fen())
    MakeBoardListUsable(displayingboard)

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
turn = chess.WHITE
board = chess.Board(StartFEN)
ClearVariables()
CreateGraphicalBoard()
ReloadDisplayingBoardlistFromFEN()
DrawPieces()

run = True
while run:
    CreateGraphicalBoard()
    DrawPieces()
    
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
            if event.button == 1:
                PutPieceOnNewSquare()
                ReloadDisplayingBoardlistFromFEN()
    if Dragmode == 1:
        PutPieceUnderMouseCurser()
    pygame.display.flip()
pygame.quit()