from collections import Counter, defaultdict

N_ITERATIONS = 25

def main():
    s = ""
    total = 0
    with open('sample_input.txt') as f:
    # with open('input.txt') as f:
        s = f.read()

    l = [int(x) for x in s.split()]
    for _ in range(N_ITERATIONS):
        new_list = []
        for x in l:
            if x == 0:
                new_list.append(1)
            elif len(str(x)) % 2 == 0:
                x = str(x)
                left, right = x[:len(x)//2], x[len(x)//2:]
                right.lstrip('0')
                new_list.append(int(left))
                new_list.append(int(right))
            else:
                new_list.append(x * 2024)
        l = new_list

    return len(l)

print(main())
