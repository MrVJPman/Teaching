#Question 1) Create a variable set to an empty list

var = []

#Question 2) Create a second variable using the variable from question 1 and 10 values of your choice. 
#You should’ve created a List. 

var2 = var + [0,0,0,0,0,0,0,0,0,0 ]

#Question 3) Use len() somehow in an READ from the left operation to retrieve the last value in the List in question 2. 
#Display the value with print()

print(var2[len(var2)-1])

#Question 4) Use len() somehow in an READ from the right operation to retrieve the first value in the List in question 2.
#Display the value with print().

print(var2[-len(var2)])

#Question 5) Without using len(), retrieve the third value and UP TO the and including third-to-last value. 
#Excluding the second to last and last value.
#Use both a positive and negative index
#Display the values with print()

print(var2[2:-2])

#Question 6) How do you check if the list you created in question 2 has None?
#Display the boolean with print()

print(None in var2)
