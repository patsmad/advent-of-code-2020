from get_input import get_input
import re

response = get_input(4)

data_map = [{b.split(':')[0]: b.split(':')[1] for b in a.strip().replace('\n', ' ').split(' ')} for a in response.text.split('\n\n')]

fields = """
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

fields = {a.split(' ')[0] for a in fields.split('\n')[1:-1]}
required_fields = fields.copy()
required_fields.remove('cid')

valid = 0
for d in data_map:
    if len([a for a in d if a in required_fields]) == 7:
        valid += 1
print(valid)

# Part II
# requirements = """
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# """

requirements = {
    'byr': lambda x: len(x) == 4 and int(x) >= 1920 and int(x) <= 2002,
    'iyr': lambda x: len(x) == 4 and int(x) >=2010 and int(x) <= 2020,
    'eyr': lambda x: len(x) == 4 and int(x) >=2020 and int(x) <= 2030,
    'hgt': lambda x: re.match('^[0-9]*cm$|^[0-9]*in$', x) and ((int(x.split('cm')[0]) >= 150 and int(x.split('cm')[0]) <= 193) if 'cm' in x else (int(x.split('in')[0]) >= 59 and int(x.split('in')[0]) <= 76)),
    'hcl': lambda x: bool(re.match('^\#[0-9a-f]{6}$', x)),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: bool(re.match('^[0-9]{9}$', x)),
    'cid': lambda x: True
}

def validate(d):
    return len([a for a in d if a in required_fields]) == 7 and all([requirements[a](d[a]) for a in d])

valid_2 = 0
for d in data_map:
    if validate(d):
        valid_2 += 1
print(valid_2)