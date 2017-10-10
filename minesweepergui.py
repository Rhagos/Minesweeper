import minesweeper
import sys, pygame

game_board = minesweeper.MineBoard(16,16,40)
overlay_board = minesweeper.DisplayBoard(game_board)
game_board.init_board()
game_board.seed_board()
game_board.load_numbers()

pygame.init()


size = width, height = 320, 240
black = 0,0,0

screen = pygame.display.set_mode(size)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    pygame.display.flip()
