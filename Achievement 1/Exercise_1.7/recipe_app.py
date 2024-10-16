from sqlalchemy.types import Integer, String
from sqlalchemy import Column
from sqlalchemy.sql.expression import or_

# Database Configuration for MySQL
USERNAME = "cf-python"
PASSWORD = "password"
HOST = "localhost"
DATABASE = "task_database"

# Create the bridge to database
from sqlalchemy import create_engine
engine = create_engine(f"mysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}")

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Create the session for database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Create Recipe model and table
class Recipe(Base):
    __tablename__= "final_recipes"
    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(225))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    # Quick representation method
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + self.difficulty + ">"
    # String representation method
    def __str__(self):
        ingredients_list = self.return_ingredients_as_list()
        ingredients_str = ", ".join(ingredients_list)
        output = f"\nRecipe: {self.name}\n\tIngredients: {ingredients_str}\n\tCooking Time: {self.cooking_time} minutes\n\tDifficulty: {self.difficulty}"
        return output
    # Method used to calculate difficulty using cooking_time and ingredients
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

    # Method to retrieve ingredients string object as a list
    def return_ingredients_as_list(self):
        if self.ingredients:
            # Return individual ingredients
            return self.ingredients.split(", ")
        else:
            return []

Base.metadata.create_all(engine)

# Function #1: Create recipe
def create_recipe():
    print("\nFollow the steps below to create a recipe")
    print("==========================================================")
    # logic for name input
    n_input = input("Enter the name of your recipe: ")
    if len(n_input) > 50 or not all(n.isalnum() or n.isspace() for n in n_input):
        print("## Invalid characters, please try again. ##")
        return
    # logic for ingredient input
    ingredients = []
    i_input = input("How many ingredients would you like to enter?: ")
    if not i_input.isnumeric():
        print("## The input was not a number, please try again. ##")
        return
    else:
        i_input = int(i_input)
        for i in range(i_input):
            ingredient = input(f"Enter ingredient #{i + 1}: ")
            ingredients.append(ingredient)
        ingredients_str = ", ".join(ingredients)
    # logic for cooking time input
    c_input = input("Enter cooking time (in minutes): ")
    if not c_input.isnumeric() or int(c_input) < 0:
        print("## Input was not a positive number, please try again. ##")

    recipe_entry = Recipe(
        name=n_input, ingredients=ingredients_str, cooking_time=int(c_input)
    )
    recipe_entry.calc_difficulty(recipe_entry.cooking_time, recipe_entry.ingredients)


    # Add recipes to the session
    session.add(recipe_entry)
    session.commit()
    print("\nRecipe has been added successfully!")
    print("Returning back to main menu...")


# Function #2: View all recipes
def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("==========================================================")
        print("No recipes were found. Try creating a new one!")
        print("==========================================================")
        print("\nReturning back to main menu...")
        return
    
    print("\n-----Displaying all Available Recipes------")
    for recipe in recipes:
        print(recipe)

    print()        
    print("\nReturning back to main menu...")

# Function #3: Search by ingredient
def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("==========================================================")
        print("No recipes were found. Try creating a new one!")
        print("==========================================================")
        return
    
    results = session.query(Recipe.ingredients).all()
    all_ingredients = sorted(set(
        ingredient for result in results for ingredient in result[0].split(", ")
    ))

    print("==========================================================")
    print("Available ingredients:")
    print("==========================================================")
    for i, ingredient in enumerate(all_ingredients):
        print(f"{i + 1}. {ingredient}")

    # User input for ingredient search
    print("-"*58)
    selected_ingredients = input("Enter the number(s) of the ingredient you want to look up (separate each number with a space): ").split()

    # Validate input
    if not all(
        i.isnumeric() and 0 < int(i) <= len(all_ingredients)
        for i in selected_ingredients
    ):
        print("\n## Invalid selection, please try again. ##")
        print("Returning back to main menu...")
        return
    
    # Get ingredients based on user selection
    search_ingredients = [all_ingredients[int(i) - 1] for i in selected_ingredients]

    # Apply AND condition to search for recipes that include all selected ingredients
    conditions = [Recipe.ingredients.like(f"%{ingredient}%") for ingredient in search_ingredients]
    results = session.query(Recipe).filter(*conditions).all()

    # Output results
    if results:
        print("\n-----Displaying all Available Recipes------")
        for recipe in results:
            print(recipe)
        print("\nSearch Successful!")
        print("Returning back to main menu...")
    else:
        print("\n## No recipes were found with the selected ingredients. ##")
        print("Returning to main menu...")
        
    
# Function #4: Edit recipe
def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("==========================================================")
        print("No recipes were found. Try creating a new one!")
        print("==========================================================")
        return
    print("\nFollow the steps below to edit a recipe")
    print("==========================================================")
    results = session.query(Recipe.id, Recipe.name).all()
    # Print existing recipe data
    for recipe_id, name in results:
        print(f"{recipe_id}. {name}")

    # User input for editing
    print("-"*58)
    selected_id = input("Enter the ID of the recipe you would like to edit: ")
    if not selected_id.isnumeric():
        print("\n## Invalid input, please try again. ##")
        print("Returning back to main menu...")
        return
    
    recipe_to_edit = session.query(Recipe).filter_by(id=int(selected_id)).first()
    if not recipe_to_edit:
        print("\n## Recipe not found, please try again. ##")
        print("Returning back to main menu...")
        return
    
    print(f"\n1.) Name: {recipe_to_edit.name}")
    print(f"2.) Ingredients: {recipe_to_edit.ingredients}")
    print(f"3.) Cooking Time: {recipe_to_edit.cooking_time}")

    print("-"*58)
    att_edit = input("Enter the number of the asset you would like to edit: ")
    if att_edit not in ["1", "2", "3"]:
        print("\n## Invalid input, please enter a number from the list. ##")
        print("Returning back to main menu...")
        return
    if att_edit == "1":
        new_n = input("Enter the new name of your recipe: ")
        if len(new_n) > 50 or not all(
            n.isalnum() or n.isspace() for n in new_n
        ):
            print("\n## Invalid recipe name, please try again. ##")
            print("Returning back to main menu...")
            return
        
        recipe_to_edit.name = new_n
    elif att_edit == "2":
        new_ingredients = []
        new_i = int(input("How many ingredients would you like to enter?: "))
        for i in range(new_i):
            ingredient = input(f"Enter ingredient #{i + 1}: ")
            new_ingredients.append(ingredient)
        recipe_to_edit.ingredients = ", ".join(new_ingredients)
    elif att_edit == "3":
        new_ct = input("Enter the new cooking time (in minutes): ")
        if not new_ct.isnumeric():
            print("\n## Invalid cooking time! ##")
            print("Returning back to main menu...")
            return
        recipe_to_edit.cooking_time = int(new_ct)

    recipe_to_edit.calc_difficulty(recipe_to_edit.cooking_time, recipe_to_edit.ingredients)
    session.commit()
    print("\nRecipe updated successfully!")
    print("Returning back to main menu...")


# Function #5: Delete recipe
def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("==========================================================")
        print("No recipes were found. Try creating a new one!")
        print("==========================================================")
        return
    print("\nFollow the steps below to edit a recipe")
    print("==========================================================")
    results = session.query(Recipe.id, Recipe.name).all()
    for recipe_id, name in results:
        print(f"{recipe_id}. {name}")

    # User input for recipe deletion
    print("-"*58)
    selected_id = input("Enter the ID of the recipe you would like to delete: ")
    if not selected_id.isnumeric():
        print("\n## Invalid input, please try again. ##")
        print("Returning to main menu...")
        return
    recipe_to_delete = session.query(Recipe).filter_by(id=int(selected_id)).first()
    if not recipe_to_delete:
        print("Recipe does not exist. Please try again.")
        return
    confirm = input(f"Are you sure you want to delete '{recipe_to_delete.name}'? Y/N: ")
    if confirm.lower() == "yes" or confirm.lower() == "y":
        session.delete(recipe_to_delete)
        session.commit()
        print(f"\n'{recipe_to_delete.name}' has been deleted successfully!")
        print("Returning back to main menu...")
    else:
        print("\nDeletion has been cancelled.")
        print("Returning back to main menu...")
        return

def main_menu():
    while True:
        print()
        print("\n==========================================================")
        print("             Welcome to the Recipe App ! ")
        print(" Please pick a choice from the following options below:")
        print("==========================================================")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredient")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit main menu")

        print("-"*58)
        choice = input("Please choose an option [1-5] or type 'quit' to exit the menu: ")    

        if choice == "1" or choice.lower() == "create a new recipe":
            create_recipe()
        elif choice == "2" or choice.lower() == "view all recipes":
            view_all_recipes()
        elif choice == "3" or choice.lower() == "search for recipes by ingredient":
            search_by_ingredients()
        elif choice == "4" or choice.lower() == "edit a recipe":
            edit_recipe()
        elif choice == "5" or choice.lower() == "delete a recipe":
            delete_recipe()
        elif choice.lower() == "quit":
            print("Exiting the application....")
            session.close()
            session.commit()
            break
        else:
            print("\nInvalid input. Please choose one of the options or type 'quit' to exit.")

# Bring back to the main menu
main_menu()

