spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [] # first, initialize an empty list called names
    for spicy_food in spicy_foods: 
        names.append(spicy_food["name"])
        # loop over each dictionary in the spicy_foods list, and then for each dictionary (spicy_food), append the value of the 'name' key to the names list
    return names


def get_spiciest_foods(spicy_foods):
    above_five = [] # first, initialize an empty list called above_five
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            above_five.append(spicy_food)
        # loop over each dictionary in the spicy_foods list, and then for each dictionary (spicy_food), IF the value of the key 'heat_level' is greater than 5, append the value of the 'heat_level' key to the above_five list
        return above_five

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
        # loop over each dictionary in the spicy_foods list, and then for each dictionary (spicy_food), print the value of the 'name' key, followed by a space, followed by the value of the 'cuisine' key, followed by a space, followed by the value of the 'heat_level' key, followed by a space, followed by the string '🌶' * the value of the 'heat_level' key

def get_spicy_food_by_cuisine(spicy_foods, cuisine): #function takes two arguments; spicy_foods is the list of dictionaries,where each dictionary represents a spicy food and has a key called 'cuisine'. Cuisine is a string that represents the type of cuisine i'm looking for
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
        # function loops over each dictionary in the spicy_foods list. For each food, it checks to see if the value of the 'cuisine' key is the same as the cuisine argument. 
        # if there is a match, the function will return that food dictionary. 

def print_spiciest_foods(spicy_foods):
    above_five = []
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            above_five.append(spicy_food)
    for food in above_five:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    total_heat = 0 # move total outside of the loop, otherwise there will be a reset in the value of total
    for food in spicy_foods:
        total_heat += food["heat_level"]
    average_heat = total_heat / len(spicy_foods) # length of spicy foods
    return average_heat


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
