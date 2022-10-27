import cv2
import numpy as np

img = cv2.imread("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_12\stonktoken.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

#set structuring element    
kernel = np.ones((3,3),np.uint8)

#reduce the pixel (foreground)
imgErosion = cv2.erode(imgGray,kernel,iterations = 1)
updatedErosion = cv2.erode(imgGray,kernel,iterations = 3)
#Add pixel (foreground)
imgDilation = cv2.dilate(imgGray,kernel,iterations = 1)
updatedDilation = cv2.dilate(imgGray,kernel,iterations = 3)

cv2.imshow('Erosion Operation - reduce', imgErosion)
cv2.imshow('Updated Erosion', updatedErosion)
cv2.imshow('Dilation Operation - increase', imgDilation)
cv2.imshow('Updated Dilation', updatedDilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
