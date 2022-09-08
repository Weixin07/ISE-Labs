#By using a continuos variable to draw the histogram makes the noise much more evenly distributed.
import cv2
import numpy as np
import matplotlib.pyplot as plot
from scipy.stats import norm
 
#read an image (grayscale)
img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6II\grey.jpg',0)

# Generate Gaussian noise
#Draw random samples from a normal (Gaussian) distribution
gauss = np.random.normal(0,1,img.size)
plot.hist(gauss, bins=25, density=True, alpha=0.6, color='b')

#mean and standard deviation
mu, std = norm.fit(gauss) 
# Plot the PDF (probability density function)
xmin, xmax = plot.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plot.plot(x, p, 'k', linewidth=2)
plot.show()

#Gives a new shape to an array without changing its data.
gauss = gauss.reshape(img.shape[0],img.shape[1]).astype('uint8')
cv2.imshow('noise',gauss)

# Add the Gaussian noise to the image
img_gauss = cv2.add(gauss,img)
# Display the image
cv2.imshow('Noise Image',img_gauss)

cv2.waitKey(0)
