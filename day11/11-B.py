from collections import Counter, defaultdict
import functools



MAX_DEPTH = 75

memo = {}

@functools.cache
def split(n, depth):
    if depth == 0:
        return 1
    str_n = str(n)
    if n == 0:
        return split(1, depth-1)
    elif len(str_n) % 2 == 0:
        left = int(str_n[:len(str_n)//2])
        right = str_n[len(str_n)//2:].lstrip('0')
        if len(right) == 0:
            right = 0
        else:
            right = int(right)
        return split(left, depth-1) + split(right, depth-1)
    else:
        return split(n * 2024, depth-1)

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()

    l = [int(x) for x in s.split()]
    new_list = []
    for x in l:
        total += split(x, MAX_DEPTH)

    return total

print(main())
