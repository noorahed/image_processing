#image_processign p.2
#Drawing Shapes


#Import all needed libraries
import cv2 as cv
import os
import numpy as np

#Read_Image
imag_path = r"C:\Users\FTS\OneDrive\Desktop\photos\cat_dog.jpg"

if imag_path is None:
    print('ERROR: Image not found, Chech the path ')
else:
    imag= cv.imread(imag_path)
    print(imag.shape)   #(541, 612, 3)
    cv.imshow('ca&dog', imag)
    cv.waitKey(0)
    
imag0 = imag.copy()


#Drawing Rectangle
imag0 = imag.copy()
rect = cv.rectangle(imag0, (200,300),(510,128),(0,255,0),3)
cv.imwrite('Rectangle.jpg', rect)
cv.imshow('Rectangle', rect)
cv.waitKey(0)

#Drawing Circle
circle = cv.circle(imag, (400,200), 100, (0,0,255), 2)
cv.imwrite("Circle.jpg", circle)
cv.imshow('Circle', circle)
cv.waitKey(0)

#Drawing Ellipse
ellipse= cv.ellipse(imag0,(200,250),(100,50),0,0,360,255,-1)
cv.imwrite("Ellips.jpg", ellipse)
cv.imshow('Ellipse', ellipse)
cv.waitKey(0)

#Drawing Polygon
points = np.array([[90,100],[50,60],[70,20],[50,10]], np.int32)
points= points.reshape((-1,1,2))
cv.polylines(imag0, [points], True, (0,255,255), 3)
cv.imwrite('Polygon.jpg', imag0)
cv.imshow('Polygon', imag0)
cv.waitKey(0)


