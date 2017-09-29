import random
class MineBoard:
    def __init__(self, board_x = 16, board_y = 16, mine_count = 40):
        self.x = board_x
        self.y = board_y
        self.board = []
        self.mines = mine_count

    def init_board(self):
        for i in range(self.x):
            board_row = []
            for j in range(self.y):
                board_row.append(0)
            self.board.append(board_row)
        return

    def seed_board(self):
        for i in range(self.mines):
            rand_x = int(random.random() * self.x)
            rand_y = int(random.random() * self.y)
            while self.board[rand_x][rand_y] == 'x':
                rand_x = int(random.random() * self.x)
                rand_y = int(random.random() * self.y)

            self.board[rand_x][rand_y] = 'x'
        return

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
        for i in self.board:
            for j in i:
                print(j, end= '|')
            print('\n')

game_board = MineBoard(16,16,40)

print(game_board.board)
game_board.init_board()
game_board.seed_board()
game_board.load_numbers()

print(game_board.to_string())
