# mandelbrot.py
# Lab 9
# I pledge my honor that I have abided by the Stevens Honor System.
# Name:Jonathan Joshua

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult(c,n):
    ''' Returns the product of c times n but without multiplication. '''
    a=0
    for x in range(n):
        a+=c
    return a
        
def update(c,n):
    ''' Starts a new value, z at zero, and then repeatedly updates the value of z using the assignment statement z = z**2 + c for a total of n times. Function returns the final value of z.  '''
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

def inMSet(c,n):
    ''' Takes as input a complex number c and an integer n and returns a Boolean True or False. '''
    z = 0
    for x in range(n):
        z = z**2 + c
        if abs(z)>2: return False
    return True

def weWantThisPixel(col, row):
    ''' a function that returns True if we want
the pixel at col, row and False otherwise '''
    if col%10 == 0 and  row%10 == 0:
        return True
    else:
        return False

def test():
    ''' a function to demonstrate how to create and save a png image '''
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
    
def scale(pix, pixMax, floatMin, floatMax):
    ''' scale takes in
pix, the CURRENT pixel column (or row)
pixMax, the total # of pixel columns
floatMin, the min floating-point value
floatMax, the max floating-point value
scale returns the floating-point value that
corresponds to pix '''
    return (pix / pixMax) * (floatMax - floatMin) + floatMin

def mset():
    ''' Will generate images of width width and height height with that computes the set of points in the Mandelbrot set on the complex plane and creates a bitmap of them. '''
    width = 300
    height = 200
    x_Min = -2.0
    y_Min = -1.0
    x_Max = 1.0
    y_Max = 1.0
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        x = scale(col,width,x_Min,x_Max)
        for row in range(height):
            y = scale(row,height,y_Min,y_Max)
            if inMSet( x + y*1j,25 ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
