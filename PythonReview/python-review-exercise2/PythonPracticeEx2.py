import random
randomNumber = random.randint(1,100)
myRandomNumber = 20

guess = int(input("Guess my age"))

while guess != myRandomNumber:
    if guess < myRandomNumber:
        print("Nope! go higher", guess)
    elif guess > myRandomNumber:
        print("Nope! go lower" , guess)

    guess = int(input("Guess my age"))


print("You're right, I am", guess)
