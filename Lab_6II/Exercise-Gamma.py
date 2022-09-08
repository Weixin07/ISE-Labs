import cv2
import numpy as np
import matplotlib.pyplot as plot
 
img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6II\grey.jpg',0)

gamma = np.random.gamma(3,20,img.size)

plot.hist(gamma, bins=25, density=True, alpha=0.6, color='b')
plot.show()

gamma = gamma.reshape(img.shape[0],img.shape[1]).astype('uint8')
cv2.imshow('noise',gamma)

img_gamma = cv2.add(gamma,img)

cv2.imshow('Noise Image',img_gamma)
cv2.waitKey(0)
