import os 
# os.getrandom~
# os.urandom ~
# os.GRND_NONBLOCK
# os.GRND_RANDOM

import time
import random

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

ContentsList()