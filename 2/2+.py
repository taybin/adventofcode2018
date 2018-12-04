with open('input.txt') as f:
    lines = f.readlines()

def cmp(str1, str2):
    differences = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            differences += 1
            if differences > 1:
                return False
    if differences == 0:
        return False
    return True

for line in lines:
    set1 = set(line)
    for line2 in lines:
        if line == line2:
            continue
        if cmp(line, line2):
            print('found difference')
            print(set(line) - set(line2))
            print(set(line).intersection(set(line2)))
            print(line)
            print(line2)
