import cv2
import numpy as np
import matplotlib.pyplot as plot
 
img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6II\grey.jpg',0)

poisson = np.random.poisson(img)

plot.hist(poisson)
plot.show()

poisson = poisson.reshape(img.shape[0],img.shape[1]).astype('uint8')
cv2.imshow('noise',poisson)

img_poisson = cv2.add(poisson,img)

cv2.imshow('Noise Image',img_poisson)
cv2.waitKey(0)
