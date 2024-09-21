nums = (1,4,9,16,25,36,49,64,81,100)
i = 0
x = int(input("Enter a number"))
while i < len(nums):
    if nums[i] == x:
        print("Number found at index", i)
        break
    else:
        print('Not found')
        break
    i += 1
