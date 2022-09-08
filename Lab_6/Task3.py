import cv2 as cv
import numpy as np

img = cv.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6\damage.jpeg',0)
#img = cv.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6\damage.jpeg')
#mask = np.zeros(img.shape, img.dtype)
#cv.imwrite('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6\mask.png', mask)

#mannually modify the mask as per the noise in the original image
#load the updated mask
mask = cv.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6\mask3.jpg',0)

res = cv.inpaint(img, mask, 3, cv.INPAINT_TELEA)
cv.imshow("Gray Image", img)
cv.imshow("improved Image", res)

cv.waitKey()
cv.destroyAllWindows()
