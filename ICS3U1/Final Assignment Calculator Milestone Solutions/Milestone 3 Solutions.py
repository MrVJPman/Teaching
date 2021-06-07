import math
#=======================================================

#Mr Kong's Solution to milestone 3

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
      #updated code
      if number_2 > number_1:
        for index in range(number_1):
          sum = sum + number_2
        return -sum 
      #updated code
      for index in range(number_2):
        sum = sum + number_1
      return -sum
    sum = 0
    #updated code
    if number_2 > number_1:
      for index in range(number_1):
        sum = sum + number_2
      return sum 
    #updated code
    for index in range(number_2):
      sum = sum + number_1
    return sum

assert(multiply(1, 5)==5)
assert(multiply(5, 5)==25)
assert(multiply(5, 1)==5)
assert(multiply(-5, 1)==-5)
assert(multiply(5, -1)==-5)

def multiply_float(number1, number2):
  shifts = 0
  while number1 % 1 != 0:
    number1 = number1 * 10
    shifts = shifts + 1
  while number2 % 1 != 0:
    number2 = number2 * 10
    shifts = shifts + 1
#  print(number1, number2)
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
    raise ValueError("Factorial can only accept positive values")
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

#square root
def square_root(number):
  if number < 0:
    raise ValueError("Square root can only accept positive values")
  if number == 0:
#  print(number)
    return 0 
  a = float(number) 
  index = 1 
  previous_number = 0.0
  while str(number) != str(previous_number):
    previous_number = number
    number = multiply_float(0.5, (number + a / number)) 
    index += 1
#  print(number)
  return number

assert(square_root(0)==0.0)
assert(square_root(1)==1.0)
assert(square_root(100)==10)
assert(square_root(50)==7.0710678118654755)

#power
def power(base, exponent):
  if base == 0 and exponent < 0:
    raise ZeroDivisionError("Exponent can not be lesser than 0 when base is 0")
  elif exponent == 0.5:
    return square_root(base)
  elif exponent == -0.5:
    return 1 / square_root(base)
  elif exponent != int(exponent):
    raise ValueError("Exponent cannot be float aside from 0.5")
  exponent = int(exponent)
  power_value = 1
  for index in range(absolute(exponent)):
    power_value = power_value * base
 
  if exponent < 0:
    return 1 / power_value
  else:
    return power_value  
    
assert(power(2, 3)==8)
assert(power(2, 0)==1)
assert(power(2, -3)==1/8)
assert(power(0, 0)==1)


def log(base, exponent):
  if base <= 1:
    raise ArithmeticError("Base of log cannot be less than 1")
  elif exponent <= 0:
    raise ArithmeticError("Logarithms ")


#Getting exact value of e
def e_value():
  e = 0
  index = 1 
  previous_e = 0.0
  while str(e) != str(previous_e):
    previous_e = e
    e += (1 / factorial(index- 1))
    index += 1
  return e
assert(e_value() == 2.7182818284590455)

#Use Leibniz formula for pi
def pi_value():
  pi = 0.0
  index = 0
  while str(pi)[:6] != str("3.1415"):
    pi += 8  / ((4 * index + 1) * (4 * index + 3))
    index += 1
  return float(str(pi)[:6])
assert(pi_value() == 3.1415)


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
    while "|" in expression:
      first_vertical_line_index = expression.find("|")
      second_vertical_line_index = expression.find("|",  first_vertical_line_index+1)
      absolute_section = expression[first_vertical_line_index:second_vertical_line_index+1]
      
      if expression[first_vertical_line_index+1] == "~":
        new_value = absolute(-float(expression[first_vertical_line_index+2:second_vertical_line_index])) 
      else:
        new_value = absolute(float(expression[first_vertical_line_index+1:second_vertical_line_index])) 
      expression = expression.replace(absolute_section, str(new_value))
      print("Expression after handling one absolute", expression)   
    
    while "!" in expression:
      #looks for where ! is located
      factorial_index  = expression.find("!")
      #looks for where the start is or the first operator
      previous_operator_index = factorial_index 
      while previous_operator_index >= 0 and expression[previous_operator_index] not in ["^", "*", "/", "%", "+", "-"]:
        previous_operator_index = previous_operator_index - 1
      
      factorial_section = expression[previous_operator_index+1:factorial_index+1]
      #check if the number is positive/negative
      if expression[previous_operator_index + 1] == "~":
        factorialized_value = factorial(-int(expression[previous_operator_index+2: factorial_index]))
      else:
        factorialized_value = factorial(int(expression[previous_operator_index+1: factorial_index]))
      #replace factorial with the actual number
      expression = expression.replace( factorial_section, str(factorialized_value))
      print("Expression after handling one factorial", expression)   

    #Handling the power operation
    while "^" in expression:
      power_index = expression.find("^")
      
      first_number_index = power_index - 1
      while first_number_index >= 0 and expression[first_number_index] not in ["^", "*", "/", "%", "+", "-"]:
        first_number_index = first_number_index - 1
      second_number_index = power_index + 1
      
      while second_number_index < len(expression) and expression[second_number_index] not in ["^", "*", "/", "%", "+","-"]:
        second_number_index = second_number_index + 1

      power_section = expression[first_number_index+1:second_number_index]
      
      if expression[first_number_index] == "~":
        first_number = -float(expression[first_number_index+2:power_index])
      else:
        first_number = float(expression[first_number_index+1:power_index])

      if expression[power_index + 1] == "~":
        second_number = -float(expression[power_index+2:second_number_index])
      else:
        second_number = float(expression[power_index+1:second_number_index])

      powered_value = power(first_number, second_number)
      if expression[first_number_index] == "~":
        expression = expression.replace( power_section, "~" + str(powered_value))
      else:
        expression = expression.replace( power_section, str(powered_value))
      print("Expression after handling one power", expression)   

    while "*" in expression or "/" in expression or "%" in expression:
      #Looks for the first *, / or %
      operator_index = 0
      for letter in expression:
        if letter in ["*", "/", "%"]:
          break
        else:
          operator_index = operator_index + 1
      #looks for where the first number is 
      first_number_index = operator_index - 1
      while first_number_index >= 0 and expression[first_number_index] not in ["*", "/", "%", "+", "-"]:
        first_number_index = first_number_index - 1

      #looks for where the second number is        
      second_number_index = operator_index + 1        
      while second_number_index < len(expression) and expression[second_number_index] not in ["*", "/", "%", "+","-"]:
        second_number_index = second_number_index + 1

      mdm_section = expression[first_number_index+1:second_number_index]
  #    print(mdm_section)
       
      #gets both numbers 
      if expression[first_number_index] == "~":
        first_number = -float(expression[first_number_index+2:operator_index])
      else:
        first_number = float(expression[first_number_index+1:operator_index])

      if expression[operator_index + 1] == "~":
        second_number = -float(expression[operator_index+2:second_number_index])
      else:
        second_number = float(expression[operator_index+1:second_number_index])

      #Calculate the value 
      if expression[operator_index] == "*":          
        calculated_mdm_value = multiply_float(first_number, second_number)
      elif expression[operator_index] == "/":          
        calculated_mdm_value = divide_float(first_number, second_number)
      elif expression[operator_index] == "%":          
        calculated_mdm_value = mod(first_number, second_number)
      
      #Replace expression with the value 
      if expression[first_number_index] == "~":
        expression = expression.replace(mdm_section, "~" + str(calculated_mdm_value))
      else:
        expression = expression.replace(mdm_section, str(calculated_mdm_value))

      print("Expression after handling one multiply/divide/mod", expression)   


    while "+" in expression or "-" in expression :
      #Looks for the first *, / or %
      operator_index = 0
      for letter in expression:
        if letter in ["+", "-"]:
          break
        else:
          operator_index = operator_index + 1
      #looks for where the first number is 
      first_number_index = operator_index - 1
      while first_number_index >= 0 and expression[first_number_index] not in ["+", "-"]:
        first_number_index = first_number_index - 1

      #looks for where the second number is        
      second_number_index = operator_index + 1        
      while second_number_index < len(expression) and expression[second_number_index] not in ["+","-"]:
        second_number_index = second_number_index + 1

      as_section = expression[first_number_index+1:second_number_index]
#      print(as_section)
       
      #gets both numbers 
      if expression[first_number_index] == "~":
        first_number = -float(expression[first_number_index+2:operator_index])
      else:
        first_number = float(expression[first_number_index+1:operator_index])

      if expression[operator_index + 1] == "~":
        second_number = -float(expression[operator_index+2:second_number_index])
      else:
        second_number = float(expression[operator_index+1:second_number_index])

      #Calculate the value 
      if expression[operator_index] == "+":          
        calculated_as_value = add(first_number, second_number)
      elif expression[operator_index] == "-":          
        calculated_as_value = subtract(first_number, second_number)
      
      #Replace expression with the value 
      if expression[first_number_index] == "~":
        expression = expression.replace(as_section, "~" + str(calculated_as_value))
      else:
        expression = expression.replace(as_section, str(calculated_as_value))

      print("Expression after handling one add/subtract", expression)   

    print("Final expression", expression)       
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

