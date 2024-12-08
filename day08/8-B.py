from collections import Counter, defaultdict
from tqdm import tqdm
from itertools import combinations

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    
    grid = [[x for x in line] for line in s.split('\n')]
    node_map = defaultdict(list)
    nodes = defaultdict(str)
    anti_nodes = set()

    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            nodes[(i, j)] = c
            if c != '.':
                node_map[c].append((i, j))

    max_x = len(grid)
    max_y = len(grid[0])

    # for each node key, get distances between each combination
    for key in node_map.keys():
        # print(list(combinations(node_map[key], 2)), end='\n\n')
        for comb in combinations(node_map[key], 2):
            # get distance between two points
            p1, p2 = comb
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            
            anti_node_1 = (p1[0] - dx, p1[1] - dy)
            while in_bounds(anti_node_1, max_x, max_y):
                if anti_node_1 not in anti_nodes:
                    anti_nodes.add(anti_node_1)
                anti_node_1 = (anti_node_1[0] - dx, anti_node_1[1] - dy)

            anti_node_2 = (p2[0] + dx, p2[1] + dy)
            while in_bounds(anti_node_2, max_x, max_y):
                if anti_node_2 not in anti_nodes:
                    anti_nodes.add(anti_node_2)
                anti_node_2 = (anti_node_2[0] + dx, anti_node_2[1] + dy)
            for pt in comb:
                if pt not in anti_nodes:
                    anti_nodes.add(pt)


    # filter anti_nodes

    anti_nodes = {p for p in anti_nodes if p[0] >= 0 and p[0] < max_x and p[1] >= 0 and p[1] < max_y}
    # print(list(sorted(anti_nodes)))
    return len(anti_nodes)

def in_bounds(p, max_x, max_y):
    return p[0] >= 0 and p[0] < max_x and p[1] >= 0 and p[1] < max_y

print(main())
