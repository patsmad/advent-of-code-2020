from get_input import get_input

response = get_input(3)

data_map = response.text.split('\n')[:-1]
total_trees = 1
for sx, sy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    x = 0
    y = 0
    trees = 0
    while y < len(data_map) - 1:
        y += sy
        x = (x + sx) % len(data_map[0])
        if data_map[y][x] == '#':
            trees += 1
    total_trees *= trees
print(total_trees)