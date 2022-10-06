import pywt
from pywt import wavedec
import numpy as np
import matplotlib.pyplot as plt
import skimage.measure 

noisy = plt.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_9\Fruit.jpg')

# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
LL, (LH, HL, HH) = pywt.dwt2(noisy, 'haar')
fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(20, 15))
for i, a in enumerate([LL, LH, HL, HH]):
    ax[i].imshow(a, cmap=plt.cm.gray)
    ax[i].set_title(titles[i], fontsize=10)
    ax[i].set_xticks([])
    ax[i].set_yticks([])

fig.tight_layout()
plt.show()

# denoising
titles = ['noisy', 'denoised']
denoised = pywt.idwt2((LL, (LH, HL, None)), 'haar')
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 10))
for i, a in enumerate([noisy, denoised]):
    ax[i].imshow(a, cmap=plt.cm.gray)
    ax[i].set_title(titles[i], fontsize=10)
    ax[i].set_xticks([])
    ax[i].set_yticks([])

fig.tight_layout()
plt.show()

#print('PSNR value: {}'.format(compare_psnr(noisy, denoised)))

