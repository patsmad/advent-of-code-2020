from get_input import get_input

data = '952438716'

class Cup:
    def __init__(self, label):
        self.label = label
        self.n = None

    def set_next(self, next):
        self.n = next

    def next(self, i):
        if i == 0:
            return self
        else:
            return self.n.next(i - 1)

def get_destination(possible_value, max_value, exempt_values):
    if possible_value == 0:
        return get_destination(max_value, max_value, exempt_values)
    if possible_value in exempt_values:
        return get_destination(possible_value - 1, max_value, exempt_values)
    return possible_value

def move(cups_dict, current_cup, max_value):
    cups_to_move = [current_cup.next(i) for i in range(1, 4)]
    destination_cup = cups_dict[get_destination(current_cup.label - 1, max_value, [c.label for c in cups_to_move])]
    current_cup.set_next(current_cup.next(4))
    cups_to_move[-1].set_next(destination_cup.next(1))
    destination_cup.set_next(cups_to_move[0])

# Part 1
cups = [Cup(int(a)) for a in data]
for i in range(len(cups)):
    cups[i].set_next(cups[(i+1) % len(cups)])
cups_dict = {cup.label: cup for cup in cups}
current_cup = cups[0]
for _ in range(100):
    move(cups_dict, current_cup, max(cups_dict))
    current_cup = current_cup.next(1)
print(''.join(map(str, [cups_dict[1].next(i).label for i in range(1, 9)])))

# Part 2
cups = [Cup(int(a)) for a in data] + [Cup(i) for i in range(10, 1000001)]
for i in range(len(cups)):
    cups[i].set_next(cups[(i+1) % len(cups)])
cups_dict = {cup.label: cup for cup in cups}
current_cup = cups[0]
max_value = max(cups_dict)
for i in range(10000000):
    move(cups_dict, current_cup, max_value)
    current_cup = current_cup.next(1)
    if i % 1000000 == 0:
        print(i)
print(cups_dict[1].next(1).label * cups_dict[1].next(2).label)