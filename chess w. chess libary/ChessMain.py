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
                displayingboard[rank * 8 + file] = Empty
                file += 1
        else:
            board[rank * 8 + file] = fen[i]
            displayingboard[rank * 8 + file] = fen[i]
            file += 1
    
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
    OldSquare = ClickedSquare
    NewSquare = GetSquareUnderMouse()
    Move = str(OldSquare) + str(NewSquare)
    if Move in str(legal_moves):
        print(Move)
        if Dragmode == 1:
            legal_move = 1
            if OldSquare != NewSquare:
                if board[NewSquare] == Empty:
                    pygame.mixer.music.load("chess w. chess libary/sounds/move.mp3")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("chess w. chess libary/sounds/capture.mp3")
                    pygame.mixer.music.play()
                board[NewSquare] = DraggedPiece
                board[OldSquare] = Empty
                displayingboard[NewSquare] = DraggedPiece
                displayingboard[OldSquare] = Empty
                if turn == "w":
                    turn = "b"
                elif turn == "b":
                    turn = "w"
            else:
                board[OldSquare] = DraggedPiece
                displayingboard[OldSquare] = DraggedPiece
                OldSquare = -1
                NewSquare = -1
            Dragmode = 0
            HighlightMoveSquares()
    else:
        if Dragmode == 1:
            board[OldSquare] = DraggedPiece
            displayingboard[OldSquare] = DraggedPiece
            Dragmode = 0
            legal_move = 0
            if OldSquare != NewSquare:
                pygame.mixer.music.load("chess w. chess libary/sounds/illegal.mp3")
                pygame.mixer.music.play()
        else:
            pass

def HighlightSquare(squarenumber, color):
    file = squarenumber % 8
    rank = squarenumber // 8
    square_x = file * square_width
    square_y = rank * square_height
    square = pygame.Rect((square_x, square_y, square_width, square_height))
    pygame.draw.rect(transparent, color, square)
    
def HighlightMoveSquares():
    global PervHighlightSquare
    global PervHighlightSquare2
    HighlightSquare(OldSquare, MoveSquareHighlightColor)
    HighlightSquare(NewSquare, MoveSquareHighlightColor)
    PervHighlightSquare = OldSquare
    PervHighlightSquare2 = NewSquare
    
def MarkLegalMoves():
    GetLegalMoves("single", GetSquareUnderMouse())
    for i in range(len(legal_moves)):
        NewSquare = int(legal_moves[i][2])
        NewSquare = str(NewSquare) + str(int(legal_moves[i][3]))
        NewSquare = int(NewSquare)
        HighlightSquare((NewSquare), PossibleSquareHighlightColor)
        
def GetLegalMoves(mode, squarenumber):
    global legal_moves
    legal_moves = []
    if mode == "all":
        for i in range(64):
            if turn == "w":
                if board[i] == WhiteKing:
                    GetKingMoves(i)
                elif board[i] == WhitePawn:
                    GetPawnMoves(i)
                elif board[i] == WhiteKnight:
                    GetKnightMoves(i)
                elif board[i] == WhiteBishop:
                    GetBishopMoves(i)
                elif board[i] == WhiteRook:
                    GetRookMoves(i)
                elif board[i] == WhiteQueen:
                    GetQueenMoves(i)
            elif turn == "b":
                if board[i] == BlackKing:
                    GetKingMoves(i)
                elif board[i] == BlackPawn:
                    GetPawnMoves(i)
                elif board[i] == BlackKnight:
                    GetKnightMoves(i)
                elif board[i] == BlackBishop:
                    GetBishopMoves(i)
                elif board[i] == BlackRook:
                    GetRookMoves(i)
                elif board[i] == BlackQueen:
                    GetQueenMoves(i)
            else:
                pass
    elif mode == "single":
        if turn == "w":
            if board[squarenumber] == WhiteKing:
                GetKingMoves(squarenumber)
            elif board[squarenumber] == WhitePawn:
                GetPawnMoves(squarenumber)
            elif board[squarenumber] == WhiteKnight:
                GetKnightMoves(squarenumber)
            elif board[squarenumber] == WhiteBishop:
                GetBishopMoves(squarenumber)
            elif board[squarenumber] == WhiteRook:
                GetRookMoves(squarenumber)
            elif board[squarenumber] == WhiteQueen:
                GetQueenMoves(squarenumber)
        elif turn == "b":
            if board[squarenumber] == BlackKing:
                GetKingMoves(squarenumber)
            elif board[squarenumber] == BlackPawn:
                GetPawnMoves(squarenumber)
            elif board[squarenumber] == BlackKnight:
                GetKnightMoves(squarenumber)
            elif board[squarenumber] == BlackBishop:
                GetBishopMoves(squarenumber)
            elif board[squarenumber] == BlackRook:
                GetRookMoves(squarenumber)
            elif board[squarenumber] == BlackQueen:
                GetQueenMoves(squarenumber)
        else:
            pass
        

def GetPawnMoves(i):
    global legal_moves
    global turn
    rank = i // 8
    file = i % 8
    if turn == "w":
        if board[i - 8] == Empty:
            legal_moves.append(str(i) + str(i - 8))
            if rank == 6 and board[i - 16] == Empty:
                legal_moves.append(str(i) + str(i - 16))
        if file >= 1 and file <= 6:
            if board[i - 7] != Empty:
                legal_moves.append(str(i) + str(i - 7))
            if board[i - 9] != Empty:
                legal_moves.append(str(i) + str(i - 9))
        if file == 0:
            legal_moves.append(str(i) + str(i - 9))
        if file == 7:
            legal_moves.append(str(i) + str(i - 7))
    elif turn == "b":
        if board[i + 8] == Empty:
            legal_moves.append(str(i) + str(i + 8))
            if rank == 1 and board[i - 16] == Empty:
                legal_moves.append(str(i) + str(i + 16))
        if file >= 1 and file <= 6:
            if board[i + 7] != Empty:
                legal_moves.append(str(i) + str(i + 7))
            if board[i + 9] != Empty:
                legal_moves.append(str(i) + str(i + 9)) 
        if file == 0:
            legal_moves.append(str(i) + str(i + 9))
        if file == 7:
            legal_moves.append(str(i) + str(i + 7))
            
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

board = [0 for row in range(64)]
displayingboard = [0 for row in range(64)]

ClearVariables()
CreateGraphicalBoard()
board = chess.Board(StartFEN)
displayingboard = StartFEN
DrawPieces()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                RemovePieceFromClickedSquare()
                MarkLegalMoves()                            # Marks legal moves (temporary)
            if event.button == 3:
                mousesquare = GetSquareUnderMouse()
                print(mousesquare)
            
        if event.type == pygame.MOUSEBUTTONUP:
            if Dragmode == 1:
                PutPieceOnNewSquare()
    
    if MoveChosen == 1:
        screen.blit(transparent, (0, 0))
        DrawPieces()
        MoveChosen = 0
        
    if Dragmode == 1:
        CreateGraphicalBoard()
        DrawPieces()
        PutPieceUnderMouseCurser()
        screen.blit(transparent, (0, 0))
    else:
        CreateGraphicalBoard() 
        HighlightMoveSquares()
        screen.blit(transparent, (0, 0))
        DrawPieces()
    
    pygame.display.flip()
pygame.quit()