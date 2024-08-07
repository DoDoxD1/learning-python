from replit import clear
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

coffees = ["espresso", "latte", "cappuccino"]


def ask_money():
    """Asks user to enter amount of coins and return back the total input money"""
    print("Please insert coins.")
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))
    money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return money


def are_ingredients_enough(ingredients):
    """Checks if the available resources the enough to fulfill the ingredient requirement and returns a boolean value"""
    for key in ingredients:
        if resources[key] < ingredients[key]:
            return False
    return True


def process_coffee(coffee_type, ingredients, money, cost):
    """Processes and serves the delicious coffee to our customers"""
    clear()
    # use ingredients from the machine
    for key in ingredients:
        resources[key] -= ingredients[key]

    # adding money to the machine
    change = money - cost
    resources["money"] += cost

    # giving the coffee to user
    print(f"Here is {change} in change.")
    print(f"Here is your {coffee_type} ☕. Enjoy!\n")


def make_coffe(coffee_type):
    """Makes delicious coffe for our customers"""
    # checking if coffee type is valid
    if coffee_type not in coffees:
        print("Unable to process your request!")
        return

    # starting basic variables
    coffee = MENU[coffee_type]
    cost = coffee["cost"]
    ingredients = coffee["ingredients"]

    # are ingredients enough
    if not are_ingredients_enough(ingredients):
        print("Ingredients not enough. Sorry")
        return

    # asking user to enter the money
    money = ask_money()
    # checking if money is enough for the cost of coffee
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return

    process_coffee(coffee_type, ingredients, money, cost)


machine_is_on = True
while machine_is_on:
    # asking user input
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${resources['money']}\n")
    elif choice == "off":
        machine_is_on = False
    else:
        make_coffe(choice)
