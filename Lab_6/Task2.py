import cv2 as cv

#load the image and show it
#img = cv.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6\damage.jpeg',0)
img = cv.imread('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6\damage.jpeg')
cv.imshow("Gray Image", img)

#https://docs.opencv.org/4.5.4/d1/d79/group__photo__denoise.html#ga03aa4189fc3e31dafd638d90de335617
#void fastNlMeansDenoising(InputArray src, OutputArray dst, float h=3, int templateWindowSize=7, int searchWindowSize=21 )
#h = filter strength for luminance component
#hcolor = filter strength for color component = 10 is sufficient

#improved_img = cv.fastNlMeansDenoising(img,None,25,7,21)
improved_img = cv.fastNlMeansDenoisingColored(img,None,20,10,7,21)
cv.imshow("Improved Image", improved_img)

cv.waitKey()
cv.destroyAllWindows()
