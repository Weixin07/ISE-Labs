nums = []
  
for i in range(0, 5):
    ele = int(input("Please enter 5 values: "))
  
    nums.append(ele)
      
print(nums)

def calculateArray(nums):

    total = str(sum(nums))
    print("The total is " + total + ".")
    return total
    
calculateArray(nums)