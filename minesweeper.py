import random
class MineBoard:
    def __init__(self, board_x = 16, board_y = 16, mine_count = 40):
        self.x = board_x
        self.y = board_y
        self.board = []
        self.mines = mine_count
        if mine_count > board_x * board_y:
            self.mines = 1
            print("Invalid number of mines!")


    def get_size(self):
        return [self.x, self.y, self.mines]
    def init_board(self):
        for i in range(self.x):
            board_row = []
            for j in range(self.y):
                board_row.append(0)
            self.board.append(board_row)

    def seed_board(self):
        for i in range(self.mines):
            rand_x = int(random.random() * self.x)
            rand_y = int(random.random() * self.y)
            while self.board[rand_x][rand_y] == 'x':
                rand_x = int(random.random() * self.x)
                rand_y = int(random.random() * self.y)

            self.board[rand_x][rand_y] = 'x'

    def get_adjacent(self,p_x,p_y):
        valid_x = [-1,0,1]
        valid_y = [-1,0,1]
        if p_x == 0:
            valid_x = [0, 1]
        if p_y == 0:
            valid_y = [0, 1]
        if p_x == self.x-1:
            valid_x = [-1, 0]
        if p_y == self.y-1:
            valid_y = [-1, 0]

        return valid_x, valid_y

    def load_numbers(self):
        for i in range(self.x):
            for j in range(self.y):
                if self.board[i][j] == 'x':
                    x_range, y_range = self.get_adjacent(i,j)
                    for a in range(len(x_range)):
                        for b in range(len(y_range)):
                            if not (x_range[a] == 0 and y_range[b] == 0):
                                if not self.board[i+x_range[a]][j+y_range[b]] == 'x':
                                    self.board[i+x_range[a]][j+y_range[b]] += 1


    def to_string(self):
        row_index = 0
        print("   ", end = ' ')
        for i in range(self.x):
            print(i, end = '  ')
        print('\n')
        for i in self.board:
            print(row_index, end = ' '*(4-len(str(row_index))))
            col_index = 0
            while col_index < self.x:
                print(i[col_index], end= ' '*(1+len(str(col_index))))
                col_index += 1
            print('\n')
            row_index += 1

    def prep_board(self):
        self.init_board()
        self.seed_board()
        self.load_numbers()
class DisplayBoard:
    #Overlay grid will begin with all 0,
    #When a space is changed to -1, the underlay is displayed
    #When a space is changed to 1, it is flagged

    def __init__(self, mine_board):
        self.underlay = mine_board
        self.x = mine_board.get_size()[0]
        self.y = mine_board.get_size()[1]
        self.overlay = []
    def generate_overlay(self):
        for i in range(self.x):
            row = []
            for j in range(self.y):
                row.append(0)
            self.overlay.append(row)
    def flag_space(self, x_coord, y_coord):
        self.overlay[y_coord][x_coord] = 1
    def unflag_space(self, x_coord,y_coord):
        self.overlay[y_coord][x_coord] = 0


class Minesweeper:
    def __init__(self, display, mine_board):
        self.display_board = display
        self.underlay = mine_board
        self.flags = self.underlay.mines
        #Game status represents which stage of the game is currently going on
        #0 = Still playing
        #1 = Victory
        #-1 = Defeat
        self.game_status = 0

    def flip_tile(self, targ_x, targ_y):
        if targ_x < 0 or targ_x > self.underlay.x:
            return "Out of bounds"
        if targ_y < 0 or targ_y > self.underlay.y:
            return "Out of bounds"
        if self.display_board.overlay[targ_y][targ_x] == 0:
            self.display_board.overlay[targ_y][targ_x] = -1
            if self.underlay.board[targ_y][targ_x] == 0:
                fillable = self.underlay.get_adjacent(targ_x, targ_y)
                for i in fillable[0]:
                    for j in fillable[1]:
                        if not (i == 0 and j == 0):
                            self.flip_tile(targ_x + i, targ_y + j)

    def flag_tile(self, x_coord, y_coord):
        print(self.flags)
        if self.display_board.overlay[y_coord][x_coord] == -1:
            print('Can\'t flag a discovered tile')
        elif self.display_board.overlay[y_coord][x_coord] == 0:
            if self.flags <= 0:
                print('Not enough flags')
                return
            else:
                self.flags -= 1
                self.display_board.flag_space(x_coord, y_coord)
        else:
            self.flags += 1
            self.display_board.unflag_space(x_coord, y_coord)



    def display(self):
        if self.game_status != 0:
            print("Game has ended")

        row_index = 0

        #Prints the column indexes at the top
        print("   ", end = ' ')
        for i in range(self.underlay.x):
            print(i, end = '  ')
        print('\n')

        while row_index < self.underlay.y:
            #Prints the row number
            print(row_index, end = ' '*(4-len(str(row_index))))

            col_index = 0
            while col_index < self.underlay.x:
                #Spaces the column number
                col_num_spacing = ' '*(1+len(str(col_index)))

                #Prints H if not revealed(True), else prints the corresponding value
                if self.display_board.overlay[row_index][col_index] == 0:
                    print("H", end = col_num_spacing)
                elif self.display_board.overlay[row_index][col_index] == 1:
                    print("F", end = col_num_spacing)
                else:
                    print(self.underlay.board[row_index][col_index], end=col_num_spacing)
                    if self.underlay.board[row_index][col_index] == 'x':
                        self.game_status = -1

                #Increment
                col_index += 1

            print('\n')
            row_index += 1


    def check_status(self):
        if self.game_status == -1:
            return "TERRORISTS WIN"
        elif self.game_status == 1:
            return "BOMBS DEFUSED"
        else:
            return "Defusing..."

    #Returns 1 if game has been won (All uncovered spaces are all mines)
    #Returns 0 if the game has yet to be won (Not all uncovered spaces are mines)
    def check_victory(self):
        for i in range(self.underlay.y):
            for j in range(self.underlay.x):
                if self.display_board.overlay[i][j] == 0:
                    if self.underlay.board[i][j] == 'x':
                        #If there is an unflagged, uncovered mine, keep playing
                        return 0

        return 1

    def action(self, list_args):
        if not len(list_args) == 3:
            print("Incorrect args")
            return
        if list_args[0] != "flip_tile" and list_args[0] != "flag_tile":
            print("Invalid command")
            return
        if hasattr(self, list_args[0]):
            params = []
            for arg in list_args[1:]:
                params.append(int(arg))
            getattr(self, list_args[0])(params[0], params[1])
        else:
            print("Incorrect Function")
    def play_loop(self):
        self.display()
        while self.game_status == 0:
            # x, y = input("X and Y to clear: ").split()
            # x, y = int(x), int(y)
            # if x >= 0 and x < self.underlay.x and y >= 0 and y < self.underlay.y:
            #     self.flip_tile(x,y)
            #     for i in range(5):
            #         print('\n')
            #     self.display()
            #     if self.check_victory():
            #         self.game_status = 1
            # else:
            #     print('Invalid coordinates')
            self.action(input(">").split())
            for i in range(5):
                print('\n')

            if self.check_victory():
                self.game_status = 1

            self.display()

        print(self.check_status())

def terminal_gui():
    game_board = MineBoard(16,16,40)
    overlay_board = DisplayBoard(game_board)
    game_board.prep_board()
    game = Minesweeper(overlay_board, game_board)
