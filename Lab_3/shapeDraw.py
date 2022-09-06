from PIL import Image
import numpy as np

w, h = 100, 100
data = np.zeros((h, w), dtype=np.uint8) #black color
print(data) #show all zeros
img = Image.fromarray(data, '1') # 'L'
img.show()

print(data.shape)
print(data.size)
data[0:50,0:50] = 255
print(data) #show all zeros
img = Image.fromarray(data, 'L')
img.show()

data[0:100,0:100] = 0 #reset back to black color
for i in range(len(data)): #create tone
        value = 0
        for j in range(len(data[i])):

            data[i][j]=value 
            value += 1 

img = Image.fromarray(data, 'L')
img.show()
