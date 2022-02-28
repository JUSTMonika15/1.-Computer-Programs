"""CSC 161 Lab: Computer Programs

Lihang Liu
Lab Section TR 2:00-3:15pm
Spring 2022
"""


# File: chaos.py
# A simple program illustrating chaotic behavior.


def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    n = int(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)


if __name__ == "__main__":
    main()
