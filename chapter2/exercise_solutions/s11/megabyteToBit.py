#11. Write a program to perform a unit conversion of your own choosing. Make
#sure that the program prints an introduction that explains what it does.

def main():

    print("Hello this programs lets you convert megabyte to bit")

    hasCorrect = False
    megabytes = input("Enter the amount of megabytes: ")

    while hasCorrect == False:

        try:
            bits = float(megabytes)*8000000
            hasCorrect = True

        except ValueError:
            megabytes = input("Enter the amount of megabytes")

    print(roundbits)




main()
