# Write your solution here
def read_file(filename: str) -> dict:
    recipes = []
    recipes_d = {}
    with open(filename, 'r') as f:
        for line in f:
            recipes.append(line.strip())
    c = 0
    for words in recipes:
        if words != '':
            if c == 0:
                recipe = words
                recipes_d[recipe] = []
            else:
                recipes_d[recipe].append(words)
        else:
            c = 0
            continue
        c += 1
    return recipes_d

def search_by_name(filename: str, word: str) -> list:
    recipes_d = read_file(filename) 
    found_recipes = [k for k, v in recipes_d.items() if word.lower() in k.lower()]
    return found_recipes

def search_by_time(filename: str, prep_time: str) -> list:
    recipes_d = read_file(filename)
    found_recipes = [f'{k}, preparation time {v[0]} min' for k, v in recipes_d.items() if int(v[0]) < prep_time]
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str) -> list:
    recipes_d = read_file(filename) 
    found_recipes = [f'{k}, preparation time {v[0]} min' for k, v in recipes_d.items() if ingredient in v[1:]]
    return found_recipes

if __name__ == "__main__":
    print(search_by_ingredient('recipes1.txt', 'eggs'))
