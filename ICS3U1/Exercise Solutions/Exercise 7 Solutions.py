#Question 1)
#Call the input() function. Once the user enters some keyboard input, store the user’s keyboard input into a variable. 
#Now display the user input back using print() using the same variable.

user_input = input()
print(user_input)

#Question 2)
#Create a program where an user will enter a number and write a message stating the user has to enter a number. 
#Then display the input number divided by 2. 

user_input_as_str = input("Enter a number")
user_input_as_int = int(user_input_as_str)
print(user_input_as_int/2)

#Question 3)
#Create a program where an user will be requested an integer and then will be requested a float 
#(both requests should have a message). 
#Then display the original integer, the original float, their sum, their difference, and their product.

user_input_1_as_str = input("Enter an int")
user_input_1_as_int = int(user_input_1_as_str)

user_input_2_as_str = input("Enter an int")
user_input_2_as_float = float(user_input_1_as_str)

print(user_input_1_as_int, user_input_2_as_float, user_input_1_as_int + user_input_2_as_float
      , user_input_1_as_int - user_input_2_as_float
      , user_input_1_as_int * user_input_2_as_float)