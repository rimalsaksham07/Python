def calc_gmean(a,b):
    mean = (a*b)/(a+b)
    return mean
a = 5
b = 6
x = calc_gmean(a,b)
print(x)
c = 7
d = 8
y = calc_gmean(c,d)
print(y)