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

while(len(done) < len(graph)):
    next_nodes = [key for (key, value) in graph.items() if value.issubset(done) and key not in done]
    next_nodes.sort()
    done |= set(next_nodes[0])
    order += [next_nodes[0]]
print(''.join(order))
