def sum_of_n(n):
  if n == 1:
    return 1
  else:
    return n + sum_of_n(n-1)

assert(sum_of_n(1) == 1)
assert(sum_of_n(3) == 6)
assert(sum_of_n(5) == 15)
assert(sum_of_n(100) == 5050)