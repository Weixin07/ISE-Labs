from traceback import FrameSummary
import cv2
import time
import numpy as np
from datetime import datetime

static_back = None
time = []

# Capturing video
video = cv2.VideoCapture(0)

while True:
    # Reading frame(image) from video
    check, frame = video.read()
    # set motion = 0(no motion)
    motion = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)  # filtering - smoothing
   
    # set static back as first frame
    if static_back is None:
        static_back = gray
        continue

    # find different between frame and smoothing result
    diffFrame = cv2.absdiff(static_back, gray)

    # get threshold black and white
    #threshold(src, threshold value, maxval, type of threshold) ->  retval, dst
    threshFrame = cv2.threshold(diffFrame, 30, 255, cv2.THRESH_BINARY)[1]

    threshFrame = cv2.dilate(threshFrame, None, iterations=2)

    # Find contour of moving object
    contours, _ = cv2.findContours(threshFrame.copy(),
                                   cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cont in contours:
        if cv2.contourArea(cont) < 1000:
            continue
        motion = 1
        (x, y, w, h) = cv2.boundingRect(cont)
        # use red rectangle around the moving object
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imshow("Processing... ", np.concatenate(
        (gray, diffFrame, threshFrame), axis=0)) 
    cv2.imshow("Result Frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        if motion == 1:
            time.append(datetime.now())
        break

video.release()
cv2.destroyAllWindows()
