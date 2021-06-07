#Mr Kong's Solution to milestone 1


#Addition
def add(number_1, number_2):
  return number_1 + number_2

assert(add(0, 0)==0)
assert(add(1, 2)==3)
assert(add(999,-99)==900)

#Subtraction
def subtract(number_1, number_2):
  return number_1 - number_2

assert(subtract(0, 0)==0)
assert(subtract(2, 1)==1)
assert(subtract(0,5)==-5)

#Absolute
def absolute(number):
  if number < 0:
    return -number
  return number 

assert(absolute(5)==5)
assert(absolute(-5)==5)
assert(absolute(0)==0)

#Multiplication
def multiply(number_1, number_2):
  if number_1 == 0 or number_2 == 0:
    return 0
  else:
    if number_1 < 0 and number_2 < 0:
      number_1 = -number_1 
      number_2 = -number_2 
    elif number_1 < 0 or number_2 < 0:
      number_1 = absolute(number_1)
      number_2 = absolute(number_2)
      sum = 0
      for index in range(number_2):
        sum = sum + number_1
      return -sum
    sum = 0
    for index in range(number_2):
      sum = sum + number_1
    return sum

assert(multiply(1, 5)==5)
assert(multiply(5, 5)==25)
assert(multiply(5, 1)==5)
assert(multiply(-5, 1)==-5)
assert(multiply(5, -1)==-5)

#Division
def divide(number_1, number_2):
  if number_2 == 0:
    raise ZeroDivisionError("2nd number can't be 0")
  quotient = 0
  while number_1 >= number_2:
     number_1 = number_1 - number_2
     quotient = quotient + 1
  return quotient    

assert(divide(25, 5)==5)
assert(divide(25, 1)==25)
assert(divide(5, 1)==5)
assert(divide(10, 3)==3)

#Mod
def mod(number_1, number_2):
  if number_2 == 0:
    raise ZeroDivisionError("2nd number can't be 0")
  while number_1 >= number_2:
     number_1 = number_1 - number_2
  return number_1  

assert(mod(5, 1)==0)
assert(mod(10, 3)==1)
assert(mod(40, 21)==19)


#START : NEW CODE FROM NOVEMBER 20, 2020
#**********************************************
memory_strings = []
memory_values = []
#Milestone 2 function:
def add_to_or_replace_memory(list_of_strs, list_of_values, new_memory_name, value):
  #For you to implement
  pass
def retrieve_from_memory(list_of_strs, list_of_values, memory):
  #For you to implement
  #There will be an raised Exception in here for certain
  value = 0 #Change this
  return 5

add_to_or_replace_memory(memory_strings, memory_values, "m", 5)
memory_strings = ["m"] #your add_to_or_replace_memory should change this list. Delete this line later on
memory_values = [5] #your add_to_or_replace_memory should change this list. Delete this line later on
assert(memory_strings == ["m"] and memory_values == [5])
assert(retrieve_from_memory(memory_strings, memory_values, "m") == 5)
#reset memory_string and memory_values after testing
memory_strings = []
memory_values = []
#END : NEW CODE FROM NOVEMBER 20, 2020
#**********************************************



memory_value = ""
while True :
  try: 
    expression = input("Enter an mathematial expresson to calculate: ")
    
    #Handling memory value
    if "m=" in expression:
      memory_value = expression[2:]
      continue
    elif "m" in expression:
      if (memory_value == ""):
        raise NameError("Memory has no values yet")
      else: 
        expression = expression.replace("m", memory_value)
    
    if "+" in expression:
      operator_index = expression.index("+")
      print(add(int(expression[:operator_index]), int(expression[operator_index+1])))
    elif "-" in expression:
      operator_index = expression.index("-")
      print(subtract(int(expression[:operator_index]), int(expression[operator_index+1])))
    elif "*" in expression:
      operator_index = expression.index("*")
      print(multiply(int(expression[:operator_index]), int(expression[operator_index+1])))
    elif "/" in expression:
      operator_index = expression.index("/")
      print(divide(int(expression[:operator_index]), int(expression[operator_indexx+1])))
    elif "%" in expression:
      operator_index = expression.index("%")
      print(divide(int(expression[:operator_index]), int(expression[operator_index+1])))
    elif expression.count("|") == 2:
      left_index = expression.find("|")
      right_index = expression.rfind("|")
      print(absolute(int(expression[left_index+1:right_index])))
    else:
      raise ArithmeticError("Invalid input!")
  except ZeroDivisionError as err: 
    print(err)
  except NameError as err:
    print(err)
  except ArithmeticError as err:
    print(err)
    expression = input("Continue calculation? Press N to exit")
    if expression == "N":
      print("Exited!")
      break
