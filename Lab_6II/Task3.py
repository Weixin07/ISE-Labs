import cv2
import numpy as np
 
def AddSaltPepperNoise(img, noiselevel):
    row, col = img.shape
    NoiseMask = np.zeros(img.shape)
    NoOfNoise = int(img.size * noiselevel)
    
    for i in range(NoOfNoise):
        # random coordinate (x and y)
        y=np.random.randint(0, row - 1)
        x=np.random.randint(0, col - 1)
        # set the pixel to white
        img[y][x] = 255
        #optional
        NoiseMask[y][x] = 255
        cv2.imshow('noise distribution',NoiseMask)
    return img

#read an image (grayscale)
img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6II\grey.jpg',0)
imgNoise = AddSaltPepperNoise(img,0.05)
cv2.imshow('Noise Image',imgNoise)
cv2.waitKey(0)
