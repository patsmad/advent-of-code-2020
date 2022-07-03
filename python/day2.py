from get_input import get_input

response = get_input(2)

data = response.text.split('\n')[:-1]
formatted_data = []
for d in data:
    pieces = d.split(' ')
    num_range = pieces[0].split('-')
    letter = pieces[1][0]
    pw = pieces[2]
    formatted_data.append({'min': int(num_range[0]), 'max': int(num_range[1]), 'letter': letter, 'pw': pw})

valid = 0
for d in formatted_data:
    n = len([a for a in d['pw'] if a == d['letter']])
    if n >= d['min'] and n <= d['max']:
        valid += 1

print(valid)

valid = 0
for d in formatted_data:
    value = (d['pw'][d['min']-1] == d['letter']) + (d['pw'][d['max']-1] == d['letter'])
    if value == 1:
        valid += 1

print(valid)
