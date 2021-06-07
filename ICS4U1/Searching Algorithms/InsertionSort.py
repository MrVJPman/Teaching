import random

def insertion_sort(list_to_be_sorted):
    #Perform len(list_to_be_sorted) - 1 swaps
    #Visiting every value one by one 
    for index in range(1, len(list_to_be_sorted)):
        print(list_to_be_sorted, list_to_be_sorted[index])
        #saves a copy of the current value to be sorted for later 
        current_value = list_to_be_sorted[index]       
        #create a copy of the current value's index
        swap_index = index

        #shifts part/full aspect of currently sorted list repeatedly to the right
        #stop once we've find the proper position to "insert" the current value
        while swap_index > 0 and current_value < list_to_be_sorted[swap_index-1]:
            list_to_be_sorted[swap_index] = list_to_be_sorted[swap_index-1]
            swap_index = swap_index - 1

        #now that we've find the position, insert the value
        list_to_be_sorted[swap_index] = current_value 
    return list_to_be_sorted

L =  [random.randint(1,100) for number in range(20)]
print(insertion_sort(L))