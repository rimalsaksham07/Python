import random
# random.randrange(start , stop )
steps = 0
for i in range(1,100):
    number = random.randrange(1,10)
    guess = int(input("Guess a number:"))
    if guess == number:
        print("Guessed Correctly......")
        break
    else:
        if guess > number:
            print("To high!!!")
        else:
            print("To low!!!!!!")
    
    steps += 1  
print(f"Steps: {steps}")

