#Hint for both questions : go back to your previous homework solutions and may be some of them still have unresolved compile/runtime #errors


#To confirm you should run the code and comment/uncomment as needed

#Question 1)

#Create three different faulty Python code that has three different sources of compile-errors

Compile Error #1 : Missing double quotes

#new_string = "abc'

#Compile Error #2: #forces an indentation error
 
  print("indentation error") 

#Compile Error #3

L = [1, 2 ) #Syntax Error : Improper brackets

#Question 2) 

#Create three different faulty Python code that has three different sources of runtime-errors

#Runtime error #1 : adding two different types. TypeError
new = "123" + 1

#Runtime error #2 : accessing values that doesn't exist. IndexError
L = [1, 2, 3]
L[4]

#Runtime error #3 : conversion error.  ValueError

abc = "abc"
int(abc)
