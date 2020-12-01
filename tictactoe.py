#!/usr/bin/env python

# size of the grid
GRID_SIZE = 9
# create the grid
grid = ["-"] * GRID_SIZE

# player
player1 = "x"
player2 = "o"
# set player on game start
player = player1

# if game still running
game_still_running = True
# draw
tie = False

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

    if player == player1:
        player = player2
    else:
        player = player1

def set_grid_value(key):
    global grid, player

    grid[key-1] = player

def field_is_occupied(key):
    global grid

    return grid[field-1] != "-"

# start the game
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
    elif not game_still_running:
        print("Congratulation, " + player + " you won!")
    else:
        change_player()