#2016 SENIOR #2

def CCC_2015_Question_2(mode, N, D_citizens, P_citizens):
    mode = int(mode)
    N = int(N)

    D_citizens_list = []
    P_citizens_list = []
    if N > 1:
        D_citizens_list = D_citizens.split() 
        P_citizens_list = P_citizens.split()
    else:
        D_citizens_list.append(D_citizens) 
        P_citizens_list.append(P_citizens)
        
    for index in range(N):
        D_citizens_list[index] = int(D_citizens_list[index])
        P_citizens_list[index] = int(P_citizens_list[index])
    D_citizens_list.sort()
    P_citizens_list.sort()
    if mode == 1:
        min_sum_max_pairs = 0
        for index in range(N):
            min_sum_max_pairs += max(D_citizens_list[index], P_citizens_list[index])
        return str(min_sum_max_pairs)  
    if mode == 2:
        P_citizens_list.reverse()
        max_sum_max_pairs = 0
        for index in range(N):
            max_sum_max_pairs += max(D_citizens_list[index], P_citizens_list[index])
        return str(max_sum_max_pairs)  

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

combined_file_contents = {}

for content in all_input_file_contents:
    combined_file_contents[content[:-3]] = [all_input_file_contents[content], all_output_file_contents[content[:-3]+".out"]]
print(combined_file_contents)


def run_all_test_cases():
    for testcase in combined_file_contents:
        print("Test case: ", testcase)
        inputs = combined_file_contents[testcase][0].split("\n")
        index = 1
        for line in inputs[:-1]: #[:-1] to ignore the last empty line
            print("User Input Line ", index, ": ", line)
            index += 1
        
        received_output = CCC_2015_Question_2(inputs[0], inputs[1], inputs[2], inputs[3]) #CHANGE ONLY THIS LINE
        expected_output = combined_file_contents[testcase][1].strip()       
        print("Expected: ", expected_output)
        print("Received: ", received_output)
        assert(received_output == expected_output)
        print("\n")


run_all_test_cases()

mode = input()
N = input()
D_citizens = input() 
P_citizens = input()
print(CCC_2015_Question_2(mode, N, D_citizens, P_citizens))

