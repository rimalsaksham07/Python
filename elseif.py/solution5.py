distance = int(input("Enter a distance to walk in km"))
if distance < 3:
    print("Walk")
elif 3< distance < 15:
    print("Bike")
elif distance > 15:
    print("Car")

