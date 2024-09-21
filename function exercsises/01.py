#DUITA FUNCTION USE GAREKO 
def addition(num1,num2):
    return num1 + num2

def display(num1,num2):
    x = addition(num1,num2)
    print(f"Sum is {x}")

display(1,2)

#OTHER PROCCES
def addition(num1,num2):
    return num1 + num2

def display(result):
    print(f"Result: {result}")

result = addition(1,2)
display(result)


# other process

class addition:
    def __init__(self,num1,num2):
        self.first = num1
        self.second = num2 
    def add(self,first,second):
        return first +second 
    def display(self,result):
        print(f"result is {result}")
obj = addition(1,2)
result = obj.add(1,2)
display(result)

# other process
 
class addition:
    def add(self, first,second):
        return first + second 
    def display(self,first,second):
        x = self.add(first,second)
        print(f"Result:{x}")
obj = addition()
obj.display(1,2)

