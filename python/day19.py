from get_input import get_input
import re

response = get_input(19)
rules, data = response.text.strip().split('\n\n')
rules = rules.strip().split('\n')
data = data.strip().split('\n')

def get_formatted_rules(rules):
    formatted_rules = {}
    letters = {}
    for rule in rules:
        if '\"' in rule:
            letters[int(rule.split(': ')[0])] = rule.split(': ')[1][1]
        else:
            formatted_rules[int(rule.split(': ')[0])] = [tuple([int(b) for b in a.split(' ')]) for a in rule.split(': ')[1].split(' | ')]
    return formatted_rules, letters
formatted_rules, letters = get_formatted_rules(rules)

def unwrap_rule(rule, all_rules, all_letters, max_recursion_depth, depth):
    if depth > max_recursion_depth:
        return ''
    if isinstance(rule, list):
        return '(' + '|'.join([unwrap_rule(a, all_rules, all_letters, max_recursion_depth, depth + 1) for a in rule]) + ')'
    elif isinstance(rule, tuple):
        return ''.join([unwrap_rule(a, all_rules, all_letters, max_recursion_depth, depth + 1) for a in rule])
    else:
        if rule in all_rules:
            return unwrap_rule(all_rules[rule], all_rules, all_letters, max_recursion_depth, depth + 1)
        else:
            return all_letters[rule]

pattern = '^' + unwrap_rule(formatted_rules[0][0], formatted_rules, letters, len(formatted_rules), 0) +'$'
print(pattern)
count = 0
for d in data:
    if re.match(pattern, d):
        count += 1
print(count)

rules += """8: 42 | 42 8
11: 42 31 | 42 11 31""".strip().split('\n')
formatted_rules, letters = get_formatted_rules(rules)

pattern = '^' + unwrap_rule(formatted_rules[0][0], formatted_rules, letters, len(formatted_rules), 0) +'$'
count = 0
for d in data:
    if re.match(pattern, d):
        count += 1
print(count)
