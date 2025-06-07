import random

# Maze dimensions (should be odd numbers for proper generation)
WIDTH = 21
HEIGHT = 21

# Maze elements
WALL = '#'
PATH = ' '
START = 'S'
END = 'E'
SOLUTION = '.'

# Create a grid full of walls
def create_maze(width, height):
    return [[WALL for _ in range(width)] for _ in range(height)]

# Recursive function to generate maze
def generate_maze(maze, x, y):
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 1 <= nx < WIDTH - 1 and 1 <= ny < HEIGHT - 1:
            if maze[ny][nx] == WALL:
                maze[ny][nx] = PATH
                maze[y + dy//2][x + dx//2] = PATH
                generate_maze(maze, nx, ny)

# Print the maze to the terminal
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# DFS Maze Solver
def solve_maze(maze, x, y, end_x, end_y):
    if x == end_x and y == end_y:
        return True
    if maze[y][x] != PATH:
        return False
    maze[y][x] = SOLUTION
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        if solve_maze(maze, x + dx, y + dy, end_x, end_y):
            return True
    maze[y][x] = PATH
    return False

# Main program
maze = create_maze(WIDTH, HEIGHT)

# Start from (1,1)
maze[1][1] = PATH
generate_maze(maze, 1, 1)

# Define start and end points
start_x, start_y = 1, 1
end_x, end_y = WIDTH - 2, HEIGHT - 2

# Solve the maze
solve_maze(maze, start_x, start_y, end_x, end_y)

# Mark start and end
maze[start_y][start_x] = START
maze[end_y][end_x] = END

# Print the result
print_maze(maze)