age= int(input("Enter age"))
day= input("Enter a day")
if day =="wednesday":
 
        print("Everyone gets $2 discount")
        if age>=18:
          print("$10 for adults")
        elif age<18:
          print("$6 for children")

else:
    if age>=18:
      print("$12 for adults")
    elif age<18:
      print("$8 for children")