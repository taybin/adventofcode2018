import string

with open('input.txt') as f:
    lines = f.readlines()

size = 375
area = [['x' for i in range(size)] for j in range(size)]
points = []

def distance(p, q):
    return sum([abs(p[i]-q[i]) for i in range(2)])

for i in range(len(lines)):
    line = lines[i]
    coord = [int(n) for n in line.split(', ')]
    name = string.ascii_letters[i]
    points += [(coord[0], coord[1], name)]
    area[coord[1]][coord[0]] = name

print(points)
#for y in area:
#    print(''.join(y))

for y in range(len(area)):
    print('looking at row', y)
    for x in range(len(area[y])):
        distances = []
        min_value = 500
        min_point = None
        for p in points:
            d = distance(p, (x,y))
            if d < min_value:
                min_value = d
                min_point = p
            distances += [d]
        if distances.count(min_value) > 1:
            area[y][x] = '.'
        else:
            area[y][x] = min_point[2]

infinites = set()
infinites |= set([y[0] for y in area])
infinites |= set([y[-1] for y in area])
for x in range(size):
    infinites |= set(area[0][x]) 
    infinites |= set(area[-1][x]) 
print(infinites)

count = {}
for y in range(len(area)):
    for x in range(len(area[y])):
        point = area[y][x]
        if point not in infinites:
            if point in count:
                count[point] += 1
            else:
                count[point] = 1
print(count)
