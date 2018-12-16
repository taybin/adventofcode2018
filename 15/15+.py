from collections import namedtuple
import copy
from operator import attrgetter

from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

finder = DijkstraFinder()

area = []
mobs = []

Point = namedtuple('Point', ['x', 'y'])
Path = namedtuple('Path', ['length', 'step_x', 'step_y', 'dest_x', 'dest_y'])


class Finished(Exception):
    pass

class ElfDied(Exception):
    pass


class MyGrid(Grid):
    def neighbors(self, node, diagonal_movement):
        """
        get all neighbors of one node
        :param node: node
        """
        x = node.x
        y = node.y
        neighbors = []

        # ↑
        if self.walkable(x, y - 1):
            neighbors.append(self.nodes[y - 1][x])
        # ←
        if self.walkable(x - 1, y):
            neighbors.append(self.nodes[y][x - 1])
        # →
        if self.walkable(x + 1, y):
            neighbors.append(self.nodes[y][x + 1])
        # ↓
        if self.walkable(x, y + 1):
            neighbors.append(self.nodes[y + 1][x])

        return neighbors


class Mob:
    mob_positions = {}

    def __init__(self, x, y):
        self.pos = Point(x, y)
        self.hp = 200
        Mob.mob_positions[self.pos] = self


    def neighbors(self, point):
        return [
            Point(point.x+1, point.y),
            Point(point.x-1, point.y),
            Point(point.x, point.y+1),
            Point(point.x, point.y-1)
        ]

    def get_open_squares(self, target):
        x, y = target.pos
        points = self.neighbors(target.pos)
        points = [p for p in points if area[p.y][p.x] == 1]
        points = [p for p in points if p not in Mob.mob_positions]
        return points

    def turn(self, grid):
        self_range = self.neighbors(self.pos)
        targets = self.get_targets()
        move_options = {}
        attack_options = []
        for targ in targets:
            if targ.pos in self_range:
                attack_options.append(targ)
                continue
            squares = self.get_open_squares(targ)
            for square in squares:
                grid.cleanup()
                start = grid.node(self.pos.x, self.pos.y)
                end = grid.node(square.x, square.y)
                path, runs = finder.find_path(start, end, grid)
                if path:
                    move_options[square] = Path(
                        length=len(path),
                        step_x=path[1][0],
                        step_y=path[1][1],
                        dest_x=path[-1][0],
                        dest_y=path[-1][1]
                    )
        if not attack_options and move_options:
            self.move(move_options.values())
            self_range = self.neighbors(self.pos)
            targets = self.get_targets()
            for targ in targets:
                if targ.pos in self_range:
                    attack_options.append(targ)
        if attack_options:
            self.attack(attack_options)
        return targets

    def move(self, move_options):
        nearest = sorted(move_options, key=attrgetter('length', 'dest_y', 'dest_x'))[0]
        del Mob.mob_positions[self.pos]
        self.pos = Point(nearest.step_x, nearest.step_y)
        Mob.mob_positions[self.pos] = self

    def attack(self, attack_options):
        nearest = sorted(attack_options, key=attrgetter('hp', 'pos.y', 'pos.x'))[0]
        nearest.hp -= self.get_ap()
        if nearest.hp <= 0:
            del Mob.mob_positions[nearest.pos]
            print(nearest, 'died')
            if isinstance(nearest, Elf):
                raise ElfDied()



# 3,10,15,17,18  ---  19:52972, 20,30,50
class Elf(Mob):
    def __init__(self, x, y):
        self.attack_power = 18
        super().__init__(x, y)

    def get_ap(self):
        return self.attack_power

    def __repr__(self):
        return 'E('+str(self.hp)+')'

    def get_targets(self):
        return [m for m in mobs if m.hp > 0 and isinstance(m, Goblin)]


class Goblin(Mob):
    def __init__(self, x, y):
        self.attack_power = 3
        super().__init__(x, y)

    def get_ap(self):
        return self.attack_power

    def __repr__(self):
        return 'G('+str(self.hp)+')'

    def get_targets(self):
        return [m for m in mobs if m.hp > 0 and isinstance(m, Elf)]


with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    new_line = list(line.replace('.', '1').replace('#', '0'))[:-1]
    if new_line:
        area.append(new_line)


for y in range(len(area)):
    for x in range(len(area[y])):
        c = area[y][x]
        if c == 'E':
            mobs.append(Elf(x, y))
            area[y][x] = 1
        elif c == 'G':
            mobs.append(Goblin(x, y))
            area[y][x] = 1

area = [[int(x) for x in y] for y in area]


def display():
    new_area = [['#' if x == 0 else '.' for x in y] for y in area]
    for m in mobs:
        if m.hp > 0:
            new_area[m.pos.y][m.pos.x] = 'E' if isinstance(m, Elf) else 'G'
    for y in range(len(new_area)):
        print(''.join(new_area[y]), ', '.join([str(m) for m in mobs if m.pos.y == y]))
    print('')


def make_matrix():
    matrix = copy.deepcopy(area)
    for m in mobs:
        if m.hp > 0:
            matrix[m.pos.y][m.pos.x] = 0
    return matrix


i = 0
print(i)
display()
try:
    while True:
        print(i+1)
        mobs = sorted(mobs, key=attrgetter('pos.y', 'pos.x'))
        for mob in mobs:
            if mob.hp > 0:
                grid = MyGrid(matrix=make_matrix())
                found_targets = mob.turn(grid)
                if not found_targets:
                    raise Finished()
        i += 1
        display()
except Finished as e:
    print(e)
    print('Finished on round', i)

display()
hp = 0
for mob in mobs:
    if mob.hp > 0:
        hp += mob.hp
print(hp)
print(i * hp)
