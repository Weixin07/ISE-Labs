val = input("Enter your value: ")
print(val)

check = int(val) % 2

if check==0:
    print(val + " is an even number.")
else:
    print(val + " is an odd number.")