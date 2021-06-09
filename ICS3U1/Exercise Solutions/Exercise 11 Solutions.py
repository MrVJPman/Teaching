#Question 1) https://www.w3schools.com/python/exercise.asp?filename=exercise_ifelse1

#Do Exercise 1-9

#Question 2) Read this : https://www.w3schools.com/python/ref_random_randint.asp
#This code randomly picks a card from Ten to Ace for you.
#It has some errors, fix the errors.



import random
card = random.randint(10, 14) #randomly picks a number from 10 to 14

print(card)

#if card >= 10: print("Ten")
#if card >= 11: print("Jack")
#if card >= 12: print("Queen")
#if card >= 13: print("King")
#if card != 14: print("Ace")

if card == 10: print("Ten")
if card == 11: print("Jack")
if card == 12: print("Queen")
if card == 13: print("King")
if card == 14: print("Ace")

#Question 3)
#Copy the fixed code from question 2 and replace it with a right number of elif statements

import random
card = random.randint(10, 14) #randomly picks a number from 10 to 14

if card == 10: print("Ten")
elif card == 11: print("Jack")
elif card == 12: print("Queen")
elif card == 13: print("King")
elif card == 14: print("Ace")

#Question 4)
#Copy the fixed code from question 3 and replace it with a right number of else statements

import random
card = random.randint(10, 14) #randomly picks a number from 10 to 14
if card == 10: print("Ten")
elif card == 11: print("Jack")
elif card == 12: print("Queen")
elif card == 13: print("King")
else: print("Ace")
#