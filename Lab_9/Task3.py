import numpy as np
import cv2
from matplotlib import pyplot as plt

parrot = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_9\parrot.jpg')

print("Original Image shape",parrot.shape)

f = plt.figure(figsize=(20,8))
f.add_subplot(2, 4, 1).set_title('Original Image')
plt.imshow(parrot)

lower_reso1 = cv2.pyrDown(parrot)
print("First Lower Pyramid Image shape ",lower_reso1.shape)
f.add_subplot(2, 4, 2).set_title(lower_reso1.shape)
plt.imshow(lower_reso1)

lower_reso2 = cv2.pyrDown(lower_reso1)
f.add_subplot(2, 4, 3).set_title(lower_reso2.shape)
plt.imshow(lower_reso2)

lower_reso3 = cv2.pyrDown(lower_reso2)
f.add_subplot(2, 4, 4).set_title(lower_reso3.shape)
plt.imshow(lower_reso3)

higher_reso2 = cv2.pyrUp(parrot)
f.add_subplot(2, 4, 5).set_title(higher_reso2.shape)
plt.imshow(higher_reso2)

higher_reso3 = cv2.pyrUp(higher_reso2)
f.add_subplot(2, 4, 6).set_title(higher_reso3.shape)
plt.imshow(higher_reso3)

higher_reso4 = cv2.pyrUp(higher_reso3)
f.add_subplot(2, 4, 7).set_title(higher_reso4.shape)
plt.imshow(higher_reso4)

higher_reso5 = cv2.pyrUp(higher_reso4)
f.add_subplot(2, 4, 8).set_title(higher_reso5.shape)
plt.imshow(higher_reso5)

plt.waitforbuttonpress()
