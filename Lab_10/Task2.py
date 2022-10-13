from PIL import Image, ImageDraw

img1 = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_10\Birdpark.png").convert("RGBA")
img2 = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_10\earth.png")
img2.convert("RGBA")

#study the image
print(img1.format, img1.size, img1.mode)
print(img2.format, img2.size, img2.mode)

#draw on the existing image 1
img_mask = Image.new("L", img2.size, 0)
draw = ImageDraw.Draw(img_mask)

x1 = img2.width*0.05
y1 = img2.height*0.05
x2 = img2.width*0.9
y2 = img2.height*0.9

draw.ellipse((x1,y1,x2,y2), fill=255, outline=150, width=10)
#img_mask.show()

back_im = img1.copy()
back_im.putalpha(150) #transparency

#merge the image
back_im.paste(img2, (int(img1.width*0.38), int(img1.height*0.65)), img_mask)
back_im.show()
