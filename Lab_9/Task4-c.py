from skimage import data
from skimage.transform import rescale
import cv2

image = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_9\parrot.jpg')
rescale(image, 0.1).shape
(51, 51)
rescale(image, 0.5).shape
(256, 256)

cv2.imshow('Resized',image)
cv2.waitKey(0)
