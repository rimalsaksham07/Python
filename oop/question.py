# # class Animal:
# #     @staticmethod
# #     def sound():
# #         print("Some generic animal sound")
    
# # class Dog(Animal):
# #     @staticmethod
# #     def sound():
# #         print("bark")

# # obj1 = Dog()
# # obj1.sound()


# # using static method 
# class Person:
#     @staticmethod
#     def greet(name):
#         print(f"Hello, I am {name}")
    
# class Student(Person):
#     @staticmethod
#     def greet(name,student_id):
#         print(f"Hello, I am {name} and my student ID is {student_id}")

# obj = Student()
# obj.greet("Ram",123)

# # class method
# class Person:
#     def __init__(self ,name):
#         self.name = name
#     def greet(self):
#          print(f"Hello, I am {self.name}")

# class Student(Person):
#     def __init__(self ,name, stu_id):
#         super().__init__(name)
#         self.stu_id = stu_id
#     def greet(self):
#          print("Hello, I am", self.name, "and my Student ID is", self.stu_id)
        
# obj1 = Student("Ram",123) 
# obj1.greet()   

class Vehicle:
    def __init__(self):
        pass
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
    def info(self):
        super().info()
        print("This is a car")
    
obj = Car()
obj.info()
    

        
