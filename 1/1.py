value = 0
found = {}
found_it = False
with open('input1.txt') as f:
    lines = f.readlines()

    while not found_it:
        for line in lines:
            value = value + int(line)
            if str(value) in found:
                print(value)
                found_it = True
                break
            found[str(value)] = True
