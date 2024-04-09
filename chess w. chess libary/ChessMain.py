import pygame
import chess
import time
import chess.engine
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
SuperSecretMode = 0
AIDifficulty = 0
PrintDebug = False
Gamemode = "PvP"
AIvAITimeDelay = 0
StockfishTest = False
StockfishTurn = chess.WHITE
Playercolor = chess.WHITE
StockfishThinkingTime = 0

if Gamemode == "PvP":
    Gamemode = 0
elif Gamemode == "PvAI":
    Gamemode = 1
elif Gamemode == "AIvAI":
    Gamemode = 2
else:
    print("Invalid Gamemode")
    exit()
    
MainMenu = True

if SCREEN_WIDTH <= SCREEN_HEIGHT:
    SmallestValue = SCREEN_WIDTH
else:
    SmallestValue = SCREEN_HEIGHT

square_height = SmallestValue // 8
square_width = SmallestValue // 8

already_initialized = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess")
transparent = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

font = pygame.font.Font("freesansbold.ttf", 24)

def init():
    global WhiteKing_png
    global BlackKing_png
    global WhitePawn_png
    global BlackPawn_png
    global WhiteKnight_png
    global BlackKnight_png
    global WhiteBishop_png
    global BlackBishop_png
    global WhiteRook_png
    global BlackRook_png
    global WhiteQueen_png
    global BlackQueen_png
    global sounds
    global IllegalSound
    global CaptureSound
    global MoveSound
    global CheckSound
    global CheckmateSound
    global PromoteSound
    global CastleSound
    global GameStartSound
    global BackgroundMusic
    global already_initialized
    global displayingboard
    global turn
    global board
    global Empty
    global WhiteKing
    global BlackKing
    global WhitePawn
    global BlackPawn
    global WhiteKnight
    global BlackKnight
    global WhiteBishop
    global BlackBishop
    global WhiteRook
    global BlackRook
    global WhiteQueen
    global BlackQueen
    global HighlightPossibleMoves
    global SuperSecretMode
    global SoundFiles
    global StartFEN
    global HighlightPossibleMoves
    global CountBGMusicSoundTimer
    global stockfish
    if already_initialized:
        pass
    else:            
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
        if SuperSecretMode == 0:
            SoundFiles = ["chess w. chess libary/sounds/illegal.mp3",
                        "chess w. chess libary/sounds/capture.mp3", 
                        "chess w. chess libary/sounds/move.mp3", 
                        "chess w. chess libary/sounds/check.mp3",
                        "chess w. chess libary/sounds/game-end.mp3", 
                        "chess w. chess libary/sounds/promote.mp3", 
                        "chess w. chess libary/sounds/castle.mp3",
                        "chess w. chess libary/sounds/game-start.mp3"]
        elif SuperSecretMode == 1:
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
        if SuperSecretMode == 1:
            BackgroundMusic = 8
            CountBGMusicSoundTimer = 1
        already_initialized = True
        if PlayStartSound:
            sounds[GameStartSound].play()
        displayingboard = [0 for row in range(64)]
        turn = chess.WHITE
        board = chess.Board(StartFEN)
        stockfish = chess.engine.SimpleEngine.popen_uci(r"chess w. chess libary\TestAgainstStockfish\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe")
        ClearVariables()
        CreateGraphicalBoard()
        ReloadDisplayingBoardlistFromFEN()
        DrawPieces()
        transparent.fill((255, 255, 255, 0))
        
def MenuEventHandler():
    global MainMenu
    global Gamemode
    global run
    global HighlightPossibleMoves
    global SuperSecretMode
    global already_initialized
    global Playercolor
    global PlayercolorButton
    global PrintDebugButton
    global PrintDebug
    global AIDifficulty
    global AIDifficultyButton
    global StockfishTest
    run = True
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if Gamemode == 0:
                    if GamemodeButton.collidepoint(event.pos):
                        Gamemode = 1
                elif Gamemode == 1: 
                    if GamemodeButton.collidepoint(event.pos):
                        Gamemode = 2
                elif Gamemode == 2:
                    if GamemodeButton.collidepoint(event.pos):
                        Gamemode = 0
                if HighlightPossibleMovesButton.collidepoint(event.pos):
                    if HighlightPossibleMoves == 1:
                        HighlightPossibleMoves = 0
                    elif HighlightPossibleMoves == 0:
                        HighlightPossibleMoves = 1
                    else:
                        print("Invalid HighlightPossibleMoves Setting")
                        exit()
                if SuperSecretModeButton.collidepoint(event.pos):
                    if SuperSecretMode == 1:
                        SuperSecretMode = 0
                    elif SuperSecretMode == 0:
                        SuperSecretMode = 1
                    else:
                        print("Invalid SuperSecretMode Setting")
                        exit()
                if PlayercolorButton.collidepoint(event.pos):
                    if Playercolor == chess.WHITE:
                        Playercolor = chess.BLACK
                    elif Playercolor == chess.BLACK:
                        Playercolor = chess.WHITE
                    else:
                        print("Invalid Playercolor Setting")
                        exit()
                if PrintDebugButton.collidepoint(event.pos):
                    if PrintDebug:
                        PrintDebug = False 
                    elif not PrintDebug:
                        PrintDebug = True
                    else:
                        print("Invalid PrintDebug Setting")
                        exit()
                if AIDifficultyButton.collidepoint(event.pos):
                    if AIDifficulty == 0:
                        AIDifficulty = 1
                    elif AIDifficulty == 1:
                        AIDifficulty = 2
                    elif AIDifficulty == 2:
                        AIDifficulty = 3
                    elif AIDifficulty == 3:
                        AIDifficulty = 0
                    else:
                        print("Invalid AIDifficulty Setting")
                        exit()
                if StockfishTestButton.collidepoint(event.pos):
                    if StockfishTest:
                        StockfishTest = False
                    elif not StockfishTest:
                        StockfishTest = True
                    else:
                        print("Invalid StockfishTest Setting")
                        exit()
                if StartButton.collidepoint(event.pos):
                    MainMenu = False
                    already_initialized = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.QUIT:
            run = False
            
def DrawMenuScreens():
    global StartNewAIGame
    if StartNewAIGame == 1:
        startAIgame()
        StartNewAIGame = 0
    global Gamemode
    if Gamemode == 0:
        DrawPvPMenu()
    elif Gamemode == 1:
        DrawPvAIMenu()
    elif Gamemode == 2:
        DrawAIvAIMenu()

def DrawPvPMenu():
    global MainMenu
    global Gamemode
    global GamemodeButton
    GamemodeButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 130, 50, 260, 70], 0, 5)
    pygame.draw.rect(screen, "dark gray", [SCREEN_WIDTH // 2 - 130, 50, 260, 70], 5, 5)
    text = font.render("Player vs Player", True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 85))
    screen.blit(text, text_rect)
    DrawHighlightPossibleMovesButton()
    DrawSuperSecretModeButton()
    DrawPrintDebugButton()
    DrawStartButton()

def DrawPvAIMenu():
    global MainMenu
    global Gamemode
    global GamemodeButton
    global PlayercolorButton
    GamemodeButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 130, 50, 260, 70], 0, 5)
    pygame.draw.rect(screen, "dark gray", [SCREEN_WIDTH // 2 - 130, 50, 260, 70], 5, 5)
    text = font.render("Player vs AI", True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 85))
    screen.blit(text, text_rect)
    DrawHighlightPossibleMovesButton()
    DrawSuperSecretModeButton()
    DrawPlayercolorButton()
    DrawPrintDebugButton()
    DrawAIDifficultyButton()
    DrawStartButton()

def DrawAIvAIMenu():
    global MainMenu
    global Gamemode
    global GamemodeButton
    GamemodeButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 130, 50, 260, 70], 0, 5)
    pygame.draw.rect(screen, "dark gray", [SCREEN_WIDTH // 2 - 130, 50, 260, 70], 5, 5)
    text = font.render("AI vs AI", True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 85))
    screen.blit(text, text_rect)
    DrawHighlightPossibleMovesButton()
    DrawSuperSecretModeButton()
    DrawPrintDebugButton()
    DrawAIDifficultyButton()
    DrawStockfishTestButton()
    DrawStartButton()

def DrawHighlightPossibleMovesButton():
    global HighlightPossibleMovesButton
    if HighlightPossibleMoves == 1:
        text = font.render("Highlight Possible Moves: ON", True, (0, 0, 0))
    else:
        text = font.render("Highlight Possible Moves: OFF", True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 185))
    HighlightPossibleMovesButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 200, 150, 400, 70], 0, 5)
    pygame.draw.rect(screen, "dark gray", [SCREEN_WIDTH // 2 - 200, 150, 400, 70], 5, 5)
    screen.blit(text, text_rect)

def DrawSuperSecretModeButton():
    global SuperSecretModeButton
    if SuperSecretMode == 1:
        text = font.render("Super Secret Mode: ON", True, (0, 0, 0))
    else:
        text = font.render("Super Secret Mode: OFF", True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 285))
    SuperSecretModeButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 200, 250, 400, 70], 0, 5)
    pygame.draw.rect(screen, "dark gray", [SCREEN_WIDTH // 2 - 200, 250, 400, 70], 5, 5)
    screen.blit(text, text_rect)

def DrawPlayercolorButton():
    global PlayercolorButton
    if Playercolor == chess.WHITE:
        color = "White"
    elif Playercolor == chess.BLACK:
        color = "Black"
    text = font.render("Player Color: " + color, True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 400))
    PlayercolorButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 130, 365, 260, 70], 0, 5)
    pygame.draw.rect(screen, "dark gray", [SCREEN_WIDTH // 2 - 130, 365, 260, 70], 5, 5)
    screen.blit(text, text_rect)

def DrawPrintDebugButton():
    global PrintDebugButton
    global PrintDebug
    if PrintDebug:
        buttontxtextention = "ON"
    else:
        buttontxtextention = "OFF"
    text = font.render("Print Debug: " + buttontxtextention, True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 485))
    PrintDebugButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 130, 450, 260, 70], 0, 5)
    pygame.draw.rect(screen, "dark gray", [SCREEN_WIDTH // 2 - 130, 450, 260, 70], 5, 5)
    screen.blit(text, text_rect)

def DrawAIDifficultyButton():
    global AIDifficultyButton
    if AIDifficulty == 0:
        buttontxtextention = "Plays Randomly"
    elif AIDifficulty == 1:
        buttontxtextention = "Takes every piece"
    elif AIDifficulty == 2:
        buttontxtextention = "Minimax"
    elif AIDifficulty == 3:
        buttontxtextention = "Stockfish"
        
    text = font.render("AI Difficulty: " + buttontxtextention, True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 585))
    AIDifficultyButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 200, 550, 400, 70], 0, 5)
    pygame.draw.rect(screen, "dark gray", [SCREEN_WIDTH // 2 - 200, 550, 400, 70], 5, 5)
    screen.blit(text, text_rect)

AIDifficultyButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 200, 550, 400, 70], 0, 5)
StockfishTestButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 130, 650, 260, 70], 0, 5)
PlayercolorButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 200, 330, 400, 70], 0, 5)

def DrawStockfishTestButton():
    global StockfishTestButton
    if StockfishTest:
        buttontxtextention = "ON"
    else:
        buttontxtextention = "OFF"
    text = font.render("Stockfish Test: " + buttontxtextention, True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 685))
    StockfishTestButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 130, 650, 260, 70], 0, 5)
    pygame.draw.rect(screen, "dark gray", [SCREEN_WIDTH // 2 - 130, 650, 260, 70], 5, 5)
    screen.blit(text, text_rect)

def DrawStartButton():
    global StartButton
    text = font.render("Start", True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
    StartButton = pygame.draw.rect(screen, "light gray", [SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT - 135, 260, 70], 0, 5)
    pygame.draw.rect(screen, "dark gray", [SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT - 135, 260, 70], 5, 5)
    screen.blit(text, text_rect)

def startAIgame():
    global Gamemode
    global MainMenu
    global already_initialized
    Gamemode = 2
    MainMenu = False
    already_initialized = False

def FindAIvAICheckmate():
    global board
    global MainMenu
    global StartNewAIGame
    global Gamemode
    if (board.is_checkmate() == True or (Gamemode != 2)):
        pass
    else:
        MainMenu = True
        StartNewAIGame = 1
    
def PromotionEventHandler():
    global run
    global MainMenu
    global Promote
    global Move
    global FinishedPromote
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] in range(100, 200) and event.pos[1] in range(100, 200):
                    Move = (chess.Move.from_uci(MoveBeforePromote.uci() + "q"))
                    Promote = False
                    FinishedPromote = False
                elif event.pos[0] in range(100, 200) and event.pos[1] in range(200, 300):
                    Move = (chess.Move.from_uci(MoveBeforePromote.uci() + "r"))
                    Promote = False
                    FinishedPromote = False
                elif event.pos[0] in range(100, 200) and event.pos[1] in range(300, 400):
                    Move = (chess.Move.from_uci(MoveBeforePromote.uci() + "b"))
                    Promote = False
                    FinishedPromote = False
                elif event.pos[0] in range(100, 200) and event.pos[1] in range(400, 500):
                    Move = (chess.Move.from_uci(MoveBeforePromote.uci() + "n"))
                    Promote = False
                    FinishedPromote = False
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                MainMenu = True
                
def DrawPromotionScreen():
    global MainMenu
    global Promote
    pygame.draw.rect(screen, "light gray", [100, 100, 100, 100], 0, 5)
    pygame.draw.rect(screen, "dark gray", [100, 100, 100, 100], 5, 5)
    pygame.draw.rect(screen, "light gray", [100, 200, 100, 100], 0, 5)
    pygame.draw.rect(screen, "dark gray", [100, 200, 100, 100], 5, 5)
    pygame.draw.rect(screen, "light gray", [100, 300, 100, 100], 0, 5)
    pygame.draw.rect(screen, "dark gray", [100, 300, 100, 100], 5, 5)
    pygame.draw.rect(screen, "light gray", [100, 400, 100, 100], 0, 5)
    pygame.draw.rect(screen, "dark gray", [100, 400, 100, 100], 5, 5)
    font = pygame.font.Font("freesansbold.ttf", 24)
    text = font.render("Queen", True, (0, 0, 0))
    text_rect = text.get_rect(center=(150, 150))
    screen.blit(text, text_rect)
    text = font.render("Rook", True, (0, 0, 0))
    text_rect = text.get_rect(center=(150, 250))
    screen.blit(text, text_rect)
    text = font.render("Bishop", True, (0, 0, 0))
    text_rect = text.get_rect(center=(150, 350))
    screen.blit(text, text_rect)
    text = font.render("Knight", True, (0, 0, 0))
    text_rect = text.get_rect(center=(150, 450))
    screen.blit(text, text_rect)

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
    global displayingboard
    global Empty
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
    global WhiteKing
    global BlackKing
    global WhitePawn
    global BlackPawn
    global WhiteKnight
    global BlackKnight
    global WhiteBishop
    global BlackBishop
    global WhiteRook
    global BlackRook
    global WhiteQueen
    global BlackQueen
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
    global WhiteKing
    global BlackKing
    global WhitePawn
    global BlackPawn
    global WhiteKnight
    global BlackKnight
    global WhiteBishop
    global BlackBishop
    global WhiteRook
    global BlackRook
    global WhiteQueen
    global BlackQueen
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
        global SquareDictFileToNum
        SquareDictFileToNum = {
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
        OldSquare = SquareDictFileToNum[uci_move[:2]]
        NewSquare = SquareDictFileToNum[uci_move[2:4]]
        
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
    global ClickedSquare
    if HighlightPossibleMoves == 1:
        for move in board.legal_moves:
            if InvertSquare(ClickedSquare) == move.from_square:
                HighlightSquare(int(InvertSquare(move.to_square)), PossibleMovesSquareHighlightColor)

def InvertSquare(squarenumber):
    return 63 - squarenumber

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
    GameOverSoundHandler()
    BGMusicSoundHandler()
    
def GameOverSoundHandler():
    global CheckmateSoundTimer
    global CountCheckmateSoundTimer
    if CountCheckmateSoundTimer == 1:
        CheckmateSoundTimer += 1
        if CheckmateSoundTimer == 13:
            sounds[CheckmateSound].play()
            if SuperSecretMode == 1:
                sounds[BackgroundMusic].stop()
            CountCheckmateSoundTimer = 0
            CheckmateSoundTimer = 0         
            
def BGMusicSoundHandler():
    global SuperSecretMode
    global BGMusicSoundTimer
    global CountBGMusicSoundTimer
    global BGMusicRunning
    if SuperSecretMode == 1:
        if CountBGMusicSoundTimer == 1:
            BGMusicSoundTimer += 1
            if BGMusicSoundTimer == 300:
                sounds[BackgroundMusic].play()
                CountBGMusicSoundTimer = 0
                BGMusicSoundTimer = 0
                BGMusicRunning = True
        if not BGMusicRunning:
            CountBGMusicSoundTimer = 1 
       
def GetCorrectSoundPreMove(PlayedMove):
    if isinstance(PlayedMove, str):
        PlayedMove = chess.Move.from_uci(PlayedMove)
    if isinstance(PlayedMove, chess.Move):
        if PrintDebug:
            print("Played Move (sounddebug): " + str(PlayedMove))
        Sound = None
        if board.is_capture(PlayedMove):
            Sound = "Capture"
        elif board.is_castling(PlayedMove):
            Sound = "Castle"
        elif len(str(PlayedMove)) > 4:
            Sound = "Promote"
        else:
            Sound = "Move"
        if PrintDebug:
            print("Sound: " + Sound)
        return Sound

def GetCorrectSoundPostMove(Sound):
    if board.is_check():
        return "Check"
    else:
        return Sound

def ClearVariables():
    global Dragmode
    Dragmode = 0
    global EnPassantSquare
    EnPassantSquare = -1
    global playsound
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
    global BGMusicRunning
    BGMusicRunning = False
    global Promote
    Promote = False
    global FinishedPromote
    FinishedPromote = True
    global StartNewAIGame
    StartNewAIGame = False
            
def ReloadDisplayingBoardlistFromFEN():
    BoardFENToDisplayingBoard(board.fen())
    MakeBoardListUsable(displayingboard)
    
def HandleGameOver():
    global HandledGameOver
    global GameOver
    global CountCheckmateSoundTimer
    if board.is_game_over() and not HandledGameOver:
        GameOver = True
        NumMoves = str(board.fullmove_number)
        CountCheckmateSoundTimer = 1
        if board.is_checkmate():
            if (Gamemode == 0 or Gamemode == 2):
                if StockfishTest:
                    if board.turn == StockfishTurn:
                        print("Somehow Black defeated Stockfish by checkmate in " + NumMoves + " moves!")
                    else:
                        print("Stockfish won by checkmate in " + NumMoves + " moves (no surprise)")
                else:
                    if board.turn == chess.WHITE:
                        print("Black wins by checkmate in " + NumMoves + " moves!")
                    else:
                        print("White wins by checkmate in " + NumMoves + " moves!")
            elif Gamemode == 1:
                if AIDifficulty == 3:
                    if board.turn == Playercolor:
                        print("Stockfish wins by checkmate in " + NumMoves + " moves (no fucking suprise)")
                    else:
                        print("You somehow defeated stockfish in " + NumMoves + " moves (probably cheats)")
                else:
                    if board.turn == Playercolor:
                        print("AI wins by checkmate in " + NumMoves + " moves!")
                    else:
                        print("You win by checkmate in " + NumMoves + " moves!")
        elif board.is_stalemate():
            print("Draw By Stalemate (" + NumMoves + "moves)")
        elif board.is_insufficient_material():
            print("Draw By Insufficient Material (" + NumMoves + " moves)")
        elif board.is_seventyfive_moves():
            print("Draw By Seventy Five Move Rule (" + NumMoves + " moves)")
        elif board.is_fivefold_repetition():
            print("Draw By Fivefold Repetition (" + NumMoves + " moves)")
        else:
            print("Draw By Other Reason (" + NumMoves + " moves)")
        HandledGameOver = True
                
def PickUpPiece():
    global ClickedSquare
    global DraggedPiece
    global Dragmode
    global MoveSquareHighlightColor
    if TURN == "Player":
        if turn:
            ClickedSquare = GetSquareUnderMouse()
            DraggedPiece = displayingboard[ClickedSquare]
            if DraggedPiece[0] == "w":
                Dragmode = 1
                displayingboard[ClickedSquare] = Empty
                HighlightSquare(ClickedSquare, MoveSquareHighlightColor)
            elif DraggedPiece[0] == "b":
                print("It's not your turn!")
        elif not turn:
            ClickedSquare = GetSquareUnderMouse()
            DraggedPiece = displayingboard[ClickedSquare]
            if DraggedPiece[0] == "b":
                Dragmode = 1
                displayingboard[ClickedSquare] = Empty
                HighlightSquare(ClickedSquare, MoveSquareHighlightColor)
            elif DraggedPiece[0] == "w":
                print("It's not your turn!")

def PutDownPieceGetMove():
    global Dragmode
    global NewSquare
    global OldSquare
    global Promote
    global MoveBeforePromote
    global DynamicOldSquare
    global DynamicNewSquare
    global SquareDict_NumToFile
    if (Dragmode == 1):
        Dragmode = 0
        SquareDict_NumToFile = {
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
        DynamicOldSquare = SquareDict_NumToFile[OldSquare]
        DynamicNewSquare = SquareDict_NumToFile[NewSquare]
        GetPlayerMove()
        

def GetPlayerMove():
    global Move
    global Promote
    global MoveBeforePromote
    global FinishedPromote
    global DynamicNewSquare
    global DynamicOldSquare
    if PrintDebug:
        print("OldSquare: ", OldSquare)
        print("NewSquare: ", NewSquare)
    if OldSquare != NewSquare:
        if FinishedPromote:
            Move = chess.Move.from_uci(DynamicOldSquare + DynamicNewSquare)
        if ((DraggedPiece[1] == "P") or (DraggedPiece[1] == "p")) and FinishedPromote:
            if NewSquare <= 7 or NewSquare >= 56:
                Promote = True
                if PrintDebug:
                    print("Send Help")
                MoveBeforePromote = Move
        if not Promote:
            if PrintDebug:
                print("Validating Move: ", Move)
            if ValidateMove(Move):
                HandleValidMove(Move)
                if PrintDebug:
                    print(Move, "Move Validated")
            else:
                HandleInvalidMove()
    else:
        transparent.fill((0, 0, 0, 0))

        
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
    transparent.fill((0, 0, 0, 0))
    
def PlayMoveAndSound():
    global Move
    global turn
    if ((Move != None) and (Move != "Illegal") and (Move != "Game Over")) and LegalMove == True:
        if isinstance(Move, str):
            Move = chess.Move.from_uci(Move)
        if isinstance(Move, chess.Move):
            if PrintDebug:
                print("move pushed: ", Move)
            Sound = GetCorrectSoundPreMove(Move)
            board.push(Move)
            Sound = GetCorrectSoundPostMove(Sound)
            if PrintDebug:
                print("Sound: ", Sound)
            PlaySound(Sound)
            turn = not turn

def GetMove():
    global TURN
    global board
    global Move
    global LegalMove
    global AIDifficulty
    global StockfishTest
    global StockfishTurn
    global StockfishThinkingTime
    if Gamemode == 0 or (Gamemode == 1 and Playercolor == turn):
        TURN = "Player"
    elif (Gamemode == 1 and Playercolor != turn) or Gamemode == 2:
        transparent.fill((0, 0, 0, 0))
        TURN = "AI"
        if (Gamemode == 2 and StockfishTest and (turn == StockfishTurn)) or AIDifficulty == 3:
            result = stockfish.play(board, chess.engine.Limit(time=StockfishThinkingTime))
            Move = result.move
        else:
            Move = GetAIMove(board.fen(), AIDifficulty)
        LegalMove = True
        
def EventHandler():
    global TURN
    global MainMenu
    global run
    global StartNewAIGame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if TURN == "Player" and Dragmode == 0 and not GameOver and not MainMenu:
                    PickUpPiece()
                    MarkLegalMoves()
            if event.button == 3 and not MainMenu:
                PrintDebugInfo()
            if (((event.button == 2) and not MainMenu) and GameOver) and Gamemode == 2:
                MainMenu = True
                StartNewAIGame = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if TURN == "Player" and Dragmode == 1 and not GameOver and not MainMenu:
                    PutDownPieceGetMove()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not MainMenu:
                    MainMenu = True
                else:
                    run = False
                
def PrintDebugInfo():
    print("TURN: ", TURN)
    print("turn: ", turn)
    print("Move: ", Move)
    print("board:")
    print(board)    

run = True
def MainGameLoop():
    global FinishedPromote 
    global run
    global TURN
    global board
    global Move
    global GameOver
    while run:
        if MainMenu:
            screen.fill((0, 0, 0))
            MenuEventHandler()
            DrawMenuScreens()
            pygame.display.flip()
        else:
            if Promote:
                PromotionEventHandler()
                CreateGraphicalBoard()
                DrawPieces()
                DrawPromotionScreen()
                pygame.display.flip()
            else:
                init()
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
                    if not FinishedPromote:
                        if PrintDebug:
                            print("Promote")
                        GetPlayerMove()
                        FinishedPromote = True
                    PlayMoveAndSound()
                    GetOldAndNewSquareFromMove(Move)
                    HighlightMoveSquares()
                    Move = None
                else:
                    EventHandler()
                    FindAIvAICheckmate()
                pygame.display.flip()
                if Gamemode == 2:
                    time.sleep(AIvAITimeDelay)
PlayStartSound = False
init()
PlayStartSound = True
displayingboard = [0 for row in range(64)]
turn = chess.WHITE
board = chess.Board(StartFEN)
ClearVariables()
CreateGraphicalBoard()
ReloadDisplayingBoardlistFromFEN()
DrawPieces()



MainGameLoop()
pygame.quit()
stockfish.quit()
exit()