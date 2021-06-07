
def ReverseLinearSearchInt(search_list, search_value):
    i = len(search_list)-1  
    while True:
        if i < 0:
            return -1
        elif search_list[i] == search_value:
            return i
        else:
            i = i - 1

print("Index of reverse search", ReverseLinearSearchInt([6,3,7,1,4,9,2], 4))