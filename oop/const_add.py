class addition:
    first = 0 
    second = 0 
    answer = 0 
    
    def __init__(self,f,s):
        self.first = f
        self.second = s
    
    def display(self):
        print("First Number = " , self.first)
        print("Second NUmber = ", self.second)
        print("Addition of two number" ,self.answer)
    
    def calculation(self):
        self.answer = self.first + self.second

obj = addition(100,200)
obj.calculation()
obj.display()


