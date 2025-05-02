# import colorgram
# from colorgram import extract

import turtle
import random
from random import choice

# colors = extract('image.jpg',38)
# color_list = []
#
# for number_of_color in range(len(colors)):
#     first_colors = colors[number_of_color]
#
#     r = first_colors.rgb.r
#     g = first_colors.rgb.g
#     b = first_colors.rgb.b

#     rgb_color = (r,g,b)
#     color_list.append(rgb_color)
#
# print(color_list)

#colour list which contains r g b color value in a form of tuple
color_list = [(243, 242, 238), (245, 236, 241), (234, 240, 245), (235, 244, 240), (233, 219, 106), (225, 150, 96),
              (100, 185, 220), (223, 62, 96), (222, 130, 156), (15, 114, 193), (181, 11, 48), (11, 185, 220),
              (235, 162, 179), (124, 220, 234), (186, 45, 84), (9, 40, 162), (23, 194, 142), (222, 80, 61), (7, 33, 77),
              (180, 68, 42), (87, 10, 45), (117, 227, 217), (155, 25, 17), (95, 201, 156), (165, 167, 36), (232, 168, 161),
              (70, 115, 208), (168, 181, 229), (19, 135, 102), (11, 97, 75), (76, 15, 13), (11, 85, 101), (8, 63, 53),
              (249, 7, 43), (227, 210, 28), (245, 13, 11), (5, 60, 251), (10, 243, 224)]


timmy = turtle
timmy.colormode(255)
timmy.shape()
timmy.speed("fastest")

def create_dot():
   """this function will help us to create a colored dot by getting a random tuple value form the list."""
   for dot in range(15):

      random_col = choice(color_list)
      timmy.dot(10, random_col)
      timmy.forward(20)

# this function will remove the pen colour
timmy.penup()
timmy.hideturtle()
timmy.setheading(700)
timmy.forward(300)
timmy.setheading(0)
y_axis = 0
num = 0

# sety function value is going to be changed each time the loop will run so the dot value can restart from new position.
for to_color in range(15):

   timmy.setx(-110)
   timmy.sety(y_axis)
   if num < 15:
      create_dot()
      num += 1
   y_axis += 20

timmy.exitonclick()


