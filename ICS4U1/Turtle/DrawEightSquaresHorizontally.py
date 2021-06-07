import turtle
turtle.shape("arrow")
turtle.pencolor("black")
turtle.fillcolor("darkblue")

index = 0 
#Draw 8 squares
while index < 8:
  #penup/pendown to prevent drawing a line when jumping to draw a new square
  turtle.penup()
  turtle.goto(-180 + 40 * index, 0)
  turtle.pendown()

  #Draw the new square
  turtle.begin_fill()
  turtle.forward(15)
  turtle.right(90)
  turtle.forward(15)
  turtle.right(90)
  turtle.forward(15)
  turtle.right(90)
  turtle.forward(15)
  turtle.right(90)
  turtle.end_fill()

  #Increase by 1 to setup for the next square
  index = index + 1 
