import random

# initialize the game board
board = [[0] * 4 for i in range(4)]

# add two random numbers to the board at the start of the game
def add_random():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2 if random.random() < 0.9 else 4

# check if the player has won
def has_won():
    for row in board:
        if 2048 in row:
            return True
    return False

# check if the player has lost
def has_lost():
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
    return True

# merge the cells in a row or column
def merge(cells):
    new_cells = [c for c in cells if c != 0]
    for i in range(len(new_cells) - 1):
        if new_cells[i] == new_cells[i + 1]:
            new_cells[i] *= 2
            new_cells[i + 1] = 0
    new_cells = [c for c in new_cells if c != 0] + [0] * (len(cells) - len(new_cells))
    return new_cells

# move the board in a given direction
def move(direction):
    if direction == 'left':
        for i in range(4):
            board[i] = merge(board[i])
    elif direction == 'right':
        for i in range(4):
            board[i] = merge(board[i][::-1])[::-1]
    elif direction == 'up':
        for j in range(4):
            column = [board[i][j] for i in range(4)]
            column = merge(column)
            for i in range(4):
                board[i][j] = column[i]
    elif direction == 'down':
        for j in range(4):
            column = [board[i][j] for i in range(4)][::-1]
            column = merge(column)
            for i in range(4):
                board[i][j] = column[::-1][i]

# print the current state of the board
def print_board():
    print('-' * 25)
    for row in board:
        print('|', end='')
        for cell in row:
            if cell == 0:
                print(' ' * 4, end='')
            else:
                print(f'{cell:4}', end='')
            print('|', end='')
        print()
        print('-' * 25)

# main game loop
while True:
    add_random()
    print_board()
    if has_won():
        print('Congratulations, you have won!')
        break
    if has_lost():
        print('Game over, you have lost!')
        break
    direction = input('Enter direction (left, right, up, down): ')
    move(direction.lower())
