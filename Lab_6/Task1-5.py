from PIL import Image, ImageFilter as filter

img = Image.open('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\ISE-Labs\Lab_6\sugar.png')
#img.show()
       
img = img.filter(filter.EDGE_ENHANCE)
#img = img.filter(filter.EDGE_ENHANCE_MORE)  
#img = img.filter(filter.BLUR)  
#img = img.filter(filter.CONTOUR)  
#img = img.filter(filter.DETAIL)   
#img = img.filter(filter.EMBOSS)    
#img = img.filter(filter.FIND_EDGES)   
#img = img.filter(filter.SHARPEN)   
#img = img.filter(filter.SMOOTH)     
#img = img.filter(filter.SMOOTH_MORE)  

img.show()
