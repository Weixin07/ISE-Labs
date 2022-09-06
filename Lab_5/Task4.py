from PIL import Image, ImageFilter, ImageEnhance
import cv2
#import numpy as np
  
# Opening the image 
image = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_5\sugar.png")
  
newImage = image.resize((500, 500))
blurimage = newImage.filter(ImageFilter.GaussianBlur(5))
sharpenImage = ImageEnhance.Sharpness(newImage).enhance(30)

im1 = newImage
im2 = blurimage
im3 = sharpenImage

def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_h_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_h_blank(_im, im)
    return _im

get_concat_h_multi_blank([im1, im2, im3]).save('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_5\pillow_concat_h.png')

seeImage = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_5\pillow_concat_h.png")
seeImage.show()