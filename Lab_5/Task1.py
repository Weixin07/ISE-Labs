from PIL import Image, ImageFilter, ImageEnhance
  
# Opening the image 
image = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_5\logo.png")
  
newImage = image.resize((500, 500))
# Blurring image 
#default radius is 2 (standard deviation)
blurimage = newImage.filter(ImageFilter.GaussianBlur(5))
#blurimage = newImage.filter(ImageFilter.GaussianBlur(0))
#blurimage = newImage.filter(ImageFilter.GaussianBlur(1))
#blurimage = newImage.filter(ImageFilter.GaussianBlur(25))
#blurimage = newImage.filter(ImageFilter.GaussianBlur(50))

EdgeEnhanceImage = newImage.filter(ImageFilter.EDGE_ENHANCE)
#sharpenImage = newImage.filter(ImageFilter.SHARPEN)
sharpenImage = ImageEnhance.Sharpness(newImage).enhance(30)
#sharpenImage = ImageEnhance.Sharpness(newImage).enhance(0)
#sharpenImage = ImageEnhance.Sharpness(newImage).enhance(10)
#sharpenImage = ImageEnhance.Sharpness(newImage).enhance(100)

#pick the lowest / highest pixel value in the a window with the given size
res1 = newImage.filter(ImageFilter.MinFilter(5))
#res1 = newImage.filter(ImageFilter.MinFilter(1))
#res1 = newImage.filter(ImageFilter.MinFilter(9))

res2 = newImage.filter(ImageFilter.MaxFilter(3))
#res2 = newImage.filter(ImageFilter.MaxFilter(1))
#res2 = newImage.filter(ImageFilter.MaxFilter(9))

# display image
image.show(title="Original Image")
blurimage.show(title="Blur Image")
sharpenImage.show(title="SharpenImage")
EdgeEnhanceImage.show(title="EdgeEnhanceImage")
res1.show(title="Min filter image")
res2.show(title="Max filter image")
