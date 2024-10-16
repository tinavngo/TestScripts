class ShoppingList(object):
    def __init__(self, list_name):
        # Initialize the list_name and shopping_list
        self.list_name = list_name
        self.shopping_list = []

    # Create method for adding items to the shopping list
    def add_item(self, item):
        if not item in self.shopping_list:
            self.shopping_list.append(item)
            print(f"{item} has been added to {self.list_name}.")
        else:
            print(f"{item} is already in {self.list_name}.")

    # Create method for removing items from the shopping list
    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"{item} has been removed from {self.list_name}.")
        else:
            print(f"{item} is not in {self.list_name}.")

   # Create method for displaying the updated list to users 
    def view_list(self):
       if not self.shopping_list:
            print(f"The {self.list_name} is empty.")
       else:
           print(self.list_name)
           for item in self.shopping_list:
               print(f"- {item}")
           

# Create an object from the ShoppingList class
pet_store_list = ShoppingList("Pet Store Shopping")

# Add items to object pet_store_list
for item in ['dog food' ,'frisbee', 'bowl', 'collars', 'flea collars']:
    pet_store_list.add_item(item)
print(pet_store_list.view_list())

# Remvove "flea collars" from the list
pet_store_list.remove_item("flea collars")

# Try to add "frisbee" again
pet_store_list.add_item("frisbee")

# Display the entire list
print(pet_store_list.view_list())
