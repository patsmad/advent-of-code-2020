from get_input import get_input

response = get_input(13)
data = response.text.strip().split('\n')

timestamp = int(data[0])
buses_raw = data[1].split(',')
number_of_x = len([a for a in buses_raw if a == 'x'])
buses = [int(a) for a in buses_raw if a != 'x']

wait_times = [a - timestamp % a for a in buses]
min_wait = min(wait_times)
wait_for_bus = buses[wait_times.index(min_wait)]
print(min_wait * wait_for_bus)

buses_with_min = [(i, int(a)) for i, a in enumerate(buses_raw) if a != 'x']

def get_new_mb(m, b, bus, target):
    while b % bus != (bus - target) % bus:
        b += m
    t = 1
    while (b + t * m) % bus != (bus - target) % bus:
        t += 1
    m *= t
    return m, b

m = buses_with_min[0][1]
b = 0
for target, bus in buses_with_min:
    m, b = get_new_mb(m, b, bus, target)

print(b)

