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

