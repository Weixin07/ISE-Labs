import cv2
import numpy as np

img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6II\grey.jpg',0)

gauss = np.random.normal(0,1,img.size)

gauss = gauss.reshape(img.shape[0],img.shape[1]).astype('uint8')

img_gauss = cv2.add(gauss,img)

##########################
mask = img_gauss
cv2.imwrite('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6II\Task4-Task1.png', mask)

img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6II\Task4-Task1.png')
improved_img = cv2.fastNlMeansDenoisingColored(img,None,75,10,7,21)
cv2.imshow("Improved Image", improved_img)

cv2.waitKey()
cv2.destroyAllWindows()

