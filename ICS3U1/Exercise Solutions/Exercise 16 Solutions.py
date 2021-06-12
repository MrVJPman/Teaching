#Question 1)

#For Homework 15 Q3, how many local variables did you create?

#Two
#Variable 1 : new_list = []
#Variable 2 : new_string = "" 

#Question 2)

#If you haven’t done so back in H15Q3, 
#Change homework 15 Q3 by creating two global variables, the values of each should be the two inputs in 3b and 3c.
#The inputs were [1, 2, 3] and “abc” 

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
print(str_list_combination(global_variable_list))
print(str_list_combination(global_variable_string))

#Question 3)  

#Create a function that has no input. It should combine the two global variables you created in question 2 as a single string (use + operator and use str()), and return this as a single string. Now print the returned string with a function call.

def question_three():
  return str(global_variable_list) + global_variable_string
print(question_three())


#Question 4)

#Create a function with only one input. The input name should share the same name as the first global variable you created in question 2. This function should print the function input 
#Call this function with a different value than the first global variable and check it is different.

def question_four(global_variable_list):
  print(global_variable_list)
question_four([4, 5, 6])

#Question 5)

#Create a function with no input.
#Create a local variable inside this function that shares the same variable name as the second global variable you created in question 2. 
#The local variable should have a different value than the second global variable. Print the local variable inside the function.
#Call this function and check the display message is different from the second global variable


def question_five():
  global_variable_string = "def"
  print(global_variable_string)
question_five()

#Question 6) 

#Redo Homework 15 Q3 but inside the function : double the data structure
#Hint: you only have to add one extra line of code.

#input : [1, 2, 3] --> output : [1, 2, 3, 1, 2, 3, “123123”]
#input : “abc”  --> output : [“a”, “b”, “c”, “a”, “b”, “c” “abcabc”]

def new_str_list_combination(input_data_structure): 
 new_list = []
 new_string = "" 
 input_data_structure = input_data_structure * 2
 for value in input_data_structure: 
   print(value)
   new_list.append(value)
   new_string = new_string + str(value)
 new_list.append(new_string) 
 return new_list


print(new_str_list_combination(global_variable_list))
print(new_str_list_combination(global_variable_string))