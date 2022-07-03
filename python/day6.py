from get_input import get_input

response = get_input(6)

data_map = [a.strip().split('\n') for a in response.text.split('\n\n')]

s = 0
for group in data_map:
    s += len(list(set(''.join(group))))
print(s)

s2 = 0
for group in data_map:
    i = set(''.join(group))
    for person in group:
        i = i.intersection(person)
    s2 += len(i)
print(s2)