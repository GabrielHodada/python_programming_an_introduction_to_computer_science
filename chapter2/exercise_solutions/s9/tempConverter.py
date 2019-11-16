# 9. Write a program that converts temperatures from Fahrenheit to Celsius.
# Formula for Fahrenheit Celsius conversion T(°C) = (T(°F) - 32) × 5/9

def main () :

    tempF = input("Please type the temperature in fahrenheit: ")
    hasCorrect = False

    while hasCorrect == False:

        try:
            temp = float(tempF)
            hasCorrect = True

        except ValueError:
            tempF = input("Please type the temperature in fahrenheit: ")

    tempC = (int(tempF) -32) * (5/9)
    print(tempC)

main()
