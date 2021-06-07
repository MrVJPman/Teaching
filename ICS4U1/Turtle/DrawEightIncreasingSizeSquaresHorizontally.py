import turtle
turtle.shape("arrow")
turtle.pencolor("black")
turtle.fillcolor("darkblue")

index = 0 
while index < 8:
    #penup/pendown to prevent drawing a line when jumping to draw a new square
  turtle.penup()
  turtle.goto(-180 + 45 * index, 0)
  turtle.pendown()

  #Draw the new square, with index increasing square length
  turtle.begin_fill()
  turtle.forward(10 + 5 * index)
  turtle.right(90)
  turtle.forward(10 + 5 * index)
  turtle.right(90)
  turtle.forward(10  + 5 * index)
  turtle.right(90)
  turtle.forward(10  + 5 * index)
  turtle.right(90)
  turtle.end_fill()
  index = index + 1 
