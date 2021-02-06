#2020 Junior Q5

def get_all_possible_coordinates_of_number(number, M, N):
    coordinates_list_of_number = []
    index = 0
    while index * index <= number:
        index += 1
        if number % index == 0 :
            if (index - 1) == ((number // index) - 1) and (index - 1) < M and (index - 1) < N:
                coordinates_list_of_number.append( ((index - 1), (number // index) - 1))      
                continue
            if (index - 1) < M and (number // index) - 1 < N:
                new_coordinate = (index - 1, (number // index) - 1)
                coordinates_list_of_number.append(new_coordinate)                
            if (number // index) - 1 < M and (index - 1) < N :
                new_coordinate = ((number // index) - 1, index - 1)
                coordinates_list_of_number.append(new_coordinate)
    return coordinates_list_of_number
    

def CCC_2020_Question_5(input_string):
    #this will always be here strip()
    lines = input_string.strip().split("\n") 
    #strip : to remove last newline
    #split : to divide into individual lines
    
    #Your Solution Starts Here
    
    M = int(lines[0])
    N = int(lines[1])
    
    coordinates_values_dict = {}
    values_coordinates_dict = {}
    for row in range(M):
        for value in range(N):
            coordinates_values_dict[(row,value)] = int(lines[row+2].split()[value])
            
#    print(coordinates_values_dict)
    
    visited_coordinates = [(0, 0)]
    coordiates_to_check_queue = [(0, 0)]
    
    while coordiates_to_check_queue != []:
        coordinate_to_check = coordiates_to_check_queue.pop(0)
        if coordinate_to_check == (M-1, N-1):
            return("yes")
        cc_x = coordinate_to_check[0]
        cc_y = coordinate_to_check[1]
        for potential_coordinate in get_all_possible_coordinates_of_number(coordinates_values_dict[(cc_x, cc_y)], M, N):
            if potential_coordinate in visited_coordinates:
                continue
            else: 
                coordiates_to_check_queue.append(potential_coordinate)
                visited_coordinates.append(potential_coordinate)
    return ("no")
    #return str(None) #This is here by default. Don't forget to comment this
    #Your Solution Ends Here



#=======================

import os 

all_input_file_contents = {}
all_output_file_contents = {}
for filename in os.listdir("."):
    if "in" in filename:
        opened_file = open(filename)
        opened_file_contents = opened_file.read()
        all_input_file_contents[filename] = opened_file_contents
    elif "out" in filename:
        opened_file = open(filename)
        opened_file_contents = opened_file.read()
        all_output_file_contents[filename] = opened_file_contents

#print(all_input_file_contents)
#print(all_output_file_contents)

combined_file_contents = {}
for content in all_input_file_contents:
    combined_file_contents[content[:-3]] = [all_input_file_contents[content], all_output_file_contents[content[:-3]+".out"]]
#print(combined_file_contents)

#test_dict structure
#key is test case name
#value list item 0 is inputs
#value list item 1 is outputs
#{'s2.1': ['1\n1\n327707\n928587\n', '928587\n']}
def run_all_test_cases(test_dict):
    for testcase in test_dict:
        print("--------------------TEST CASE: ", testcase, "--------------------")
        input_string = combined_file_contents[testcase][0]
        print("----------Input:  ")
        #print(input_string)
        received_output = CCC_2020_Question_5(input_string) #CHANGE NAME OF THIS FUNCTION
        expected_output = combined_file_contents[testcase][1].strip()       
        print("----------Expected: ")
        print(expected_output)
        print("----------Received: ")
        print(received_output)
        assert(expected_output == received_output)
        print("\n")
    print("CONGRATULATIONS!!! ALL TEST CASES PASS!")

#Comment this as needed
run_all_test_cases(combined_file_contents)


print("ENTER inputs")
user_input_string = ""
#START : change everything here to take inputs
N = input()
M = input()
user_input_string += N + "\n" + M + "\n" 
for index in range(int(N)):
    user_input_string += input() + "\n"    
#END : change everything here to take inputs
print("user_input string:")
print(user_input_string)
print("result: ")
print(CCC_2020_Question_5(user_input_string)) #CHANGE NAME OF THIS FUNCTION