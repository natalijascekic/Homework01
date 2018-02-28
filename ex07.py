# File:  chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x,y = eval(input("Enter two a numbers between 0 and 1 separated by a coma: "))
    print("input", x, y)
    print("--------------------")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * x * (1 - x)
        print(round(x,6), round(y,6))

main()
