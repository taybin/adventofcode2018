with open('input.txt') as f:
    lines = f.readlines()

two_count = 0
three_count = 0
for line in lines:
    found_two = False
    found_three = False
    letters = {}
    for c in line:
        if c in letters:
            letters[c] = letters[c] + 1
        else:
            letters[c] = 1
    for x in letters:
        if letters[x] == 2 and not found_two:
            two_count = two_count + 1
            found_two = True
            print(line)
        if letters[x] == 3 and not found_three:
            three_count = three_count + 1
            found_three = True
            print(line)
print(two_count * three_count)
