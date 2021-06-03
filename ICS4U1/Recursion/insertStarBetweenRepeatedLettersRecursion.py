def insertStar(repeating_string):
    #base case 
    if len(repeating_string) <= 1:
        return repeating_string
    if len(repeating_string) == 2 and (repeating_string[0] == repeating_string[-1]):
        return repeating_string[0] + "*" + repeating_string[-1]
    #Recursive case
    else:
        #Case when two adjacent characters are the same 
        #recursive step : repeating_string[0]
        #recursive call : insertStar(repeating_string[1:])        
        if (repeating_string[0] == repeating_string[1]):
            return repeating_string[0] + "*" + insertStar(repeating_string[1:]) 
        #Case when two adjacent characters are not the same
        else:
            return repeating_string[0] + insertStar(repeating_string[1:]) 
assert(insertStar("") == "")
assert(insertStar("a") == "a")
assert(insertStar("ll") == "l*l")
assert(insertStar("lll") == "l*l*l")
assert(insertStar("hello") == "hel*lo")
assert(insertStar("xxyy") == "x*xy*y")
assert(insertStar("aaaa") == "a*a*a*a")