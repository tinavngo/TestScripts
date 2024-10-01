# Empty lists for recipes and ingredients
recipes_list = []
ingredients_list = []

# Function for user input for recipe
def take_recipe():
    name = str(input("Enter the recipe name: "))
    cooking_time = int(input("Enter the amount of time this recipe will take (in minutes): "))
    ingredients = list(input("Enter the ingredients: ").split(", "))
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }

    return recipe

# User prompt: Number of recipes
n = int(input("How many recipes would you like to enter?: "))

# Iterates through number of recipes
for i in range(n):
    recipe = take_recipe()

    # Checks if an ingredient already exists in ingredients_list
    for ingredient in recipe["ingredients"]:
        if not ingredient in [ingredients_list]:
            ingredients_list.append(ingredient)


    recipes_list.append(recipe)


# Iterates through recipes_list to determine difficulty
for recipe in recipes_list:
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Easy"

    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Medium"

    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Intermediate"
    
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Hard"


# Iterates through recipes_list to display elements
for recipe in recipes_list:
    print("Recipe: ", recipe["name"])
    print("Cooking time: ", recipe["cooking_time"])
    print("Ingredients: ", recipe["ingredients"])
    print("Difficulty: ", recipe["difficulty"])

