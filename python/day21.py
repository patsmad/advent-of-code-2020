from get_input import get_input

response = get_input(21)
data = response.text.strip().split('\n')
# data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)""".strip().split('\n')

all_ingredients = []
allergen_map = {}
for d in data:
    ingredients = d.split(' (contains ')[0].split(' ')
    allergens = d.split(' (contains ')[1][:-1].split(', ')
    for allergen in allergens:
        allergen_map[allergen] = allergen_map.get(allergen, set(ingredients)).intersection(set(ingredients))
    all_ingredients += ingredients
possible_allergen_ingredients = set([b for a in allergen_map.values() for b in a])
print(len([a for a in all_ingredients if a not in possible_allergen_ingredients]))

known_allergens = {}
while len(allergen_map) > 0:
    for allergen, possible_ingredients in list(allergen_map.items()):
        allergen_map[allergen] = [a for a in possible_ingredients if a not in known_allergens]
        if len(allergen_map[allergen]) == 1:
            known_allergens[allergen_map[allergen][0]] = allergen
            allergen_map.pop(allergen)
output = [(v, k) for k, v in known_allergens.items()]
output.sort()
print(','.join([a[1] for a in output]))