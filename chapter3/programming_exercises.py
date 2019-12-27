import math

#1.
def calculateSphere(radius):

    v = 4/3*math.pi*radius**3
    a = 4*math.pi*(radius**2)

    print("The Volume of your sphere is " +str(v))
    print("the Area of your sphere is " +str(a))
#2.
def calPizzaSquarePrize(diameter,prize):
    radius = diameter/2
    area = math.pi*radius**2
    prizePerSquareInch = area/prize

    print("The prize of every square inch of your pizza is "+str(prizePerSquareInch))

#3.
def calculateMolecular(H,C,O,name):
    molWeight= 1.00794*H+C*12.0107+O*15.9994
    print("the molecular weight of "+name+" is " +molWeight)

#4.
def lightningDistance(seconds):
    distance = 1150*seconds/5280
    print("The distance between the lightning strikes is "+str(round(distance,2))+ " miles.")

#5.
def CoffeeOrderPrize(pounds):

    prize = 1.50 + 10.50*pounds+0.86*pounds
    print("The total prize for your order is " + str(prize) + " dollars.")

#6. 
def slope(x1,x2,y1,y2):
    
    slope=(y2-y1)/(x2-x1)
    print("The slope of your line is "+ slope)

#7.
def pointDistance(x1,x2,y1,y2):
    
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("The distance between the two points is " + distance)

#8.
def calculateEaster(year):

    c = year//100
    print(c)

    epact=(8+(c//4)-c+((8*c+13)//25)+11*(year%19))%30

    print("easter falls on " +str(epact) )

#9.
def calculateTrianleArea(a,b,c,unit):

    s = (a+b+c)/2

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("The area of your triangle is " + str(area) + " " + unit)

#10.
def calculateLadder(height,degreesAngle,unit):

    radians = (math.pi/180)*degreesAngle

    length= height/math.sin(radians)

    print("The length required for the ladder to reach the given height is " + str(round(length,2)) + " " + unit)

# 11.
def sumN(n):
   
    if n == 1:
        return 1
    else :
        return sumN(n-1) + n

#12.
def sumNcubed(n):
    if n == 1:
        return 1
    else :
        return sumNcubed(n-1) + n **3 


#13.
def sumSeries():
    
    count = int(input("Count of numbers to add "))

    nums = list()
    sum = 0

    for i in range(count):
        
        num = int(input("Enter a number to add in your list "))
        nums.append(num)
        sum += num 

    print("the sum of "+ str(nums)+ " is " + str(sum))

#14.

def averageSumSeries():

    count = int(input("Count of numbers to calculate average "))

    nums = list()
    average = 0

    for i in range(count):
        
        num = int(input("Enter a number to add in your list "))
        nums.append(num)
        average += num 

    average /= count
    print("the the average of "+ str(nums)+ " is " + str(average))

#15.

def estimatePi(n):

    x=4
    y=1
    minus = True
    estimate = x/y

    for j in range(n-1):
        
        if minus:

            y +=2
            estimate -= x/y
            minus = False

        elif minus != True:
            y+=2
            estimate += x/y
            minus = True

    print(estimate)

#16.

def fib(n):

    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#17.
def guessSquareRoot():
    x = float(input("Enter a number to approximate the square root of "))
    guesses = int(input('Enter the number of times to approximate '))
    guess = x/2

    for i in range(guesses):
       newX=(guess+(x/guess))/2
    

    print(newX)



print(sumNcubed(3))