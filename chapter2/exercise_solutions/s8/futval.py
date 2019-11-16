"""

8. 
As an alternative to APR, the interest accrued on an account is often de­
scribed in terms of a nominal rate and the number of compounding peri­
ods. For example, if the interest rate is 3o/o and the interest is compounded
quarterly, the account actually earns �% interest every 3 months.
Modify the futval . py program to use this method of entering the
interest rate. The program should prompt the user for the yearly rate
(rate) and the number of times that the interest is compounded each year
(periods). To compute the value in ten years, the program will loop 10 *
periods times and accrue rate/period interest on each iteration.
"""

def main () :

    print ("This program calculates the future value")
    print ("of a certain number of years of a yearly fixed-investment.")
    startAmount = float(input ("Enter the amount you wanna start with: ") )
    years = int(input("Enter the amount of years of interest: "))
    total_accumelation = 0

    

    for i in range(years):

        nominalRate =  float(input ("Enter the annual interest rate: ") )
        compound = float(input("Enter the annuall compounding: "))

        startAmount += float((nominalRate / compound)/100)*compound

        print("The accumalation for this year made your balance" ,startAmount)

        
    print ("The accumelation of your balance in", years," years is: ",round(startAmount,2))
main ()
