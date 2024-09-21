# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# positive_number_count = 0
# for num in numbers:
#   if num > 0:
#     positive_number_count += 1
# print("Final count of pos number:", positive_number_count)

number = int(input("Enter a number"))
sum_even = 0 

for i in range(1, number+1):
    if i%2 == 0:
        sum_even += 1
print(sum_even)
    
