#https://i.ytimg.com/vi/vsIa8KjzpBU/hqdefault.jpg

user_choice = input("Which option?")
if user_choice == "rise/run":
  rise = float(input("Rise?"))
  run = float(input("Run?"))
else:
  y2 = float(input("y2?"))
  x2 = float(input("x2?"))
  y1 = float(input("y1?"))
  x1 = float(input("x1?"))
  rise = y2-y1
  run = x2-x1

if (run == 0):
  print("line is vertical, slope is undefined")
else:
  slope = rise/run
  print(round(slope, 2))