from collections import Counter, defaultdict
import pprint
import time

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

    for _ in range(501):
        new_robot_positions = []
        for i, pos in enumerate(robot_positions):
            velocity = robot_velocities[i]
            new_pos = (pos[0] + velocity[0]) % WIDTH, (pos[1] + velocity[1]) % HEIGHT
            new_robot_positions.append(new_pos)

        # display_robots_on_grid(new_robot_positions)
        # print(_, '\n\n\n')
        robot_positions = new_robot_positions
    
    mid_x, mid_y = WIDTH // 2, HEIGHT // 2
    # print(robot_positions)
    upper_left_quad = [p for p in robot_positions if p[0] < mid_x and p[1] < mid_y]
    upper_right_quad = [p for p in robot_positions if p[0] > mid_x and p[1] < mid_y]
    lower_left_quad = [p for p in robot_positions if p[0] < mid_x and p[1] > mid_y]
    lower_right_quad = [p for p in robot_positions if p[0] > mid_x and p[1] > mid_y]
    total = len(upper_left_quad) * len(upper_right_quad) * len(lower_left_quad) * len(lower_right_quad)
    return total

def display_robots_on_grid(robot_positions):
    grid = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
    for p in robot_positions:
        grid[p[1]][p[0]] += 1
    for row in grid:
        print(''.join(str(x) for x in row))

print(main())