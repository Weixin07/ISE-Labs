from PIL import Image, ImageOps

img = Image.open('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_10\earth.png').convert("RGB")
img_flip = ImageOps.flip(img)
new_img = Image.new('RGB', (img.width,img.height*2))

new_img.paste(img, (0, 0))
new_img.paste(img_flip, (0, img.height))

new_img.show()
