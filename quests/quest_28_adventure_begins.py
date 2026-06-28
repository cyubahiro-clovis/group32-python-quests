#!/usr/bin/python3
import time

# My adventure game

def player_choice():
    choice = input("Choose to go right or left: ").lower()
    return choice

def Rwanda():
    print()
    print("Oh sorry! you're headed to Rwanda. ")
    time.sleep(3)
    print("=" * 40)
    print("Welcome to the national park")
    print("=" * 40)
    print()
    print("Oh sorry you're about to fight Gorillas")

def Congo():
    print()
    print("Oh --! you're headed to Congo. ")
    print()
    time.sleep(3)
    print("=" * 40)
    print("Welcome to Lake Kivu")
    print("=" * 40)
    print()
    print("Oh sorry you're about to start fighting sharks in the lake! ")    

def determining_country():

    print()
    print("=" * 45)
    print("Welcome to the scariest travel of your life")
    print("=" * 45)
    print("You're standing in no man's land. \nIf you choose badly, \nYou end somewhere you don't want. ")
    print()
    print("Choose which path are you choosing: ")
    print("left")
    print("right")
    print()

    choosing = player_choice()
     
    while choosing not in ["left", "right"]:
        print("That's not a valid choice")
        choosing = player_choice()

    if choosing == "left":
        Rwanda()
    else:
        Congo()

    print()
    print("End! Please survive your adventure")
    print()



determining_country()
