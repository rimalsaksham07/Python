# @staticmetho - decorator ho 

class student:
    @staticmethod
    def hello():
        print("hello")
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg_marks(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hi" , self.name , "your avg score is" ,sum/3)

s1 = student("Tony" , [90,92,93])
s1.avg_marks()
s1.hello()
s1.name = "ironman"
s1.avg_marks()


