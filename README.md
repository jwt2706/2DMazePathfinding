# Maze Pathfinding

Algorithmically solves randomly generated 2D mazes.

Here's an example of a generated maze: (S = start, E = end)
```
# # # # # # # # # # # # # # # # # # # #
#   #     #       #       #     #   # #
#     # #   # # #       #             #
#   #   # #       #     #         # E #
#   #       # # #   #           #   # #
# #   #                 # # #     #   #
# #     #   #                 # # #   #
#     #     #   #     #     #   #   # #
#   # #   #     #     #   #           #
# #       #     #   # #         #     #
#               # #       #   #     # #
#   #           #         #     #     #
# #   S           # #     #           #
# #                 # #     #   #     #
# #             # #     #             #
#     # #       #         # # #       #
# #   # #   #   # # #               # #
#   # # #   # #     #                 #
#           #               #         #
# # # # # # # # # # # # # # # # # # # #
```
And here is the solved version:
```
# # # # # # # # # # # # # # # # # # # #
#   #     #       #       #     #   # #
#     # #   # # #       # . . . . . . #
#   #   # #       #     # .       # P #
#   #       # # #   # . . .     #   # #
# #   #   . . . . . . . # # #     #   #
# #     # . #                 # # #   #
#     # . . #   #     #     #   #   # #
#   # # . #     #     #   #           #
# #   . . #     #   # #         #     #
#     .         # #       #   #     # #
#   # .         #         #     #     #
# #   .           # #     #           #
# #                 # #     #   #     #
# #             # #     #             #
#     # #       #         # # #       #
# #   # #   #   # # #               # #
#   # # #   # #     #                 #
#           #               #         #
# # # # # # # # # # # # # # # # # # # #
```








#### TODO
- Add option to play the game as a player
- Add option to manually design a maze
- Add another dimension to make it 3D

# Docs

### Maze Generation

The maze generation is handled by the `create_maze` function. Here's how it works:

1. It initializes a 2D list called `maze` with dimensions specified by the `ROWS` and `COLS` constants.
2. It fills the entire maze with walls (`#` symbol) by default.
3. For each cell in the maze (excluding the outer border), it randomly decides whether to make the cell empty (` ` symbol) or a wall based on a probability of 0.7. This probability can be adjusted to control the density of walls in the maze.
4. It randomly selects two cells within the maze and designates one as the start cell (`S` symbol) and the other as the end cell (`E` symbol).
5. Finally, it returns the generated maze.

### Pathfinding Algorithm

The pathfinding algorithm is a simple breadth-first search (BFS) implemented in the `find_path` function. Here's how it works:

1. It initializes a `queue` as a deque (double-ended queue) and enqueues the `start_pos` along with an empty `path` list.
2. It also initializes a `visited` set to keep track of visited positions in the maze.
3. While the `queue` is not empty, it dequeues the current position (`curr_pos`) and the corresponding path.
4. If the `curr_pos` is the same as the `end_pos`, it means the end point has been reached, and the function returns the `path`.
5. Otherwise, for each possible direction (up, down, left, right), it checks if the move is valid (not a wall) and the new position has not been visited before.
6. If the move is valid, it enqueues the new position along with the updated path, and adds the new position to the `visited` set.
7. The process continues until either the end point is found or there are no more positions to explore.
8. If no path is found, the function returns `None`.

### Maze Printing

The `print_maze` function is responsible for printing the maze to the console. It takes the `maze` as input and iterates over each row of the maze, printing the cells separated by spaces. This function is used to display the maze before and after the player's movement.

### Movement

The `move_player` function handles the movement of the player within the maze. It takes the current `maze`, the `direction` to move in, and the `player_pos` (current position of the player) as inputs. Here's how it works:

1. It retrieves the current position of the player as `row` and `col`.
2. Based on the given `direction`, it checks if the cell in the desired direction is not a wall.
3. If the move is valid, it updates the maze by replacing the player's current position with a path (`.` symbol) and updates the new cell with the player symbol (`P`).
4. It returns the updated `player_pos` as the new position of the player.

### Starting Position

The `find_start_position` function is used to find the starting position (`S`) in the maze. It takes the `maze` as input and iterates over each cell to find the coordinates of the cell with the `START` symbol. It returns the `(row, col)` tuple representing the position of the starting cell.

### Playing the Maze Game

The `play_maze_game` function orchestrates the entire maze game. Here's how it works:

1. It calls the `create_maze` function to generate a random maze and assigns it to the `maze` variable.
2. It calls the `print_maze` function to print the initial state of the maze.
3. It finds the starting position (`player_pos`) using the `find_start_position` function.
4. It searches for a path from the starting position to the end position using the `find_path` function.
5. If a path is found, it iterates over each direction in the path and moves the player accordingly using the `move_player` function.
6. After the player has reached the end position, it updates the maze with the player symbol (`P`) and prints the final state of the maze.
7. If no path is found, it prints a message indicating that no path was found to the end point.
8. Finally, it updates the maze with the end symbol (`E`) and prints "Game Over" to indicate the end of the game.