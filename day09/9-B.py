from collections import Counter, defaultdict

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    
    # grid = [[x for x in line] for line in s.split('\n')]
    free = False
    l = []
    count = 0
    literal_count = 0
    free_spaces = []
    file_sizes = {}
    file_positions = {}
    for c in s:
        if c.isdigit():
            if free:
                free_pos = len(l)
                l.extend(['.'] * int(c))
                free = not free
                # length of free space starting at free_pos
                free_spaces.append((free_pos, int(c)))
            else:
                file_positions[count] = len(l)
                file_sizes[count] = int(c)
                l.extend([str(count)] * int(c))
                literal_count += int(c)
                count += 1
                free = not free

    # tick down counts, find their earliest free space they fit in
    prefix = set()
    prefix.add(0)
    # slow condition, check it later
    for i in range(count-1, -1, -1):
        # print(''.join(l))
        if i in prefix:
            continue
        file_size = file_sizes[i]
        file_pos = file_positions[i]
        for free_idx, (free_pos, free_size) in enumerate(free_spaces):
            if free_size >= file_size and free_pos < file_pos:
                # transfer
                for x in range(file_size):
                    l[free_pos+x] = l[file_pos+x]
                    l[file_pos+x] = '.'
                diff = free_size - file_size
                free_spaces[free_idx] = (free_pos+file_size, diff)
                prefix.add(i)
                break
    # print(l)


    for i, n in enumerate(l):
        if n != '.':
            total += i * int(n)

    return total    

print(main())
