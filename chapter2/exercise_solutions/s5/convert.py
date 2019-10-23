"""5. Modify the convert.py program (Section 2.2) so that it computes and
prints a table of Celsius temperatures and the Fahrenheit equivalents every
10 degrees from 0°C to 100°C.
"""

def main () :
    c = 0
    f = 0
    for i in range(11):

        f = (9/5)*c+32
        print("%3s" % c + '%15s' % f)

        c+=10  
      
    celsius = float(input ("What is the Celsius temperature? ") )
    fahrenheit = 9/5 * celsius + 32
    print ("The temperature is", fahrenheit, "degrees Fahrenheit.")
main ()

