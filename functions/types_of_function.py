# arguments in functions
# these are default argumnets 
# if the values is passed in the function then it will take
# that specific value 
# but if not then it will take default arguments
def average(a=9 ,b=1 ):
    print("The average is ", a +b )

average(a = 9)

# keyword argument 
# in this argument order those not matter
# in the function defination a and b are given 
# in function calling b and a are given 
def average(a=9 , b=1):
    print("Sum is",a+b)
average(b = 1 , a = 2)

# Required Argument
# in this argument if there are 3 argument 
#then we must provide value for two argument
# and remaining one as a default
def average(a=1,b=1,c=1):
    average = (a+b+c)/2
    return average 
x = average()
print(x)

# varibale length arguments
def avaerag(*numbers):
    sum  = 0 
    for i in numbers:
        sum = sum + i 
        return sum / len(numbers)
x = avaerag(2,3)
print(x)