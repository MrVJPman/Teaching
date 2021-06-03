def sum_of_digits(x):
  x = abs(x)
  #If x is between -9 to 9, then it should 0-9
  if x <= 9: #Base case
    return x
  else: #Recursive case
    return sum_of_digits(x // 10) + x % 10

assert(sum_of_digits(9) == 9)
assert(sum_of_digits(12) == 3)
assert(sum_of_digits(39) == 12)
assert(sum_of_digits(234) == 9)
assert(sum_of_digits(-234) == 9)

#Step 1 : handle the base [1/5]
#base case is simplest case
#just write an if 
 
#Step 2: determine the recursive call, how are you gonig to reduce it by one? [1/5]
#Copy the function again
#Then the input variable
#Now, you're reduce the input variable by 1 unit somehow

#In the recursive call, what should you extract for reduced int from"
#We want to reduce the input 12 into input 2
#We want to reduce the input 39 into input 9
#We want to reduce the input 234 into input 34
#We want to reduce the input 234 into input 23

#Step 3 : Determine the recursive step, the remaining one unit from step 2?  [1/5]

#The recursive step, what is the difference taken from input - input for recursive call
#HINT : this step should be ONE unit
#difference for 12 - > 1
#difference for 39  - > 3
#difference for 234 -> 2
#difference for 234 -> 4

#step 4 : combine them together [2/5

#Checks the output of sum_of_digits(9) is 9,
#If it is 9, then do nothing
#if it is not 9, then show error
