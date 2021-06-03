def print_list(array_of_integers):
  if len(array_of_integers) == 0:
    return
  if len(array_of_integers) == 1:
    print(array_of_integers[0])
  else:
    print(array_of_integers[0])
    print_list(array_of_integers[1:])

print_list([])
print_list([1])
print_list([1,2,3,4,5,6,7,8,9, 10])

#original input : array_of_integers
#part of input used for recursive CALL INPUT : array_of_integers[1:]
#part of input used for recursive step : array_of_integers[0]
#original input = recursive CALL INPUT(input-1 unit) + recursive step(1 unit)

def print_list_reverse(array_of_integers):
  if len(array_of_integers) == 0:
    return
  if len(array_of_integers) == 1:
    print(array_of_integers[0])
  else:
    print_list_reverse(array_of_integers[1:])
    print(array_of_integers[0])

print("Now doing print list reverse")
print_list_reverse([])
print_list_reverse([1])
print_list_reverse([1,2,3,4,5,6,7,8,9, 10])