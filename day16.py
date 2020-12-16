from get_input import get_input

response = get_input(16)
data = response.text.strip().split('\n\n')

def compare(field, rule):
    return (field >= rule[0][0] and field <= rule[0][1]) or (field >= rule[1][0] and field <= rule[1][1])

rules = {}
for d in data[0].split('\n'):
    key, ranges = d.split(': ')
    range_values = [(int(a.split('-')[0]), int(a.split('-')[1])) for a in ranges.split(' or ')]
    rules[key] = range_values

my_ticket = list(map(int, data[1].split('\n')[1].split(',')))
other_tickets = [list(map(int, a.split(','))) for a in  data[2].split('\n')[1:]]

invalid_fields = []
invalid_tickets = []
for i, ticket in enumerate(other_tickets):
    for field in ticket:
        if all([not compare(field, rule) for rule in rules.values()]):
            invalid_fields.append(field)
            invalid_tickets.append(i)
print(sum(invalid_fields))

other_tickets = [a for i, a in enumerate(other_tickets) if i not in invalid_tickets]

valid_keys = []
for i in range(len(my_ticket)):
    valid_keys.append([])
    for key, rule in rules.items():
        if all([compare(ticket[i], rule) for ticket in other_tickets]):
            valid_keys[i].append(key)

unique_keys = {}
while len(unique_keys) < len(rules):
    unique_keys.update({i: a[0] for i, a in enumerate(valid_keys) if len(a) == 1})
    valid_keys = [[b for b in a if b not in unique_keys.values()] for a in valid_keys]

output_keys = [i for i, a in unique_keys.items() if 'departure' in a]
m = 1
for key in output_keys:
    m *= my_ticket[key]
print(m)
