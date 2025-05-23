"""""
Image Gradients


We will see following functions :
cv.Sobel(), cv.Scharr(), cv.Laplacian() etc
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
#Reading image
image_path = r'C:\Users\FTS\OneDrive\Desktop\photos\home.jpg'
img = cv.imread(image_path)
#cv.imshow('home', img)
#cv.waitKey(0)

#Edge detection
laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5) #horizontal edge
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)#vertical edge


# Displaying the images
plt.subplot(2, 2, 1), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))  # Convert BGR to RGB for correct display
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')  # Use sobely here
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()