from skimage import restoration as res
import matplotlib.pyplot as plt 
import cv2

#read gray
img = cv2.imread("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_9\Fruit.jpg",0)

fig = plt.figure(figsize=(10, 5))
fig.add_subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original")

result = res.denoise_wavelet(img, wavelet='haar')
fig.add_subplot(1, 2, 2)
plt.imshow(result)
plt.title("result")

plt.waitforbuttonpress()
