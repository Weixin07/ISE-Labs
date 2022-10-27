import cv2

img = cv2.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_12\shion.jpeg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

lapResult = cv2.Laplacian(imgGray, cv2.CV_16S, ksize=3)
imgLaplacian = cv2.convertScaleAbs(lapResult)

CannyResult = cv2.Canny(imgGray,0,255,3)
imgCanny = cv2.convertScaleAbs(CannyResult)

cv2.imshow('Gray Image', imgGray)
cv2.imshow('Lap Image',imgLaplacian)
cv2.imshow('Canny Image',imgCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()
