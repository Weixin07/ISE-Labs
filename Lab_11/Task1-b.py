from PIL import Image, ImageFont, ImageDraw 

img = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_11\sunflower.jpg")
print(img.format, img.size, img.mode)
new_img = img.crop((img.width*0.2, 0, img.width*0.8,img.height))

title_font = ImageFont.truetype("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_11\Saber.ttf", 100)
poster_text = "@copyright 2022"
poster = ImageDraw.Draw(new_img)
        
for x in range (3):
    if x == 0:
        poster.text((new_img.width*0.4,new_img.height*0.9), poster_text, (255, 255, 255), font=title_font)
        
    if x == 1:
        poster.text((new_img.width*0.4,new_img.height*0.8), poster_text, (255, 255, 255), font=title_font)    
        
    if x == 2:
        poster.text((new_img.width*0.4,new_img.height*0.7), poster_text, (255, 255, 255), font=title_font)

new_img.show()

