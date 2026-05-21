import locale

cc, encoding = locale.getlocale()
game_name = "Tic-Tac-Toe" # US, Canada, Caribbean nations
if cc in ['en_AU', 'en_GB', 'en_IN', 'en_LK', 'en_NZ', 'en_ZA']:
    game_name = "Noughts and Crosses"
elif cc == 'en_IE':
    game_name = "Xs and Os"
elif cc in ['nb_NO', 'nn_NO']:
    game_name = "Twiddles and Bears"

print(f"Welcome to {game_name}!", end="\n\n")

class Board():
    def __init__(self):
        self.grid = []
        for i in [0, 1, 2]:
            self.grid.append(["_", "_", "_"])
        self.move_num = 0
    def other(self, current):
        return "X" if current == "O" else "O"
    def display(self):
        for i in [2, 1, 0]:
            print(i+1, " ".join(self.grid[i]))
        print("  a b c", end="\n\n")
    def place(self, symbol, i, j):
        move_type = 'normal'
        if not self.grid[i][j] == "_":
            return False
        elif self.move_blocks_opponent(current, i, j):
            move_type = 'blocking'
        self.grid[i][j] = symbol # Overwrites move_blocks_opponent()
        self.move_num += 1
        return move_type
    def move_blocks_opponent(self, symbol, i, j):
        self.grid[i][j] = self.other(symbol) # Will be overwritten in place()
        return self.move_wins_game(self.other(symbol), i, j)
    def move_wins_game(self, symbol, i, j):
        unit = symbol * 3
        return "".join(self.grid[i]) == unit \
            or self.grid[0][j] + self.grid[1][j] + self.grid[2][j] == unit \
            or self.grid[0][0] + self.grid[1][1] + self.grid[2][2] == unit \
            or self.grid[0][2] + self.grid[1][1] + self.grid[2][0] == unit
        
current = ""
while current not in ["X", "O"]:
    current = input("Who will play first, X or O? ").upper()
print()

board = Board()
while board.move_num < 9:
    board.display()
    move = ""
    while not len(move) == 2 or move[0] not in "abc" or move[1] not in "123":
        move = input(f"{current}, make a move in the format a1: ")
    i = int(move[1])-1
    j = ord(move[0])-97
    move_type = board.place(current, i, j)
    if not move_type:
        print("That space is occupied.", end="\n\n")
        continue
    elif board.move_wins_game(current, i, j):
        break
    comment, extra = f"{current} takes {move}.", ""
    if board.move_num == 1:
        extra = "Good move!" if move == 'b2' \
            else "There must have been a better move?"
    elif move_type == 'blocking':
        extra = f"{current} blocked {board.other(current)} from a winning move!"
    print(" ".join([comment, extra]), end="\n\n")
    current = board.other(current) 

board.display()
if board.move_wins_game(current, i, j):
    print(f"{current} has won!", end="\n\n")
elif not board.move_num == 9:
    print("It's a draw.", end="\n\n")
