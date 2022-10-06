import numpy as np
import cv2 

#create circle
circleImg = np.zeros((400,400,3), np.uint8)
circleImg[:,0,0] = 255  #bgr
#   cv.circle(  img, center, radius, color[, thickness[, lineType[, shift]]]    ) ->    img
cv2.circle(circleImg,(200,200), 160, (128,0,255), -1)
cv2.circle(circleImg,(200,200), 150, (255,0,128), -1)

#display the shape
cv2.imshow("image", circleImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
