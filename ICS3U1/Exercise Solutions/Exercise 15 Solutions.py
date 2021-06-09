#Question 1) https://www.w3schools.com/python/exercise.asp?filename=exercise_functions1

#Question 2)
#Create a function with no input that also return None as an output. You must write the return statement! 
#Call the function, and verify that the function call output None via print()

def no_input_return_None() : return None
print(no_input_return_None())

#Question 3)
#Hint : Use code from Homework 12-14 to help you with this
#a)Create a function that accepts only one input. The input will be a data structure (a list or a string). #The function prints all the values in a data structure one-by-one. 
#The function builds a list of every single character/value from the data structure  
#The function builds a new string from the values of the data structure. 
#you will need type conversion. Use str()
#The function then adds the new string at the end of the list
#The function finally returns the list

def str_list_combination(input_data_structure): 
    new_list = []
    new_string = "" 
    for value in input_data_structure: 
        print(value)
        new_list.append(value)
        new_string = new_string + str(value)
    new_list.append(new_string) 
    return new_list


#b) Call this function with this example input List. You should display the correct output. : 
#input : [1, 2, 3] 
#output : [1, 2, 3, “123”]

print(str_list_combination([1, 2, 3]))

#c) Call this function with this example input String. You should display the correct output. :
#input : “abc” 
#output : [“a”, “b”, “c”, “abc”]

print(str_list_combination("abc"))