from collections import Counter, defaultdict

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def get_neighbors(p):
    for dir in DIRS:
        yield (p[0] + dir[0], p[1] + dir[1])

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
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if (i, j) in visited:
                continue
            symbol = graph[(i, j)]
            print(symbol, component_num)
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
        area = len(nodes)
        node_set = set(nodes)
        perimeter = len([x for p in nodes for x in get_neighbors(p) if x not in node_set])
        print(component, area, perimeter, area * perimeter)
        total += area * perimeter

    return total

print(main())
