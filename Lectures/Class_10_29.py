#Task 1.4.9: Using a comprehension, create a new plot in which the points of S are rotated by 90 degrees, scaled by
#1/2, and then shifted down by one unit and to the right by two units. Use a comprehension in which the points of
#S are multiplied by one complex number and added to another

S = {(1.75 + 1j), (2 + 1j), (2.25 + 1j), (2.5 + 1j), (2 + 2j), (3 + 2j), (2.75 + 1j), (3 + 1j), (3.25 + 1j)}

plot({(1/2) * z * 1j - 1j + 2 for z in S}, 4)
#1/2 because scaling by 1/2
#z represents each coordinate in S
#*1j represents the rotation by 90 degrees
#-1j is shifting down by 1 unit
#+2 is shifting to the right by 2 units
#Order matters!!!!


#Task 1.4.18: Write a comprehension whose value is the set consisting of rotations by pi/4
#of the elements of S. Plot the value of this comprehension.

#Solution:
from math import e, pi
from plotting import plot
S = {(1.75 + 1j), (2 + 1j), (2.25 + 1j), (2.5 + 1j), (2 + 2j), (3 + 2j), (2.75 + 1j), (3 + 1j), (3.25 + 1j)}

#I will save the comprehension to a variable called coordinates. You don't have to do this, you can put the
#comprehension directly in the plot function if you want.

coordinates = {x* (**e((pi/4) * 1j)) for x in S}
plot(coordinates, 4)

#x is each coordinate with S
#e is part of Euler's formula
#pi/4 is the rotation amount
#1j is part of Euler's formula
S is the set of coordinates


#Task 1.4.10: We have provided a module image with a procedure file2image(filename) that reads in an image
#stored in a file in the .png format. Import this procedure and invoke it, providing as argument the name 
# of a file containing an image in this format, assigning the returned value to variable data.
#An example grayscale image, img01.png is available for download.

#The value of data is a list of lists, and data[y][x] is the intensity of pixel (x,y).
#Pixel (0,0), is at the bottom-left of the image, and pixel(width-1, height-1) is at the top-right.
#The intensity of a pixel is a number between 0 (black) and 255 (white)

#Use a comprehension to assign to a list pts the set of complex numbers x + yi such that the
#image intensity of pixel (x, y) is less than 120, and plot the list pts.

#Solution:
from plotting import plot 
from image import file2image
#We have to know the dimensions of the image.
x-axis = 189 #Length
y-axis = 166 #Width


Solution
pts = [x + (189 - y) * 1j for x in range(166) for y in range(189)[::-1] for intensity in data[y][x] if intensity < 120]
plot(pts, 300)