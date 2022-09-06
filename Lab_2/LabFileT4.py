from PIL import Image
# Open the image from working directory
image = Image.open('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_2\APULogo.png')
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)
# show the image
image.show()
