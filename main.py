import os
import time
from termcolor import colored

# prints a 2D list grid nicely
def print_grid(grid):
    for r in range(len(grid)): # rows
        for c in range(len(grid[0])):  # columns
            print(grid[r][c], end="")
        print()


# returns a list where the 1st element is the ROW
# containing the robot (the 1) and the 2nd element
# is the COLUMN containing the robot; for example,
# if the list returned by this function is [5, 3],
# then the "1" is currently in row 5, column 3
def find_robot_in_grid(grid):
    location = []
    for r in range(len(grid)): # rows
        for c in range(len(grid[0])):  # columns
            if grid[r][c] == "🤖":
                location.append(r)
                location.append(c)
                return location
    return [] # if the function gets here, then there was no 1


def can_move_up(grid, from_row, from_column):
  find_robot_in_grid(grid)
  if grid[from_row - 1][from_column] == "⬛":
    return False
  elif grid[from_row - 1][from_column] == "🔒" and get_key == False:
    return False
  else:
    return True


def can_move_down(grid, from_row, from_column):
  find_robot_in_grid(grid)
  if grid[from_row + 1][from_column] == "⬛":
    return False
  else:
    return True


def can_move_left(grid, from_row, from_column):
  find_robot_in_grid(grid)
  if grid[from_row][from_column - 1] == "⬛":
    return False
  elif grid[from_row][from_column - 1] == "🏆" and get_treasure == False:
    return False
  elif grid[from_row][from_column - 1] == "💧" and get_bucket == False:
    return False
  else:
    return True


def can_move_right(grid, from_row, from_column):
  find_robot_in_grid(grid)
  if grid[from_row][from_column + 1] == "⬛":
    return False
  else:
    return True


def dragon_fire():
  while dragon_alive == True:
    maze[2][7] == "🔥"
    time.sleep(1)
    maze[2][7] == "⬜"
    time.sleep(2)
  find_robot_in_grid(grid)
  
    
# MAIN PROGRAM
maze = [["🏆", "⬜", "⬜", "⬜", "⬜", "⬜", "⬛","⬛", "💰"],
        ["⬛", "⬛", "⬛", "⬛", "⬛", "⬜", "⬛", "⬛", "⬜"],
        ["⬛", "🔑", "⬛", "⬛", "⬜", "⬜", "⬛", "⬛", "🐉"],
        ["⬛", "⬜", "⬛", "⬛", "🔒", "⬛", "⬛", "⬛", "🔥"],
        ["⬛", "⬜", "⬜", "⬛", "⬜", "⬜", "🪣 ", "⬜", "⬜"],
        ["⬛", "⬛", "⬜", "⬛", "⬜", "⬛", "⬛", "⬛", "⬛"],
        ["🏹", "⬜", "⬜", "⬜", "⬜", "⬛", "⬛", "⬛", "⬛"],
        ["⬛", "⬛", "⬛", "⬛", "⬜", "⬜", "⬜", "⬜", "🤖"],
        ["⬜", "💧", "⬜", "⬜", "⬜", "⬛", "⬛", "⬛", "⬛"]]



direction = ""
reach_trophy = False
weapon = ""
get_weapon = False
get_key = False
unlock_door = False
dragon_alive = True
get_treasure = False
get_bucket = False
fill_water = False
fire_out = False

while (direction != "q") or (reach_trophy == False):
    os.system("clear")
    print_grid(maze)
    print()
    robot_location = find_robot_in_grid(maze)
    row = robot_location[0]
    column = robot_location[1]

    # [0, 0] is the trophy's location
    # if robot_location is at the trophy's location, then the loop breaks
    if robot_location == [0, 0]:
        reach_trophy = True
        break
    
    # [6, 0] is the location of the bow and arrow
    # tell player they have picked up a weapon
    if robot_location == [6, 0] and get_weapon == False:
      weapon = "bow and arrow"
      print(colored("You picked up a weapon!", "blue"))
      print()
      get_weapon = True
      
    # [2, 8] is the dragon location
    # if player has a weapon, they are able to kill the dragon
    # if player doesn't have a weapon, they die
    if robot_location == [2, 8] and dragon_alive == True:
      if weapon == "bow and arrow":
        dragon_alive = False
        print(colored("You slain the dragon!", "blue"))
        print()
      else:
        print(colored("You attempted to fight the dragon without a weapon. The dragon ate you alive. You died.", "red"))
        break

    # [2, 1] is the key's location
    if robot_location == [2, 1] and get_key == False:
      get_key = True
      print(colored("You received the key. You can go through the lock.", "blue"))
      print()

    # [3, 4] is the door's location
    # if player has the key, door unlock
    if robot_location == [3, 4] and get_key == True and unlock_door == False:
      unlock_door = True
      print(colored("You unlocked the door.", "blue"))
      print()

    # [0, 8] is the treasure's location
    if robot_location == [0, 8] and get_treasure == False:
      get_treasure = True
      print(colored("You found the treasure! You can now exit this level.", "blue"))
      print()

    if robot_location == [4, 6] and get_bucket == False: # bucket's location
      get_bucket = True
      print(colored("You obtained a bucket!", "blue"))
      print()

    # [8, 1] is water's location
    if robot_location == [8, 1] and get_bucket == True and fill_water == False:
      fill_water = True
      print(colored("You filled your bucket with water!", "blue"))
      print()

    # [3, 8] is the fire's location
    if robot_location == [3, 8] and fill_water == False:
      print(colored("You tried to go through the fire. You got burnt to death.", "red"))
      break
    elif robot_location == [3, 8] and fire_out == False:
      fire_out = True
      print(colored("You extinguished the fire!", "blue"))
      print()

      
    print("Move the robot using W, S, A, or D")
    print("for Up, Down, Left, Right; enter Q to quit")
    direction = input("Enter direction to move > ")
    direction = direction.lower()
  
        
    if direction == "w":
        # write code to move the "1" UP one spot in the grid
        # UNLESS the robot is already in the top row,
        # then print an error message ("The robot can't move up!") for 1 second
      
        if (row == 0) or can_move_up(maze, row, column) == False:
            if maze[row - 1][column] == "🔒" and get_key == False:
                print()
                print(colored("You need a key to pass through.", "red"))
                time.sleep(1)
            else:
                print("The robot can't move up!")
                time.sleep(1)
        else:
            maze[row - 1][column] = "🤖"
            maze[row][column] = "⬜"       
    elif direction == "s":
        # write code to move the "1" DOWN one spot in the grid
        # UNLESS the robot is already in the bottom row,
        # then print an error message ("The robot can't move down!") for 1 second
        if (row == 8) or can_move_down(maze, row, column) == False:
            print("The robot can't move down!")
            time.sleep(1)
        else:
            maze[row + 1][column] = "🤖"
            maze[row][column] = "⬜"
    elif direction == "a":
        # write code to move the "1" LEFT one spot in the grid
        # UNLESS the robot is already in the leftmost column,
        # then print an error message ("The robot can't move left!") for 1 second
        if (column == 0) or can_move_left(maze, row, column) == False:
            if maze[row][column - 1] == "🏆":
                print()  
                print(colored("You must have the treasure to exit the level!", "red"))
                time.sleep(1)

            elif maze[row][column - 1] == "💧":
                print()
                print(colored("You need a bucket first.", "red"))
                time.sleep(1)
              
            else:
                print("The robot can't move left!")
                time.sleep(1)
        else:
            maze[row][column - 1] = "🤖"
            maze[row][column] = "⬜"
    elif direction == "d":
        # write code to move the "1" RIGHT one spot in the grid
        # UNLESS the robot is already in the rightmost column,
        # then print an error message ("The robot can't move left!") for 1 second
        if (column == 8) or can_move_right(maze, row, column) == False:
            print("The robot can't move right!")
            time.sleep(1)
        else:
            maze[row][column + 1] = "🤖"
            maze[row][column] = "⬜"
      
if reach_trophy == True:
  print(colored("YOU WIN!", "green"))