import string

with open('input.txt') as f:
    lines = f.readlines()

size = 375
points = []

def distance(p, q):
    return sum([abs(p[i]-q[i]) for i in range(2)])

for i in range(len(lines)):
    line = lines[i]
    coord = [int(n) for n in line.split(', ')]
    points += [(coord[0], coord[1])]

print(points)

within = 0
for y in range(size):
    for x in range(size):
        total_distance = 0
        for p in points:
            total_distance += distance(p, (x,y))
        if total_distance < 10000:
            within += 1
print(within)
