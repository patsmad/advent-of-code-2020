from get_input import get_input

response = get_input(20)
tiles = response.text.strip().split('\n\n')

data = {int(a.split('\n')[0].split('Tile ')[1][:-1]): a.split('\n')[1:] for a in tiles}

def get_all_borders(tile):
    return {tile[0], tile[-1], ''.join([a[0] for a in tile]), ''.join([a[-1] for a in tile]),
            tile[0][::-1], tile[-1][::-1], ''.join([a[0] for a in tile[::-1]]), ''.join([a[-1] for a in tile[::-1]])}

borders = {}
for id, d in data.items():
    borders[id] = get_all_borders(d)

connections = {id: [other_id for other_id, other_borders in borders.items() if len(other_borders - id_borders) != len(other_borders) and other_id != id] for id, id_borders in borders.items()}
corners = [id for id, connection in connections.items() if len(connection) == 2]

corner_multiply = 1
for id in corners:
    corner_multiply *= id
print(corner_multiply)

# first fill edge
tile_map = {(0, 0): corners[0]}
for i in range(1, 12):
    tile_map[(0, i)] = [id for id in connections[tile_map[(0, i-1)]] if len(connections[id]) < 4 and id not in tile_map.values()][0]
for i in range(1, 12):
    tile_map[(i, 11)] = [id for id in connections[tile_map[(i-1, 11)]] if len(connections[id]) < 4 and id not in tile_map.values()][0]
for i in range(1, 12):
    tile_map[(11, 11-i)] = [id for id in connections[tile_map[(11, 12-i)]] if len(connections[id]) < 4 and id not in tile_map.values()][0]
for i in range(1, 11):
    tile_map[(11-i, 0)] = [id for id in connections[tile_map[(12-i, 0)]] if len(connections[id]) < 4 and id not in tile_map.values()][0]

# fill in center
for i in range(1, 11):
    for j in range(1, 11):
        tile_map[(i, j)] = [id for id in connections[tile_map[(i, j-1)]] if id in connections[tile_map[(i-1, j)]] and id not in tile_map.values()][0]

def rotate(tile):
    new_tile = [''] * len(tile)
    for i in range(len(tile)):
        new_tile[i] = ''.join([tile[j][(len(tile) - 1)-i] for j in range(len(tile[i]))])
    return new_tile

# rotate
for i in range(0, 12):
    for _ in range(4):
        if ''.join([a[-1] for a in data[tile_map[(i, 0)]]]) in borders[tile_map[(i, 1)]] or ''.join([a[-1] for a in data[tile_map[(i, 0)]][::-1]]) in borders[tile_map[(i, 1)]]:
            break
        data[tile_map[(i, 0)]] = rotate(data[tile_map[(i, 0)]])
    for j in range(1, 12):
        for _ in range(4):
            if ''.join([a[0] for a in data[tile_map[(i, j)]]]) in borders[tile_map[(i, j-1)]] or ''.join([a[0] for a in data[tile_map[(i, j)]][::-1]]) in borders[tile_map[(i, j-1)]]:
                break
            data[tile_map[(i, j)]] = rotate(data[tile_map[(i, j)]])

#flip
for i in range(0, 12):
    for j in range(0, 11):
        if ''.join([a[-1] for a in data[tile_map[(i, j)]]]) != ''.join([a[0] for a in data[tile_map[(i, j+1)]]]):
            data[tile_map[(i, j+1)]] = data[tile_map[(i, j+1)]][::-1]

# flip rows
for i in range(0, 11):
    if data[tile_map[(i, 0)]][-1] not in borders[tile_map[(i+1, 0)]]:
        for j in range(0, 12):
            data[tile_map[(i, j)]] = data[tile_map[(i, j)]][::-1]

actual_map = []
for i in range(0, 12):
    for j in range(1, 9):
        actual_map.append(''.join([data[tile_map[(i, k)]][j][1:9] for k in range(0, 12)]))

sea_monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
    ]
inds = [(i, j) for i in range(3) for j in range(len(sea_monster[i])) if sea_monster[i][j] == '#']
s_inds = []
for r in range(4):
    for i in range(len(actual_map[0]) - len(sea_monster[0])):
        for j in range(len(actual_map) - len(sea_monster)):
            if all([actual_map[j+ind[0]][i+ind[1]] == '#' for ind in inds]):
                s_inds += [(j+ind[0], i+ind[1]) for ind in inds]
    actual_map = rotate(actual_map)
print(sum([sum([1 for b in line if b == '#']) for line in actual_map]) - len(s_inds))