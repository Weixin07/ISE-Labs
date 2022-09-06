nums = []
  
for i in range(0, 5):
    ele = int(input("Please enter 5 values: "))
  
    nums.append(ele)
      
print(nums)

first = nums[0]
second = nums[1]
third = nums[2]
forth = nums[3]
fifth = nums[4]

total = str(first+second+third+forth+fifth)

print("The total is " + total + ".")