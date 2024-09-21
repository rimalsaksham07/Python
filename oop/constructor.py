# # class student:
# #     def __init__(self):
# #         self.name = "Saksham"

# # obj = student()
# # print(obj.name)

# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def print_name(self):
#         print(self.name)
#     def print_marks(self):
#         print(self.marks)
# obj = student("Saksham",98)
# obj.print_name()
# obj.print_marks()

# class CAR:
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model
#     def print_make(self):
#         print(self.make)
#     def print_model(self):
#         print(self.model)
# obj = CAR("Toyota","Corolla")
# obj.print_make()
# obj.print_model()

# class book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#     def print_title(self):
#         print(self.title)
#     def print_author(self):
#         print(self.author)
# obj = book("To kill a Mockingbird", "Harper Lee")
# obj.print_title()
# obj.print_author()

# class book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def print_title(self):
#         print(self.title)
#     def print_author(self):
#         print(self.author)
#     def is_long_book(self):
#         if self.pages > 300:
#              print("Is this a long book?, True" )
#         else:
#              print("Is this a long book?, False" )
# obj = book("To kill a Mockingbird", "Harper Lee",281)
# obj.print_title()
# obj.print_author()
# obj.is_long_book()


# class book:
#     def __init__(self,title,pages,author="Unknown"):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def print_title(self):
#         print(self.title)
#     def print_author(self):
#         print(self.author)
#     def is_long_book(self):
#         print(self.pages)
# obj = book("To kill a Mockingbird",281, "Harper Lee")
# obj1 = book("The Great Gatsby" , 180)
# obj.print_title()
# obj.print_author()
# obj.is_long_book()
# print("-------------------")
# obj1.print_title()
# obj1.print_author()
# obj1.is_long_book()


class student:
    def __init__(self,name,Math,Science,English):
        self.name = name
        self.Math = Math
        self.Science = Science
        self.English = English
    def average(self):
        average = (self.Math + self.Science + self.English)/3
        print("Average = ",average)
    def print_average(self):
        print(self.name)
obj= student("Saksham",10,20,30)
obj.print_average()
obj.average()

# using list method 
 
class student:
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

s1.name = "ironman"
s1.avg_marks()

