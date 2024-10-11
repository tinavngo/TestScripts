
class Recipe(object):

    # Class variable set to be used for all recipes
    all_ingredients = set()

    # Initialize all needed attributes
    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None

    # Calculate the difficulty for recipe based off of len(ingredients) and int(cooking_time)
    def calc_difficulty(self, cooking_time, ingredients):
        if cooking_time < 10 and len(ingredients) < 4:
            self.difficulty = "Easy"
        elif cooking_time < 10 and len(ingredients) >= 4:
            self.difficulty = "Medium"
        elif cooking_time >= 10 and len(ingredients) < 4:
            self.difficulty = "Intermediate"
        elif cooking_time >= 10 and len(ingredients) >= 4:
            self.difficulty = "Hard"
        else:
            print("Something went wrong, please try again!")
        
    # Getter method which calls for calculation 
    def get_difficulty(self):
        # if difficulty has not been set
        if not self.difficulty:
            self.calc_difficulty()
        return self.difficulty

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def get_cooking_time(self):
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
    
    # Method for adding multiple elements to the tuple
    def add_ingredients(self, *args):
        for ingredient in args:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()

    # Method for getting ingredients for recipe
    def get_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient)

    # Method for returning true or false for ingredients in recipe
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
    
    # Method to update all_ingredients list
    def update_all_ingredients(self):
        # Iterates through current object's ingredients
        for ingredient in self.ingredients:
            # Check if ingredient does not already exist
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.add(ingredient)

    def __str__(self):
        # String representation of the recipe
        output = f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.difficulty}"
        return output

# Method for searching a recipe through ingredients
def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


# Main code for printing recipes
tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")

print(tea)
print(coffee)
print(cake)
print(banana_smoothie)

# Wrap recipes into a recipe list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Using method to search for recipes that contain specific ingredients
print("\nRecipes containing Water: ")
print("-------------------------------")
recipe_search(recipes_list, "Water")

print("\nRecipes containing Sugar: ")
print("-------------------------------")
recipe_search(recipes_list, "Sugar")

print("\nRecipes containing Bananas: ")
print("-------------------------------")
recipe_search(recipes_list, "Bananas")

