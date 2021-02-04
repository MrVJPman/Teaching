#2020 Junior Q4

def CCC_2020_Question_4(input_string):
    lines = input_string.split() #this will always be here
    line_1 = lines[0]
    line_2 = lines[1]
    all_cyclic_shifts = []
    current_shift = line_2
    all_cyclic_shifts.append(current_shift)
    for index in range(len(line_2)):
        current_shift = current_shift[1:] + current_shift[0]
        all_cyclic_shifts.append(current_shift)
    for shift_string in all_cyclic_shifts:
        if shift_string in line_1:
            return "yes"
    return "no"
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
print(combined_file_contents)

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
        received_output = CCC_2020_Question_4(input_string) #CHANGE NAME OF THIS FUNCTION
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
#END : change everything here to take inputs
print("user_input string:")
print(user_input_string)
print("result: ")
print(CCC_2020_Question_4(user_input_string)) #CHANGE NAME OF THIS FUNCTION