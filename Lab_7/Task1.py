import numpy as np
import cv2 

# Create a black square
img = np.zeros((300,300,3), np.uint8)
cv2.imshow("black square", img)

#create white square 
white_img = np.zeros((300,300,3), np.uint8)
white_img[:] = 255
cv2.imshow("white square", white_img)

#create blue square 
blue_img = np.zeros((300,300,3), np.uint8)
blue_img[:,:,0] = 255  #bgr

#create retangular
rectangularImg = np.zeros((300,300,3), np.uint8)
#void cv::rectangle (   InputOutputArray    img,
# Rect  rec,
# const Scalar &    color,
# int   thickness = 1,
# int   lineType = LINE_8,
# int   shift = 0 
# )     
cv2.rectangle(rectangularImg,(20,20),(200,100),(0,255,255),5)
rectangularImg[0:100,0:200,0]=100 #different size
rectangularImg[0:100,0:200,1]=200

#create circle
circleImg = np.zeros((300,300,3), np.uint8)
#   cv.circle(  img, center, radius, color[, thickness[, lineType[, shift]]]    ) ->    img
cv2.circle(circleImg,(150,150), 75, (0,0,255), -1)

#display the shape
shapes = np.concatenate((img, white_img, blue_img,rectangularImg,circleImg), axis=1)
cv2.imshow("shapes", shapes)

cv2.waitKey(0)
cv2.destroyAllWindows()
