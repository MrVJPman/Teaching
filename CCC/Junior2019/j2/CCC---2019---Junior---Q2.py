def CCC_2019_Junior_Question_2(input_string):
    #this will always be here strip()
    lines = input_string.strip().split("\n") 
    #strip : to remove last newline
    #split : to divide into individual lines

    #Your Solution Starts Here 
    solution_string = None    
    solution_string = ""
    for line in lines[1:]:    
        number_symbol_list = line.split() 
        number = int(number_symbol_list[0])
        symbol = number_symbol_list[1]
        new_str = ""
        solution_string += number * symbol + "\n"
    #Your Solution Ends Here
    return str(solution_string[:-1]) 


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
        received_output = CCC_2019_Junior_Question_2(input_string) #CHANGE NAME OF THIS FUNCTION
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
n_as_string = input()
user_input_string = n_as_string + "\n"
for index in range(int(n_as_string)):
    user_input_string +=  input() + "\n"
#END : insert your user input handling code above
print("user_input_string:")
print(user_input_string)
print("result:")
print(CCC_2019_Junior_Question_2(user_input_string)) 
#CHANGE NAME OF ABOVE FUNCTION