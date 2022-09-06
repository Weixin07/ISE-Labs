rows, cols = (4, 5)
arr = [[0]*cols]*rows

row1 = int(input("Enter the location of value to change (row): "))
col1 = int(input("Enter the location of value to change (column): "))
val = input("Enter the value to be changed to: ")

def update_location_and_value(row1,col1,val):
    arr = [[0 for i in range(cols)] for j in range(rows)]
  
    arr[row1][col1] = val
    for row in arr:
        print(row)
        
    return row1,col1,val

update_location_and_value(row1,col1,val)
