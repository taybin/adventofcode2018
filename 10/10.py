import re

with open('input.txt') as f:
    lines = f.readlines()

class Point:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
    def step(self):
        self.x += self.xv
        self.y += self.yv

points = []

reg = re.compile('position=<([- ]?\d+), ([- ]?\d+)> velocity=<([- ]?\d+), ([- ]?\d+)>')
for line in lines:
    m = reg.match(line)
    points += [Point(
        x = int(m.group(1)),
        y = int(m.group(2)),
        xv = int(m.group(3)),
        yv = int(m.group(4)),
    )]


i = 0
x_range = [p.x for p in points]
old_max_x = max(x_range)
old_min_x = min(x_range)
max_x = old_max_x
min_x = old_min_x
while(i < 10405):
    i += 1
    for p in points:
        p.step()
    print(i)
    x_range = [p.x for p in points]
    old_max_x = max_x
    old_min_x = min_x
    max_x = max(x_range)
    min_x = min(x_range)
    if old_max_x <= max_x:
        break
    if old_min_x >= min_x:
        break

while True:
    i += 1
    print(i)
    input()
    for p in points:
        p.step()

    area = [[' ' for i in range(300)] for j in range(300)]
    print(len(points))
    for p in points:
        print(p.x, p.y)
        area[p.y][p.x] = '*'
    for a in area:
        print(''.join(a))
