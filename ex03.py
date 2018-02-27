# File:  chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)


main()

#Primjećujemo da se u ex03 od 6 koraka svaki rezultat od x ne mijenja, već je vrijednost ista