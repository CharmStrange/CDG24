import os 
# os.getrandom~
# os.urandom ~
# os.GRND_NONBLOCK ~
# os.GRND_RANDOM ~

import time
import random
import string

# Guide
def ContentsList():
    print("Lifestyle : 1")
    print("Education : 2")
    print("Business: 3")
    print("Science & Technology : 4")
    print("Health & Wellness : 5")
    print("Entertainment : 6")
    print("Society & Politics : 7")
    print("Environment : 8")
    print("Fashion & Beauty : 9")
    print("Hobby : 10")

    _a = int(input("\nChoose one : "))

    if _a == 1 : # Lifestyle
        print("Food")
        print("Travel")
        print("Home")
        print("Family")

    elif _a == 2 : # Education
        print("Language")
        print("Academic Study")
        print("Online Study")
        print("Certification")

    elif _a == 3 : # Business
        print("Company")
        print("Marketing")
        print("Finance")

    elif _a == 4 : # Science & Technology
        print("Physics")
        print("Biology")
        print("Chemistry")
        print("Engineering")

    elif _a == 5 : # Health & Wellness
        print("Diet")
        print("Exercise")
        print("Fitness")
        print("Mental Health")
        
    elif _a == 6 : # Entertainment
        print("Movie")
        print("Music")
        print("")

    elif _a == 7 : # Society & Politics
        print("Society")
        print("Economy")
        print("Friend")
        print("Politics")

    elif _a == 8 : # Environment
        print("Nature")
        print("Energy")
        print("Recycle")

    elif _a == 9 : # Fashion & Beauty
        print("Fashion")
        print("Accessory")
        print("Beauty")

    elif _a == 10 : # Hobby
        print("Videos")
        print("Game")
        print("Making")
        print("Activity")

# Make alphabets
def mixed_case_mapping(times=5):
    alphabet = string.ascii_letters  # azAZ
    mapping = {}
    for i in range(times):
        rand_num = os.urandom(1)[0] % len(alphabet)
        mapping[alphabet[rand_num]] = rand_num
    return mapping

class Lifestyle:
    def __init__(self):
        self.ret = []
        print("Type category parameter, default is 'Meal'.")
        print("Category list : ['Meal', 'Snack', 'Dessert']")

    def __del__(self):
        pass

    def Food(self, category):
        if category == 'Meal':
            rand_num1 = os.urandom(1)[0] % (os.urandom(1)[0]) % 11
            rand_num2 = os.urandom(1)[0] % (os.urandom(1)[0]) % 11

            tmp_list1 = [dicts for dicts in mixed_case_mapping(rand_num1)]
            tmp_list2 = [dicts for dicts in mixed_case_mapping(rand_num2)]

            #print(tmp_list1); print(''.join(tmp_list1)); print((''.join(tmp_list1), rand_num1))
            #print(tmp_list2); print(''.join(tmp_list2)); print((''.join(tmp_list2), rand_num2))
            print("| Name | Type | Taste | Quality |")
            print((''.join(tmp_list1), ''.join(tmp_list2), rand_num1, rand_num2))
            return (''.join(tmp_list1), ''.join(tmp_list2), rand_num1, rand_num2)
        
        elif self.category == 'Snack':
            pass
        elif self.category == 'Dessert':
            pass

class Education:
    pass

class Business:
    pass

class ST: # Science & Technology
    pass

class HW: # Health & Wellness
    pass

class Entertainment:
    pass

class SP: # Society & Politics
    pass

class Environment:
    pass

class FB: # Fashion & Beauty
    pass

class Hobby:
    pass

t = Lifestyle()
t.Food('Meal')