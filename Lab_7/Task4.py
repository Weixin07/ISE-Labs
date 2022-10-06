import cv2
import numpy as np

# Reading the image
img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_7\sunflower.jpg')

#Resizing the image
img = cv2.resize(img, (400,400))

# convert to hsv colorspace
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(hsv)
SingleHSV = np.concatenate((h,s,v),axis=1)

# Hue range is [0,179], 
# Saturation range is [0,255] 
# Intensity/ Value range is [0,255].

# shift the hue
huevalue = 100 
newH = cv2.add(h, huevalue)
newHSV = cv2.merge([newH, s, v])

SingleONHSV = np.concatenate((hsv, newHSV),axis=1)

#convert back to color
newImage = cv2.cvtColor(newHSV, cv2.COLOR_HSV2RGB)

SingleONImage = np.concatenate((img, newImage),axis=1)

#show Hue Saturation Value
cv2.imshow("HSV", SingleONHSV)
cv2.imshow("Images", SingleONImage)
cv2.imshow("Hue-Saturation-Value", SingleHSV)

cv2.waitKey(0)
cv2.destroyAllWindows()
