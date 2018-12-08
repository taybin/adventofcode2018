with open('input.txt') as f:
    series = f.read().split(' ')

class Node:
    def __init__(self, series):
        self.nodes = []
        self.meta = []
        node_count = int(series.pop(0))
        metadata_count = int(series.pop(0))

        for i in range(node_count):
            self.nodes += [Node(series)]
        for i in range(metadata_count):
            self.meta += [int(series.pop(0))]

    def size(self):
        return 2 + len(self.meta) + sum(
            [n.size() for n in self.nodes])

    def metadata(self):
        return sum(self.meta) + sum(
            [n.metadata() for n in self.nodes])

n = Node(series)
print(n.metadata())
