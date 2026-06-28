#!/usr/bin/python3
secret = 6
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")

print("You got it!!")
