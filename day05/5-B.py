from collections import Counter, defaultdict

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    # grid = [[x for x in line] for line in s.split('\n')]
    lines = s.split('\n')
    rules = defaultdict(list)
    case_lines = []
    for line in lines:
        if '|' in line:
            x, y = line.split('|')
            # x must be printed before y
            # rules[y] shows the values that must be printed before it
            rules[y].append(x)
        else:
            if any(c != "" for c in line):
                case_lines.append(line)

    incorrect = []
    for line in case_lines:
        valid = True
        prefix_set = set()
        for i, n in enumerate(line.split(',')):
            for before in rules[n]:
                if before in line[i+1:] and before not in prefix_set:
                    # print("Found violation in rule", n, before, prefix_set, line[i+1:])
                    valid = False
            prefix_set.add(n)
        if not valid:
            # print(line, "], is valid")
            incorrect.append(line)

    for line in incorrect:
        values = line.split(',')
        invalid = True
        found_valid = False
        while not found_valid:
            found_error = False
            prefix_set = set()
            for i, n in enumerate(values):
                for before in rules[n]:
                    if before in values[i+1:] and before not in prefix_set:
                        # print("Found violation in rule", n, before, prefix_set, line[i+1:])
                        found_error = True
                        # insert n before this one
                        old_pos = values[i+1:].index(before) + i+1
                        values.pop(old_pos)
                        values.insert(i, before)
                prefix_set.add(n)
                if found_error:
                    break
            if not found_error:
                found_valid = True
        total += int(values[len(values) // 2])

    return total

print(main())




# example complex number grid:
# grid = defaultdict(complex)
# for x, line in enumerate(s.split('\n')):
#   for y, c in enumerate(line):
#       grid[x+yj] = c