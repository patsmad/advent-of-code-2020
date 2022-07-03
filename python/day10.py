from get_input import get_input

response = get_input(10)

all_data = list(map(int, response.text.strip().split('\n')))
all_data.sort()
all_data = [0] + all_data + [all_data[-1] + 3]
out = {1: 0, 2: 0, 3: 0}
for i in range(1, len(all_data)):
    diff = all_data[i] - all_data[i-1]
    out[diff] += 1
print(out[1] * out[3])

connections = {}
for d in all_data:
    connections[d] = [a for a in all_data if (a - d) > 0 and (a - d) <= 3]

count = {}
for d in all_data[::-1]:
    count[d] = sum([count[a] for a in connections[d]]) if len(connections[d]) > 0 else 1
print(count[0])