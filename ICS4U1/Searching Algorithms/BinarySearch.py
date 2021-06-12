def BinarySearch(search_list, search_value, start_index, end_index):
  print(search_list[start_index : end_index+1])
  if (end_index < start_index): 
    return -1
  else:
    mid_index = int(start_index+((end_index-start_index)/2))
  if(search_list[mid_index] ==search_value):
    return mid_index
  elif search_list[mid_index] > search_value:
    return BinarySearch(search_list, search_value, start_index, mid_index-1)
  else:
    return BinarySearch(search_list, search_value, mid_index+1, end_index)

L = [4,5,7,9,10,14,16,19]
print(BinarySearch(L, 4, 0, len(L)-1))
