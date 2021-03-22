def CCC_2017_Junior_Question_3(input_string):
    #this will always be here strip()
    lines = input_string.strip().split("\n") 
    #strip : to remove last newline
    #split : to divide into individual lines

    #Your Solution Starts Here 
    solution_string = None    
    starting_coordinate = lines[0]
    ending_coordinate = lines[1]
    units_electric_charge = int(lines[2])
    
    start_x, start_y = int(starting_coordinate.split()[0]), int(starting_coordinate.split()[1])
    end_x, end_y = int(ending_coordinate.split()[0]), int(ending_coordinate.split()[1])
    
    x_diff = abs(end_x - start_x)
    y_diff = abs(end_y - start_y)
    
    if (x_diff + y_diff <= units_electric_charge) and abs((x_diff + y_diff) - units_electric_charge) % 2 == 0:
        solution_string = "Y"
    else:
        solution_string = "N"
    #Your Solution Ends Here
    return str(solution_string) 


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
        received_output = CCC_2017_Junior_Question_3(input_string) #CHANGE NAME OF THIS FUNCTION
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
user_input_string = input() + "\n"
user_input_string = input() + "\n"
user_input_string = input() + "\n"
#END : insert your user input handling code above
print("user_input_string:")
print(user_input_string)
print("result:")
print(CCC_2017_Junior_Question_3(user_input_string)) 
#CHANGE NAME OF ABOVE FUNCTION