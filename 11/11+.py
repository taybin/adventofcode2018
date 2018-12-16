area = [[0]*300 for i in range(300)]

def power_level(x, y, input_value):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += input_value
    power_level *= rack_id
    hundredth = int(list(str(power_level))[-3])
    output = hundredth - 5
    return output

print(power_level(3,5,8), 4)
print(power_level(122,79,57), -5)
print(power_level(217,196,39), 0)
print(power_level(101,153,71), 4)

for x in range(300):
    for y in range(300):
        area[x][y] = power_level(x+1, y+1, 1718)

def fast_largest_square(size):
    Np = 300 - size + 1
    subcols = [[0]*(Np) for i in range(300)]
    for j in range(Np):
        for i in range(300):
            if j == 0:
                subcols[i][j] = sum(area[i][j:j+size])
            else:
                subcols[i][j] = subcols[i][j-1] + area[i][j+size-1] - area[i][j-1]

    b = 0
    bp = None
    for x in range(300-(size-1)):
        for y in range(300-(size-1)):
            total = 0
            for k in range(size):
                total += subcols[x+k][y]
            if bp is None or total > b:
                b = total
                bp = (x+1,y+1)
    return bp, b

def largest_square(size):
    b = 0
    bp = None
    for x in range(300-(size-1)):
        for y in range(300-(size-1)):
            total = 0
            for x1 in range(x, x+size):
                for y1 in range(y, y+size):
                    total += area[x1][y1]
            if bp is None or total > b:
                b = total
                bp = (x+1,y+1)
    return bp, b

#print(largest_square(3))
biggest = 0
biggest_point = None
biggest_size = 1
for i in range(1, 300):
    point, total = fast_largest_square(i)
    if biggest_point is None or total > biggest:
        biggest = total
        biggest_point = point
        biggest_size = i
    print(i, point, total)
print(biggest_point, biggest_size)
