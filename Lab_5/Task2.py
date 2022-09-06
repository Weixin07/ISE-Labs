import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

im = cv.imread("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_5\Figure.png",0)
plt.figure(figsize=(5,5))
plt.imshow(im, cmap="gray")
plt.axis('off')
plt.show()

Ff1 = np.fft.fft2((im).astype(float))
Ff2 = np.fft.fftshift(Ff1)
plt.figure(figsize=(5,5))
plt.imshow((20*np.log10( 0.1 + Ff2)).astype(int), cmap="gray")
plt.show()

(w, h) = im.shape
half_w, half_h = int(w/2), int(h/2)

# high pass filter
n = 25
Ff2[half_w-n:half_w+n+1,half_h-n:half_h+n+1] = 0 # select all but the range (low) frequencies
plt.figure(figsize=(5,5))
plt.imshow((20*np.log10( 0.1 + Ff2)).astype(int), cmap="gray")
plt.show()

im1 = np.fft.ifft2(np.fft.ifftshift(Ff2)).real
plt.figure(figsize=(5,5))
plt.imshow(im1, cmap='gray')
plt.axis('off')
plt.show()
