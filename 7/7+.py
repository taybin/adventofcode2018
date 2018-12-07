import re

with open('input.txt') as f:
    lines = f.readlines()

reg = re.compile("Step (\S) must be finished before step (\S) can begin.")
graph = {}

for line in lines:
    m = reg.match(line)
    dep = m.group(1)
    node = m.group(2)
    if node not in graph:
        graph[node] = set(dep)
    else:
        graph[node] |= set(dep)
    if dep not in graph:
        graph[dep] = set()

for k in graph:
    print(k, graph[k])

done = set()
order = []
timer = 0
elves = {0:None,1:None,2:None,3:None,4:None}
working = set()

def lazy_elves():
    return len([key for (key, value) in elves.items() if value is None])

def assign_elf(node, current_time):
    time = ord(node) - 64 + 60 + current_time
    if elves[0] is None:
        elves[0] = (node, time)
    elif elves[1] is None:
        elves[1] = (node, time)
    elif elves[2] is None:
        elves[2] = (node, time)
    elif elves[3] is None:
        elves[3] = (node, time)
    elif elves[4] is None:
        elves[4] = (node, time)
    else:
        raise Exception('')

print('Second   Worker 1   Worker 2   Worker 3   Worker 4   Worker 5   Done')
timer = -1
while(len(done) < len(graph)):
    timer += 1
    for elf in elves:
        if elves[elf] is None:
            continue
        elif elves[elf][1] == timer:
            done |= set(elves[elf][0])
            working -= set(elves[elf][0])
            elves[elf] = None
    next_nodes = [key for (key, value) in graph.items() if value.issubset(done) and key not in done and key not in working]
    next_nodes.sort()
    while lazy_elves() > 0 and len(next_nodes):
        node = next_nodes.pop()
        working |= set(node)
        assign_elf(node, timer)
    print('  {timer}    {elf1}    {elf2}    {elf3}   {elf4}   {elf5}   {done}'.format(timer=timer, elf1=elves[0], elf2=elves[1], elf3=elves[2], elf4=elves[3], elf5=elves[4], done=''.join(done)))

print(timer)
