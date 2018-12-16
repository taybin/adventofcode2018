recipes = '37'

class Elf:
    def __init__(self, idx):
        self.idx = idx

    def recipe(self):
        return int(recipes[self.idx])

    def move(self):
        current = self.recipe()
        self.idx = (self.idx + current + 1) % len(recipes)

elf1 = Elf(0)
elf2 = Elf(1)

i = 0
value = 147061

def find_value(recipes, value):
    search = recipes[-8:]
    return str(value) in search

while find_value(recipes, value) is False:
    i += 1
    print(i, len(recipes))
    total = elf1.recipe() + elf2.recipe()
    recipes += str(total)
    elf1.move()
    elf2.move()
print(recipes[-10:])
print(len(recipes))
