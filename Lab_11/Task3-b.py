from PIL import Image

foo = Image.open('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_11\sunflower.jpg')  # My image is a 200x374 jpeg that is 102kb large
foo.size  # (200, 374)
 
# downsize the image with an ANTIALIAS filter (gives the highest quality)
foo = foo.resize((160,300),Image.ANTIALIAS)
 
foo.save('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_11\sunflowerPILCompress.jpg', quality=95)  # The saved downsized image size is 24.8kb
 
foo.save('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_11\sunflowerPILCompressOptimized.jpg', optimize=True, quality=95)  # The saved downsized image size is 22.9kb