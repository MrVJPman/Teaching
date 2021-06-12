#Question 1) Test this function with two more assert statements

def ANDop(boolean_1, boolean_2):
    return boolean_1 * boolean_2

assert(ANDop(False, False) == False)
assert(ANDop(True, False) == False)
assert(ANDop(False, True) == False)
assert(ANDop(True, True) == True)

#Question 2) Test this function with 4 different assert statements

def ORop(boolean_1, boolean_2):
    return (boolean_1 + boolean_2) >= 1

assert(ORop(False, False) == False)
assert(ORop(True, False) == True)
assert(ORop(False, True) == True)
assert(ORop(True, True) == True)

#Question 3) 
#Copy the function definition for Homework 15Q3a
#Rewrite the two input-output pair you were given for Homework 15 Q3bc as two assert statements

def str_list_combination(input_data_structure): 
    new_list = []
    new_string = "" 
    for value in input_data_structure: 
        print(value)
        new_list.append(value)
        new_string = new_string + str(value)
    new_list.append(new_string) 
    return new_list

global_variable_list = [1, 2, 3]
global_variable_string = "abc"
assert(str_list_combination(global_variable_list) == [1, 2, 3, "123"])
assert(str_list_combination(global_variable_string) == ["a", "b", "c", "abc"])

#Question 4) Test the function in Homework 15Q3a with two different empty cases

assert(str_list_combination([]) == [""])
assert(str_list_combination("") == [""])

#Question 5) Test the function in Homework 15Q3a with two different complex cases

import random
#generates a random list of 10 integers from 1 to 10
random_list = [random.randint(1,10) for number in range(10)]
print (random_list)
assert(str_list_combination(random_list) == random_list + ["".join(map(str, random_list))])

import string 
#generates a random string of 10 letters
random_string = ''.join(random.choices(string.ascii_uppercase, k = 10))
print (random_string)
assert(str_list_combination(random_string) == [letter for letter in random_string] + [random_string])