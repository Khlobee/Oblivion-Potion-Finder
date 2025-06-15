import json

#Code will read a dictionary from a json file
#Will have a few functions but the primary one is to list keys that have matching potion effects from oblivion
#Json format
#List is "Ingredients"
#Keys are "Name", "Effect1", "Effect2", "Effect3", "Effect4"
#May add location later

#File load function

list_of_ingredients = []

def load_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found")
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON format")
        return {}
    except Exception as e:
        print("Unexpected error occurred: {e}")
        return {}
    
#Search through dictionary and find 

#Main body
file_path = "IngredientsList.json"
ingredient_dict = load_from_json(file_path)

if ingredient_dict:
    print("Dictionary Loaded.")
else:
    print("Failed to Load Dictionary.")

if isinstance(ingredient_dict, list) and all(isinstance(item, dict)
    for item in ingredient_dict):
        list_of_ingredients = ingredient_dict
        print("right format")
else:
    print ("Not in right format")

loop = True

def one_effect_search():
    effect_request = input("What effect are you looking for?: ")

    print("These ingredients have", effect_request)
    for x in list_of_ingredients:
        if x["Effect1"] == effect_request or x["Effect2"] == effect_request or x["Effect3"] == effect_request or x["Effect4"] == effect_request:
            print(x["Name"])
        else:
            continue

def two_effect_search():
    first_effect = input("What is the first effect?: ")
    second_effect = input("What is the second effect?: ")
    set1 = set()
    set2 = set()
    

    for x in list_of_ingredients:
        if x["Effect1"] == first_effect or x["Effect2"] == first_effect or x["Effect4"] == first_effect or x["Effect4"] == first_effect:
            set1.add(x["Name"])
        if x["Effect1"] == second_effect or x["Effect2"] == second_effect or x["Effect4"] == second_effect or x["Effect4"] == second_effect:
            set2.add(x["Name"])

    print(list(set1 & set2))
#End of Func

def ingredient_search():
    ingredient_name = input("What ingredient do want to see the effects for?")
    for x in list_of_ingredients:
        if x["Name"] == ingredient_name:
            print(x["Name"])
            print(x["Effect1"])
            print(x["Effect2"])
            print(x["Effect3"])
            print(x["Effect4"])
#End of Func

def potion_maker():
    #Code to pick out a series of effects then provide a combination of ingredients to achieve those effects
    #For an effect to be valid you need two instances of the same effect
    #
    return

#Main code loop
while loop == True:
    print("1) One effect search")
    print("2) two effect search")
    print("3) Search by Name")
    print("any other option will close")
    userChoice = input("What would you like to do?")

    match userChoice:
        case "1":
            one_effect_search()
        case "2":
            two_effect_search()
        case "3":
            ingredient_search()
        case _:
            loop = False

print("Bye bye!")
#We can try to find ingredients with multiple effects by adding the results to two separate lists then comparing the list for matches (to be done later)
#So basically search twice and add the results into a list each
#Then Compare the two lists and add the resulting matches into another list
#Then print that list

