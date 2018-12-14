# Harry Tian
# Image processing: defining functions for four filters
import sys
from cImage import *

def oneColor(image, color):
    #create a new copy of the image 
    oneCIm = image.copy()
    numPix = image.getNumPixels()
    # set every pixel in the new oneColor image to have only the red, green,
    # or blue aspects of the original image depending on the color argument
        # loop through each pixel in the original image
    if color == "r":
        for i in range(numPix):
            p = image.getPixel1D(i)
            p.green = 0
            p.blue = 0
            oneCIm.setPixel1D(i, p)
    if color == "g":
        for i in range(numPix):
            p = image.getPixel1D(i)
            p.red = 0
            p.blue = 0
            oneCIm.setPixel1D(i, p)
    if color == "b":
        for i in range(numPix):
            p = image.getPixel1D(i)
            p.green = 0
            p.red = 0
            oneCIm.setPixel1D(i, p)
    return oneCIm

#Filter #2: negate
def negate(image):
    #create a new copy of the image 
    negateIm = image.copy()
    numPix = image.getNumPixels()
    # set every pixel in the new negate image to its negative form
        # loop through each pixel in the original image
    for i in range(numPix):
        p = image.getPixel1D(i)
        p.red = 255 - p.getRed()
        p.green = 255 - p.getGreen()
        p.blue = 255 - p.getBlue()
        negateIm.setPixel1D(i, p)
    return negateIm

# Filter #3: scale
def scale(image, scale_factor):
    #change scale_factor from string to float
    scale_factor = float(scale_factor)
    #create a new canvas to draw the scale image
    width = int(image.getWidth()*scale_factor)
    height = int(image.getHeight()*scale_factor)
    scaleIm = EmptyImage(width,height)
    # set every pixel in the new scale image to its scale form
        # loop through each pixel in the original image
    for x in range(width):
        for y in range(height):
            p = image.getPixel(int(x/scale_factor),int(y/scale_factor))
            scaleIm.setPixel(x,y,p)
    return scaleIm

# Filter #4: blur'''
def blur(image,radius):
    #change radius from string to int
    radius = round(float(radius))
    #create a new copy of the image
    # set variables for future use
    blurIm = image.copy()
    width = image.getWidth()
    height = image.getHeight()
    # loop through each pixel in the original image
    # set square in middle to exclude edge cases:
    for x in range(radius,width-radius):
        for y in range(radius,height-radius):
            p = image.getPixel(x,y)
            p2_red = 0
            p2_green = 0
            p2_blue = 0
            numPix = 0
            #extract the color statistics from square's every pixel
            for a in range(x-radius,x+radius):
                for b in range(y-radius,y+radius):
                    p2 = image.getPixel(a,b)
                    p2_red += p2.getRed()
                    p2_green += p2.getGreen()
                    p2_blue += p2.getBlue()
                    numPix += 1
            #get the average color of every pixel 
            p2 = image.getPixel1D(x)
            p2.red = p2_red//numPix
            p2.green = p2_green//numPix
            p2.blue = p2_blue//numPix
            #paint the pixels in the square
            blurIm.setPixel(x,y,p2)
    # deal with non-square edge cases: divide outer square into four parts:
    for x in range(radius):
        for y in range(height):
            p = image.getPixel(x,y)
            p2_red = 0
            p2_green = 0
            p2_blue = 0
            numPix = 0
            #extract the color statistics from square's every pixel
            for a in range(radius):
                start = y - radius
                if start < 0:
                    start = 0
                end = y + radius
                if end > height:
                    end = height
                for b in range(start,end):
                    p2 = image.getPixel(a,b)
                    p2_red += p2.getRed()
                    p2_green += p2.getGreen()
                    p2_blue += p2.getBlue()
                    numPix += 1
            #get the average color of every pixel 
            p2 = image.getPixel1D(x)
            p2.red = p2_red//numPix
            p2.green = p2_green//numPix
            p2.blue = p2_blue//numPix
            #paint the pixels in the square
            blurIm.setPixel(x,y,p2)
    for x in range(width-radius,width):
        for y in range(height):
            p = image.getPixel(x,y)
            p2_red = 0
            p2_green = 0
            p2_blue = 0
            numPix = 0
            #extract the color statistics from square's every pixel
            for a in range(width-radius,width):
                start = y - radius
                if start < 0:
                    start = 0
                end = y + radius
                if end > height:
                    end = height
                for b in range(start,end):
                    p2 = image.getPixel(a,b)
                    p2_red += p2.getRed()
                    p2_green += p2.getGreen()
                    p2_blue += p2.getBlue()
                    numPix += 1
            #get the average color of every pixel 
            p2 = image.getPixel1D(x)
            p2.red = p2_red//numPix
            p2.green = p2_green//numPix
            p2.blue = p2_blue//numPix
            #paint the pixels in the square
            blurIm.setPixel(x,y,p2)
    for x in range(radius,width-radius):
        for y in range(radius):
            p = image.getPixel(x,y)
            p2_red = 0
            p2_green = 0
            p2_blue = 0
            numPix = 0
            #extract the color statistics from square's every pixel
            for a in range(x-radius,x+radius):
                for b in range(radius):
                    p2 = image.getPixel(a,b)
                    p2_red += p2.getRed()
                    p2_green += p2.getGreen()
                    p2_blue += p2.getBlue()
                    numPix += 1
            #get the average color of every pixel 
            p2 = image.getPixel1D(x)
            p2.red = p2_red//numPix
            p2.green = p2_green//numPix
            p2.blue = p2_blue//numPix
            #paint the pixels in the square
            blurIm.setPixel(x,y,p2)
    for x in range(radius,width-radius):
        for y in range(height-radius,height):
            p = image.getPixel(x,y)
            p2_red = 0
            p2_green = 0
            p2_blue = 0
            numPix = 0
            #extract the color statistics from square's every pixel
            for a in range(x-radius,x+radius):
                for b in range(height-radius,height):
                    p2 = image.getPixel(a,b)
                    p2_red += p2.getRed()
                    p2_green += p2.getGreen()
                    p2_blue += p2.getBlue()
                    numPix += 1
            #get the average color of every pixel 
            p2 = image.getPixel1D(x)
            p2.red = p2_red//numPix
            p2.green = p2_green//numPix
            p2.blue = p2_blue//numPix
            #paint the pixels in the square
            blurIm.setPixel(x,y,p2)
    return blurIm

def main():
    # open a picture using command line (2nd argument)
    origImage = FileImage(sys.argv[1])
    #use its dimensions to make a suitably sized window
    win = ImageWin("oneColor and negate",origImage.getWidth()*3 + 3,origImage.getHeight())
    origImage.draw(win)
    
    # draw the oneColor version of origImage to the right of origImage
    # determine color argument using command line (3rd argument)
    oneColorImage = oneColor(origImage,sys.argv[2])
    oneColorImage.setPosition(origImage.getWidth()+1,0)
    oneColorImage.draw(win)

    # draw the negate version of origImage to the right of oneColor image
    negateImage = negate(origImage)
    negateImage.setPosition(origImage.getWidth()*2 + 2,0)
    negateImage.draw(win)    
main()

# Ask the user to hit enter to continue to the next set.
input("enter to continue to next set")

def main2():
    # draw the scale version of orignal image to the right of origImage
    # determine scale argument using command line (4th argument)
    origImage = FileImage(sys.argv[1])
    scaleImage = scale(origImage,sys.argv[3])
    # create different canvases depending on whether scale shrinks or grows
    if float(sys.argv[3]) > 1:
        win = ImageWin("scale and blur",scaleImage.getWidth() + origImage.getWidth()*2,scaleImage.getHeight() + origImage.getHeight()*2)
    else:
        win = ImageWin("scale and blur",origImage.getWidth()*3 + 3,origImage.getHeight())        
    origImage.draw(win)
    scaleImage.setPosition(origImage.getWidth() + 2,0)
    scaleImage.draw(win)
    
    # draw the blur version of orignal image 
    # determine blur radius using command line (5th argument)    
    blurImage = blur(origImage,sys.argv[4])
    # draws blurImage in different positions depneding on canvas
    if float(sys.argv[3]) > 1:
        blurImage.setPosition(0,origImage.getHeight()+1)
    else:
        blurImage.setPosition(origImage.getWidth() + 2 + scaleImage.getWidth(),0)
    blurImage.draw(win)
    # Ask the user to hit enter to quit
    input("enter to quit")
main2()
