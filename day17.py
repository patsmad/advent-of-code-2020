from get_input import get_input

response = get_input(17)
data = response.text.strip().split('\n')

class Node:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.state = '.'
        self.neighbors = []

    def set_state(self, s):
        self.state = s

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def neighbor_num(self):
        return sum([neighbor.state == '#' for neighbor in self.neighbors])

    def set_next_state(self):
        if self.state == '#' and self.neighbor_num() not in [2, 3]:
            self.next_state = '.'
        elif self.state == '.' and self.neighbor_num() == 3:
            self.next_state = '#'
        else:
            self.next_state = self.state

    def set_new_state(self):
        changed = 1 if self.state != self.next_state else 0
        self.state = self.next_state
        return changed

class NodeMap:
    def __init__(self, data, dimensions = 3):
        self.nodes = {}
        for x in range(-6, len(data[0]) + 6):
            for y in range(-6, len(data) + 6):
                for z in range(-6, 7):
                    for w in range(-6, 7) if dimensions == 4 else [0]:
                        self.nodes[(x, y, z, w)] = Node(x, y, z, w)
        self.neighbor_indices = [
            (x, y, z, w) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) for w in (range(-1, 2) if dimensions == 4 else [0]) if (x, y, z, w) != (0, 0, 0, 0)
            ]

        for y, line in enumerate(data):
            for x, a in enumerate(line):
                self.nodes[(x, y, 0, 0)].set_state(a)

        self.add_all_neighbors()

    def add_all_neighbors(self):
        for (x, y, z, w) in list(self.nodes.keys()):
            self.add_neighbors(x, y, z, w)

    def add_neighbors(self, x, y, z, w):
        this_node = self.nodes[(x, y, z, w)]
        this_node.neighbors = []
        for dx, dy, dz, dw in self.neighbor_indices:
            if (x + dx, y + dy, z + dz, w + dw) in self.nodes:
                this_node.add_neighbor(self.nodes[(x + dx, y + dy, z + dz, w + dw)])

    def update_map(self):
        for n in self.nodes.values():
            n.set_next_state()
        for n in self.nodes.values():
            n.set_new_state()

    def count(self):
       return sum([1 if node.state == '#' else 0 for node in self.nodes.values()])

    def print_map(self):
        xs = [x for (x, _, _, _) in self.nodes]
        ys = [y for (_, y, _, _) in self.nodes]
        zs = [z for (_, _, z, _) in self.nodes]
        ws = [w for (_, _, _, w) in self.nodes]
        for z in (min(zs), max(zs) + 1):
            for w in range(min(ws), max(ws) + 1):
                print('z: {}; w: {}'.format(z, w))
                print('\n'.join([''.join([self.nodes[(x, y, z, w)].state for x in range(min(xs), max(xs) + 1)]) for y in range(min(ys), max(ys) + 1)]) + '\n')

node_map = NodeMap(data)
for _ in range(6):
    node_map.update_map()
print(node_map.count())

node_map = NodeMap(data, dimensions=4)
for _ in range(6):
    node_map.update_map()
print(node_map.count())