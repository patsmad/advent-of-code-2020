from get_input import get_input

response = get_input(9)

all_data = list(map(int, response.text.strip().split('\n')))

N = 25
preamble = all_data[:N]
data = all_data[N:]
ind = None
for i in range(len(data)):
    s_preamble = {data[i] - a for a in preamble}
    if len(s_preamble.intersection(preamble)) == 0:
        ind = i + N
        break
    else:
        preamble = preamble[1:] + [data[i]]
print(all_data[ind])

out = None
for i in range(ind):
    for j in range(i + 1, ind):
        if sum(all_data[i:j]) == all_data[ind]:
            out = all_data[i:j]
            break
    if out:
        break
print(min(out) + max(out))
