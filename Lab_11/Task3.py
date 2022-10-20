import os
import cv2

def print_file_size(file):
    File_Size = os.path.getsize(file)
    File_Size_MB = round(File_Size/1024/1024,2)
    print("Image File Size is " + str(File_Size_MB) + "MB" )
    
#read image
img=cv2.imread("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_11\sunflower.jpg")
print_file_size("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_11\sunflower.jpg")  

#compressing 
cv2.imwrite("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_11\sunflowerCompress.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 0])
print("Image Saved Successfully!!")
print_file_size("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_11\sunflowerCompress.jpg")