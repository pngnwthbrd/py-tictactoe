#!/usr/bin/env python

# size of the grid
GRID_SIZE = 9

# init the grid
grid = []

# player
PLAYER1 = "x"
PLAYER2 = "o"
# set player on game start
player = PLAYER1

# if game still running
game_still_running = True
# draw
tie = False

# create the grid
def create_empty_grid():
    global grid
    grid = ["-"] * GRID_SIZE

def display_grid():
    global grid

    print(grid[0] + " | " + grid[1] + " | " + grid[2])
    print(grid[3] + " | " + grid[4] + " | " + grid[5])
    print(grid[6] + " | " + grid[7] + " | " + grid[8])

def check_grid():
    global game_still_running, grid, tie

    if "-" not in grid:
        tie = True
        game_still_running = False
        pass

    # check row's
    row1 = grid[0] == grid[1] == grid[2] != "-"
    row2 = grid[3] == grid[4] == grid[5] != "-"
    row3 = grid[6] == grid[7] == grid[8] != "-"
    # check col's
    col1 = grid[0] == grid[3] == grid[6] != "-"
    col2 = grid[1] == grid[4] == grid[7] != "-"
    col3 = grid[2] == grid[5] == grid[8] != "-"
    # check diagonals
    dia1 = grid[0] == grid[4] == grid[8] != "-"
    dia2 = grid[6] == grid[4] == grid[2] != "-"
    dia3 = grid[2] == grid[4] == grid[6] != "-"
    dia4 = grid[8] == grid[4] == grid[0] != "-"

    if row1 or row2 or row3 or \
       col1 or col2 or col3 or \
       dia1 or dia2 or dia3 or dia4:
        game_still_running = False
    

def change_player():
    global player

    if player == PLAYER1:
        player = PLAYER2
    else:
        player = PLAYER1

def set_grid_value(key):
    global grid, player

    grid[key-1] = player

def field_is_occupied(key):
    global grid

    return grid[field-1] != "-"

def check_revenge():
    global game_still_running
    revenge = ""
    while revenge not in ("y", "n"):
        revenge = input("Play again? (y/n): ")

    if revenge == "y":
        game_still_running = True
        create_empty_grid()
        display_grid()


# start the game
create_empty_grid()
display_grid()
while game_still_running:
    field = int(input(player + " please choose your field (1-9): "))
    if not field_is_occupied(field):
        set_grid_value(field)
        check_grid()
        display_grid()
    else:
        print("Field is occupied! Try again...")
        continue

    if tie:
        print("Tie!")
        check_revenge()
    elif not game_still_running:
        print("Congratulation, " + player + " you won!")
        check_revenge()
    else:
        change_player()