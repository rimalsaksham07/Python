
def main():
    num = [8,2,3,0,7]
    i = 0
    sum = 0
    while i < len(num):
      sum = sum + num[i]
      i += 1
    return sum

sum = main()
print("Sum is",sum)
