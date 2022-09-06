from PIL import Image
import cv2
import numpy as np

img = cv2.imread("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_3\grayscaleCat.jpg",0)
#before
cv2.imshow("original image", img)
print('Image size:', img.size)
print('Image shape:', img.shape)

#create sampling
[m, n] = img.shape
sampleRate = 5
img_array = np.zeros((m//sampleRate, n//sampleRate), dtype=np.int8)

#Using numpy
#As numpy is for statistics and others, thus it works more as editing directly from the rows and columns
#If sizing up, the codes will increase the numbers of rows and columns
#If sizing down, the codes will decrease the numbers of rows and columns
sampling_array = img_array
for i in range(0, m, sampleRate):
    for j in range(0, n, sampleRate):
        try:
            sampling_array[i//sampleRate][j//sampleRate] = img[i][j]
        except: 
            pass
print('Down Sampled (reduce quality):')
sampling_image=Image.fromarray(sampling_array)
sampling_image.show()

#Here, its using openCV
#Since it deals with images, with built-in functions
#Thus, we need to only call the function
# Image up sampling 
upSample = cv2.pyrUp(img)
# Display images 
cv2.imshow('Image Up Sampling', upSample)
cv2.waitKey()
cv2.destroyAllWindows()

#Similarly, this uses pillow
#Calling the function would also be able to achieve what we want
print("Apply Quantization")
quantizeImage50=Image.fromarray(img) #from array back to image
quantizeImage50.quantize(25)
quantizeImage50.show()

quantizeImage100=Image.fromarray(img)
quantizeImage100.quantize(100)
quantizeImage100.show()

quantizeImage200=Image.fromarray(img)
quantizeImage200.quantize(200)
quantizeImage200.show()

