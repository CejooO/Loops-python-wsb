#31

human_age = int(input("Input a dog's age in human years: "))

if human_age < 0:
    print("Age cannot be 0")
    exit()
elif human_age <= 2:
    dog_age = human_age * 10.5
else:
    dog_age = 21 + (human_age - 2) * 4

print("Dog Age:", dog_age)