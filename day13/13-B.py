from collections import Counter, defaultdict
import numpy as np
import math

LARGE_NUM_PAD = 10000000000000

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    
    # grid = [[x for x in line] for line in s.split('\n')]

    games = s.split('\n\n')
    for i, game in enumerate(games):
        A, B, prize = game.split('\n')
        Ax_str, Ay_str = A.split(': ')[1].split(', ')
        Ax = int(Ax_str[2:])
        Ay = int(Ay_str[2:])
        Bx_str, By_str = B.split(': ')[1].split(', ')
        Bx = int(Bx_str[2:])
        By = int(By_str[2:])
        prizeX_str, prizeY_str = prize.split(': ')[1].split(', ')
        prizeX = int(prizeX_str[2:]) + LARGE_NUM_PAD
        prizeY = int(prizeY_str[2:]) + LARGE_NUM_PAD
        A = (Ax, Ay)
        B = (Bx, By)
        prize = (prizeX, prizeY)


        # solve linalg
        arr = np.array([[Ax, Bx], [Ay, By]])
        b = np.array([prizeX, prizeY])
        solution = np.linalg.solve(arr, b).tolist()
        if all(is_close_to_whole(x) for x in solution) and np.allclose(np.dot(arr, solution), b):
            solution = [round(x) for x in solution]
            total += 3 * solution[0] + solution[1]

    return total

def is_close_to_whole(x, tol=1e-3):
  return abs(x - round(x)) < tol

print(main())