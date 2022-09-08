import cv2
import numpy as np
import matplotlib.pyplot as plot
 
#read an image (grayscale)
img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6II\grey.jpg',0)

# Generate Gaussian noise
gauss = np.random.normal(0,1,img.size)

# plot histogram of the noise
plot.hist(gauss, bins=25, density=True, alpha=0.6, color='b')

# show the histogram of the noise
#plot.show(block=True)
plot.show()

#Gives a new shape to an array without changing its data.
gauss = gauss.reshape(img.shape[0],img.shape[1]).astype('uint8')

#show the noise in image form
cv2.imshow('noise',gauss)

# Add the Gaussian noise to the image
img_gauss = cv2.add(gauss,img)

# Display the image
cv2.imshow('Noise Image',img_gauss)
cv2.waitKey(0)
