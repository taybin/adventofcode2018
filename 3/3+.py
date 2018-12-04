import re

with open('input.txt') as f:
    lines = f.readlines()

area = [[None for i in range(1000)] for j in range(1000)]
claims = {}

prog = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
for line in lines:
    m = prog.match(line)
    claim = m.group(1)
    start_x = int(m.group(2))
    start_y = int(m.group(3))
    claims[claim] = True
    for x in range(start_x, start_x + int(m.group(4))):
        for y in range(start_y, start_y + int(m.group(5))):
            if area[x][y] is not None:
                claims[claim] = False
                claims[area[x][y]] = False
            area[x][y] = claim

for key in claims:
    if claims[key] is True:
        print(key)
