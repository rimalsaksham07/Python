
grade = int(input("Enter a grade"))
if 90 <= grade <= 100:
    grade = "A" 
elif 80 <= grade <= 89:
    grade = "B"
elif 70 <= grade <= 79:
    grade = "C"
elif 60 <= grade <= 69:
    grade = "D"
elif grade < 60:
    grade = "F"
elif grade > 100:
    exit()
print(grade)

   
