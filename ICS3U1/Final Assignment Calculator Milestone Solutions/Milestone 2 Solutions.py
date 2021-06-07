#Mr Kong's Solution to milestone 2

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

from decimal import *

def multiply_float(number1, number2):
  shifts = 0
  while number1 % 1 != 0:
    number1 = number1 * 10
    shifts = shifts + 1
  while number2 % 1 != 0:
    number2 = number2 * 10
    shifts = shifts + 1
  shifted_product = multiply(int(number1), int(number2))
  unshifted_product = shifted_product * 10 ** - shifts
  return unshifted_product

assert(multiply_float(400.005, 0.1) == 40.0005) 
assert(multiply_float(12.5, 0.5) == 6.25) 
assert(multiply_float(0.5, 0.5) == 0.25) 
assert(multiply_float(0.1, 0.05) == 0.005) 
assert(multiply_float(3.3, 3.3) == 10.89) 


#Factorial : repeatedly calls multiply
def factorial(number):
  if number < 0:
    raise Exception("Factorial can only accept positive values")
  else:
    product = 1
    index = 1
    while index < number + 1: 
      product = multiply(product, index)
      index = index + 1
    return product

assert(factorial(0)==1)
assert(factorial(1)==1)
assert(factorial(2)==2)
assert(factorial(3)==6)
assert(factorial(4)==24)
assert(factorial(5)==120)
assert(factorial(10)==3628800)

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

def divide_float(number1, number2):
  extra_shifts_later = max(len(str(number1)), len(str(number2)))
  shifts = 0
  while number1 % 1 != 0 or number2 % 1 != 0:
    number1 = number1 * 10
    number2 = number2 * 10
  #print(number1, number2)
  #This is to make sure the shifted number 1 is bigger than number 2
  shifts = shifts + extra_shifts_later
  number1 = number1 * 10 ** extra_shifts_later
  shifted_quotient = divide(int(number1), int(number2))
  while shifts > 0 :
    shifted_quotient = shifted_quotient / 10 
    shifts = shifts - 1
  #print(round(shifted_quotient, extra_shifts_later))
  return round(shifted_quotient, extra_shifts_later)

assert(divide_float(1.5, 1.0)==1.5)
assert(divide_float(5.0, 3.0)==1.666)
assert(divide_float(0.5, 0.5)==1.0)
assert(divide_float(1.0, 0.7)==1.428)
assert(divide_float(1.0, 0.5)==2.0)
assert(divide_float(5.5, 1.1)==5)

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


def add_to_or_replace_memory(list_of_strs, list_of_values, new_memory_name, value):
  if not new_memory_name in list_of_strs:
    list_of_strs.append(new_memory_name)
    list_of_values.append(value)
  else:
    index_of_memory = list_of_strs.index(new_memory_name)
    list_of_values[index_of_memory] = value

def retrieve_from_memory(list_of_strs, list_of_values, memory):
  if memory not in list_of_strs:
    raise NameError("Attempted to use uninitialized memory")
  index_of_memory = list_of_strs.index(memory)
  return list_of_values[index_of_memory] 

#**********************************************
#START TEST : reset memory_string and memory_values after testing
memory_strings = []
memory_values = []
#Test #1
add_to_or_replace_memory(memory_strings, memory_values, "m", 5)
assert(memory_strings == ["m"] and memory_values == [5])
assert(retrieve_from_memory(memory_strings, memory_values, "m") == 5)

#Test #2
add_to_or_replace_memory(memory_strings, memory_values, "m", 3)
assert(memory_strings == ["m"] and memory_values == [3])
assert(retrieve_from_memory(memory_strings, memory_values, "m") == 3)

#Test #3
add_to_or_replace_memory(memory_strings, memory_values, "c", 4)
assert(memory_strings == ["m", "c"] and memory_values == [3, 4])
assert(retrieve_from_memory(memory_strings, memory_values, "m") == 3)
assert(retrieve_from_memory(memory_strings, memory_values, "c") == 4)


memory_strings = []
memory_values = []
#END TEST : reset memory_string and memory_values after testing
#**********************************************

import traceback

while True :
  try: 
    expression = input("Enter a mathematial expresson to calculate: ")
   
    #Handling memory add and replace a memory whenever needed
    if expression.count("=") > 1:
      raise ValueError("Only one memory added/replaced are allowed at a time")
    elif "=" in expression: 
      equal_sign_index = expression.index("=")
      memory_name = expression[:equal_sign_index]
      memory_value = float(expression[equal_sign_index+1:])
      #Ensures memory can only have letters
      for letter in memory_name:
          if not letter.isalpha():
            raise ValueError("Memory may only have letters")
      add_to_or_replace_memory(memory_strings, memory_values, memory_name, memory_value)
      print("Status of memory strings are", memory_strings )
      print("Status of memory values are", memory_values )
      continue

    #Handling all absolute values
    if (expression.count("|") % 2 == 1):
      raise ArithmeticError("Invalid input for absolute values!")
    while expression.count("|") > 0 :
      first_vertical_line_index = expression.find("|")
      second_vertical_line_index = expression.find("|",  first_vertical_line_index+1)
      absolute_section = expression[first_vertical_line_index:second_vertical_line_index+1]
      new_value = absolute(float(expression[first_vertical_line_index+1:second_vertical_line_index])) 
      expression = expression.replace(absolute_section, str(new_value))
    print("Expression after handling all absolutes", expression)   

    #Handling the five operations 
    while "+" in expression or "-" in expression or "*" in expression or "/" in expression or "%" in expression:
      operator_index = 0
      while expression[operator_index] not in ["+", "-", "*", "/", "%"]:
        operator_index = operator_index + 1
      next_operator_index = operator_index + 1
      while next_operator_index < len(expression) and expression[next_operator_index] not in ["+", "-", "*", "/", "%"] :
        next_operator_index = next_operator_index + 1
      first_value = expression[:operator_index]
      second_value = expression[operator_index+1:next_operator_index]

      #Handling Memory Retrieval
      if first_value.isalpha():
         first_float = retrieve_from_memory(memory_strings, memory_values, first_value)
      else:
         first_float = float(first_value)
      if second_value.isalpha():
         second_float = retrieve_from_memory(memory_strings, memory_values, second_value)
      else:
         second_float = float(second_value)

     #Handling each of the five operations
      if expression[operator_index] == "+":
        result = add(first_float, second_float)
      elif expression[operator_index] == "+":
        result = subtract(first_float, second_float)
      elif expression[operator_index] == "*":
        result = multiply_float(first_float, second_float)
      elif expression[operator_index] == "/":
        result = divide_float(first_float, second_float)
      elif expression[operator_index] == "%":
        result = mod(first_float, second_float)
      expression = expression.replace(expression[:next_operator_index], str(result))
      print("See the step-by-step change in expression" , expression)

    
  except ZeroDivisionError as err: 
    print(err)
    print(traceback.format_exc()) 
  except NameError as err:
    print(err)
    print(traceback.format_exc())
  except ValueError as err:
    print(err)
    print(traceback.format_exc())
  except ArithmeticError as err:
    print(err)
    print(traceback.format_exc())
    expression = input("Continue calculation? Press N to exit")
    if expression == "N":
      print("Exited!")
      break
