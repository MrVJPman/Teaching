#Simple version of poker
#Building video games require step-by-step
#Let's build the each part

#Part 1 : Drawing 5 cards from a deck

#We can use random to randomly select a card
import random

#To focus on the number, we can use randomint

all_suits = ["spades", "hearts", "clubs", "diamonds"]

for i in range(5):
  card = random.randint(1, 13)
  suit = random.randint(0, 3)
  if suit == 1:
    print("Card", i+1, "is", card ,"of", all_suits[suit])
  elif suit == 2:
    print("Card", i+1, "is", card ,"of",  all_suits[suit])
  elif suit == 3:
    print("Card", i+1, "is", card ,"of", all_suits[suit])
  else:
    print("Card", i+1, "is", card ,"of", all_suits[suit])