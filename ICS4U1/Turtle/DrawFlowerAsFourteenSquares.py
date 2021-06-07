import turtle
turtle.shape("arrow")
turtle.pencolor("black")
turtle.fillcolor("lightblue")

index = 0 
#Draw 14 squares
while index < 14:
  turtle.begin_fill()
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.end_fill()
  #Rotate only by about 25 degrees before drawing the next square
  turtle.right(25)
  index = index + 1