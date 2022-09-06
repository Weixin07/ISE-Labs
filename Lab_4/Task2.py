import cv2
import numpy as np

#Method 1: Using LogTransform to increase value of image matrix
def LogTransform(imgMatrix):
    # scaling of image (Log transformation of an image)
    # c = 255/(log (1 + m))
    c = 255/(np.log(1 + np.max(imgMatrix)))
    logTrans = c * np.log(1 + imgMatrix)
    #8bits
    return np.array(logTrans, dtype = np.uint8)

#Using method 2: Using functions to stretch the pixel intensity value 
def StretchPixelIntensity(imgMatrix):
     #adjust pixel value over a range (min, max))
    adjustImgmatrix= (((imgMatrix-imgMatrix.min())/(imgMatrix.max()-imgMatrix.min())) * 255)
    return np.array(adjustImgmatrix, dtype = np.uint8)

#Method 3: Using function to adjust pixel intensity value
def AdjustPixelIntensity(imgMatrix, vals):
    
    adjustImgmatrix = imgMatrix + vals #max is 255 exceed value restart from 0
    #exceed 255 (kept as 255)
    if vals>=0:
        adjustImgmatrix = [np.where(i < vals, 255, i) for i in adjustImgmatrix]
    elif vals<=0:
        adjustImgmatrix = [np.where(vals < i, 0, i) for i in adjustImgmatrix]

    return np.array(adjustImgmatrix, dtype = np.uint8)

#read the image (grayscale color - flag 0)
imgMatrix = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_4\Task1n2n5.png',0) # 0 for grayscale.
#imgMatrix = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_4\sugar.png',0) # 0 for grayscale.

#Result from multiple methods
#result = LogTransform(imgMatrix) #Becomes brighter
#result = StretchPixelIntensity(imgMatrix) #Becomes darker
#result = AdjustPixelIntensity(imgMatrix,50) #Becomes brighter
#result = AdjustPixelIntensity(imgMatrix,255) 
#result = AdjustPixelIntensity(imgMatrix,300) #Anything more than 255 reset to 255 (supposedly)
result = AdjustPixelIntensity(imgMatrix,-20) #Anything less than 0 the condition is set back to 0
#cv2.imshow("Original Image",imgMatrix)
#cv2.imshow("Transform Image",result)
concatImage = np.concatenate((imgMatrix, result), axis=1)
cv2.imshow("Images",concatImage)

#print(result)
cv2.waitKey()
cv2.destroyAllWindows()
