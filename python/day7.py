from get_input import get_input

response = get_input(7)

def convert_value(v):
    if v == 'contain no other bags.':
        return []
    else:
        filtered_v = v.replace('contain', '').replace('.', '')
        split_v = [a.split(' ')[1:-1] for a in filtered_v.split('bag')[:-1]]
        return [(int(a[0]), ' '.join(a[1:])) for a in split_v]

data = response.text.strip().split('\n')
# data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.""".split('\n')

bags = {a.split(' bags ')[0]: convert_value(a.split(' bags ')[1]) for a in data}

count = 0
for bag in bags:
    new_bag = [bag]
    while True:
        new_new_bag = list(set([a[1] for b in new_bag for a in bags[b]] + new_bag))
        if len(new_new_bag) == len(new_bag):
            break
        else:
            new_bag = new_new_bag
    if 'shiny gold' in new_bag and bag != 'shiny gold':
        count += 1
print(count)

def recursive_bags(bags, bag):
    if bags[bag] == []:
        return 1
    else:
        return sum([a[0] * recursive_bags(bags, a[1]) for a in bags[bag]]) + 1


print(recursive_bags(bags, 'shiny gold') - 1)