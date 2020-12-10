from get_input import get_input

response = get_input(5)

def fromFB(input):
    return int(''.join(['0' if a == 'F' else '1' for a in input]), 2)

def fromRL(input):
    return int(''.join(['0' if a == 'L' else '1' for a in input]), 2)

def fromFBRL(input):
    return fromFB(input[:7]) * 8 + fromRL(input[7:])

data = response.text.strip().split('\n')

maxID = 0
for d in data:
    id = fromFBRL(d)
    if id > maxID:
        maxID = id

data_array = [0] * (maxID + 1)
for d in data:
    data_array[fromFBRL(d)] = 1

first_1 = data_array.index(1)
seat_id = data_array[first_1:].index(0) + first_1
print(seat_id)


