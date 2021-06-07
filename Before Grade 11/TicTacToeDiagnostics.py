#Mr. Bob Kong's tic-tac-toe diagnostics

current_game_board = "012\n345\n678"
import random

while (True):
  print(current_game_board)
  user_move = input("You are X. Where would you to go next?")
  if user_move in current_game_board:
    current_game_board = current_game_board.replace(user_move, "X")
  
  computer_move = str(random.randint(1, 8))
  while computer_move not in current_game_board:
    computer_move = str(random.randint(1, 8))
  print("Computer (O) went", computer_move)
  current_game_board = current_game_board.replace(computer_move, "O")

#1 : How many variables are there in this game?
#2 : why do we need to do  
#current_game_board = current_game_board.replace(user_move, "X") 
#instead of just
#current_game_board.replace(user_move, "X")
#3 : How many if statements do we need to check for victory?
#4 : why is it a bad idea to use [else] for victory checking?
#5 : How can you make it so that the computer goes first?
#6 : Explain how the computer decides its move
#7 : What happens if we input an integer besides 1-8?
#8 : Why do we need a while loop in line 16?
#9 : How can we change the code using Lists so we don't use the while loop on line 16?
#10 : Explain how we can use [for loops] to make this game "better"  