from collections import Counter, defaultdict

MAX_TIMES = 100

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    
    # grid = [[x for x in line] for line in s.split('\n')]

    games = s.split('\n\n')
    for game in games:
        A, B, prize = game.split('\n')
        Ax_str, Ay_str = A.split(': ')[1].split(', ')
        Ax = int(Ax_str[2:])
        Ay = int(Ay_str[2:])
        Bx_str, By_str = B.split(': ')[1].split(', ')
        Bx = int(Bx_str[2:])
        By = int(By_str[2:])
        prizeX_str, prizeY_str = prize.split(': ')[1].split(', ')
        prizeX = int(prizeX_str[2:])
        prizeY = int(prizeY_str[2:])
        A = (Ax, Ay)
        B = (Bx, By)
        prize = (prizeX, prizeY)


        # brute force check all combinations of moving
        minimum_solution = None
        any_found = False
        for A_iter in range(MAX_TIMES):
            for B_iter in range(MAX_TIMES):
                if (Ax * A_iter + Bx * B_iter, Ay * A_iter + By * B_iter) == prize:
                    if not any_found:
                        any_found = True
                        minimum_solution = 3 * A_iter + B_iter
                    else:
                        minimum_solution = min(minimum_solution, 3 * A_iter + B_iter)
        print(minimum_solution)
        if minimum_solution is not None:
            total += minimum_solution
    return total

print(main())