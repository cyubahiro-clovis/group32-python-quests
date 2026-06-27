#!/usr/bin/python3
import random

def get_player_choice():
    choice = input("Pick rock, paper or scissors: ").lower()    
    return choice

def get_computer_choice():
    choice = random.choice(["rock", "paper", "scissors"])
    return choice


def decide_winner(player, computer):
    if player == computer:
        print("We tied!")
    elif player == "rock" and computer == "scissors":
        print("You win! ")
    elif player == "paper" and computer == "rock":
        print("You win! paper covers rock")
    elif player == "scissors" and computer == "paper":
        print("You win! scissors cuts the paper")
    else:
        print("Sorry! computer wins")

def playing_game():
    print()
    print("==" * 25)
    print("Rock Paper Scissors")
    print("==" * 25)

    print("Pick one: ")
    print("rock")
    print("paper")
    print("scissors")
    print()

    player = get_player_choice()
    while player not in ["rock", "paper", "scissors"]:
        print("That's not a valid choice!")
        player = get_player_choice()

    computer = get_computer_choice()
    print(f"You picked : {player}")
    print(f"Computar picked: {computer}")
    decide_winner(player, computer)

    
    while True:
        again = input("Play again? (yes/no): ").lower()
        if again in ["yes", "no"]:
            break
        print("Please type yes or no!")
    
    if again == "yes":
        playing_game()
    else:
        print()
        print("END")
        print()
        print("=" * 50)
        print()
        print("Thanks for playing! ")

playing_game()


