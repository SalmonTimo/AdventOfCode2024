from collections import Counter, defaultdict
from itertools import product
from tqdm import tqdm


def recur_combinations(operands, solutions):
    first_operator, rest = operands[0] 
    

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    # grid = [[x for x in line] for line in s.split('\n')]
    # try brute force pt 1
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
            # if target == 292:
            #     print(target, operands, operator_comb, prod)
            if prod == target:
                # print("Found prod for target", prod, target, operator_comb, operands)
                total += target
                break

    return total

print(main())
