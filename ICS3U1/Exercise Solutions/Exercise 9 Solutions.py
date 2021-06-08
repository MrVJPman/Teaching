#Question 1)

#https://www.w3schools.com/python/exercise.asp?filename=exercise_strings1

#Do exercise 1-8 for Strings. Show screenshot when you’re done.

#Question 2)

#https://www.w3schools.com/python/exercise.asp?filename=exercise_lists1

#Do exercise 1-8 for Lists. Show screenshot when you’re done.

#Question 3)

example_list = [5, 4, 3, 2, 1]
L = example_list
L[2] = None
print(example_list)
print(L)
#See Slide 6-7.
#Write code to change 3 to None without using the variable example_list. See Slide 2, 6-7.

#Question 4)
example_list = [5, 4, 3, 2, 1]
example_list2 = example_list[:]
example_list2[0] = None
example_list2[1] = None
example_list2[2] = None
example_list2[3] = None
example_list2[4] = None
print(example_list)
print(example_list2)

#See Slide 2, 6-7.
#Create a new list into a variable example_list2 from example_list
#Now change every example_list2’s value into None
#Verify example_list and example_list2 are different using print twice
