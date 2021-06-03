def powerN(base, n):
    if n==0:
        return 1
    #step 1 what is the base case?
    #base is when it's 1
    if n==1:
        return base
    #step 2: what is the recursive call's input : n-1
    #powerN(base, n-1)
    #step 3: what is the recursive step remainder piece : base
    #recursive step is related to what is suppose to do 
    #step 4: combine them 
    else:
        return base * powerN(base, n-1)
assert(powerN(3, 0) == 1)
assert(powerN(3, 1) == 3)
assert(powerN(3, 2) == 9)
assert(powerN(3, 3) == 27)
assert(powerN(2, 4) == 16)
