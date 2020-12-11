import turtle as tr
import math

l = 20
tr.speed(0)
tr.goto(0,0)
tr.color("black")
color_list = ["black", "gray", "orange", "yellow" "white"]
pixel_x = 13
pixel_y = 13
tr.xcor = 0
tr.ycor = 0
layout = 0
def draw_pixel():
  tr.setheading(45)
  tr.pendown()
  tr.begin_fill()
  tr.circle(10, 360, 4)
  tr.end_fill()
  tr.penup()

def check_color():
  if c == 1:
    tr.color("black")
    tr.fillcolor("black")
  elif c == 2:
    tr.color("gray")
    tr.fillcolor("gray")
  elif c == 3:
    tr.color("orange")
    tr.fillcolor("orange")
  elif c == 4:
    tr.color("yellow")
    tr.fillcolor("yellow")
  elif c == 5:
    tr.color("white")
    tr.fillcolor("white")
  elif c == 6:
    tr.color("brown")
    tr.fillcolor("brown")

tr.penup()
tr.xcor = -13
tr.ycor = -10
while l > layout:
  layout = layout + 1
  if layout == 1:
    color_list = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]
  elif layout == 2:
    color_list = [1, 1, 1, 1, 1, 1, 2, 5, 5, 5, 2, 1, 1, 1, 1, 1, 2, 5, 5, 5, 2, 1, 1, 1, 1, 1, 1]
  elif layout == 3:
    color_list = [1, 1, 1, 1, 1, 2, 5, 6, 6, 6, 5, 2, 1, 1, 1, 2, 5, 6, 6, 6, 5, 2, 1, 1, 1, 1, 1]
  elif layout == 4:
    color_list = [1, 1, 1, 1, 2, 5, 6, 3, 6, 3, 6, 5, 2, 1, 2, 5, 6, 3, 6, 3, 6, 5, 2, 1, 1, 1, 1]
  elif layout == 5:
    color_list = [1, 1, 1, 2, 5, 6, 3, 3, 6, 3, 3, 6, 2, 1, 2, 6, 3, 3, 6, 3, 3, 6, 5, 2, 1, 1, 1]
  elif layout == 6:
    color_list = [1, 1, 2, 5, 6, 3, 3, 3, 6, 3, 3, 3, 6, 5, 6, 3, 3, 3, 6, 3, 3, 3, 6, 5, 2, 1, 1]
  elif layout == 7:
    color_list = [1, 1, 2, 5, 6, 6, 6, 6, 6, 3, 3, 3, 6, 5, 6, 3, 3, 3, 6, 6, 6, 6, 6, 5, 2, 1, 1]
  elif layout == 8:
    color_list = [1, 1, 2, 5, 6, 3, 3, 3, 6, 3, 3, 3, 6, 5, 6, 3, 3, 3, 6, 3, 3, 3, 6, 5, 2 ,1, 1]
  elif layout == 9:
    color_list = [1, 2, 5, 6, 3, 3, 3, 3, 6, 3, 3, 3, 6, 5, 6, 3, 3, 3, 6, 3, 3, 3, 3, 6, 5, 2, 1]
  elif layout == 10:
    color_list = [2, 5, 6, 3, 3, 3, 3, 3, 6, 3, 3, 3, 6, 5, 6, 3, 3, 3, 6, 3, 3, 3, 3, 3, 6, 5, 2]
  elif layout == 11:
    color_list = [2, 5, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3, 6, 5, 6, 3, 3, 3, 6, 6, 6, 6, 6, 6, 6, 5, 2]
  elif layout == 12:
    color_list = [2, 5, 5, 5, 5, 5, 5, 5, 6, 3, 3, 3, 3, 6, 3, 3, 3, 3, 6, 5, 5, 5, 5, 5, 5, 5, 2]
  elif layout == 13:
    color_list = [2, 2, 2, 2, 2, 2, 2, 5, 6, 3, 3, 3, 3, 6, 3, 3, 3, 3, 6, 5, 2, 2, 2, 2, 2, 2, 2]
  elif layout == 14:
    color_list = [1, 1, 1, 1, 1, 1, 2, 5, 6, 3, 3, 3, 3, 6, 3, 3, 3, 3, 6, 5, 2, 1, 1, 1, 1, 1, 1]
  elif layout == 15:
    color_list = [1, 1, 1, 1, 1, 1, 1, 2, 5, 6, 3, 3, 3, 6, 3, 3, 3, 6, 5, 2, 1, 1, 1, 1, 1, 1, 1]
  elif layout == 16:
    color_list = [1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 6, 6, 6, 5, 6, 6, 6, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1]
  elif layout == 17:
    color_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 5, 5, 5, 5, 5, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  elif layout == 18:
    color_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  l = 18
  tr.xcor = -13
  tr.ycor = tr.ycor + 1 
  for i in range (27):
    c = color_list.pop()
    tr.goto(tr.xcor * pixel_x, tr.ycor * pixel_y)
    check_color()
    draw_pixel()
    tr.xcor = tr.xcor + 1

tr.mainloop()
