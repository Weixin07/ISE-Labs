import cv2
import matplotlib.pyplot as plt
img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_8\week8TutorialImage.jpg',0) # 0 for grayscale.

sr = cv2.dnn_superres.DnnSuperResImpl_create()

path = "ESPCN_x3.pb"

sr.readModel(path)

sr.setModel("espcn",3)

result = sr.upsample(img)

# Resized image
resized = cv2.resize(img,dsize=None,fx=3,fy=3)

plt.figure(figsize=(12,8))
plt.subplot(1,3,1)
# Original image
plt.imshow(img[:,:,::-1])
plt.subplot(1,3,2)
# SR upscaled
plt.imshow(result[:,:,::-1])
plt.subplot(1,3,3)
# OpenCV upscaled
plt.imshow(resized[:,:,::-1])
plt.show()