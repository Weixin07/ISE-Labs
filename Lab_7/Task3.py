import cv2
import numpy as np

# Reading the image
img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_7\sunflower.jpg')

#Resizing the image
img = cv2.resize(img, (400,400))

# convert to hsv colorspace
hsvColor = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgbColor = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
labColor = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
labColor = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

oriNhsv = np.concatenate((img,hsvColor,rgbColor, labColor),axis=1)
cv2.imshow("color space-ori, hsv, rgb, lab",oriNhsv)

black_col_img = np.zeros(img.shape[:2], dtype="uint8")

red_img = cv2.merge([black_col_img, black_col_img,img[:,:,2]])

blue_img = cv2.merge([img[:,:,0] ,black_col_img, black_col_img])

green_img = cv2.merge([black_col_img, img[:,:,1] ,black_col_img])

channels = np.concatenate((blue_img,green_img,red_img), axis=1)
cv2.imshow("Color channels-blue,green, red", channels)

cv2.waitKey(0)
cv2.destroyAllWindows()
