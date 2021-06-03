def count8(n):
  #base case
  #base case is related to the simplest input
  #base case for the input is an integer between 0 to 9 , a digit of one value
  if n <= 9:
    if n == 8:
      return 1
    else:
      return 0 
  #recursive case
  #recursive input call : cut the input by 1 unit
  #the unit is based on the function is suppose to do
  else:
    #recursive step : the 1 unit that's been cut
    if n % 10 == 8:
      return 1 + count8(n // 10)  
    else:
      return count8(n // 10)  
assert(count8(8) == 1)
assert(count8(88) == 2)
assert(count8(818) == 2)
assert(count8(8818) == 3)