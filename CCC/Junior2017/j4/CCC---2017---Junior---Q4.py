def CCC_2017_Junior_Question_4(input_string):
    #this will always be here strip()
    lines = input_string.strip().split("\n") 
    #strip : to remove last newline
    #split : to divide into individual lines
 

    #Your Solution Starts Here 
    solution_string = None    
    minutes_after_12_00 = int(lines[0])
    
    number_of_cycles_pass_12_00 = int(minutes_after_12_00 / (60 * 12)) 
    total_number_of_sequences_from_cycles_pass_12_00 = number_of_cycles_pass_12_00 * 31
    remainder_from_total = minutes_after_12_00 % (60 * 12)
    
    arithmetic_sequence_list = [
     34,        
     60 + 11, 60 + 23, 60 + 35, 60 + 47, 60 + 59,
     60 * 2 + 10, 60 * 2 + 22, 60 * 2 + 34, 60 * 2 + 46, 60 * 2 + 58, 
     60 * 3 + 21, 
     60 * 3 + 33, 60 * 3 + 45, 60 * 3 + 57, 
     60 * 4 + 20, 60 * 4 + 32, 60 * 4 + 44, 60 * 4 + 56, 
     60 * 5 + 31, 60 * 5 + 43, 60 * 5 + 55, 
     60 * 6 + 30, 60 * 6 + 42, 60 * 6 + 54, 
     60 * 7 + 41, 60 * 7 + 53, 
     60 * 8 + 40, 60 * 8 + 52,  
     60 * 9 + 51, 
     60 * 11 + 11]
    
    number_of_sequences = 0
    for value in arithmetic_sequence_list:
        if value > remainder_from_total:
            break
        else:
            number_of_sequences = number_of_sequences + 1
    solution_string = str(number_of_sequences + total_number_of_sequences_from_cycles_pass_12_00)  
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
        received_output = CCC_2017_Junior_Question_4(input_string) #CHANGE NAME OF THIS FUNCTION
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
#END : insert your user input handling code above
print("user_input_string:")
print(user_input_string)
print("result:")
print(CCC_2017_Junior_Question_4(user_input_string)) 
#CHANGE NAME OF ABOVE FUNCTION