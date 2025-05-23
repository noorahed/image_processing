import cv2

# Load the 'jordan.webp' image
img = cv2.imread('C:/VScode/images/jordan.webp', 1)

# Function to display the coordinates of the points clicked on the image
def click_event(event, x, y, flags, params):

    # Checking for left mouse click
    if event == cv2.EVENT_LBUTTONDOWN:
        # Displaying the coordinates on the Shell
        print(x, ' ', y)

        # Displaying the coordinates on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' + str(y), (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', img)

    # Checking for right mouse click
    if event == cv2.EVENT_RBUTTONDOWN:
        # Displaying the coordinates on the Shell
        print(x, ' ', y)

        # Displaying the color values at the coordinates
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x, y), font, 1, (255, 255, 0), 2)
        cv2.imshow('image', img)

# Driver function
if __name__ == "__main__":

    # Displaying the image
    cv2.imshow('image', img)

    # Setting mouse handler for the image and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # Wait for a key to be pressed to exit
    cv2.waitKey(0)

    # Close the window
    cv2.destroyAllWindows()
