import cv2
import numpy as np
from PIL import Image, ImageFilter

#import ori image
imgMatrix = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_8\week8TutorialImage.jpg',0) # 0 for grayscale.
imageMatrixResized = cv2.resize(imgMatrix, (300,300))
imageMatrixAdjusted = cv2.cvtColor(imageMatrixResized,cv2.COLOR_GRAY2BGR)

#Copy 1 - Increase Brightness
def AdjustPixelIntensity(imgMatrix, vals):    
    adjustImgmatrix = imgMatrix + vals 
    if vals>=0:
        adjustImgmatrix = [np.where(i < vals, 255, i) for i in adjustImgmatrix]
    elif vals<=0:
        adjustImgmatrix = [np.where(vals < i, 0, i) for i in adjustImgmatrix]

    return np.array(adjustImgmatrix, dtype = np.uint8)

imgMatrix = cv2.resize(imgMatrix, (300,300))
copy1result = AdjustPixelIntensity(imgMatrix,50)
copy1 = cv2.cvtColor(copy1result,cv2.COLOR_GRAY2BGR)

# concatImage = np.concatenate((imgMatrix, result), axis=1)
# cv2.imshow("Images",concatImage)

#Copy 2 - Using Histogram Equalisation Method to Improve Quality
imgMatrix = cv2.resize(imgMatrix, (300,300))

def histEqual_cv2(imageMatrix):
    return cv2.equalizeHist(imageMatrix)

copy2result = histEqual_cv2(imgMatrix)
copy2 = cv2.cvtColor(copy2result,cv2.COLOR_GRAY2BGR)

# concatImage = np.concatenate((imgMatrix, equalizeImg), axis=1)
# cv2.imshow("Images",concatImage)

#Copy 3 - Use Filtering Method to Increase Quality (Colour)
colourImage = Image.open('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_8\week8TutorialImage.jpg')
newImage = colourImage.resize((300, 300))
copy3 = newImage.filter(ImageFilter.DETAIL)

# concatImage = np.concatenate((newImage, copy3), axis=1)
# cv2.imshow("Images",concatImage)

#Copy 4 - Use Split to Improve Quality
colourImage = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_8\week8TutorialImage.jpg')
newImage = cv2.resize(colourImage, (300,300))

hsv = cv2.cvtColor(newImage, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
SingleHSV = np.concatenate((h,s,v),axis=1)

intensityvalue = 50
newV = cv2.add(v, intensityvalue)
newHSV = cv2.merge([h, s, newV])

copy4 = cv2.cvtColor(newHSV, cv2.COLOR_HSV2BGR)

# cv2.imshow("Ori", newImage)
# cv2.imshow("Adjusted Pic", adjusted)

#Copy 5 - Add All Results Together
concatImage = np.concatenate((imageMatrixAdjusted, copy1, copy2, copy3, copy4), axis=1)
cv2.imshow("Ori - Brightness - Histogram Equalization - Filtering - Split",concatImage)

cv2.waitKey()
cv2.destroyAllWindows()
