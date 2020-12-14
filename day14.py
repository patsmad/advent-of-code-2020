from get_input import get_input

response = get_input(14)
data = response.text.strip().split('\n')

instructions = []
for d in data:
    if 'mask = ' in d:
        instructions.append(('mask', d.split(' = ')[1]))
    else:
        index = int(d.split('[')[1].split(']')[0])
        num = int(d.split(' = ')[1])
        instructions.append(('mem', index, num))

mask = None
memory = {}
for instruction in instructions:
    if instruction[0] == 'mask':
        mask = instruction[1]
    else:
        binary_number = bin(instruction[2])
        padded_number = '0' * (len(mask) - len(binary_number) + 2) + binary_number[2:]
        masked_number = ''.join([mask[i] if mask[i] != 'X' else padded_number[i] for i in range(len(mask))])
        memory[instruction[1]] = int(masked_number, 2)
print(sum(memory.values()))

floating_map = {'1': ['1'], '0': ['0'], 'X': ['1', '0']}

mask = None
memory = {}
for instruction in instructions:
    if instruction[0] == 'mask':
        mask = instruction[1]
    else:
        binary_address = bin(instruction[1])
        padded_address = '0' * (len(mask) - len(binary_address) + 2) + binary_address[2:]
        masked_address = ''.join([mask[i] if mask[i] != '0' else padded_address[i] for i in range(len(mask))])
        masked_addresses = [masked_address]
        for i in range(len(masked_address)):
            if masked_address[i] == 'X':
                masked_addresses = [a[:i] + '0' + a[i+1:] for a in masked_addresses] + [a[:i] + '1' + a[i+1:] for a in masked_addresses]
        for address in masked_addresses:
            memory[int(address, 2)] = instruction[2]
print(sum(memory.values()))