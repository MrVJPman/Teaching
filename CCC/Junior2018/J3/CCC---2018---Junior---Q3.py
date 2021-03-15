def CCC_2018_Junior_Question_3(input_string):
    #this will always be here strip()
    lines = input_string.strip().split("\n") 
    #strip : to remove last newline
    #split : to divide into individual lines


    four_positive_integers_as_distances = lines[0]
    distances = four_positive_integers_as_distances.split()
    distances[0] = int(distances[0])
    distances[1] = int(distances[1])
    distances[2] = int(distances[2])
    distances[3] = int(distances[3])

    #Your Solution Starts Here 
    solution_string = None    
    solution_string = ""
    for i_index in range(5):
        new_str = ""
        for j_index in range(5):
            if i_index == j_index:
                new_str += "0 "
            elif i_index < j_index:
                new_str += str(sum(distances[i_index:j_index])) + " "
            else: #i_index < i_index    
                new_str += str(sum(distances[j_index:i_index])) + " "
        solution_string += new_str + "\n"       

    solution_string = solution_string.strip()
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
user_input_string = input() + "\n"
#END : insert your user input handling code above
print("user_input_string:")
print(user_input_string)
print("result:")
print(CCC_2018_Junior_Question_3(user_input_string)) 
#CHANGE NAME OF ABOVE FUNCTION