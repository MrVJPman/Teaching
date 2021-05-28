def CCC_2015_Question_1(str1, str2):
    str1_as_a_list = list(str1)
    for character in str2:
        if character == "*":
            pass
        else: #when it's not the star
            if character in str1_as_a_list:
                str1_as_a_list.remove(character)
            else:
                break   
    if len(str1_as_a_list) == str2.count("*"):
        return "A"
    else:
        return "N"

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

def run_all_test_cases():
    for testcase in combined_file_contents:
        print("Test case: ", testcase)
        inputs = combined_file_contents[testcase][0].split("\n")
        index = 1
        for line in inputs[:-1]: #[:-1] to ignore the last empty line
            print("User Input Line ", index, ": ", line)
            index += 1
        
        received_output = CCC_2015_Question_1(inputs[0], inputs[1]) #CHANGE ONLY THIS LINE
        expected_output = combined_file_contents[testcase][1].strip()       
        print("Expected: ", expected_output)
        print("Received: ", received_output)
        assert(received_output == expected_output)
        print("\n")
    print("CONGRATULATIONS!!! ALL TEST CASES PASS!")


run_all_test_cases()

str1 = input()
str2 = input()
print(CCC_2015_Question_1(str1, str2))


