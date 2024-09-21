# age = int(input("Enter age: \n"))

# day = (input("Enter a day \n"))

# if (age < 18):
#     price1 = 8
#     print("Price is $",price1)
#     if day == "wednesday":
#         price2 = price1 - 2
#         print("After discount $",price2)

# if (age > 18):
#     price3 = 12
#     print("Price is $",price3)
#     if day == "wednesday":
#         price4 = price3 -2
#         print("After Discount $",price4)


# --------------- easy code ----------------------------

age = int(input("Enter age: \n"))

day = (input("Enter a day \n"))

price = 12  if age >= 18 else 8

if day == "wednesday":
    price -= 2 

print("Ticket price for you is $",price)
 