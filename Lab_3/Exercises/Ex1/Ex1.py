# use opencv library
import cv2 

imageNumber = 1
#Opens a camera for video capturing.
#0 index => default value
camObject = cv2.VideoCapture(0)

#set the camera properties
camObject.set(cv2.CAP_PROP_EXPOSURE, -2) #exposure
camObject.set(cv2.CAP_PROP_ISO_SPEED, 800)  #ISO 

#camera is initalize and read to capture video
while camObject.isOpened():      
# Capture  video frame
#return image (true-frame/false-no more frame)
    retval, img = camObject.read()
    
# show the window with the img frame capture by cam
#parameter(framename , matrix for image)
    cv2.imshow('MyCamera',img)
     
#wait for 1 millisecond and capture the userinput 
    userkey = cv2.waitKey(1) & 0xFF
    
#ord function convert character to unicode value
    if userkey == ord('q'): #close the camera
        print("closing the camera!")  
        break
    elif userkey == ord('c'): #capture the image
        #save image to specific file.
        #parameter(filename, image) 
        cv2.imwrite("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_3\Exercises\image_%d.jpg" %imageNumber, img)
        print("new image %d captured!" %(imageNumber))
        imageNumber += 1

# close the cam
camObject.release()

# close and destroy window
cv2.destroyAllWindows()

