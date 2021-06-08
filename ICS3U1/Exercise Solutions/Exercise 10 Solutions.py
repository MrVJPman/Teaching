#Question 1) Create an if statement that has
#i) no indentation
#ii) print out “Hi my name is ”
#iii) Use .format() to write out your first name

first_name = "Bob"
if True:print("Hi my name is {}".format(first_name))

#Question 2) Create an if statement with indentation that always displays “Hello Mr.Kong”

if True:
  print("Hello Mr.Kong")


#Question 3) Create an if statement with indentation that never displays “Goodbye Mr.Kong”

if False:
  print("Goodbye Mr.Kong")

#Question 4) Create an if statement with indentation that has two print statements belonging to the if statement and two print statements that doesn’t and is outside of it. Both must be below the if statement

if True:
  print("Inside #1")
  print("Inside #2")
print("Outside #1")
print("Outside #2")


#Question 5) Create an if statement with indentation that has a pass 

if True:
  pass

#Question 6) Create an if statement with indentation that has nothing in it that should produce an error

if True:
  #Error