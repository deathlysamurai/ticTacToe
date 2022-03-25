import random
import time

grid = [1,2,3,4,5,6,7,8,9]
positions = {"X":[], "O":[]}

def main():
    display_grid(grid)
    clear_grid(grid)
    win = False
    while win == False:
        get_player_choice()
        display_grid(grid)
        win = check_win()
        if win == True:
            break
        if check_draw():
            print("DRAW!")
            break
        get_computer_choice()
        time.sleep(.5)
        display_grid(grid)
        win = check_win()

def display_grid(grid):
    for index in range(len(grid)):
        print("|" + str(grid[index]), end="")
        if index == len(grid)-1:
            print("|")
        elif ((index+1)%3)==0:
            print("|")

def get_player_choice():
    choice = 0
    while choice < 1 or choice > 9 or grid[choice-1] == "X" or grid[choice-1] == "O":
        if choice < 1 or choice > 9:
            print("Please enter a number from 1-9")
        elif grid[choice-1] == "X" or grid[choice-1] == "O":
            print("That square has already been chosen, please choose another.")
        choice_input = input()
        if choice_input.isdigit():
            choice = int(choice_input)
    grid[choice-1] = "X"
    positions["X"].append(choice)

def get_computer_choice():
    choice = random.randint(1, 9)
    while grid[choice-1] == "X" or grid[choice-1] == "O":
        choice = random.randint(1, 9)
    grid[choice-1] = "O"
    positions["O"].append(choice)

def clear_grid(grid):
    for index in range(len(grid)):
        grid.insert(index, " ")
        del grid[index+1]
        
def check_win():
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    for x in solution:
        if all(y in positions["X"] for y in x):
            print("Congratulations, you win!")
            return True

    for x in solution:
        if all(y in positions["O"] for y in x):
            print("Sorry, the computer wins. Better luck next time.")
            return True
        
    return False

def check_draw():
    if (len(positions["X"]) + len(positions["O"])) == 9:
        return True
    return False


main()