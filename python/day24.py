from get_input import get_input

response = get_input(24)
data = response.text.strip().split('\n')

black = []
for d in data:
    position = (0, 0)
    while len(d) > 0:
        if d[0] in ['e', 'w']:
            position = (position[0] + (1 if d[0] == 'e' else -1), position[1])
            d = d[1:]
        else:
            position = (position[0] + (0.5 if d[1] == 'e' else -0.5), position[1] + (1 if d[0] == 'n' else -1))
            d = d[2:]
    if position in black:
        black.pop(black.index(position))
    else:
        black.append(position)

class Tile:
    def __init__(self, position, state):
        self.x = position[0]
        self.y = position[1]
        self.neighbors = []
        self.new_state = None
        self.state = state

    def add_neighbors(self, neighbors):
        self.neighbors = neighbors

    def set_new_state(self):
        self.state = self.new_state

    def get_new_state(self):
        black_neighbors = len([tile for tile in self.neighbors if tile.state == 'black'])
        if self.state == 'black' and (black_neighbors == 0 or black_neighbors > 2):
            self.new_state = 'white'
        elif self.state == 'white' and black_neighbors == 2:
            self.new_state = 'black'
        else:
            self.new_state = self.state

x_range = (min([a[0] for a in black]), max([a[0] for a in black]))
y_range = (min([a[1] for a in black]), max([a[1] for a in black]))

# Since we know the black tiles can only advance one space per move I just make the grid big enough to allow for all potential black tiles
all_tiles = {}
for x in range(int(x_range[0] - 100), int(x_range[0] + 100)):
    for y in range(y_range[0] - 100, y_range[0] + 100):
        position = (x + (0.5 * (y % 2)), y)
        all_tiles[position] = Tile(position, 'black' if position in black else 'white')

def neighboring_positions(p):
    return [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0] - 0.5, p[1] - 1), (p[0] - 0.5, p[1] + 1), (p[0] + 0.5, p[1] - 1), (p[0] + 0.5, p[1] + 1)]

for position, tile in all_tiles.items():
    neighbors = [all_tiles[n_position] for n_position in neighboring_positions(position) if n_position in all_tiles]
    tile.add_neighbors(neighbors)

print(len([tile for tile in all_tiles.values() if tile.state == 'black']))
for i in range(1, 101):
    for tile in all_tiles.values():
        tile.get_new_state()
    for tile in all_tiles.values():
        tile.set_new_state()
    print(i, len([tile for tile in all_tiles.values() if tile.state == 'black']))