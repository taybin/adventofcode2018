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

print(0, ''.join(state))
for i in range(1, 21):
    current_state = states[-1]
    new_state = []
    for j in range(0, len(current_state)):
        rule = ''.join(current_state[j-2:j+3])
        if rule in rules:
            new_state.append(rules[rule])
        else:
            new_state.append('.')
    new_state.append('.')
    new_state.insert(0, '.')
    states.append(new_state)
    print(i, ''.join(new_state))

value = 0
state = states[-1]
for i in range(len(state)):
    if state[i] == '#':
        value += i - 23
print(value)
