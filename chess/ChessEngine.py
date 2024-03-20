import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
if SCREEN_WIDTH <= SCREEN_HEIGHT:
    SmallestValue = SCREEN_WIDTH
else:
    SmallestValue = SCREEN_HEIGHT

square_height = SmallestValue / 8
square_width = SmallestValue / 8

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def CreateGraphicalBoard():
    rank = 0
    lightColor = 240, 216, 192
    darkColor = 168, 121, 101
    for i in range(64):
        file = i % 8
        square_x = file * square_width
        square_y = rank * square_height

        if (file + rank) % 2 == 0:
            color = lightColor
        else:
            color = darkColor

        square = pygame.Rect((square_x, square_y, square_width, square_height))
        pygame.draw.rect(screen, color, square)

        if file == 7:
            rank += 1
            
def DrawPieces():
    for i in range(64):
        file = i % 8
        rank = i // 8
        square_x = file * square_width
        square_y = rank * square_height

        if board[i] == WhiteKing:
            screen.blit(WhiteKing_png, (square_x, square_y))
        elif board[i] == BlackKing:
            screen.blit(BlackKing_png, (square_x, square_y))
        elif board[i] == WhitePawn:
            screen.blit(WhitePawn_png, (square_x, square_y))
        elif board[i] == BlackPawn:
            screen.blit(BlackPawn_png, (square_x, square_y))
        elif board[i] == WhiteKnight:
            screen.blit(WhiteKnight_png, (square_x, square_y))
        elif board[i] == BlackKnight:
            screen.blit(BlackKnight_png, (square_x, square_y))
        elif board[i] == WhiteBishop:
            screen.blit(WhiteBishop_png, (square_x, square_y))
        elif board[i] == BlackBishop:
            screen.blit(BlackBishop_png, (square_x, square_y))
        elif board[i] == WhiteRook:
            screen.blit(WhiteRook_png, (square_x, square_y))
        elif board[i] == BlackRook:
            screen.blit(BlackRook_png, (square_x, square_y))
        elif board[i] == WhiteQueen:
            screen.blit(WhiteQueen_png, (square_x, square_y))
        elif board[i] == BlackQueen:
            screen.blit(BlackQueen_png, (square_x, square_y))

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


CreateGraphicalBoard()
FenToBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
MakeBoardUsable()
DrawPieces()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    DrawPieces()
    pygame.display.update()
pygame.quit()