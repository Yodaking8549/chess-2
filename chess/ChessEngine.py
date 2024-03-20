import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
if SCREEN_WIDTH <= SCREEN_HEIGHT:
    SmallestValue = SCREEN_WIDTH
else:
    SmallestValue = SCREEN_HEIGHT

square_height = SmallestValue / 8
square_width = SmallestValue / 8

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def CreateGraphicalBoard():
    counter = 0
    rank = 0
    lightColor = 240, 216, 192
    darkColor = 168, 121, 101
    while counter <= 63:
        file = counter % 8
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
        counter += 1

CreateGraphicalBoard()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()