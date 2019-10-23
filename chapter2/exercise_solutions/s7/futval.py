"""
7. Suppose you have an investment plan where you invest a certain fixed
amount every year. Modify futval . py to compute the total accumulation
of your investment. The inputs to the program will be the amount to invest
each year, the interest rate, and the number of years for the investment.
"""


def main () :

    print ("This program calculates the future value")
    print ("of a certain number of years of a yearly fixed-investment.")
    yearlyAmount = float(input ("Enter a amount you want to invest each year: ") )
    apr =  float(input ("Enter the annual interest rate: ") )
    years = int(input("Enter the years of interest: "))
    total_accumelation = 0
    
    for i in range (years):

       total_accumelation += yearlyAmount + (yearlyAmount *(1+apr))
        
    print ("The value in", years," years is: ",round(total_accumelation,2))
main ()
