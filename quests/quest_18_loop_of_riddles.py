# Quest 18: Loop of Riddles

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number: "))

    if guess != secret_number:
        print("Wrong guess. Try again!")

print("Congratulations! You guessed it!")