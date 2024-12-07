from collections import Counter, defaultdict
from itertools import product
from tqdm import tqdm

def main():
    s = ""
    total = 0
    with open('input.txt') as f:
        s = f.read()

    for line in tqdm(s.split('\n')):
        target, operands = line.split(': ')
        target = int(target)
        operands = [int(x) for x in operands.split(' ')]
        operator_combs = product(['+', '*', '||'], repeat=len(operands) - 1)
        for operator_comb in operator_combs:
            prod = operands[0]
            for op, operand in zip(operator_comb, operands[1:]):
                if op == '+':
                    prod += operand
                else:
                    prod *= operand
            if prod == target:
                total += target
                break

    return total

print(main())
