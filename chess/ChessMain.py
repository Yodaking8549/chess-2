import pygame
pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
StartFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
lightColor = 240, 216, 192
darkColor = 168, 121, 101
SquareHighlightColor = 217, 162, 13, 120
turn = "w"
    
if SCREEN_WIDTH <= SCREEN_HEIGHT:
    SmallestValue = SCREEN_WIDTH
else:
    SmallestValue = SCREEN_HEIGHT

square_height = SmallestValue // 8
square_width = SmallestValue // 8

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
transparent = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)


def ClearVariables():
    global PieceDropped
    PieceDropped = 0
    global MoveChosen
    MoveChosen = 0
    global ClickedSquare
    ClickedSquare = 0
    global Dragmode
    Dragmode = 0
    global OldSquare
    OldSquare = -1
    global NewSquare
    NewSquare = -1
    global DraggedPiece
    DraggedPiece = 0

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

def SummonPieceFromBoardArray(n, piece_x, piece_y):
    if board[n] == WhiteKing:
        screen.blit(WhiteKing_png, (piece_x, piece_y))
    elif board[n] == BlackKing:
        screen.blit(BlackKing_png, (piece_x, piece_y))
    elif board[n] == WhitePawn:
        screen.blit(WhitePawn_png, (piece_x, piece_y))
    elif board[n] == BlackPawn:
        screen.blit(BlackPawn_png, (piece_x, piece_y))
    elif board[n] == WhiteKnight:
        screen.blit(WhiteKnight_png, (piece_x, piece_y))
    elif board[n] == BlackKnight:
        screen.blit(BlackKnight_png, (piece_x, piece_y))
    elif board[n] == WhiteBishop:
        screen.blit(WhiteBishop_png, (piece_x, piece_y))
    elif board[n] == BlackBishop:
        screen.blit(BlackBishop_png, (piece_x, piece_y))
    elif board[n] == WhiteRook:
        screen.blit(WhiteRook_png, (piece_x, piece_y))
    elif board[n] == BlackRook:
        screen.blit(BlackRook_png, (piece_x, piece_y))
    elif board[n] == WhiteQueen:
        screen.blit(WhiteQueen_png, (piece_x, piece_y))
    elif board[n] == BlackQueen:
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
        
def DrawPieces():
    for i in range(64):
        file = i % 8
        rank = i // 8
        piece_x = file * square_width
        piece_y = rank * square_height
        SummonPieceFromBoardArray(i, piece_x, piece_y)

def FenToBoard(fen):
    rank = 0
    file = 0
    for i in range(len(fen)):
        if fen[i] == " ":
            break
        elif fen[i] == "/":
            rank += 1
            file = 0
        elif fen[i].isdigit():
            for j in range(int(fen[i])):
                board[rank * 8 + file] = Empty
                file += 1
        else:
            board[rank * 8 + file] = fen[i]
            file += 1

def MakeBoardUsable():
    for i in range(len(board)):
        if board[i] == "0":
            board[i] = "0"
        elif board[i] == "K":
            board[i] = WhiteKing
        elif board[i] == "k":
            board[i] = BlackKing
        elif board[i] == "P":
            board[i] = WhitePawn
        elif board[i] == "p":
            board[i] = BlackPawn
        elif board[i] == "N":
            board[i] = WhiteKnight
        elif board[i] == "n":
            board[i] = BlackKnight
        elif board[i] == "B":
            board[i] = WhiteBishop
        elif board[i] == "b":
            board[i] = BlackBishop
        elif board[i] == "R":
            board[i] = WhiteRook
        elif board[i] == "r":
            board[i] = BlackRook
        elif board[i] == "Q":
            board[i] = WhiteQueen
        elif board[i] == "q":
            board[i] = BlackQueen
    
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
        board[ClickedSquare] = Empty
        
def PutPieceUnderMouseCurser():
    piece_x = pygame.mouse.get_pos()[0] - square_width / 2
    piece_y = pygame.mouse.get_pos()[1] - square_height / 2
    SummonPieceFromName(DraggedPiece, piece_x, piece_y)

def PutPieceOnNewSquare():
    global Dragmode
    global OldSquare
    global NewSquare
    global Move
    OldSquare = ClickedSquare
    NewSquare = GetSquareUnderMouse()
    legal_moves = GetLegalMoves()
    Move = str(OldSquare) + str(NewSquare)
    if Move in str(legal_moves):
        if Dragmode == 1:
            if OldSquare != NewSquare:
                if board[NewSquare] == Empty:
                    pygame.mixer.music.load("chess/sounds/move.mp3")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("chess/sounds/capture.mp3")
                    pygame.mixer.music.play()
                board[NewSquare] = DraggedPiece
                board[OldSquare] = Empty
            else:
                board[OldSquare] = DraggedPiece
                OldSquare = -1
                NewSquare = -1
            Dragmode = 0
            HighlightMoveSquares()

def HighlightSquare(squarenumber):
    file = squarenumber % 8
    rank = squarenumber // 8
    square_x = file * square_width
    square_y = rank * square_height
    square = pygame.Rect((square_x, square_y, square_width, square_height))
    pygame.draw.rect(transparent, SquareHighlightColor, square)
    
def HighlightMoveSquares():
    global PervHighlightSquare
    global PervHighlightSquare2
    HighlightSquare(OldSquare)
    HighlightSquare(NewSquare)
    PervHighlightSquare = OldSquare
    PervHighlightSquare2 = NewSquare

def GetLegalMoves():
    legal_moves = []
    for i in range(64):
        if turn == "w":
            if board[i] == WhiteKing:
                legal_moves += GetKingMoves(i)
            elif board[i] == WhitePawn:
                legal_moves += GetPawnMoves(i)
            elif board[i] == WhiteKnight:
                legal_moves += GetKnightMoves(i)
            elif board[i] == WhiteBishop:
                legal_moves += GetBishopMoves(i)
            elif board[i] == WhiteRook:
                legal_moves += GetRookMoves(i)
            elif board[i] == WhiteQueen:
                legal_moves += GetQueenMoves(i)
        else:
            if board[i] == BlackKing:
                legal_moves += GetKingMoves(i)
            elif board[i] == BlackPawn:
                legal_moves += GetPawnMoves(i)
            elif board[i] == BlackKnight:
                legal_moves += GetKnightMoves(i)
            elif board[i] == BlackBishop:
                legal_moves += GetBishopMoves(i)
            elif board[i] == BlackRook:
                legal_moves += GetRookMoves(i)
            elif board[i] == BlackQueen:
                legal_moves += GetQueenMoves(i)

def GetPawnMoves(i):
    pass

def GetKnightMoves():
    pass

def GetBishopMoves():
    pass

def GetRookMoves():
    pass

def GetQueenMoves():
    pass

def GetKingMoves():
    pass

WhiteKing_png = pygame.image.load("chess/images/wK.png")
WhiteKing_png = pygame.transform.scale(WhiteKing_png, (int(square_width), int(square_height)))
BlackKing_png = pygame.image.load("chess/images/bK.png")
BlackKing_png = pygame.transform.scale(BlackKing_png, (int(square_width), int(square_height)))
WhitePawn_png = pygame.image.load("chess/images/wP.png")
WhitePawn_png = pygame.transform.scale(WhitePawn_png, (int(square_width), int(square_height)))
BlackPawn_png = pygame.image.load("chess/images/bP.png")
BlackPawn_png = pygame.transform.scale(BlackPawn_png, (int(square_width), int(square_height)))
WhiteKnight_png = pygame.image.load("chess/images/wN.png")
WhiteKnight_png = pygame.transform.scale(WhiteKnight_png, (int(square_width), int(square_height)))
BlackKnight_png = pygame.image.load("chess/images/bN.png")
BlackKnight_png = pygame.transform.scale(BlackKnight_png, (int(square_width), int(square_height)))
WhiteBishop_png = pygame.image.load("chess/images/wB.png")
WhiteBishop_png = pygame.transform.scale(WhiteBishop_png, (int(square_width), int(square_height)))
BlackBishop_png = pygame.image.load("chess/images/bB.png")
BlackBishop_png = pygame.transform.scale(BlackBishop_png, (int(square_width), int(square_height)))
WhiteRook_png = pygame.image.load("chess/images/wR.png")
WhiteRook_png = pygame.transform.scale(WhiteRook_png, (int(square_width), int(square_height)))
BlackRook_png = pygame.image.load("chess/images/bR.png")
BlackRook_png = pygame.transform.scale(BlackRook_png, (int(square_width), int(square_height)))
WhiteQueen_png = pygame.image.load("chess/images/wQ.png")
WhiteQueen_png = pygame.transform.scale(WhiteQueen_png, (int(square_width), int(square_height)))
BlackQueen_png = pygame.image.load("chess/images/bQ.png")
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

board = [0 for row in range(64)]

ClearVariables()
CreateGraphicalBoard()
FenToBoard(StartFEN)
MakeBoardUsable()
DrawPieces()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                RemovePieceFromClickedSquare()
            if event.button == 3:
                mousesquare = GetSquareUnderMouse()
                print(mousesquare)
            
        if event.type == pygame.MOUSEBUTTONUP:
            PutPieceOnNewSquare()
    
    if MoveChosen == 1:
        screen.blit(transparent, (0, 0))
        DrawPieces()
        MoveChosen = 0
        
    if Dragmode == 1:
        CreateGraphicalBoard()
        DrawPieces()
        PutPieceUnderMouseCurser()
    else:
        CreateGraphicalBoard()
        HighlightMoveSquares()
        screen.blit(transparent, (0, 0))
        DrawPieces()
    
    pygame.display.flip()
pygame.quit()