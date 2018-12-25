with open('input.txt') as f:
    lines = f.readlines()

def distance(p, q):
    return sum([abs(p[i]-q[i]) for i in range(4)])

consts = []

def search_const(const, p1):
    for p2 in const:
        if distance(p1, p2) <= 3:
            return True
    return False

for line in lines:
    point = tuple(int(n) for n in line.split(','))
    for const in consts:
        matched = search_const(const, point)
        if matched:
            const.append(point)
            break
    else:
        consts.append([point])

print(len(consts))

def shrink():
    for const1 in consts:
        for const2 in consts:
            if id(const1) == id(const2):
                continue
            for p1 in const1:
                matched = search_const(const2, p1)
                if matched:
                    const1 += const2
                    consts.remove(const2)
                    break

size1 = len(consts)
shrink()
size2 = len(consts)
print('shrunk', size1, size2)
while size1 != size2:
    size1 = size2
    shrink()
    size2 = len(consts)
    print('shrunk', size1, size2)

print(len(consts))
