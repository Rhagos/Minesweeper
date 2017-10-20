import minesweeper
import sys, pygame

game_board = minesweeper.MineBoard(16,16,40)
overlay_board = minesweeper.DisplayBoard(game_board)
game_board.prep_board()

pygame.init()

y_offset = 75

size = width, height = 600, 600 + y_offset
black = 0,0,0

screen = pygame.display.set_mode(size)
def load_image_dict():
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
    mine_raw = pygame.image.load('images/mine.png').convert()
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
    return {
            0: zero,
            1: one,
            2: two,
            3: three,
            4: four,
            5: five,
            6: six,
            7: seven,
            8: eight,
            'H': tile,
            'F': flag,
            'x': mine
        }
image_dict = load_image_dict
def draw_board(board):


    x_dist, y_dist = 40, 40

    for i in range(board.underlay.x):
        for j in range(board.underlay.y):


#
# class Button:
#     def __init__(self, x, y, size, type)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()



    screen.fill(black)


    draw_board()

    pygame.display.flip()
