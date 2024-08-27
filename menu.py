import pprint

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

print("\n----- Checkout our menu! -----\n")
# Use json.dumps to print the restaurant menu
pprint.pprint(menu)
