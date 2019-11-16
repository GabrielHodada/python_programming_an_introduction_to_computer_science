#10. Write a program that converts distances measured in kilometers to miles.
#One kilometer is approximately 0.62 miles.

def main():

    hasCorrect = False
    distanceKm = input("Enter the distance in km: ")

    while hasCorrect == False:

        try:
            distanceMi = float(distanceKm)*0.62
            hasCorrect = True
        except ValueError:
            distanceKm = input("Enter the distance in km: ")

    
    print(distanceMi)
main()
