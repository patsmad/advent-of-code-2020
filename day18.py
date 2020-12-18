from get_input import get_input

response = get_input(18)
data = response.text.strip().split('\n')

def combine_all(split_string):
    while len(split_string) > 1:
        if split_string[1] == '+':
            split_string = [str(int(split_string[0]) + int(split_string[2]))] + split_string[3:]
        else:
            split_string = [str(int(split_string[0]) * int(split_string[2]))] + split_string[3:]
    return split_string[0]

def combine_all_in_order(split_string):
    while '+' in split_string:
        ind = split_string.index('+')
        split_string = split_string[:ind-1] + [str(int(split_string[ind-1]) + int(split_string[ind+1]))] + split_string[ind+2:]
    while '*' in split_string:
        ind = split_string.index('*')
        split_string = split_string[:ind-1] + [str(int(split_string[ind-1]) * int(split_string[ind+1]))] + split_string[ind+2:]
    return split_string[0]

sum_d = 0
for d in data:
    stack_of_stacks = []
    stack = []
    for a in d:
        if a == '(':
            stack_of_stacks.append(stack)
            stack = []
        elif a == ')':
            paren_num = combine_all(''.join(stack).split(' '))
            stack = stack_of_stacks.pop()
            stack.append(paren_num)
        else:
            stack.append(a)
    sum_d += int(combine_all(''.join(stack).split(' ')))
print(sum_d)

sum_d = 0
for d in data:
    stack_of_stacks = []
    stack = []
    for a in d:
        if a == '(':
            stack_of_stacks.append(stack)
            stack = []
        elif a == ')':
            paren_num = combine_all_in_order(''.join(stack).split(' '))
            stack = stack_of_stacks.pop()
            stack.append(paren_num)
        else:
            stack.append(a)
    sum_d += int(combine_all_in_order(''.join(stack).split(' ')))
print(sum_d)
