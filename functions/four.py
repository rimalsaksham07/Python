# write a python function to find the maximum of three numbers
def MaximumAmonngstThree(a,b,c):
    if a > b and a > c:
        print(f"a is greatest = {a}")
    elif b > a and b > c:
        print(f"b is greatest = {b}")
    elif c > a and c > b:
        print(f"c is greatest = {c}")

a = int(input("Enter number a"))
b = int(input("Enter number b"))
c = int(input("Enter number c"))
MaximumAmonngstThree(a,b,c)