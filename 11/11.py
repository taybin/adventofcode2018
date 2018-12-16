area = []

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

for y in range(0, 300):
    row = []
    for x in range(0, 300):
        row.append(power_level(x+1, y+1, 1718))
    area.append(row)

biggest = 0
biggest_point = None
for y in range(0, 297):
    for x in range(0, 297):
        total = area[y][x]
        total += area[y][x+1]
        total += area[y][x+2]
        total += area[y+1][x]
        total += area[y+1][x+1]
        total += area[y+1][x+2]
        total += area[y+2][x]
        total += area[y+2][x+1]
        total += area[y+2][x+2]
        if total > biggest:
            biggest = total
            biggest_point = (x+1,y+1)
print(biggest_point)
