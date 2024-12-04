from collections import Counter, defaultdict

def in_grid(max_x, max_y, x, y):
    return x >= 0 and x < max_x and y >= 0 and y < max_y

def check_diagonal(grid, start_x, start_y, max_x, max_y):
    # start is at an A
    diag_1 = [(start_x-1, start_y-1), (start_x+1, start_y+1)]
    diag_2 = [(start_x-1, start_y+1), (start_x+1, start_y-1)]
    chars_1 = []
    chars_2 = []
    for pair in diag_1:
        if not in_grid(max_x, max_y, pair[0], pair[1]):
            return False
        else:
            chars_1.append(grid[pair[0]][pair[1]])
    for pair in diag_2:
        if not in_grid(max_x, max_y, pair[0], pair[1]):
            return False
        else:
            chars_2.append(grid[pair[0]][pair[1]])
    
    # print(start_x, start_y, diag_1, diag_2, chars_1, chars_2)
    return (set(chars_1) == {'M', 'S'}) and (set(chars_2) == {'M', 'S'})

def main():
    visited = {}
    s = ""
    total = 0
    with open('input.txt') as f:
    # with open('input.txt') as f:
        s = f.read()
    grid = [[x for x in line] for line in s.split('\n')]
    lines = s.split('\n')
    # for each 'A' in input, search left, right, down, up, diagonal
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 'A':
                if check_diagonal(grid, i, j, len(grid), len(grid[0])):
                    total += 1
    return total

print(main())