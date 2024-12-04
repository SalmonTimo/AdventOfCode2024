from collections import Counter, defaultdict

def in_grid(max_x, max_y, x, y):
    return x >= 0 and x < max_x and y >= 0 and y < max_y

def get_strings(grid, start_x, start_y, max_x, max_y):
    offsets = (-1, 0, 1)
    for x in offsets:
        for y in offsets:
            output = []
            if x == 0 and y == 0:
                continue
            for i in range(4):
                if in_grid(max_x, max_y, start_x+x*i, start_y+y*i):
                    output.append(grid[start_x+x*i][start_y+y*i])
            yield "".join(output)

def main():
    visited = {}
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    grid = [[x for x in line] for line in s.split('\n')]
    lines = s.split('\n')
    # for each 'X' in input, search left, right, down, up, diagonal
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 'X':
                for candidate in get_strings(grid, i, j, len(grid), len(grid[0])):
                    if candidate == ('XMAS') or candidate == 'SAMX':
                        total += 1
    return total

print(main())