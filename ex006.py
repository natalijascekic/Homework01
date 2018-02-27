# File:  chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    print("a")
    for i in range(100):
        x = 3.9 * x * (1 - x)

        print(x)

    print("b")
    for i in range(100):
        x = 3.9 * (x - x * x)

        print(x)

    print("c")
    for i in range(100):
        x = 3.9 * x - 3.9 * x * x

        print(x)

main()


