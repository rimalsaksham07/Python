# # child and parent class 

# # class car:
# # class toyotalcar(car)
# # inherit bhayo 

# class car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car start")
#     def stop():
#         print("car stopped")

# class toyotacar(car): # inheritance gareko
#     def __init__(self,name):
#      self.name = name

# car1 = toyotacar("fortuner")
# car2 = toyotacar("prius")
# print(car1.start())
# print(car2.name)


# # SINGLE INHERITANCE 
# # MULTI_LEVEL INHERITANCE
# # MULTIPLE INHERITANCE 

class person:
     def __init__(self, fname ,lname):
      self.firstname = fname 
      self.lastname = lname

     def printname(self):
        print(self.firstname , self.lastname)

class student(person):
   def __init__(self,fname,lname): # child class ma init rakhyo bhane it will no longer inherit the properties of the parent class
      person.__init__(self,fname,lname)

x = student("John" , 'Doe')

x.printname()

class person:
     def __init__(self, fname ,lname):
      self.firstname = fname 
      self.lastname = lname

     def printname(self):
        print(self.firstname , self.lastname )

class student(person):
   def __init__(self,fname,lname,year): # child class ma init rakhyo bhane it will no longer inherit the properties of the parent class
      super().__init__(fname,lname) # ki ta tyo function ko name use gar e or super() bhanne use garne 
      self.graduationyear = year

   def welcome(self):
      print("Welcome" ,self.firstname , self.lastname , "to class of" , self.graduationyear )

x = student("John" , 'Doe', 2019)
x.welcome()


    
    
   