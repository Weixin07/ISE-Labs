import cv2
import numpy as np

img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_4\sugarBrightnessAdjusted.png')
#img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_4\Task4.png')

cv2.imshow("Original_img", img) 

# calculates absolute values and convert to 8bits
#alpha => brightness (1-3), beta => contrast (1-100)
updatedImg = cv2.convertScaleAbs(img, alpha=2, beta=100)
#updatedImg = cv2.convertScaleAbs(img, alpha=2, beta=30)
cv2.imshow('ConvertScale Image', updatedImg)

alpha=2
beta=40
#addWeighted use for blending both image  alpha, beta and gamma. adjust gradient
updatedImg1=cv2.addWeighted(img,alpha,np.zeros(img.shape, img.dtype),0,beta)
cv2.imshow('addWeighted Image', updatedImg1)

cv2.waitKey(0)
cv2.destroyAllWindows()
