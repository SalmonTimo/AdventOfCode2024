from collections import Counter, defaultdict

nxt_dir = {
    (0 , -1) : (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1)
}

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    grid = [[x for x in line] for line in s.split('\n')]
    graph = defaultdict(str)
    start = (-1, -1)
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            graph[(x, y)] = c
            if c == '^':
                start = (x, y)
                graph[(x, y)] = '.'

    dir = (0, -1)
    visited = {start}
    visited_pos = {(start, dir)}
    # print(start)
    cur_pos = start
    while True:
        nxt = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])
        if (nxt, dir) in visited:
            break
        if graph[nxt] == '':
            break
        if graph[nxt] == '#':
            # rotate
            dir = nxt_dir[dir]
        else:
            if nxt not in visited:
                visited.add(nxt)
            if (nxt, dir) not in visited_pos:
                visited_pos.add((nxt, dir))
            cur_pos = nxt
            grid[nxt[0]][nxt[1]] = 'X'
    # print('\n'.join(str(line) for line in grid))
    # print(list(sorted(visited)))
    return len(visited)

print(main())
