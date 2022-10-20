import matplotlib.pyplot as plt
from PIL import Image
import pywt

myimage = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_11\sunflower.jpg").convert("RGB")

#convert to 8-bit pixels, black and white 
myimage = myimage.convert("L")

#applying a digital wavelet transform
# Apply Wavelet transform of image, and plot approximation and details
print(pywt.wavelist())

coeffs = pywt.dwt(myimage, 'haar')
(cA, cD) = coeffs

#figure width and height in inches
fig1 = plt.figure(figsize=(10, 2))
titles = ['Approximation', 'Detail']
for i, a in enumerate([cA,cD]):
    ax = fig1.add_subplot(1, 2, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])

fig1.tight_layout()
plt.waitforbuttonpress()

#2D Discrete Wavelet Transform.
#pywt.dwt2(data, wavelet, mode='symmetric', axes=(-2, -1))
#return Approximation, horizontal detail, vertical detail, diagonal detail coefficients
coeffs2 = pywt.dwt2(myimage, 'haar')
#(cA, (cH, cV, cD)) : tuple
cA, (cH, cV, cD) = coeffs2

fig = plt.figure(figsize=(12, 3))

titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']

for i, a in enumerate([cA,cH, cV, cD]):
    ax = fig.add_subplot(1, 4, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])

fig.tight_layout()

plt.waitforbuttonpress()
