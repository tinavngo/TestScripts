import pickle

recipe = {
    'name': 'Tea',
    'ingredients': ['Tea leaves','Water','Sugar'],
    'cooking time': 5,
    'difficulty': 'Easy'
}

my_file = open('recipe_binary.bin', 'wb')
pickle.dump(recipe, my_file)
my_file.close()