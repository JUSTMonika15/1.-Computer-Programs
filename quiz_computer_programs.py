"""CSC 161 Quiz: Computer Programs

Lihang Liu
Lab Section TR 2:00-3:15pm
Spring 2022
"""


def main():
    n = 3
    print("n =", n)
    for i in range(7):
        n = 2 + n * 2
        print(n)
    print("n =", n)


if __name__ == '__main__':
    main()
