import copy
import curses
from curses import wrapper

def valid_node(point):
    x, y = point
    if x < 0 or y < 0:
        return False
    if x > len(area[0]) - 1:
        return False
    if y > len(area) - 1:
        return False
    return True

def get_neighbors(x, y):
    neighbors = [
        (x-1,y-1),
        (x,y-1),
        (x+1,y-1),
        (x-1,y),
        (x+1,y),
        (x-1,y+1),
        (x,y+1),
        (x+1,y+1)
    ]
    valid_neighbors = [n for n in neighbors if valid_node(n)]
    lands = []
    for v in valid_neighbors:
        lands.append(area[v[1]][v[0]])
    return lands

def step_node(x, y):
    node = area[y][x]
    neighbors = get_neighbors(x, y)
    if node == '.':
        if neighbors.count('|') >= 3:
            return '|'
        else:
            return '.'
    elif node == '|':
        if neighbors.count('#') >= 3:
            return '#'
        else:
            return '|'
    elif node == '#':
        if neighbors.count('|') > 0 and neighbors.count('#') > 0:
            return '#'
        else:
            return '.'

area = []
win = None

def initialize():
    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        new_line = list(line)[:-1]
        if new_line:
            area.append(new_line)

def display(stdscr):
    for y in range(len(area)):
        for x in range(len(area[y])):
            stdscr.addstr(y, x, area[y][x])
    stdscr.refresh()

def run(stdscr):
    global area
    i = 0
    display(stdscr)
    while i < 497:
        new_area = copy.deepcopy(area)
        for y in range(len(area)):
            for x in range(len(area[y])):
                new_area[y][x] = step_node(x,y)
        area = new_area
        i += 1
        display(stdscr)

    i += (28 *35714000)

    while i < 1000000000:
        new_area = copy.deepcopy(area)
        for y in range(len(area)):
            for x in range(len(area[y])):
                new_area[y][x] = step_node(x,y)
        area = new_area
        i += 1
        display(stdscr)

def calculate():
    trees = 0
    lumber = 0
    for y in range(len(area)):
        for x in range(len(area[y])):
            if area[y][x] == '|':
                trees += 1
            elif area[y][x] == '#':
                lumber += 1
    print(trees * lumber)

def main(stdscr):
    stdscr.clear()
    initialize()
    run(stdscr)
    calculate()

wrapper(main)
