from collections import Counter, defaultdict
import pprint
import time
import re

WIDTH = 101
HEIGHT = 103

def main():
    s = ""
    total = 0
    # with open('sample_input.txt') as f:
    with open('input.txt') as f:
        s = f.read()
    
    # grid = [[x for x in line] for line in s.split('\n')]
    robot_positions = []
    robot_velocities = []
    for i, line in enumerate(s.split('\n')):
        pos_part, velocity_part = line.split(' ')
        p = tuple(int(x) for x in pos_part[2:].split(','))
        v = tuple(int(x) for x in velocity_part[2:].split(','))
        robot_positions.append(p)
        robot_velocities.append(v)
    i = 0
    while True:
        if check_grid_for_solution(robot_positions):
            display_robots_on_grid(robot_positions)
            return i
        i += 1
        new_robot_positions = []
        for j, pos in enumerate(robot_positions):
            velocity = robot_velocities[j]
            new_pos = (pos[0] + velocity[0]) % WIDTH, (pos[1] + velocity[1]) % HEIGHT
            new_robot_positions.append(new_pos)

        # display_robots_on_grid(new_robot_positions)
        robot_positions = new_robot_positions

def check_grid_for_solution(robot_positions):
    grid = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
    for p in robot_positions:
        grid[p[1]][p[0]] += 1
    for row in grid:
        for n in row:
            if n > 1:
                return False
    return True


def display_robots_on_grid(robot_positions):
    grid = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
    for p in robot_positions:
        grid[p[1]][p[0]] += 1
    for row in grid:
        print(''.join(str(x) for x in row))

print(main())