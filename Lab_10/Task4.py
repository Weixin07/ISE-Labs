from PIL import Image

# Take two images    
img1 = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_10\planet.jpg").convert("RGBA")
img2 = Image.open("D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_10\galaxy.jpg").convert("RGBA")

# img1.show()
# img2.show()

# Make the sizes of images uniform
new_img2=img2.resize((img1.width, img1.height))

#add alpha channel
img1.putalpha(100)
new_img2.putalpha(150)

Composite_img = Image.alpha_composite(new_img2,img1)

# Display the alpha composited image
Composite_img.show()
