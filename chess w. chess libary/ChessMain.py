import pygame
import chess
import time
from ChessEngine import GetAIMove
pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
StartFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
lightColor = 240, 216, 192
darkColor = 168, 121, 101
MoveSquareHighlightColor = 217, 162, 13, 100
PossibleMovesSquareHighlightColor = 0, 255, 0, 120
HighlightPossibleMoves = 0
MemeMode = 0
Gamemode = "PvAI"
AIvAITimeDelay = 0.2
if Gamemode == "PvAI":
    Playercolor = chess.WHITE

if Gamemode == "PvP":
    Gamemode = 0
elif Gamemode == "PvAI":
    Gamemode = 1
elif Gamemode == "AIvAI":
    Gamemode = 2
else:
    print("Invalid Gamemode")
    exit()
    

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
    
def GetSquareUnderMouse() -> int:
    x, y = pygame.mouse.get_pos()
    file = x // square_width
    rank = y // square_height
    return rank * 8 + file

def PutPieceUnderMouseCurser():
    piece_x = pygame.mouse.get_pos()[0] - square_width / 2
    piece_y = pygame.mouse.get_pos()[1] - square_height / 2
    SummonPieceFromName(DraggedPiece, piece_x, piece_y)
    
def GetOldAndNewSquareFromMove(Move):
    if (Move is not None) and LegalMove == True:
        global OldSquare
        global NewSquare
        SquareDict = {
            "a8": 0, "b8": 1, "c8": 2, "d8": 3, "e8": 4, "f8": 5, "g8": 6, "h8": 7,
            "a7": 8, "b7": 9, "c7": 10, "d7": 11, "e7": 12, "f7": 13, "g7": 14, "h7": 15,
            "a6": 16, "b6": 17, "c6": 18, "d6": 19, "e6": 20, "f6": 21, "g6": 22, "h6": 23,
            "a5": 24, "b5": 25, "c5": 26, "d5": 27, "e5": 28, "f5": 29, "g5": 30, "h5": 31,
            "a4": 32, "b4": 33, "c4": 34, "d4": 35, "e4": 36, "f4": 37, "g4": 38, "h4": 39,
            "a3": 40, "b3": 41, "c3": 42, "d3": 43, "e3": 44, "f3": 45, "g3": 46, "h3": 47,
            "a2": 48, "b2": 49, "c2": 50, "d2": 51, "e2": 52, "f2": 53, "g2": 54, "h2": 55,
            "a1": 56, "b1": 57, "c1": 58, "d1": 59, "e1": 60, "f1": 61, "g1": 62, "h1": 63
        }
        uci_move = Move.uci()
        OldSquare = SquareDict[uci_move[:2]]
        NewSquare = SquareDict[uci_move[2:4]]
        
def HighlightSquare(squarenumber, color):
    file = squarenumber % 8
    rank = squarenumber // 8
    square_x = file * square_width
    square_y = rank * square_height
    square = pygame.Rect((square_x, square_y, square_width, square_height))
    pygame.draw.rect(transparent, color, square)
    
def HighlightMoveSquares():
    global LegalMove
    if LegalMove == True:
        HighlightSquare(OldSquare, MoveSquareHighlightColor)
        HighlightSquare(NewSquare, MoveSquareHighlightColor)
        LegalMove = False
    
def MarkLegalMoves():
    if HighlightPossibleMoves == 1:
        for move in board.legal_moves:
            HighlightSquare(int(move.to_square), PossibleMovesSquareHighlightColor)
    
def PlaySound(playsound: str):
    global GameOver
    global CountCheckmateSoundTimer
    if playsound == "Illegal":
        sounds[IllegalSound].play()
    elif playsound == "Capture":
        sounds[CaptureSound].play()
    elif playsound == "Move":
        sounds[MoveSound].play()
    elif playsound == "Check":
        sounds[CheckSound].play()
        if board.is_checkmate() == True:
            GameOver = True
            CountCheckmateSoundTimer = 1
    elif playsound == "Castle":
        sounds[CastleSound].play()
    elif playsound == "Promote":
        sounds[PromoteSound].play()

def CounterHandler():
    global CountCheckmateSoundTimer
    global CountBGMusicSoundTimer
    if CountCheckmateSoundTimer == 1:
        GameOverSoundHandler()
    if CountBGMusicSoundTimer == 1:
        BGMusicSoundHandler()
    
def GameOverSoundHandler():
    global CheckmateSoundTimer
    global CountCheckmateSoundTimer
    if CountCheckmateSoundTimer == 1:
        CheckmateSoundTimer += 1
        if CheckmateSoundTimer == 13:
            sounds[CheckmateSound].play()
            if MemeMode == 1:
                sounds[BackgroundMusic].stop()
            CountCheckmateSoundTimer = 0
            CheckmateSoundTimer = 0         
            
def BGMusicSoundHandler():
    global BGMusicSoundTimer
    global CountBGMusicSoundTimer
    if MemeMode == 1:
        if CountBGMusicSoundTimer == 1:
            BGMusicSoundTimer += 1
            if BGMusicSoundTimer == 300:
                sounds[BackgroundMusic].play()
                CountBGMusicSoundTimer = 0
                BGMusicSoundTimer = 0
                
def GetCorrectSound(PlayedMove):
    if isinstance(PlayedMove, str):
        PlayedMove = chess.Move.from_uci(PlayedMove)
    if isinstance(PlayedMove, chess.Move):
        if board.gives_check(PlayedMove):
            return "Check"
        elif board.is_capture(PlayedMove):
            return "Capture"
        elif board.is_castling(PlayedMove):
            return "Castle"
        elif len(str(PlayedMove)) > 4:
            return "Promote"
        else:
            return "Move"
   
def ClearVariables():
    global Dragmode
    Dragmode = 0
    global EnPassantSquare
    EnPassantSquare = -1
    global PlaySound
    playsound = "No Sound"
    global CheckmateSoundTimer
    CheckmateSoundTimer = 0
    global CountCheckmateSoundTimer
    CountCheckmateSoundTimer = 0
    global OldSquare
    OldSquare = -1
    global NewSquare
    NewSquare = -1
    global ClickedSquare
    ClickedSquare = -1
    global DraggedPiece
    DraggedPiece = Empty
    global Move
    Move = None
    global BGMusicSoundTimer
    BGMusicSoundTimer = 0
    global CountBGMusicSoundTimer
    CountBGMusicSoundTimer = 0
    global GameOver
    GameOver = False
    global TURN
    if Gamemode == 0 or (Gamemode == 1 and Playercolor == chess.WHITE):
        TURN = "Player"
    elif (Gamemode == 1 and Playercolor == chess.BLACK) or Gamemode == 2:
        TURN = "AI"
    global LegalMove
    LegalMove = False
    global HandledGameOver
    HandledGameOver = False
            
def ReloadDisplayingBoardlistFromFEN():
    BoardFENToDisplayingBoard(board.fen())
    MakeBoardListUsable(displayingboard)
    
def HandleGameOver():
    global HandledGameOver
    global GameOver
    global CountCheckmateSoundTimer
    if board.is_game_over() and not HandledGameOver:
        GameOver = True
        CountCheckmateSoundTimer = 1
        if board.is_checkmate():
            if Gamemode == 0:
                if board.turn == chess.WHITE:
                    print("Black wins by checkmate!")
                else:
                    print("White wins by checkmate!")
            elif Gamemode == 1:
                if board.turn == Playercolor:
                    print("AI wins by checkmate!")
                else:
                    print("You win by checkmate!")
        elif board.is_stalemate():
            print("Draw By Stalemate")
        elif board.is_insufficient_material():
            print("Draw By Insufficient Material")
        elif board.is_seventyfive_moves():
            print("Draw By Seventy Five Moves")
        elif board.is_fivefold_repetition():
            print("Draw By Fivefold Repetition")
        else:
            print("Draw By Other Reason")
        HandledGameOver = True
        
def GetPlayerMove() -> str:
    pass
                
def PickUpPiece():
    global ClickedSquare
    global DraggedPiece
    global Dragmode
    if TURN == "Player":
        if turn:
            ClickedSquare = GetSquareUnderMouse()
            DraggedPiece = displayingboard[ClickedSquare]
            if DraggedPiece[0] == "w":
                Dragmode = 1
                displayingboard[ClickedSquare] = Empty
            elif DraggedPiece[0] == "b":
                print("It's not your turn!")
        elif not turn:
            ClickedSquare = GetSquareUnderMouse()
            DraggedPiece = displayingboard[ClickedSquare]
            if DraggedPiece[0] == "b":
                Dragmode = 1
                displayingboard[ClickedSquare] = Empty
            elif DraggedPiece[0] == "w":
                print("It's not your turn!")

def PutDownPieceGetMove():
    global Dragmode
    global NewSquare
    global OldSquare
    if Dragmode == 1:
        Dragmode = 0
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
            if ValidateMove(Move):
                HandleValidMove(Move)
            else:
                HandleInvalidMove()
    
        
def ValidateMove(Move) -> bool:
    return Move.uci() in [move.uci() for move in board.legal_moves]
    
def HandleValidMove(playedMove: str):
    global Move
    global LegalMove
    displayingboard[NewSquare] = DraggedPiece
    Move = playedMove
    LegalMove = True
    transparent.fill((0, 0, 0, 0))
    
    
def HandleInvalidMove():
    global Move
    global LegalMove
    PlaySound("Illegal")
    displayingboard[ClickedSquare] = DraggedPiece
    Move = "Illegal"
    LegalMove = False
    
def PlayMoveAndSound():
    global Move
    global turn
    if ((Move != None) and (Move != "Illegal") and (Move != "Game Over")):
        if isinstance(Move, str):
            Move = chess.Move.from_uci(Move)
        if isinstance(Move, chess.Move):
            Sound = GetCorrectSound(Move)
            board.push(Move)
            PlaySound(Sound)
            turn = not turn

def GetMove():
    global TURN
    global board
    global Move
    global LegalMove
    if Gamemode == 0 or (Gamemode == 1 and Playercolor == turn):
        TURN = "Player"
    elif (Gamemode == 1 and Playercolor != turn) or Gamemode == 2:
        transparent.fill((0, 0, 0, 0))
        TURN = "AI"
        Move = GetAIMove(board.fen())
        LegalMove = True
        
def EventHandler():
    global TURN
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if TURN == "Player" and Dragmode == 0:
                    PickUpPiece()
            if event.button == 3:
                PrintDebugInfo()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if TURN == "Player" and Dragmode == 1:
                    PutDownPieceGetMove()
def PrintDebugInfo():
    print("TURN: ", TURN)
    print("turn: ", turn)
    print("Move: ", Move)
    print("board:")
    print(board)    
    
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
if MemeMode == 0:
    SoundFiles = ["chess w. chess libary/sounds/illegal.mp3",
                "chess w. chess libary/sounds/capture.mp3", 
                "chess w. chess libary/sounds/move.mp3", 
                "chess w. chess libary/sounds/check.mp3",
                "chess w. chess libary/sounds/game-end.mp3", 
                "chess w. chess libary/sounds/promote.mp3", 
                "chess w. chess libary/sounds/castle.mp3",
                "chess w. chess libary/sounds/game-start.mp3"]
elif MemeMode == 1:
    SoundFiles = ["chess w. chess libary/sounds/illegal.mp3",
                "chess w. chess libary/sounds/capture.mp3", 
                "chess w. chess libary/sounds/move.mp3", 
                "chess w. chess libary/sounds/check.mp3",
                "chess w. chess libary/sounds/memeSounds/game-end.mp3", 
                "chess w. chess libary/sounds/promote.mp3", 
                "chess w. chess libary/sounds/castle.mp3",
                "chess w. chess libary/sounds/memeSounds/game-start.mp3",
                "chess w. chess libary/sounds/memeSounds/background-music.mp3"]
sounds = [pygame.mixer.Sound(i) for i in SoundFiles]
IllegalSound = 0
CaptureSound = 1
MoveSound = 2
CheckSound = 3
CheckmateSound = 4
PromoteSound = 5
CastleSound = 6
GameStartSound = 7
if MemeMode == 1:
    BackgroundMusic = 8
    CountBGMusicSoundTimer = 1
run = True
def MainGameLoop():
    global run
    global TURN
    global board
    global Move
    global GameOver
    while run:
        HandleGameOver()
        CounterHandler()
        CreateGraphicalBoard()
        screen.blit(transparent, (0, 0))
        DrawPieces()
        if Dragmode == 1:
            PutPieceUnderMouseCurser()
        else:
            ReloadDisplayingBoardlistFromFEN()
        if not GameOver:
            GetMove()
            EventHandler()
            PlayMoveAndSound()
            GetOldAndNewSquareFromMove(Move)
            HighlightMoveSquares()
            Move = None
        pygame.display.flip()
        if Gamemode == 2:
            time.sleep(AIvAITimeDelay)
    pygame.quit()
    
    

displayingboard = [0 for row in range(64)]
turn = chess.WHITE
board = chess.Board(StartFEN)
ClearVariables()
CreateGraphicalBoard()
ReloadDisplayingBoardlistFromFEN()
DrawPieces()
sounds[GameStartSound].play()

MainGameLoop()