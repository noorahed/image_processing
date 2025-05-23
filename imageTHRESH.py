"""""
this code present Thresholding technique 

To create binary images (images with only two colors: black and white)
By segmenting an image based on pixel intensity values.
It helps to highlight specific features, remove noise, and simplify images.
"""
#needed libraries
import os
import cv2 as cv
from matplotlib import pyplot as plt


folder_path = r'C:\Users\FTS\OneDrive\Desktop\photos'
image_name = 'home.jpg'

def get_image_by_name(folder_path,image_name):
    for filename in os.listdir(folder_path):
        if filename == image_name:
            return os.path.join(folder_path, filename)
    return None

image_path = get_image_by_name(folder_path, image_name)

home = cv.imread(image_path)
if home is None:
    print('ERROR: Image not found')
else:
    home_gray = cv.cvtColor(home, cv.COLOR_BGR2GRAY) #covert image to gray scale
    
    ret,thresh1 = cv.threshold(home_gray, 127,255, cv.THRESH_BINARY)
    ret,thresh2 = cv.threshold(home_gray, 127,255, cv.THRESH_BINARY_INV)
    ret,thresh3 = cv.threshold(home_gray, 127,255, cv.THRESH_TRUNC)
    ret,thresh4 = cv.threshold(home_gray, 127,255, cv.THRESH_TOZERO)
    ret,thresh5 = cv.threshold(home_gray, 127,255, cv.THRESH_TOZERO_INV)
    
    titles = ['home', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [home, thresh1, thresh2, thresh3, thresh4, thresh5]
    
    #Display images
    for i in range(6):
        plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
        """""
        save_path = os.path.join(output_folder, f'{titles[i]}.png')  # Save as PNG (you can change the format)
        plt.savefig(save_path)
        plt.clf()
        """
    plt.show()
    
cv.imshow('home_gray', home_gray)
cv.waitKey(0)


#AdaptiveThresholding
#Note: applies a single threshold value to the entire image

img = cv.medianBlur(home_gray, 5)

ret,th1 = cv.threshold(img, 127,255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

titles2= ['home', 'Global Thresholding (v=127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images2 = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images2[i], 'gray')
    plt.title(titles2[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()

print("after")