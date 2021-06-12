#5.2.3


#code for generation a random string

'''
import random
import string 
string_list = []
for index in range(10):
  string_list.append(''.join(random.choices(string.ascii_uppercase, k = 3)))
string_list.sort()
print(string_list)'''


#BinarySearchForStrings
#Assume that we're not checking for the first value

string_list = ['GWN', 'JFF', 'KTM', 'KWH', 'MAU', 'ONN', 'RVM', 'XCO', 'YEE', 'YNB']

def StringBinarySearch(search_list, search_value, start_index, end_index):
  print(search_list[start_index : end_index + 1])
  if (end_index < start_index): 
    return -1
  else:
    mid_index = int(start_index+((end_index-start_index)/2))

  if(search_list[mid_index]== search_value):
    return mid_index
  elif search_list[mid_index] > search_value:
    return StringBinarySearch(search_list, search_value, start_index, mid_index  - 1)
  else:
    return StringBinarySearch(search_list, search_value, mid_index  + 1, end_index)

string_to_be_searched_for = input("What are you searching for?")

print(StringBinarySearch(string_list, string_to_be_searched_for, 0, len(string_list)-1))