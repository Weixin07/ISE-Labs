import numpy as np
import cv2
from matplotlib import pyplot as plt
 
# Opening the image 
img = cv2.imread("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_5\Task3.png")

img = cv2.resize(img, (400,400))

#create kernel
kernel = np.ones((5,5),np.float32)/25

#use openCV2 filter (neighbourhood method)
#   cv.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]] ) ->    dst
dst = img - cv2.filter2D(img,-1,kernel) +127 #same depth as the source.

#blur (low-pass filter kernel)
blur = cv2.blur(img,(10,10))

#display the result.
plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(blur),plt.title('Averaging - low')
plt.xticks([]), plt.yticks([])

plt.show()
