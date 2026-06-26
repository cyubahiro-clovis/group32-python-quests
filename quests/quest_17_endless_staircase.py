#!/usr/bin/env python3
"""Quest 17: The Endless Staircase - while loop"""


def main():
    """Demonstrate a while loop by climbing the endless staircase."""
    print("Climbing the Endless Staircase")
    print("=" * 40)

    counter = 0

    while counter < 5:
        print(f"Step {counter}: You climb higher and higher...")
        counter = counter + 1

    print()
    print(f"You've reached step {counter}!")
    print("The staircase ends here. You've made it!")
    print("=" * 40)


if __name__ == "__main__":
    main()
