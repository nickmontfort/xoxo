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
    def spaces_are_free(self):
        slots = False
        for i in [0, 1, 2]:
            if "_" in self.grid[i]:
                slots = True
        return slots
    def display(self):
        for i in [2, 1, 0]:
            print(i+1, " ".join(self.grid[i]))
        print("  a b c", end="\n\n")
    def place(self, symbol, i, j):
        if self.grid[i][j] == "_":
            self.grid[i][j] = symbol
        return self.grid[i][j] == symbol
    def move_won_game(self, current, i, j):
        unit = current * 3
        won = "".join(self.grid[i]) == unit \
            or self.grid[0][j] + self.grid[1][j] + self.grid[2][j] == unit \
            or self.grid[0][0] + self.grid[1][1] + self.grid[2][2] == unit \
            or self.grid[0][2] + self.grid[1][1] + self.grid[2][0] == unit
        return won
        
current = input("Who will play first, X or O? ").upper()
print()

board = Board()

while board.spaces_are_free():
    board.display()
    move = ""
    while not len(move) == 2 or move[0] not in "abc" or move[1] not in "123":
        move = input(f"{current}, make a move in the format a1: ")
    i = int(move[1])-1
    j = ord(move[0])-97
    if not board.place(current, i, j):
        print("That space is occupied.")
        continue
    elif board.move_won_game(current, i, j):
        break
    current = "X" if current == "O" else "O" 

board.display()
if board.move_won_game(current, i, j):
    print(f"{current} has won!", end="\n\n")
elif not board.spaces_are_free():
    print("It's a draw.", end="\n\n")
