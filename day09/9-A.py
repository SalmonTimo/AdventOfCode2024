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
    for c in s:
        if c.isdigit():
            if free:
                l.extend(['.'] * int(c))
                free = not free
            else:
                l.extend([str(count)] * int(c))
                literal_count += int(c)
                count += 1
                free = not free
    # print(''.join(l))
    l_ptr = l.index('.')
    r_ptr = len(l) - 1
    while (l[r_ptr] == '.'):
        r_ptr -= 1

    while l_ptr < literal_count:
        l[l_ptr] = l[r_ptr]
        l[r_ptr] = '.'
        l_ptr += 1
        r_ptr -= 1
        while (l_ptr < len(l) and l[l_ptr] != '.'):
            l_ptr += 1
        while (l[r_ptr] == '.'):
            r_ptr -= 1

    # print(''.join(l))

    for i, n in enumerate(l[:literal_count]):
        total += i * int(n)

    return total    

print(main())
