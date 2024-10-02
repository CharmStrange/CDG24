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

def transform_bytes_to_structured_data(byte_data):
    # 1. Type: 첫 번째 바이트를 65~90 사이 값(A~Z)로 변환
    type_char = chr(65 + (byte_data[0] % 26))
    
    # 2. Region: 2~3번째 바이트를 합쳐서 지역 번호로 사용 (0~65535 범위)
    region = byte_data[1] * 256 + byte_data[2]
    
    # 3. Sum: 나머지 바이트들의 합을 구해서 정수 값으로 표현
    byte_sum = sum(byte_data[3:])
    
    # 4. Qs: 특정 바이트 값이 특정 조건을 만족하면 (예: 128 이상) 'High'로 분류, 그렇지 않으면 'Low'
    qs_value = "High" if byte_data[3] > 128 else "Low"
    
    return f"| {type_char} | {region} | {byte_sum} | {qs_value} |"


class Lifestyle:
    def __init__(self):
        self.ret = []
        print("Type category parameter, default is 'Meal'.")
        print("Category list : ['Meal', 'Snack', 'Dessert', 'VM']")

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
        
        elif category == 'Snack':
            pass

        elif category == 'Dessert':
            pass

        elif category == 'VM':
            tmp = [os.urandom(10) for _ in range(10)]
            print("| Company | Region | Sum | Qs |")
            for byte_data in tmp:
                transformed_data = transform_bytes_to_structured_data(byte_data)
                print(transformed_data)
            
        else:
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
t.Food('VM')