"""
6. Modify the futval.py program (Section 2.7) so that the number of years
for the investment is also a user input. Make sure to change the final
message to reflect the correct number of years.
"""

def main () :
    print ("This program calculates the future value")
    print ("of a certain number of years investment.")
    principal = float(input ("Enter the initial principal: ") )
    apr =  float(input ("Enter the annual interest rate: ") )
    years = int(input("Enter the years of interest: "))
    
    for i in range (years):
        principal = principal * (1 + apr)
    print ("The value in", years," years is: ",round(principal,2))
main ()
