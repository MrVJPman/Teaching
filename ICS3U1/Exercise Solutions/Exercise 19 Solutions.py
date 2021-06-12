#Question 1) Raise a BaseException exception with a relevant error message

#raise BaseException("Base Exception!")

#Question 2) Create a program that calculates the reciprocal of a given integer. If the given integer is 0, then raise a ZeroDivisionError. Provide a relevant error message

number = input("Enter a integer :  ")
if int(number) == 0:
    raise ZeroDivisionError("Cannot input Zero")
print(1 / float(number)) #This line is ignored if the Exception is raised

#Question 3) Copy and paste the code you finished in Homework 18 Question 2
#Place each set of code into its own try-except block. You should have three try-except block.
#Catch each of their exceptions and print the error message
#The exceptions must be different for each one, their message must be different
#You may not use [except Exception]!


try:
  new = "123" + 1
except TypeError as caught_exception:
  print(caught_exception)

try:
  L = [1, 2, 3]
  L[4]
except IndexError as caught_exception:
  print(caught_exception)

try :
  abc = "abc"
  int(abc)
except ValueError as caught_exception:
  print(caught_exception)

#Question 4) Redo #Question 3 with the following changes : 
#Generate a random number from 0,1,2. Review https://www.w3schools.com/python/ref_random_randint.asp
#Use the random number to randomly select one set of code (from the three sets) that will raise an Exception. You will need an if statement, an elif and an else
#Place these code in a try-except block. You should have a single try-except block.
#Have three except so that you catch each of the different type of Exceptions
#You may not use [except Exception]!

import random
randomized_number = random.randint(0, 2)
print(randomized_number)

try:
    if (randomized_number == 0):
        #Runtime error #1 : adding two different types
        new = "123" + 1
    elif (randomized_number == 1):
        #Runtime error #2 : accessing values that doesn't exist
        L = [1, 2, 3]
        L[4]
    else: 
        #Runtime error #3 : assertion error
        abc = "abc"
        int(abc)
except TypeError as caught_exception:
    print(caught_exception)
except IndexError as caught_exception:
    print(caught_exception)
except ValueError as caught_exception:
    print(caught_exception)