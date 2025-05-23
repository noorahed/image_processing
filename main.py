"""""
This code presrnt the basic of image processing using OpenCV
read,show,save,scale,resising,gray scale,playing with colors,fliping,cropping, drawing shapes, adding text

"""
import cv2 as cv
import os

image_path= r"CC:\VScode\images\catt.jpg"
print('image_path:', os.path.abspath(image_path))

image = cv.imread(image_path)

if image is None:
    print("Error: Image not found")
else:
    cv.imread(image_path)
    cv.waitKey(0)  
    
#cv.imwrite('new_image.jpg', image)
    
cv.imshow('cat', image)
cv.waitKey(0)


#Resize and Rescale  images 
#to prevent the image from being too large or too small

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(image)

#cv.imwrite('resized_image.jpg', resized_image)
cv.imshow('image', resized_image)
cv.waitKey(0)

#image gray scale

image_gray= cv.cvtColor(image, cv.COLOR_BGR2GRAY)
print(image_gray.shape)
#cv.imwrite('image_gray.jpg', image_gray)
cv.imshow('gray image', image_gray)
cv.waitKey(0)


#playing with RGP colors
image[:,:,0] =0
#cv.imwrite('image_red.jpg', image)
cv.imshow('RGP colors', image)
cv.waitKey(0)

image_flip  = cv.flip(image,-1) # 0 for vertical flip, 1 for horizontal flip, -1 for both
cv.imshow('flip image', image_flip)
cv.waitKey(0)


#cropping images
image_crop = image[100:300, 200:500]

#cv.imwrite('image_crop.jpg', image_crop)

cv.imshow('crop image', image_crop)
cv.waitKey(0)

#Drawing shapes
#Drawing a Rectangle
'''We can draw a rectangle on the image using rectangle() method. It takes in 5 arguments: 

Image 
Top-left corner co-ordinates
Bottom-right corner co-ordinates
Color (in BGR format)
Line width
'''
#copying the original image
output = image.copy()

# Define rectangle coordinates (adjust to fit within the image)
x1, y1 = 100, 100  # top-left corner
x2, y2 = 400, 403 # bottom-right corner (max coordinates within image)
#using rectangle() function to create a rectangle
rectangle = cv.rectangle(output, (x1, y1),
                          (x2, y2), (255, 0, 0), 2)
# Display the result
#cv.imwrite('image_rectangle.jpg', output)
cv.imshow("Image with Rectangle", output)
cv.waitKey(0)
'''
The rectangle's bottom-right corner (x2, y2) is now set to (1100, 735), which corresponds to
the image's maximum width and height.

The top-left corner (x1, y1) can remain as (600, 400) because
it’s within bounds.
'''

'''Displaying text
It is also an in-place operation that can be done using the putText() method of OpenCV module. It takes in 7 arguments:

Image
Text to be displayed
Bottom-left corner co-ordinates, from where the text should start
Font
Font size
Color (BGR format)
Line width
'''

#copy the original image
output2 = image.copy()

#Adding the text using putText()function
text = cv.putText(output2, 'Cat',(80,100),
                   cv.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)

cv.imwrite('image_text.jpg', text)
cv.imshow("Text image", text)
cv.waitKey(0)