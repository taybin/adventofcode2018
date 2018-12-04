import re

with open('input.txt') as f:
    lines = f.readlines()

area = [[0 for i in range(1000)] for j in range(1000)]

prog = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
for line in lines:
    m = prog.match(line)
    start_x = int(m.group(2))
    start_y = int(m.group(3))
    for x in range(start_x, start_x + int(m.group(4))):
        for y in range(start_y, start_y + int(m.group(5))):
            area[x][y] += 1

count = 0
for x in range(0, 999):
    for y in range(0, 999):
        if area[x][y] >= 2:
            count += 1

print(count)
