#Adjusting the image using neighbour values
import cv2
import numpy as np

imgMatrix = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_4\sugar.png',0) # 0 for grayscale.

#Cloning the matrix, getting the shape (m,n)
adjImgMatrix = imgMatrix
m,n = adjImgMatrix.shape

for i in range(1,m-1): #adjust the size according to kernel (3X3)
    for j in range(1,n-1): #adjust the size according to kernel (3X3)
        accSumOfKernel = 0
        n=0
        # Fetch all neighbours for middle element of a 3x3 kernel
        for k in range(i-1,i+2): 
            for l in range(j-1,j+2):
                n+=1 
                #Calculate sum of all elements
                accSumOfKernel += adjImgMatrix[k,l].astype(int)
        averagepixelValue = (accSumOfKernel - adjImgMatrix[i,j]) / (n-1)
        adjImgMatrix[i,j] = averagepixelValue

cv2.imshow("Original Image",imgMatrix)
cv2.imshow("Transform Image",adjImgMatrix)

cv2.waitKey()
cv2.destroyAllWindows()
                
        

