# del s1.name
# del s1 

class student:
    def __init__(self,name):
        self.name = name
s1 = student("saksham")
print(s1.name)
del s1 # del object 
print(s1.name)