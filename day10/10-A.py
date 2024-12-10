from collections import Counter, defaultdict

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def get_neighbors_decremented(n, pos, graph):
    for dir in dirs:
        dx, dy = dir
        new_pt = (pos[0]+dx, pos[1]+dy)
        if graph[new_pt] == str(n-1):
            yield new_pt, n-1

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    
    grid = [[x for x in line] for line in s.split('\n')]
    graph = defaultdict(str)
    q = []
    origins = defaultdict(set)
    zeros = []
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == '.':
                continue
            graph[(i, j)] = c
            if int(c) == 9:
                q.append((i, j, 9, i, j))
            elif int(c) == 0:
                zeros.append((i, j))
    # DFS from each 9 to each 0
    while q:
        curr = q.pop()
        curr_x, curr_y, curr_n, origin_x, origin_y = curr
        for neighbor, new_val in get_neighbors_decremented(curr_n, (curr_x, curr_y), graph):
            if new_val != 0:
                q.insert(0, (neighbor[0], neighbor[1], new_val, origin_x, origin_y))
            elif new_val == 0:
                origins[neighbor].add((origin_x, origin_y))

    # accumulate zeros
    for zero in zeros:
        total += len(origins[zero])

    return total    

print(main())
