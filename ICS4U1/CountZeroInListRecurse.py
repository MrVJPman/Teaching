def count_number_of_zeroes(array_of_integers):
    if len(array_of_integers) == 0:
        return 0
    if len(array_of_integers) == 1:
        if array_of_integers[0] == 0:
            return 1
        else:
            return 0
    else:
        if array_of_integers[0] == 0:
            return 1 + count_number_of_zeroes(array_of_integers[1:])
        else:
            return count_number_of_zeroes(array_of_integers[1:])

assert(count_number_of_zeroes([])==0)
assert(count_number_of_zeroes([1])==0)
assert(count_number_of_zeroes([0])==1)
assert(count_number_of_zeroes([0, 0])==2)
assert(count_number_of_zeroes([0, 1])==1)
assert(count_number_of_zeroes([0, 0, 0])==3)
