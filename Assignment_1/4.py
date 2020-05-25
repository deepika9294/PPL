import random
number = random.randint(1, 100)
# print(number)
guess = int(input("Enter an integer from 1 to 100: "))

while 1:
    if guess < number:
        print("Actual number is high")
        guess = int(input("Enter an integer from 1 to 100: "))
    elif guess > number:
        print("Actual number is low")
        guess = int(input("Enter an integer from 1 to 100: "))
    else:
        print("Correct number")
        break
        
