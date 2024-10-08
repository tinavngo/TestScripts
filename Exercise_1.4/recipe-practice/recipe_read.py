import pickle

with open('recipe_binary.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print("Recipes - ")
print("Name: " + recipe['name'])
print("Ingredients: " + ", ".join(recipe['ingredients']))
print("Cooking time: " + str(recipe['cooking time']))
print("Difficulty: " + recipe['difficulty'])