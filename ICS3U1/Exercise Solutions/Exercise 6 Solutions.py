#Question 1)
#Use the function ord()
#Create one variable for each of the characters in your first name. 
#All of the characters of your first name should be initially lower case
#The value of each variable should be the ASCII/UNICODE-translated integer representing each character

letter_one = ord("b")
letter_two = ord("o")
letter_three = ord("b")

#Question 3)
#Use the function chr()
#Using all the variables in Question 1, create a single variable that will have your first name with all upper case.
#Now display your first name

print(chr(letter_one - 32) + chr(letter_two - 32) + chr(letter_three - 32))

#Question 3) What is the type of the input for this print() call?

print("Hello World!")
#String


#Question 4) DO NOT DO THIS QUESTION ON THE PYTHON INTERPRETER 
#Using the escape character, create a single-quoted-surrounded string with five characters 
#--> a newline, a tab, two double quotes and then a single quote. The order doesn't matter.  
#Now display this string


print('\n\t""\'')