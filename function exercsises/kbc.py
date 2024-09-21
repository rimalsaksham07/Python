print("What is capital city of Nepal ")
print("a) Pokhara      b)Kathmandu" )
print("c) Biratnagar   d)Jhapa" )
question1 = input()
if question1 == "b":
    reply = "Correct answer!!! You've won 10,000 \n"
    print(reply)
    amount1 = 10000
    question1 = True
else:
    print("Incorrect Answer")
    
if question1 == True:
    print("What is capital city of India")
    print("a) Delhi   b)Kolkata" )
    print("c) Mumbai  d)Kerela" )
    question2 = input()
    if (question2 == "a"):
     reply = f"Correct answer!!! You've won {amount1 + 10000}"
     print(reply)
     amount2 = 10000
     qeustion2 = True
    else:
       question2 = False
       print("Incorrect Answer")
       print(f"Amount have been deducted remaining {amount1-amount1}")

if question2 == True:
   print("What is capital city of ")
   print("a) Delhi   b)Kolkata" )
   print("c) Mumbai  d)Kerela" )
   question3 = input()
   if (question3 == ""):
      reply = f"Correct answer!!! You've won {amount1+ amount2+ 10000}"
      print(reply)
      amount3 = S
      
   

    