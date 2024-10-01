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


