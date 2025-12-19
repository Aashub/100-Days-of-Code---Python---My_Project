# the colorgram module we have used to extract the color of  another hirst painting image
import colorgram
import random
import turtle
from turtle import Turtle, Screen

# here we are extracting the colors by calling the extract method of colorgram.
# colors = colorgram.extract("image.jpg", 34)
#
# rgb_color = []

# in this for loop we are storing each rgb color in rgb_color list in the form of tuple
# for color in range(len(colors)):
    # color_object = colors[color]
    #
    # here we are using each color_object to store r g b color in the variable as mentioned
    # red = color_object.rgb.r
    # green = color_object.rgb.g
    # blue = color_object.rgb.b
    #
    # rgb_tuple = (red, green, blue)
    # rgb_color.append(rgb_tuple)


# the color_list is the list which we have created using the tuple list
color_list = [(197, 157, 107), (137, 83, 62), (59, 99, 138), (128, 162, 186), (138, 176, 151), (128, 72, 87), (73, 112, 79), (178, 152, 54), (186, 138, 150), (225, 202, 119), (61, 41, 31), (194, 95, 78), (183, 94, 108), (118, 37, 47), (32, 44, 63), (61, 32, 41), (119, 40, 35), (97, 150, 104), (36, 56, 42), (222, 177, 170), (46, 58, 98), (174, 203, 181), (96, 125, 169), (73, 75, 38), (74, 149, 168), (44, 77, 55), (217, 176, 182), (168, 202, 206), (180, 188, 209), (31, 79, 88)]

dot = Turtle()
screen = Screen()
dot.speed("fastest")
turtle.colormode(255)

dot.penup()
num = 0

# here are we are setting initial coordinate of x and y axis
y_cord = -260
x_cord = -260

# the first for loop will help to change the y coordinate position.
for y_cord_change in range(27):

    # here if y_cord_change and num value match than it will update the starting position for hirst painting
    if y_cord_change == num:
        dot.goto(x_cord, y_cord)

    # this for loop will create a random color dot after certain distance
    for each_dot in range(27):

        dot.dot(10, random.choice(color_list))
        dot.forward(20)

    y_cord += 20
    num += 1

dot.hideturtle()
screen.exitonclick()