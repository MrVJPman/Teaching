##Binary Search
small_list = list(range(0, 10)) #10 small list
medium_list = list(range(0, 100)) #100 for the medium list
large_list = list(range(0, 10000)) #10000 for large list

def BinarySearch(search_list, search_value, start_index, end_index, count):
    count += 1
    if (end_index < start_index): 
        print("# of comparsions: " + str(count))
        return -1
    else:
        mid_index = int(start_index+((end_index-start_index)/2))
        if(search_list[mid_index] == search_value):
            print("# of comparsions: " + str(count)) 
            return mid_index
        elif search_list[mid_index] > search_value:
            return BinarySearch(search_list, search_value, start_index, mid_index-1, count)
        else:
            return BinarySearch(search_list, search_value, mid_index+1, end_index, count)

BinarySearch(small_list, small_list[0], 0, len(small_list)-1, 0)
BinarySearch(small_list, small_list[len(small_list)//2 - 1], 0, len(small_list)-1, 0)
BinarySearch(small_list, small_list[-1], 0, len(small_list)-1, 0)

BinarySearch(medium_list, medium_list[0], 0, len(medium_list)-1, 0)
BinarySearch(medium_list, medium_list[len(medium_list)//2  - 1], 0, len(medium_list)-1, 0)
BinarySearch(medium_list, medium_list[-1], 0, len(medium_list)-1, 0)

BinarySearch(large_list, large_list[0], 0, len(large_list)-1, 0)
BinarySearch(large_list, large_list[len(large_list)//2  - 1], 0, len(large_list)-1, 0)
BinarySearch(large_list, large_list[-1], 0, len(large_list)-1, 0)