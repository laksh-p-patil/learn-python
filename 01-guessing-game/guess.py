import random

secret=random.randint(1,100)
attempts=0
guess=0

print("I'm thinking of a number between 1 and 100.")
print("(Testing) The secret number is:", secret)

while guess != secret:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("You got it!")
    print("It took you", attempts, "attempts.")