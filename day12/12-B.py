from collections import Counter, defaultdict

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def get_neighbors(p):
    for dir in DIRS:
        yield (p[0] + dir[0], p[1] + dir[1])

def get_neighbors_horiz(p):
    yield (p[0] + 1, p[1])
    yield (p[0] - 1, p[1])

def get_neighbors_vert(p):
    yield (p[0], p[1] + 1)
    yield (p[0], p[1] - 1)

def get_perimeter(symbol, component_nodes, graph):
    # need to sweep line to find perimeters
    # for each top, bottom, left, right, need to sweep and find contiguous blocks
    # top
    # print("top")
    perimeter = 0
    top_boundary_nodes = {node for node in component_nodes if graph[(node[0]-1, node[1])] != symbol}
    top_rows = set(x[0] for x in top_boundary_nodes)
    for row in top_rows:
        # sweep row left to right, look for contiguous
        boundary_nodes_in_row = {node for node in top_boundary_nodes if node[0] == row}
        top_cols = list(sorted(x[1] for x in top_boundary_nodes if x[0] == row))
        for col in top_cols:
            c = graph[(row, col)]
            if (c == symbol) and (row, col-1) not in boundary_nodes_in_row:
                perimeter += 1
    # bottom
    # print(perimeter)
    # print("bottom")
    bot_boundary_nodes = {node for node in component_nodes if graph[(node[0]+1, node[1])] != symbol}
    bot_rows = set(x[0] for x in bot_boundary_nodes)
    for row in bot_rows:
        # sweep row left to right, look for contiguous
        boundary_nodes_in_row = {node for node in bot_boundary_nodes if node[0] == row}
        bot_cols = list(sorted(x[1] for x in bot_boundary_nodes if x[0] == row))
        for col in bot_cols:
            c = graph[(row, col)]
            if (c == symbol) and (row, col-1) not in boundary_nodes_in_row:
                perimeter += 1
    # print(perimeter)
    # left
    # print("left")
    l_boundary_nodes = {node for node in component_nodes if graph[(node[0], node[1]-1)] != symbol}
    l_cols = set(x[1] for x in l_boundary_nodes)
    for col in l_cols:
        # sweep cols top to bottom, look for contiguous
        boundary_nodes_in_col = {node for node in l_boundary_nodes if node[1] == col}
        l_rows = list(sorted(x[0] for x in l_boundary_nodes if x[1] == col))
        for row in l_rows:
            c = graph[(row, col)]
            if (c == symbol) and (row-1, col) not in boundary_nodes_in_col:
                perimeter += 1
    # print(perimeter)
    # right
    # print("right")
    r_boundary_nodes = {node for node in component_nodes if graph[(node[0], node[1]+1)] != symbol}
    r_cols = set(x[1] for x in r_boundary_nodes)
    # print(r_cols, r_rows)
    for col in r_cols:
        # sweep col top to bottom, look for contiguous
        boundary_nodes_in_col = {node for node in r_boundary_nodes if node[1] == col}
        r_rows = list(sorted(x[0] for x in r_boundary_nodes if x[1] == col))
        for row in r_rows:
            c = graph[(row, col)]
            if (c == symbol) and (row-1, col) not in boundary_nodes_in_col:
                perimeter += 1
    # print(perimeter)
    return perimeter

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()

    grid = [[x for x in line] for line in s.split('\n')]
    graph = defaultdict(str)
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            graph[(i, j)] = c

    # do connected components
    # area is size of connected component
    # perimeter is number of non-component tiles reachable from this component
    components = {}
    visited = set()
    component_num = 0
    symbols = {}
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if (i, j) in visited:
                continue
            symbol = graph[(i, j)]
            symbols[component_num] = symbol
            q = [(i, j)]
            visited.add((i, j))
            components[component_num] = [(i, j)]
            while q:
                current = q.pop()
                for neighbor in get_neighbors(current):
                    if graph[neighbor] == symbol:
                        if neighbor not in visited:
                            components[component_num].append(neighbor)
                            visited.add(neighbor)
                            q.append(neighbor)
            component_num += 1

    for component, nodes in components.items():
        # print("Calculating component", component)
        area = len(nodes)
        perimeter = get_perimeter(symbols[component], nodes, graph)

        # print(component, symbols[component], area, perimeter, area * perimeter)
        total += area * perimeter

    return total

print(main())
