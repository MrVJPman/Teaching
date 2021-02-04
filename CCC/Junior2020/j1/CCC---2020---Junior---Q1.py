#2020 Junior Q1

def CCC_2020_Question_1(input_string):
    lines = input_string.split()
    line1 = int(lines[0])
    line2 = int(lines[1])
    line3 = int(lines[2])
    if (line1 * 1 + line2 * 2 + line3 * 3) >= 10:
        return "happy"
    else:
        return "sad"
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
        received_output = CCC_2020_Question_1(input_string) #CHANGE NAME OF THIS FUNCTION
        expected_output = combined_file_contents[testcase][1].strip()       
        print("----------Expected: ")
        print(expected_output)
        print("----------Received: ")
        print(received_output)
        assert(expected_output == received_output)
        print("\n")
    print("CONGRATULATIONS!!! ALL TEST CASES PASS!")

run_all_test_cases(combined_file_contents)


print("ENTER inputs")
user_input_string = ""
#START : change everything here to take inputs
user_input_string += input() + "\n"
user_input_string += input() + "\n"
user_input_string += input() + "\n"
#END : change everything here to take inputs
print("user_input string:")
print(user_input_string)
print("result: ")
print(CCC_2020_Question_1(user_input_string)) #CHANGE NAME OF THIS FUNCTION

