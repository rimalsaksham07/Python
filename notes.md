# concatenation
If you want to concatenate the string then we simple put '+' sign to concatenate 
'py' + 'thon'
'python'

we can simple concatenate two string by just adding spcae to it
'py' 'thon'
'python'

But we cant concatenate variable and a string using this method for eg 
prefix = 'py'
prefix 'thon'
It is an error 
but,
prefix = 'py'
prefix + 'thon'
'python'
# Slicing

Slicing is also supported in python 
characters are counted from '0' to n-1
in slicing 
word = 'python'
word[2:3]
output = 't'
word[4:]
output = 'on'
word[:3] , n-1 samma
starting to n-1
output = 'pyt'

# strings 
 strings are immutable they cant be changed after they are defined but they can be concatenated by creating a copy of the speicifc string  for example,
 x = 'PY'
 x[0] = 'J'
 error but,
 x = 'PY'
 y = 'J' + x[1:] 
 print(y)
 Thus using y as a copy refence we can change strings 

 # lists
 sqaures = [1,4,9,16,25]
 sqaures
 sqaures[-3:]
 [9,16,25]
list are mutable so we can change or add the values in the list
# to add the element at the end of the list we can simply use append functiom 
cubes.append(216)

# it is possible to nest list (create lists containting other lists)
a = ['a','b','c']
n = [1,2,3]
x = [a,n]
x = [['a','b','c'],[1,2,3]]

#