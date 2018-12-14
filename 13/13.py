import copy
from operator import attrgetter

with open('input.txt') as f:
    lines = f.readlines()

area = []

for line in lines:
    area.append(list(line)[:-1])

class Cart:
    cart_id = 0

    def __init__(self, x, y, direction):
        print('new Cart', x, y, direction)
        self.id = cart_id
        cart_id += 1
        self.x = x
        self.y = y
        self.direction = direction
        self.choice = 'left'

    def __repr__(self):
        return repr((self.id, self.x, self.y, self.direction))

    def position(self):
        return (self.x, self.y)

    def step(self):
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
        print('rotate', self.choice, self.direction)
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
        print('new choice/direction', self.choice, self.direction)

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
    print(i)
    carts = sorted(carts, key=attrgetter('y', 'x'))
    for cart in carts:
        old_pos = cart.position()
        cart.step()
        new_pos = cart.position()
        if new_pos in positions:
            print('Found', new_pos)
            raise Exception('Found', new_pos)
        positions -= set((old_pos,))
        positions |= set((new_pos,))
