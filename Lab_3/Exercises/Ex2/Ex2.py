import cv2 #import library (open cv)
videoCam = cv2.VideoCapture(0)

if videoCam.isOpened():
    #configure the video recoding file and format.
    size = (int(videoCam.get(cv2.CAP_PROP_FRAME_WIDTH)),int(videoCam.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    codec = cv2.VideoWriter_fourcc(*'MJPG')
    
    #create video writer object.  
    video = cv2.VideoWriter("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_3\Exercises\RecordedVideo.avi",codec,15.0,size)
    print(size)
    
    while True:
        retval, frame = videoCam.read()
        if not retval:
            print("Can't read frames/stream. Exiting ...")
            break
        else:
        #start recording writing frames
            video.write(frame) #writing
            cv2.imshow('frame', frame) #show the video
            userkey = cv2.waitKey(1) & 0xFF
            #ord function convert character to unicode value
            if userkey == ord('q'): #keys to close the camera
                print("closing the Video cam")  
                break

videoCam.release() #close the video camera

cv2.destroyAllWindows()
