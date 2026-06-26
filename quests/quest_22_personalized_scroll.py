#!/usr/bin/env python3
"""Quest 22: The Personalized Scroll - Functions with parameters"""


def personalized_greeting(name, quest):
    """
    Display a personalized greeting scroll for an adventurer.

    Args:
        name (str): The adventurer's name
        quest (str): The quest they're embarking on
    """
    print()
    print("=" * 50)
    print("THE PERSONALIZED SCROLL OF DESTINY")
    print("=" * 50)
    print()
    print(f"Hail, {name}!")
    print()
    print(f"Your quest awaits: {quest}")
    print()
    print("May the winds of fate guide your path,")
    print("and may your courage never falter!")
    print()
    print("=" * 50)
    print()


def main():
    """Main program to collect user input and display personalized scroll."""
    print("Welcome to the Scroll Generator!")
    print()

    adventurer_name = input("What is your name, brave adventurer? ")
    adventurer_quest = input("What quest do you wish to undertake? ")

    personalized_greeting(adventurer_name, adventurer_quest)


if __name__ == "__main__":
    main()
