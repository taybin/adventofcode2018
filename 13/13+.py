import copy
from operator import attrgetter

with open('input.txt') as f:
    lines = f.readlines()

area = []

for line in lines:
    area.append(list(line)[:-1])

class Cart:
    def __init__(self, x, y, direction):
        print('new Cart', x, y, direction)
        self.x = x
        self.y = y
        self.direction = direction
        self.choice = 'left'
        self.crashed = False

    def __repr__(self):
        return repr((self.x, self.y, self.direction))

    def position(self):
        return (self.x, self.y)

    def step(self):
        if self.crashed:
            return
        self.move()
        current = area[self.y][self.x]
        if current == '+':
            self.rotate()
        elif current == '/':
            self.corner1()
        elif current == '\\':
            self.corner2()


    def move(self):
        if self.direction == 'v':
            self.y += 1
        elif self.direction == '^':
            self.y -= 1
        elif self.direction == '>':
            self.x += 1
        elif self.direction == '<':
            self.x -= 1
        else:
            raise Exception('Unexpected direction')

    # /
    def corner1(self):
        if self.direction == '^':
            self.direction = '>'
        elif self.direction == '<':
            self.direction = 'v'
        elif self.direction == 'v':
            self.direction = '<'
        elif self.direction == '>':
            self.direction = '^'
        else:
            raise Exception('Unexpected direction')

    # \
    def corner2(self):
        if self.direction == '^':
            self.direction = '<'
        elif self.direction == '<':
            self.direction = '^'
        elif self.direction == '>':
            self.direction = 'v'
        elif self.direction == 'v':
            self.direction = '>'
        else:
            raise Exception('Unexpected direction')

    def rotate(self):
        cycle = ['^', '>', 'v', '<']
        if self.choice == 'left':
            self.direction = cycle[cycle.index(self.direction) - 1]
            self.choice = 'straight'
        elif self.choice == 'straight':
            self.choice = 'right'
        elif self.choice == 'right':
            if self.direction == '<':
                self.direction = '^'
            else:
                self.direction = cycle[cycle.index(self.direction) + 1]
            self.choice = 'left'

carts = []

for y in range(len(area)):
    for x in range(len(area[y])):
        c = area[y][x]
        if c == '<' or c == '>' or c == '^' or c == 'v':
            carts.append(Cart(x, y, c))
            if c == '<' or c == '>':
                area[y][x] = '-'
            elif c == '^' or c == 'v':
                area[y][x] = '|'

def display():
    new_area = copy.deepcopy(area)
    for c in carts:
        new_area[c.y][c.x] = c.direction
    for y in new_area:
        print(''.join(y))
    print('')

#display()
positions = set()
i = 0
while True:
    i += 1
    carts = sorted(carts, key=attrgetter('y', 'x'))
    for cart in carts:
        if cart.crashed:
            continue
        old_pos = cart.position()
        print(positions)
        positions -= set((old_pos,))
        cart.step()
        new_pos = cart.position()
        if new_pos in positions:
            print(i, 'Crash', new_pos)
            positions -= set((new_pos,))
            for c in carts:
                if c.position() == new_pos:
                    c.crashed = True
        else:
            positions |= set((new_pos,))
    non_crashed = [c for c in carts if c.crashed == False]
    print(non_crashed)
    if len(non_crashed) == 1:
        print('Last cart', non_crashed[0].position())
        break
