import re

with open('input.txt') as f:
    pattern = f.readline()
    f.readline()
    lines = f.readlines()

print(pattern)

initial_reg = re.compile('initial state: ([#\.]+)')
rule_reg = re.compile('([\.#]+) => ([\.#])')

rules = {}
for line in lines:
    m = rule_reg.match(line)
    rules[m.group(1)] = m.group(2)
print(rules)

m = initial_reg.match(pattern)
states = []
state = ['.', '.', '.']
for c in m.group(1):
    state.append(c)
state += ['.', '.', '.']

states.append(state)

print(''.join(state))
prepend = 3
for i in range(1, 50000000000):
    current_state = states[-1]
    new_state = []
    for j in range(0, len(current_state)):
        rule = ''.join(current_state[j-2:j+3])
        if rule in rules:
            new_state.append(rules[rule])
        else:
            new_state.append('.')
    if new_state[1] == '#':
        new_state.insert(0, '.')
        prepend += 1
    if new_state[-3] == '#':
        new_state.append('.')
    states.append(new_state)

    if i % 1000 == 0:
        print(i)
        value = 0
        state = states[-2]
        for i in range(len(state)):
            if state[i] == '#':
                value += i - prepend
        print(value)
        value2 = 0
        state = states[-1]
        for i in range(len(state)):
            if state[i] == '#':
                value2 += i - prepend
        print(value2)
        print(value2 - value)
