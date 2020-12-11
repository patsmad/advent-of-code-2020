from get_input import get_input

response = get_input(11)

data = response.text.strip().split('\n')

class Node:
    def __init__(self, s, occupancy_tolerance):
        self.state = s
        self.occupancy_tolerance = occupancy_tolerance
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def neighbor_num(self):
        return sum([neighbor.state == '#' for neighbor in self.neighbors])

    def set_next_state(self):
        if self.state == '#' and self.neighbor_num() >= self.occupancy_tolerance:
            self.next_state = 'L'
        elif self.state == 'L' and self.neighbor_num() == 0:
            self.next_state = '#'
        else:
            self.next_state = self.state

    def set_new_state(self):
        changed = 1 if self.state != self.next_state else 0
        self.state = self.next_state
        return changed

class NodeMap:
    def __init__(self, data, acceptable_neighbors = ['.', 'L', '#'], occupancy_tolerance = 4):
        self.acceptable_neighbors = acceptable_neighbors
        self.height = len(data)
        self.width = len(data[0])
        self.data_map = [[Node(a, occupancy_tolerance) for a in line] for line in data]
        for i, line in enumerate(self.data_map):
            for j, node in enumerate(line):
                for (di, dy) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    m = 1
                    while True:
                        new_i = i + di * m
                        new_j = j + dy * m
                        if new_i < 0 or new_i == self.height or new_j < 0 or new_j == self.width:
                            break
                        else:
                            if self.data_map[new_i][new_j].state in self.acceptable_neighbors:
                                node.add_neighbor(self.data_map[new_i][new_j])
                                break
                        m += 1

    def update_map(self):
        changed = 0
        for line in self.data_map:
            for node in line:
                node.set_next_state()
        for line in self.data_map:
            for node in line:
                changed += node.set_new_state()
        return changed

    def occupied(self):
        return sum([sum([node.state == '#' for node in line]) for line in self.data_map])

    def print_map(self):
        print('\n'.join([''.join([node.state for node in line]) for line in self.data_map]) + '\n')

node_map = NodeMap(data)
changed = node_map.update_map()
while changed != 0:
    changed = node_map.update_map()
print(node_map.occupied())

node_map = NodeMap(data, acceptable_neighbors=['L', '#'], occupancy_tolerance = 5)
changed = node_map.update_map()
while changed != 0:
    changed = node_map.update_map()
print(node_map.occupied())
