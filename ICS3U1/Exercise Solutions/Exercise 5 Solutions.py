#Question 1) 
#Why can the operators you’ve learned in Class 2 and Class 4 be considered as functions?

#Answer : They both take inputs, does some processing, and return an output

#Question 2)
#example(True, False, True, False, True)
#How many inputs does this function have?
#How many outputs will this function have?

#5 inputs
#1 output

#Question 3)
#Explain how following line of code show its the displayed message
print(print(print(None)))


#print(print(print(None)))
#               Displays None, print(None) returns None   

#print(print(None))
#      Displays None, print(None) returns None

#print(None)
#Displays None, print(None) returns None



#Question 4)
#i) Create a variable (you can pick any variable name you want) with your choice of the value (no integers allowed)
#ii) Give the variable as an input to the function type()
#iii) Set the output of the type() in step ii) into a second variable (you can pick any variable name you want)
#iv) Display the variable in i and ii using print(), with the word ''is'' in between
#The displayed message have to be on the same line
#Here’s an example if using the class notes --> 1 is <class 'int'>

var = 1.0
type_of_var = type(var)
print(var, "is", type_of_var)