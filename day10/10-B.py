from collections import Counter, defaultdict

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def get_neighbors_incremented(n, pos, graph):
    for dir in dirs:
        dx, dy = dir
        new_pt = (pos[0]+dx, pos[1]+dy)
        if graph[new_pt] == str(n+1):
            yield new_pt, n+1

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    
    grid = [[x for x in line] for line in s.split('\n')]
    graph = defaultdict(str)
    q = []
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == '.':
                continue
            graph[(i, j)] = c
            if int(c) == 0:
                q.append((i, j, 0))

    # from each 0, DFS, see how many times we hit a 9, this sums to total
    while q:
        # print(q)
        curr = q.pop()
        curr_x, curr_y, curr_n = curr
        for neighbor, new_val in get_neighbors_incremented(curr_n, (curr_x, curr_y), graph):
            if new_val != 0:
                q.insert(0, (neighbor[0], neighbor[1], new_val))
            if new_val == 9:
                total += 1

    return total    

print(main())
