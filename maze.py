import random
from collections import deque

# Maze dimensions
ROWS = 25
COLS = 25

# Maze symbols
WALL = '#'
EMPTY = ' '
START = 'S'
END = 'E'
PLAYER = 'P'
PATH = '.'

# Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Create a random maze
def create_maze():
    maze = [[WALL] * COLS for _ in range(ROWS)]
    for row in range(1, ROWS - 1):
        for col in range(1, COLS - 1):
            if random.random() < 0.7:
                maze[row][col] = EMPTY
    maze[random.randint(1, ROWS - 2)][random.randint(1, COLS - 2)] = START
    maze[random.randint(1, ROWS - 2)][random.randint(1, COLS - 2)] = END
    return maze

# Print the maze
def print_maze(maze):
    for row in maze:
       print(' '.join(row))
 
# Move the player in the maze
def move_player(maze, direction, player_pos):
    row, col = player_pos
    if direction == UP and maze[row - 1][col] != WALL:
        maze[row][col] = PATH
        maze[row - 1][col] = PLAYER
        return (row - 1, col)
    elif direction == DOWN and maze[row + 1][col] != WALL:
        maze[row][col] = PATH
        maze[row + 1][col] = PLAYER
        return (row + 1, col)
    elif direction == LEFT and maze[row][col - 1] != WALL:
        maze[row][col] = PATH
        maze[row][col - 1] = PLAYER
        return (row, col - 1)
    elif direction == RIGHT and maze[row][col + 1] != WALL:
        maze[row][col] = PATH
        maze[row][col + 1] = PLAYER
        return (row, col + 1)
    return player_pos

# Find the starting position in the maze
def find_start_position(maze):
    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == START:
                return (row, col)

# Perform breadth-first search to find the path
def find_path(maze, start_pos, end_pos):
    queue = deque([(start_pos, [])])
    visited = set()

    while queue:
        curr_pos, path = queue.popleft()
        row, col = curr_pos

        if curr_pos == end_pos:
            return path

        for direction in [UP, DOWN, LEFT, RIGHT]:
            if direction == UP and maze[row - 1][col] != WALL and (row - 1, col) not in visited:
                queue.append(((row - 1, col), path + [UP]))
                visited.add((row - 1, col))
            elif direction == DOWN and maze[row + 1][col] != WALL and (row + 1, col) not in visited:
                queue.append(((row + 1, col), path + [DOWN]))
                visited.add((row + 1, col))
            elif direction == LEFT and maze[row][col - 1] != WALL and (row, col - 1) not in visited:
                queue.append(((row, col - 1), path + [LEFT]))
                visited.add((row, col - 1))
            elif direction == RIGHT and maze[row][col + 1] != WALL and (row, col + 1) not in visited:
                queue.append(((row, col + 1), path + [RIGHT]))
                visited.add((row, col + 1))

    return None

# Play the maze game
def play_maze_game():
    maze = create_maze()
    print_maze(maze)
    player_pos = find_start_position(maze)

    end_pos = None
    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == END:
                end_pos = (row, col)
                break

    path = find_path(maze, player_pos, end_pos)
    if path:
        for direction in path:
            player_pos = move_player(maze, direction, player_pos)

        maze[player_pos[0]][player_pos[1]] = PLAYER
        print_maze(maze)
    else:
        print("No path found to the end point.")

    maze[end_pos[0]][end_pos[1]] = END
    print("Game Over")

# Start the maze game
play_maze_game()