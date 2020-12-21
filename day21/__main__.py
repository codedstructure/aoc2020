from utils import get_lines


def puzzle1():
    items = get_lines('day21')
    food = dict()

    allergen_candidates = dict()

    all_allergens = set()
    all_ingredients = set()
    for line in items:
        ingredients, _, allergens = line.partition(' (contains ')
        allergens = set(allergens.rstrip(')').split(', '))
        ingredients = set(ingredients.split())
        all_ingredients.update(ingredients)
        all_allergens.update(allergens)
        food[frozenset(ingredients)] = allergens

        for allergen in allergens:
            if allergen in allergen_candidates:
                # remove all candidates which don't appear in
                # current ingredient list
                allergen_candidates[allergen] &= ingredients
            else:
                allergen_candidates[allergen] = ingredients.copy()

    safe_ingredients = all_ingredients.copy()
    for ing in all_ingredients:
        for possible in allergen_candidates.values():
            if ing in possible:
                safe_ingredients.discard(ing)

    count = 0
    for recipe in food:
        for ing in recipe:
            if ing in safe_ingredients:
                count += 1
    print(count)


def puzzle2():
    items = get_lines('day21')
    food = dict()

    allergen_candidates = dict()

    all_allergens = set()
    all_ingredients = set()
    for line in items:
        ingredients, _, allergens = line.partition(' (contains ')
        allergens = set(allergens.rstrip(')').split(', '))
        ingredients = set(ingredients.split())
        all_ingredients.update(ingredients)
        all_allergens.update(allergens)
        food[frozenset(ingredients)] = allergens

        for allergen in allergens:
            if allergen in allergen_candidates:
                # remove all candidates which don't appear in
                # current ingredient list
                allergen_candidates[allergen] &= ingredients
            else:
                allergen_candidates[allergen] = ingredients.copy()

    known_bad = {}
    while True:
        for allergen, cand in allergen_candidates.items():
            unknown = cand - set(known_bad)
            if len(unknown) == 1:
                known_bad[next(iter(unknown))] = allergen
                break
        else:
            # implies we made no changes; we're done.
            break

    # Canonical 'bad ingredients' list *SORTED BY ALLERGEN*
    print(','.join(sorted(known_bad, key=lambda x: known_bad[x])))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
