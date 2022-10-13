from PIL import Image, ImageFont, ImageDraw 
import numpy as np

img = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_10\Bird.jpg")
print(img.format, img.size, img.mode)
#crop image 
new_img = img.crop((img.width*0.2, 0, img.width*0.8,img.height))

#adding text 
title_font = ImageFont.truetype("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_10\Saber.ttf", 120)
poster_text = "Save The Planet"

poster = ImageDraw.Draw(new_img)
#shadow
poster.text(((new_img.width*0.1)+10,(new_img.height*0.15)-10), poster_text, (20, 100, 0), font=title_font)
#Text
poster.text((new_img.width*0.1,new_img.height*0.15), poster_text, (255, 0, 0), font=title_font)

new_img.show()

# poster = ImageDraw.Draw(img)
# #shadow
# poster.text(((img.width*0.1)+10,(img.height*0.15)-10), poster_text, (20, 100, 0), font=title_font)
# #Text
# poster.text((img.width*0.1,img.height*0.15), poster_text, (255, 0, 0), font=title_font)

# img.show()
