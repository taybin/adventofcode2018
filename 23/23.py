import re

with open('input.txt') as f:
    lines = f.readlines()

p_reg = re.compile('pos=<(-*\d+),(-*\d+),(-*\d+)>, r=(\d+)')

def distance(p, q):
    return sum([abs(p[i]-q[i]) for i in range(3)])

points = []
for line in lines:
    m = p_reg.match(line)
    points.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))))

point_largest = sorted(points, key=lambda p: p[3], reverse=True)[0]
print(point_largest)
in_range = [p for p in points if distance(p, point_largest) <= point_largest[3]]
print(len(in_range))
