import cv2
import numpy as np

# Reading the image
img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_7\sunflower.jpg')

#Resizing the image
img = cv2.resize(img, (400,400))

# Split the image into 3 channels
b,g,r = cv2.split(img)

#The colours is still in grey channels
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.imshow("Blue", b)

# Merge the channel with 2D array 
zeros = np.zeros(img.shape[:2], dtype="uint8")
r = cv2.merge([zeros, zeros, r])
g = cv2.merge([zeros, g, zeros])
b = cv2.merge([b, zeros, zeros])

# Showing the output
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.imshow("Blue", b)

imagecolor = np.concatenate((r,g,b), axis=1)
# Showing the output
cv2.imshow("Red-Green-Blue", imagecolor)

cv2.waitKey(0)
cv2.destroyAllWindows()
