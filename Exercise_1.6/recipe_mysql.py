import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'cf-python',
    passwd = 'password'
)    
cursor = conn.cursor()

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(50),
               ingredients VARCHAR(255),
               cooking_time INT,
               difficulty VARCHAR(20)
)''')

def create_recipe(conn, cursor):
    print("Follow the steps below to create a new recipe")
    print("==========================================================")
    
    while True:
        try:
            n = int(input("How many recipes would you like to enter?: "))
            if n < 1:
                print("Input is invalid, please enter a positive number.")
            else:
                break
        except ValueError:
            print("Input is invalid, please enter a number.")

    for i in range(n):
        print(f"Enter recipe #{i + 1}")
        print("-------------------------------------")

        name = input("Enter the recipe name: ")
        cooking_time = int(input("Enter cooking time (in minutes): "))
        ingredients = tuple(
        ingredient.strip().capitalize()
        for ingredient in input("Enter the ingredients, separate each item with a comma: ").split(",")
    )
        joined_ingredients = ', '.join(ingredients)
        
        difficulty = calculate_difficulty(cooking_time, ingredients)

        insert_query = """
        INSERT INTO Recipes (name, cooking_time, ingredients, difficulty)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, cooking_time, joined_ingredients, difficulty))
        conn.commit()
        print("Recipe has been added successfully!")

def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    elif cooking_time >= 10 and len(ingredients) >= 4 :
        return "Hard"
    else:
        print("Something went wrong, please try again.")

def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    if not results:
        print("=============================================================================")
        print("There are no recipes within the database, try to create a new recipe instead!")
        print("Returning to main menu.........")
        print("=============================================================================")
        return

    all_ingredients = set()
    for row in results:
        ingredients = row[0]
        all_ingredients.update(ingredients.split(', '))

    print("==========================================================")
    print("Available Ingredients to Search From")
    print("==========================================================")
    for i, ingredient in enumerate(sorted(all_ingredients)):
        print(f"{i+1}.) {ingredient}")
    
    print()
    while True:
        try:
            n = int(input("Enter number of ingredient to search: "))
            if 1 <= n <= len(all_ingredients):
                break
            else:
                print("Please enter a number shown on the list.")
        except ValueError:
            print("Something went wrong, returning to main menu....")
            return

    selected_ingredient = sorted(all_ingredients)[n - 1]
    search_query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(search_query, ("%" + selected_ingredient + "%",))
    search_results = cursor.fetchall()

    if search_results:
        recipe_count = len(search_results)
        recipe_word = "recipe" if recipe_count == 1 else "recipes"
        print(f"\n{recipe_count} {recipe_word} found containing '{selected_ingredient}'\n")
        for recipe in search_results:
            print(f"\nRecipe: {recipe[1].title()}")
            print(f"Cooking Time: {recipe[3]}")
            print("Ingredients: ")
            for ingredient in recipe[2].split(", "):
                print(f" - {ingredient}")
            print(f" Difficulty: {recipe[4]}")
            print("==========================================================")
            print("Recipe search successful!")
            print("Returning to main menu........")
            return
    else:
        print("==========================================================") 
        print(f"Unable to find recipes containing '{selected_ingredient}'")
        print("Returning to main menu........")
        print("==========================================================")
    conn.commit()

def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    if not results:
        print("=============================================================================")
        print("There are no recipes within the database, try to create a new recipe instead!")
        print("Returning to main menu.........")
        print("=============================================================================")
        return

    print("==========================================================")
    print("Available Recipes to Search From")
    print("==========================================================")

    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}")

    recipe_input = int(input("Enter the ID of the recipe you'd like to update: "))
    print("\n - Name\n - Ingredients\n - Cooking time")
    column_update = input("Type an asset to update: ")

    new_value = None
    if column_update == 'name' or column_update == 'Name':
        new_value = input("Enter a new name for the recipe: ")
        update_query = "UPDATE Recipes SET name = %s WHERE id = %s"
        cursor.execute(update_query, (new_value, recipe_input))
    elif column_update == 'ingredients' or column_update == 'Ingredients':
        new_value = tuple(
        ingredient.strip().capitalize()
        for ingredient in input("Enter the ingredients, separate each item with a comma: ").split(",")
    )
        joined_ingredients = ', '.join(new_value)

        update_query = "UPDATE Recipes SET ingredients = %s WHERE id = %s"
        cursor.execute(update_query, (joined_ingredients, recipe_input))
    elif column_update == 'cooking time' or column_update == 'Cooking time' or column_update == 'Cooking Time':
        new_value = int(input("Enter the new cooking time (in minutes): "))
        update_query = "UPDATE Recipes SET cooking_time = %s WHERE id = %s"
        cursor.execute(update_query, (new_value, recipe_input))
    else:
        print("This input is invalid, please try again.")
        return
    
    if column_update in ['ingredients', 'cooking_time']:
        cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_input))
        row = cursor.fetchone()
        difficulty = calculate_difficulty(row[0], row[1])
        update_query = "UPDATE Recipes SET difficulty = %s WHERE id = %s"
        cursor.execute(column_update, (difficulty, recipe_input))

    conn.commit()
    print("Recipe has been successfully updated!")

def delete_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    print("Available Recipes to Delete")
    print("==========================================================")
    for row in recipes:
        if len(row) >= 2:
            print(f"ID: {row[0]}, Name: {row[1]}")

    recipe_id = int(input("Enter the ID corresponding to the recipe you would like to delete: "))

    if any(r[0] == recipe_id for r in recipes):
        delete_query = "DELETE FROM Recipes WHERE id = %s"
        cursor.execute(delete_query, (recipe_id,))
        conn.commit()
        print(f"Recipe with ID {recipe_id} has been deleted.")
    else:
        print(f"Recipe with ID {recipe_id} does not exist.")


def main_menu(conn, cursor):
    while True:
        print("==========================================================")
        print("             Welcome to the Recipe App ! ")
        print(" Please pick a choice from the following options below:")
        print("==========================================================")
        print("1. Create a new recipe")
        print("2. Search for recipes by ingredient")
        print("3. Update existing recipe")
        print("4. Deleting a recipe")
        print("5. Exit main menu")

        choice = input("Enter choice by number: ")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn,cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            print("Exiting main menu...")
            conn.commit()
            cursor.close()
            conn.close()
            break
        else:
            print("Input is invalid, please try again.")
            print("Hint: Choose a number from 1 to 5")

main_menu(conn, cursor)