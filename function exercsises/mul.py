def mul():
  n = [8,2,3,-1,7]
  i = 0
  mul =1 
  while i < len(n):
    mul = n[i] * mul
    i += 1
  return mul

multiply = mul()
print("Multiplication",multiply)