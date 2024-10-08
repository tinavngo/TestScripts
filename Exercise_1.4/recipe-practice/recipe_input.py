import pickle

def take_recipe():
    name = str(input("Enter recipe name: "))
    cooking_time = int(input("Enter cooking time: "))
    ingredients = [
        ingredient.strip().capitalize()
        for ingredient in input("Enter the ingredients, separate each item with a comma: ").split(", ")]
    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }
    return recipe

def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    if cooking_time < 10 and len(ingredients) <= 4:
        difficulty = "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty

filename = input("Enter name of new or existing file: ")

try:
    file = open(filename, 'rb')
    data = pickle.load(file) 
    print("File loaded successfully")
except FileNotFoundError:
    print("Creating new file: " + filename)
    data = {"recipes_list": [], "all_ingredients": []}
except:
    print("An unknown error has occured. Please try again.")
    data = {"recipes_list": [], "all_ingredients": []}
else:
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

n = int(input("How many recipes would you like to enter?: "))

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe["ingredients"]:
        if not ingredient in all_ingredients:
            all_ingredients.append(ingredient)

data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

with open(filename, 'wb') as file:
    pickle.dump(data, file)

print("Recipe(s) have been successfully uploaded!")