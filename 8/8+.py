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
        if not self.nodes:
            return sum(self.meta)
        else:
            total = 0
            for i in self.meta:
                if i > len(self.nodes):
                    continue
                else:
                    meta_value = self.nodes[i-1].metadata()
                    total += meta_value
            return total

n = Node(series)
print(n.metadata())
