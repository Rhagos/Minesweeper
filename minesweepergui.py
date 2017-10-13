import minesweeper
import sys, pygame

game_board = minesweeper.MineBoard(16,16,40)
overlay_board = minesweeper.DisplayBoard(game_board)
game_board.prep_board()

pygame.init()


size = width, height = 1940, 1600
black = 0,0,0


screen = pygame.display.set_mode(size)

one_raw = pygame.image.load('images/one.png').convert()
two_raw = pygame.image.load('images/two.png').convert()
three_raw = pygame.image.load('images/three.png').convert()
four_raw = pygame.image.load('images/four.png').convert()
five_raw = pygame.image.load('images/five.png').convert()
six_raw = pygame.image.load('images/six.png').convert()
seven_raw = pygame.image.load('images/seven.png').convert()
eight_raw = pygame.image.load('images/eight.png').convert()
tile_raw = pygame.image.load('images/tile.png').convert()
zero_raw = pygame.image.load('images/zero.png').convert()
flag_raw = pygame.image.load('images/flag.png').convert()

one = pygame.transform.scale(one_raw, (40,40))
two = pygame.transform.scale(two_raw, (40,40))
three = pygame.transform.scale(three_raw, (40,40))
four = pygame.transform.scale(four_raw, (40,40))
five = pygame.transform.scale(five_raw, (40,40))
six = pygame.transform.scale(six_raw, (40,40))
seven = pygame.transform.scale(seven_raw, (40,40))
eight = pygame.transform.scale(eight_raw, (40,40))
tile = pygame.transform.scale(tile_raw, (40,40))
zero = pygame.transform.scale(zero_raw, (40,40))
flag = pygame.transform.scale(flag_raw, (40,40))

def show_board():
    screen.blit(one, (0,0))
    screen.blit(two, (0,40))
    screen.blit(three, (0,80))
    screen.blit(four, (0,120))
    screen.blit(five, (40,0))
    screen.blit(six, (40,40))
    screen.blit(seven, (40,80))
    screen.blit(eight, (40,120))
    screen.blit(zero, (80,0))
    screen.blit(tile, (80,40))
    screen.blit(flag, (80,80))



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    screen.fill(black)


    show_board()

    pygame.display.flip()
