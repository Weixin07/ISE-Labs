from PIL import Image, ImageFilter as filter

img = Image.open('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6\gray_noise.png')
img.show()

#Looping to further reduce noise. Only once still has some noise in it.
# x = 1
# while x <= 3 :
#     img = img.filter(filter.MedianFilter) #The noise reduction method (by default the median filter is 3s)
#     x = x + 1

# x = 1
# while x <= 3 :
#     img = img.filter(filter.MedianFilter(0))
#     x = x + 1
#Returns value error, bad filter size
  
x = 1
while x <= 3 :
    img = img.filter(filter.MedianFilter(5))
    x = x + 1
        
img.show()
