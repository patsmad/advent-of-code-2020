data = list(map(int, """9,19,1,6,0,5,4""".strip().split(',')))

def get_last_entry(data, N):
    memory = {d: i + 1 for i, d in enumerate(data[:-1])}
    last_entry = data[-1]
    for i in range(len(memory) + 1, N):
        if last_entry in memory:
            age_of_last_entry = i - memory[last_entry]
        else:
            age_of_last_entry = 0
        memory[last_entry] = i
        last_entry = age_of_last_entry
    return last_entry

print(get_last_entry(data, 2020))
print(get_last_entry(data, 30000000))