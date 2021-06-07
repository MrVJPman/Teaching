#Questions Source 
#https://docs.google.com/document/d/1-WQhkeOrW2pnnB2_jMIk6nNovlDekuyyE30zZRQ171k/edit?usp=sharing


#Question 1
def not_same(data_structure_one, data_structure_two):
    if len(data_structure_one) > len (data_structure_two) or len(data_structure_one) < len (data_structure_one):
        return True
    else: #When they're same length
        index = 0
        while data_structure_one[index] > data_structure_two[index] or data_structure_one[index] < data_structure_two[index] and index < len(data_structure_one) - 1:
            index = index + 1
        return index == len(data_structure_one) - 1

assert(not_same("abc", "def")==True)
assert(not_same("abc", "abc")==False)
assert(not_same([1, 2, 3, 4], [1, 2, 3, 4])==False)

#Question 2a
def decimal_to_binary(decimal_number):
    number = decimal_number
    binary_number = ''
    while number != 0:
      binary_number = str(number % 2) + binary_number
      number = number // 2
    return int(binary_number)

assert(decimal_to_binary(132) == 10000100)
assert(decimal_to_binary(255) == 11111111)

#Question 2b
def binary_to_decimal(binary_number):
    index = -1
    decimal_number = 0
    binary_number = str(binary_number)
    while index >= -len(binary_number):
      decimal_number = decimal_number + (2 ** (abs(index) - 1)) * int(binary_number[index])
      index = index - 1
    return decimal_number

assert(binary_to_decimal(0)==0)
assert(binary_to_decimal(1)==1)
assert(binary_to_decimal(10)==2)
assert(binary_to_decimal(11)==3)
assert(binary_to_decimal(100)==4)
assert(binary_to_decimal(1000)==8)

#Question 3

def digit_to_sum(input_integer):
    number = input_integer
    total = 0
    while number > 0:
      total = total + number % 10
      number = number // 10
    return total

assert(digit_to_sum(123)==6)
assert(digit_to_sum(100)==1)
assert(digit_to_sum(1555)==16)
assert(digit_to_sum(2555)==17)

#Question 4

def question_four():
    first_three_list = input("Enter three numbers, separated by space").split()
    second_three_list = input("Enter another three numbers, separated by space").split()
    third_three_list = input("Enter final three numbers, separated by space").split()
  
  
    for index in range(3):
      first_three_list[index] = int(first_three_list[index])
      second_three_list[index] = int(second_three_list[index])
      third_three_list[index] = int(third_three_list[index])
    if sum(first_three_list) == sum(second_three_list) == sum(third_three_list):
      column_one_sum = first_three_list[0] + second_three_list[0] + third_three_list[0]
      column_two_sum = first_three_list[1] + second_three_list[1] + third_three_list[1]
      column_three_sum = first_three_list[2] + second_three_list[2] + third_three_list[2]
      if column_one_sum == column_two_sum == column_three_sum:
        diagonal_one_sum =  first_three_list[0] + second_three_list[1] + third_three_list[2]
        diagonal_two_sum = first_three_list[2] + second_three_list[1] + third_three_list[0]
        print(diagonal_one_sum == diagonal_two_sum)
      else:
        print(False)
    else: 
      print(False)

#question_four()

#Question 5

def question_five():
    N = int(input("Enter value of N: "))
    new_str = ""
    for index in range(N):
        character = input("Enter character: ") 
        number_of_characters = int(input("Enter number of characters: "))
        new_str = new_str + (character * number_of_characters) + "\n"
    print(new_str[:-1])
#question_five()

#Question 6

def question_six():
    N = int(input("Enter value of N: "))
    total_string = ""
    for index in range(N):
        characters = input("Enter characters: ") 
        characters_copy = characters
    new_str = ""
    while characters_copy != "":
        new_str = new_str + str(characters_copy.count(characters_copy[0])) + " "
        characters_copy = characters_copy.replace(characters_copy[0], "", characters_copy.count(characters_copy[0]))
    total_string = total_string + new_str + "\n"

    characters_copy = characters
    new_str = ""
    while characters_copy != "":
        new_str = new_str + characters_copy[0] + " "
        characters_copy = characters_copy.replace(characters_copy[0], "", characters_copy.count(characters_copy[0]))
    total_string = total_string + new_str + "\n"
    print(total_string[:-1])
#question_six()
