#2016 Senior Q3


def find_path_between_two_node(start, end, network):
    visited_nodes = []
    queue_of_path_to_check = [[start]]
    
    while queue_of_path_to_check != []:
        current_path_to_explore = queue_of_path_to_check.pop(0)
        last_node_of_current_path = current_path_to_explore[-1]
        if last_node_of_current_path not in visited_nodes:
            all_neighbours_of_node = network[last_node_of_current_path] 
            for neighbour in all_neighbours_of_node:
                new_path = list(current_path_to_explore)
                new_path.append(neighbour)
                queue_of_path_to_check.append(new_path)
                if neighbour == end:
                    return new_path               
            visited_nodes.append(last_node_of_current_path)

def CCC_2016_Question_3(input_string):
    #this will always be here strip()
    lines = input_string.strip().split("\n") 
    #strip : to remove last newline
    #split : to divide into individual lines

    #Your Solution Starts Here

    line1_as_list_of_integer = lines[0].split()
    N = int(line1_as_list_of_integer[0])
    M = int(line1_as_list_of_integer[1])
    line2 = lines[1]
    all_pho_locations = line2.split() 
    road_network_as_string = lines[2:]
    
    
    road_network = {}
    for line in road_network_as_string:
        pair_of_node = line.split()
        if pair_of_node[0] not in road_network:
            road_network[pair_of_node[0]] = [pair_of_node[1]]
        else:
            road_network[pair_of_node[0]].append(pair_of_node[1])
        if pair_of_node[1] not in road_network:
            road_network[pair_of_node[1]] = [pair_of_node[0]]
        else:
            road_network[pair_of_node[1]].append(pair_of_node[0])
    print(road_network)
    
    pho_path = find_path_between_two_node(all_pho_locations[0], all_pho_locations[1], road_network)
    print("pho_path_so_far", pho_path)
    for index_of_current_pho in range(2, M):     
        current_minimal_path = -1
        for index_of_prev_pho in range(index_of_current_pho):
            new_path = find_path_between_two_node(all_pho_locations[index_of_current_pho], all_pho_locations[index_of_prev_pho], road_network)
#            if new_path
            print(new_path)
        print("ENDED checking", all_pho_locations[index_of_current_pho])
#    print("total", pho_path)
    return str(len(pho_path) - 1) 

#    return str(None) #This is here by default. Don't forget to comment this
    #Your Solution Ends Here

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
        print(input_string)
        received_output = CCC_2016_Question_3(input_string) #CHANGE NAME OF THIS FUNCTION
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
N = input()
user_input_string += N + "\n"
for index in range(int(N)):
    user_input_string += input() + "\n"
#END : change everything here to take inputs
print("user_input string:")
print(user_input_string)
print("result: ")
print(CCC_2016_Question_3(user_input_string)) #CHANGE NAME OF THIS FUNCTION

