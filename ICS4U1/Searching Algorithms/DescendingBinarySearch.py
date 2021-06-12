#Binary Search
def DescendingBinarySearch(search_list, search_value, start_index, end_index):
#  print(lst[min : max+1])
  if (end_index < start_index): 
    return -1
  else:
    mid_index = int(start_index+((end_index-start_index)/2))
  if(search_list[mid_index]==search_value):
    return mid_index
  elif search_list[mid_index] < search_value:
    return DescendingBinarySearch(search_list, search_value, start_index, mid_index-1)
  else:
    return DescendingBinarySearch(search_list, search_value, mid_index+1, end_index)

L = [19, 16, 14, 10, 9, 7, 5, 4]
print(DescendingBinarySearch(L, -19, 0, len(L)-1))
