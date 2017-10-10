import minesweeper
import sys, pygame

game_board = minesweeper.MineBoard(16,16,40)
overlay_board = minesweeper.DisplayBoard(game_board)
game_board.prep_board()

pygame.init()


size = width, height = 1920, 1600
black = 0,0,0


screen = pygame.display.set_mode(size)

one = pygame.image.load('images/one.png').convert()
two = pygame.image.load('images/two.png').convert()
three = pygame.image.load('images/three.png').convert()
four = pygame.image.load('images/four.png').convert()
five = pygame.image.load('images/five.png').convert()
six = pygame.image.load('images/six.png').convert()
seven = pygame.image.load('images/seven.png').convert()
eight = pygame.image.load('images/eight.png').convert()
tile = pygame.image.load('images/tile.png').convert()
zero = pygame.image.load('images/zero.png').convert()
flag = pygame.image.load('images/flag.png').convert()





while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    screen.fill(black)

    screen.blit(one, one.get_rect())
    screen.blit(two, two.get_rect())
    screen.blit(three, three.get_rect())
    screen.blit(four, four.get_rect())
    screen.blit(five, five.get_rect())
    screen.blit(six, six.get_rect())
    screen.blit(seven, seven.get_rect())
    screen.blit(eight, eight.get_rect())
    # screen.blit(tile, tile.get_rect())
    screen.blit(zero, zero.get_rect())
    # screen.blit(flag, flag.get_rect())

    pygame.display.flip()
