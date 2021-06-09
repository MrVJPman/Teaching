#Question 1)

#https://www.w3schools.com/python/exercise.asp?#filename=exercise_for_loops1

#Do Exercise 1 

#Question 2)
#Using a for loop, and with + or .append(), update or replace name_as_integers_list into a list containing all ascii-translated integers representing your first name. 
#example. “bob” will become [98, 111, 98]

name_as_integers_list = []
name="bob"

for character in name:
  name_as_integers_list.append(ord(character))

print(name_as_integers_list)

#hint : 
#you will need this code -> name_as_integers_list.append(???)
#or this code -> name_as_integers_list = name_as_integers_list + ???

#Question 3)
#Using the list from question 2 and then another for loop, convert the integers back into letters and print them one character at a time

for letter in name_as_integers_list:
  print(chr(letter))


#Question 4)
#Repeat question 3. However, merge the letters using one string then display it all at once.
#Hint : create a variable with value of empty string at the start. Then in the for loop, replace it with each new letter/character one by one to get the full name.

name=""
for letter in name_as_integers_list:
  name = name + chr(letter)

print(name)
