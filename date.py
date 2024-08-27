import json, pprint

menu = {
    "entrees": {
        "pizza": {
            "description": "A classic Italian dish with a crispy crust, topped with marinara sauce, mozzarella cheese, and pepperoni.",
            "price": 8.75,
            "ingredients": ["cheese", "pepperoni", "marinara sauce", "dough"],
        },
        "burger": {
            "description": "A juicy beef patty served with lettuce, tomato, cheese, and a side of fries.",
            "price": 9.50,
            "ingredients": ["beef patty", "cheese", "lettuce", "tomato", "bun", "fries"],
        },
        "pasta": {
            "description": "Creamy Alfredo pasta served with grilled chicken and a sprinkle of parmesan.",
            "price": 10.25,
            "ingredients": ["pasta", "Alfredo sauce", "grilled chicken", "parmesan cheese"],
        }
    },
    "appetizers": {
        "garlic bread": {
            "description": "Toasted bread topped with garlic butter and herbs, served with marinara sauce.",
            "price": 4.50,
            "ingredients": ["bread", "garlic", "butter", "herbs", "marinara sauce"],
        },
        "mozzarella sticks": {
            "description": "Crispy breaded mozzarella sticks served with marinara sauce.",
            "price": 5.75,
            "ingredients": ["mozzarella cheese", "breadcrumbs", "marinara sauce"],
        }
    },
    "desserts": {
        "cheesecake": {
            "description": "Rich and creamy cheesecake with a graham cracker crust, topped with strawberry sauce.",
            "price": 6.50,
            "ingredients": ["cream cheese", "graham cracker crust", "strawberry sauce"],
        },
        "chocolate cake": {
            "description": "Decadent chocolate cake layered with chocolate ganache.",
            "price": 7.00,
            "ingredients": ["chocolate", "flour", "sugar", "eggs", "ganache"],
        }
    },
    "beverages": {
        "soda": {
            "description": "Chilled carbonated soft drinks available in various flavors.",
            "price": 2.50,
            "options": ["Coke", "Pepsi", "Sprite"],
        },
        "coffee": {
            "description": "Freshly brewed coffee available in regular or decaf.",
            "price": 3.00,
            "options": ["regular", "decaf"],
        }
    }
}

#Get the name of your date
date_name = input("Who are you taking on a date?: ")
print("Your dates name is: " + date_name)

# Get the user budget for the date.
while True:
    budget = input("What is your budget for this date?: ")
    try:
        # Attempt to convert the input to a float
        budget = float(budget)
        # If the user tries to set the budget below 50 then they're told to stop being cheap
        if budget < 50:
            print("Stop being cheap! You should at least budget $50.")
        else:
            break  # Exit the loop if the budget is sufficient
    except ValueError:
        # If conversion fails, prompt the user to try again
        print("Please enter a valid number for the budget (e.g., 50 or 50.75).")

print("Your budget is: $" + str(budget))


print("\n----- Checkout our menu! -----\n")
# Use json.dumps to print the restaurant menu
print(json.dumps(menu, indent=4))
# We can also use pretty print
print("\n----- Pretty Print menu -----\n")
pprint.pprint(menu)


# Function to get item choice and validate
def get_order_item(category):
    while True:
        item = input(f"Select a(n) {category} item from the menu: ").strip().lower()
        if item in [key.lower() for key in menu[category].keys()]:
            return item
        else:
            print(f"Item not found. Please select a valid {category} item.")

# Create variables for user and dates running totals
user_spent = 0
date_spent = 0
# sales tax
tax_rate = 0.0475

# Function to process the order
def process_order():
    category = input("Enter the category (entrees, appetizers, desserts, beverages): ").strip().lower()
    if category in menu:
        item = get_order_item(category)
        item_info = menu[category][item]
        print(f"\nYou selected: {item.capitalize()}")
        print(f"Description: {item_info['description']}")
        print(f"Price: ${item_info['price']:.2f}")

        confirm = input("Would you like to add this to your order? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print(f"Added {item} to your order.")
            return item_info["price"]
        else:
            print("Item not added to order.")
            return 0
    else:
        print("Invalid category. Please select a valid category.")
        return 0

# Collect your dates order
print(f'Hi {date_name}, let\'s start with your order')
while True:
    date_spent += process_order()
    while True:
        another = input("Would you like to add another item to your order? (yes/no): ").strip().lower()
        if another in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please select 'yes' or 'no'.")
    if another == 'no':
        budget -= date_spent
        print(f"Remaining budget: ${budget:.2f}")
        break

# Collect your order
print("And for you?")
while True:
    user_spent += process_order()
    while True:
        another = input("Would you like to add another item to your order? (yes/no): ").strip().lower()
        if another in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please select 'yes' or 'no'.")
    if another == 'no':
        budget -= user_spent
        print(f"Remaining budget: ${budget:.2f}")
        break


# Confirm payment
total_spent = date_spent + user_spent
print("\n----- Final Check -----")
print(f"Total spent (including tax): ${(total_spent + (total_spent * tax_rate)):.2f}")
print(f"The final amount you have remaining in your budget is: ${budget - (total_spent * tax_rate):.2f}")
payment_confirmation = input("Do you agree to pay the bill? (yes/no): ").strip().lower()

if payment_confirmation == 'yes':
    print("Thank you for dining with us! Have a great day.")
else:
    print("Please review your order and try again.")

if budget <= 0.00 and user_spent < date_spent:
    print('Never again!')
else:
    print(f'You should take {date_name} on a second date!')

