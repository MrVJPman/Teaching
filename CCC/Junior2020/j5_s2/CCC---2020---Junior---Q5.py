#2020 Junior Q5

def get_all_possible_coordinates_of_number(number, M, N, visited_coordinates):
    coordinates_list_of_number = []
#    print(number)
    for index in range(1, number+1 // 2):
        if (number % index == 0):
#            print(list(set(coordinates_list_of_number)))
            if (index - 1) < M and (number // index) - 1 < N:
#                print("index - 1", index - 1)
#                print("M", M)
                new_coordinate = (index - 1, (number // index) - 1)
                coordinates_list_of_number.append(new_coordinate)                
            if (index - 1) < N and (number // index) - 1 < M:
                new_coordinate = ((number // index) - 1, index - 1)
                coordinates_list_of_number.append(new_coordinate)
 #   print(list(set(coordinates_list_of_number)))
    return list(set(coordinates_list_of_number))
    

def CCC_2020_Question_5(input_string):
    #this will always be here strip()
    lines = input_string.strip().split("\n") 
    #strip : to remove last newline
    #split : to divide into individual lines
    
    #Your Solution Starts Here
    
    M = int(lines[0])
    N = int(lines[1])
    coordinates_values_list = [row.split() for row in lines[2:] ]
    #print(coordinates_values_list)
    
    
    coordinates_values_dict = {}
    values_coordinates_dict = {}
    for row in range(M):
        for value in range(N):
            cell_number = int(lines[row+2].split()[value])
            coordinates_values_dict[(row,value)] = cell_number
            if cell_number not in values_coordinates_dict:
                values_coordinates_dict[cell_number] = [(row,value)]
            else:
                values_coordinates_dict[cell_number].append((row,value))
            
#    print(coordinates_values_dict)


    #for row_of_list in coordinates_values_list:
        #for index in range(int(N)):
            #row_of_list[index] = int(row_of_list[index])
#    print(coordinates_values_list)
    
    visited_coordinates = [(0, 0)]
    coordiates_to_check_queue = [(0, 0)]
    
    while coordiates_to_check_queue != []:
        coordinate_to_check = coordiates_to_check_queue.pop(0)
#        print(coordinate_to_check)
        if coordinate_to_check == (M-1, N-1):
            return("yes")
        cc_x = coordinate_to_check[0]
        cc_y = coordinate_to_check[1]
        for potential_coordinate in get_all_possible_coordinates_of_number(coordinates_values_dict[(cc_x, cc_y)], M, N, visited_coordinates):
            if potential_coordinate in visited_coordinates:
                continue
            else: 
                coordiates_to_check_queue.append(potential_coordinate)
                visited_coordinates.append(potential_coordinate)

#            if coordinates_values_dict[(cc_x, cc_y)] == (potential_coordinate[0] + 1) * (potential_coordinate[1] + 1):
    return ("no")

'''        for row in range(M):
            for value in range(N):
                if (row, value) in visited_coordinates:
                    continue
                if coordinates_values_list[cc_x][cc_y] == (row+1)*(value+1) :
#                    print(coordinates_values_list[cc_x][cc_y])
                    new_coordinate = (row, value)
                    coordiates_to_check_queue.append(new_coordinate)
                    visited_coordinates.append(new_coordinate)
#                    print("new_coordinate", new_coordinate)'''
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
#        print(input_string)
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