import random
random.choice([True, False]) #Randomily picks True or False

#Question 1) 
#a <= b can be rewritten as a < b or a == b 
#So the following boolean expression is always True
#(a <= b) == (a < b or a == b)

x = 2
y = 1
#Rewrite the following by create a boolean expression similar to the one above  
(x >= y) == (x > y or x == y)

#Question 2)
#What are two different ways you can do double negation on x?

x = random.choice([True, False])
#method 1
not(not(x))
#method 2
not(x != True)
#method 3
not(x == False)
#method 4
((x != True) == False)
#method 5
((x == False) != True)
#method 6
(not(x) == False)
#method 7
(not(x) != True)

#Question 3)
m = random.choice([True, False]) 
#Convert the following boolean expression into a mathematical expression: 
not (m)
#using a mathematical operator. 
#Your answer should apply whether m is True or if m is False
1-m

#m=True(1)-->1-m = 1-1 = 0(False)
#m=False(0)-->1-m = 1-0 = 1(True)

#Question 4)
m = random.choice([True, False])
n = random.choice([True, False])
#Convert the following boolean expression into a mathematical expression:
m and n
#using a mathematical operator. 
#Your answer should apply for all four possible pairings of m and n

m * n

#m=False(0), n=False(0)--> 0 * 0 = 0 (False)
#m=True(0), n=False(0)--> 1 * 0 = 0 (False)
#m=False(0), n=True(1)--> 0 * 1 = 0 (False)
#m=True(1), n=True(1)--> 1 * 1 = 1 (True)



#Question 5)
m = random.choice([True, False])
n = random.choice([True, False])
#Convert the boolean expression:
m or n
#into another boolean expression that uses a i) a comparison operator and ii) a mathematical operator. 
#Your answer should apply for all four possible pairings of m and n

m + n > 0
#or you can also do
m + n >= 1

#m=False(0), n=False(0)--> 0 + 0 > 0 (False)
#m=True(0), n=False(0)--> 1 + 0 > 0 (True)
#m=False(0), n=True(1)--> 0 + 1 > 0 (True)
#m=True(1), n=True(1)--> 2 > 0 (True)


#Question 6)
#Create the truth table for both cases of DeMorgan’s Law
#https://blog.penjee.com/what-is-demorgans-law-in-programming-answered-with-pics/
#If you did it correctly, you should have two truth tables, with four rows each and at least four columns each.

#A  B   not (A)   not (B)   not(A) or not(B)    A and B   not(A and B)
#F  F   T         T               T             F         T  
#F  T   T         F               T             F         T
#T  F   F         T               T             F         T
#T  T   F         F               F             T         F

#A  B   not (A)   not (B)   not(A) and not(B)    A or B   not(A or B)
#F  F   T         T               T             F         T  
#F  T   T         F               F             T         F
#T  F   F         T               F             T         F
#T  T   F         F               F             T         F

#Question 7)
#Complete both boolean expressions that represents the two cases of DeMorgan’s Law.
A = random.choice([True, False])
B = random.choice([True, False]) 
#Boolean expression #1
(not(A) or not(B)) == (not(A and B))
#Boolean expression #2
(not(A) and not(B)) == (not(A or B))

#Question 8)
#Convert the following binary number into decimal, #show your work
#10101010

#128 64  32  16  8 4 2 1  
#  1  0   1   0  1 0 1 0 
#128 + 32 + 8 + 2 = 170

#Question 9)
#Convert the following decimal number into binary, #show your work
#19

#19 / 2 = 9 R 1 
#9 / 2 = 4 R 1
#4 / 2 = 2 R 0
#2 / 2 = 1 R 0
#1 / 2 = 0 R 1
#0 / 2 = 0 R 0
#0 / 2 = 0 R 0
#0 / 2 = 0 R 0

#00010011

