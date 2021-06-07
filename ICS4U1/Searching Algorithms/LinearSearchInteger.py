def linearSearchInt(search_list, search_value):
    i = 0
    max_of_search_list = len(search_list)-1 
    while True:
        if i > max_of_search_list:
            return -1
        elif search_list[i] == search_value:
            return i
        else:
            i = i + 1