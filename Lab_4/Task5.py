from PIL import Image, ImageEnhance

#read the image
#img = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_4\Task1n2n5.png")
img = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_4\sugarBrightnessAdjusted.png")

#enhance the brightness 
enImg = ImageEnhance.Brightness(img)

factor = 1 #original image
im_output = enImg.enhance(factor)
im_output.show()

factor = 0.5 #reduce the brightness 
im_output = enImg.enhance(factor)
im_output.show()

factor = 1.5 #increase brightness 
im_output = enImg.enhance(factor)
im_output.show()
