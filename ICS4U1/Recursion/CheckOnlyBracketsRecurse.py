#assume that the input is always even string
def check_only_brackets(input_string):
    #Base cases
    if len(input_string) == 0:
        return True
    if len(input_string) == 2:
        return input_string == "()"
    #Recursive cases 
    else: 
            #check the first and last chars
        if input_string[0] == "(" and input_string[-1] == ")":
            #then recurse on what's inside them
            return check_only_brackets(input_string[1:-1]) 
        else:
            return False

assert(check_only_brackets("(())") == True)
assert(check_only_brackets("((()))") == True)
assert(check_only_brackets("(((x))") == False)
