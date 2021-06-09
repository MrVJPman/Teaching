#Write code that will accept two inputs. One of them is a Tuple, and one of them is a List. Both Tuple/List have exactly one item. 

new_tuple = tuple(input())
new_list = list(input())

#Create a dictionary where the key-value where the key is the value in the tuple and the value is value in the list. Then print out three things#

new_dict = {new_tuple[0]: new_list[0]}
print("{}, {}, {}".format(new_tuple, new_list, new_dict))