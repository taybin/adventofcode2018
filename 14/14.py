recipes = [3,7]

class Elf:
    def __init__(self, idx):
        self.idx = idx

    def recipe(self):
        return recipes[self.idx]

    def move(self):
        current = recipes[self.idx]
        self.idx = (self.idx + current + 1) % len(recipes)

elf1 = Elf(0)
elf2 = Elf(1)

i = 0
value = 147061
while len(recipes) < value + 10:
    i += 1
    print(i, len(recipes))
    total = elf1.recipe() + elf2.recipe()
    recipes += [int(i) for i in list(str(total))]
    elf1.move()
    elf2.move()
print(''.join([str(i) for i in recipes[value:value+10]]))
