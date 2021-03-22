def CCC_2018_Junior_Question_3(input_string):
    #this will always be here strip()
    lines = input_string.strip().split("\n") 
    #strip : to remove last newline
    #split : to divide into individual lines


    #Your Solution Starts Here 
    solution_string = None    
    solution_string = ""
    number_of_data_lines = int(lines[0])
    data = []
    for line in lines[1:]:
        data_line = line.split()
        for index in range(len(data_line)):
            data_line[index] = int(data_line[index])
        data.append(data_line)    
        
    if data[0][0] > data[0][1] and data[0][0] < data[1][0] : #90 degrees to the right
        print_index = list(range(number_of_data_lines))
        print_index.reverse()
        for index in print_index:
            new_str = ""
            for row in data:
                new_str += str(row[index]) + " "            
            solution_string += new_str.strip() + "\n"
    elif data[0][0] < data[0][1] and data[0][0] > data[1][0]: #90 degrees to the left
        data.reverse()
        for index in range(number_of_data_lines):
            new_str = ""
            for row in data:
                new_str += str(row[index]) + " "            
            solution_string += new_str.strip() + "\n"
    elif data[0][0] > data[0][1] and data[0][0] > data[1][0]: #180 degrees turn
        data.reverse()
        print_index = list(range(number_of_data_lines))
        print_index.reverse()
        for row in data:
            new_str = ""
            for index in print_index:
                new_str += str(row[index]) + " "            
            solution_string += new_str.strip() + "\n"
    else: #data[0][0] < data[0][1] and data[0][0] < data[1][0] Everything is fine, no rotations
        for row in data:
            new_str = ""
            for value in row:
                new_str += str(value) + " "
            solution_string += new_str.strip() + "\n"  
    #Your Solution Ends Here
    return str(solution_string.strip()) 


#============================START : READ .in and .out file contents============================
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


#============================END : READ .in and .out file contents============================


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
        print(input_string)
        received_output = CCC_2018_Junior_Question_3(input_string) #CHANGE NAME OF THIS FUNCTION
        expected_output = combined_file_contents[testcase][1].strip()       
        print("----------Expected: ")
        print(expected_output)
        print("----------Received: ")
        print(received_output)
        assert(expected_output == received_output)
        print("\n")
    print("CONGRATULATIONS!!! ALL TEST CASES PASS!")

#Comment/uncomment this as needed
run_all_test_cases(combined_file_contents)

#This section is where you implement user input handling
print("MANUALLY ENTER TEST CASES HERE")
print("Enter inputs:")
user_input_string = ""
#START : insert your user input handling code below
number_of_data_lines_as_str = input()
user_input_string = number_of_data_lines_as_str + "\n"
for data_line_index in range(int(number_of_data_lines_as_str)):
    user_input_string += input() + "\n"
#END : insert your user input handling code above
print("user_input_string:")
print(user_input_string)
print("result:")
print(CCC_2018_Junior_Question_3(user_input_string)) 
#CHANGE NAME OF ABOVE FUNCTION