from PIL import Image
import numpy as np

h,w = 400,500
data = np.zeros((h, w), dtype=np.uint8) #black color

#Mine (Idea derived from Kamil's):
for i in range(len(data)): #create tone
       value = 0
        
       for j in range(len(data[i])):
           data[i][j]=value 
           value -= 1 

for i in range(int(h)):
    col_value = 255

    for j in range(int(w/2)):
        data[i][j] = col_value
        col_value -= 1

    for j in range(int(w/2), w):
        data[i][j] = col_value
        col_value += 1                     

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Difference of these 2 methods is that in mine, I separated the columns into 2 and looped separately
#In Miss's method, it is only looped once, and using if-else to differentiate which function should be used on conditions - which in this case is the halves of the columns

#Miss Mary's Method:
for i in range(int(h)):

     col_value = 255

     for j in range(w):
        data[i][j] = col_value
        if j<len(data[i])/2:
            col_value -= 1
        else:
            col_value += 1    

#---------------------Back to general code
img = Image.fromarray(data, 'L')
img.show()
