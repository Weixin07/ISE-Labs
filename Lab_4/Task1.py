import numpy as np
import cv2
from matplotlib import pyplot

imgMatrix = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_4\Task1n2n5.png',0) # 0 for grayscale.
#imgMatrix = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_4\sugar.png',0) # 0 for grayscale.

#get the histogram of the flatten image (1D)
hist , bins = np.histogram(imgMatrix.flatten(),256,[0,256])

#Compute the histogram of a dataset(array, bin, range, color)
pyplot.hist(imgMatrix.flatten(),256,[0,256], color = 'b')
#range of values (x-axis)
pyplot.xlim([0,256])
#show the plot
pyplot.show()

#Equalising the Histogram
#Method 1: create a function to equalize using numpy (manual calculation)
def histEqual_np(imageMatrix, number_bins=256):
    #compute history of imageMatrix; return values of the histogram and bins edge
    image_histogram, bins = np.histogram(imageMatrix.flatten(), number_bins, density=True)
    #cumulative sum of the elements along a given axis.
    CumSumOfEle = image_histogram.cumsum()
    # normalize
    CumSumOfEle = (number_bins-1) * CumSumOfEle / CumSumOfEle[-1] 
    #interpolation for monotonically increasing sample points.
    #param:data, x coordinate (sequence), y coordinate (sequence)
    Equal_ImageMatrix = np.interp(imageMatrix.flatten(), bins[:-1], CumSumOfEle)
    return Equal_ImageMatrix.reshape(Equal_ImageMatrix.shape)
 
#Method 2: Create a function to use Opencv built in qualizehist function
def histEqual_cv2(imageMatrix):
    return cv2.equalizeHist(imageMatrix) #for 8bits

#Calling the function for method 1
equalizeImg = histEqual_np(imgMatrix)

#Calling the function for method 2
#equalizeImg = histEqual_cv2(imgMatrix) #for 8bits

#plot the equalized histogram
hist , bins = np.histogram(equalizeImg.flatten(),256,[0,256]) 
pyplot.hist(equalizeImg.flatten(),256,[0,256], color = 'r')
pyplot.xlim([0,256])
pyplot.show()
