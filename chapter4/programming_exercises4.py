from graphics import*
from math import*

"""
1. 

Alter the program from the last discussion question in the following ways:
(a) Make it draw squares instead of circles.
(b) Have each successive click draw an additional square on the screen
(rather than moving the existing one).
(c) Print a message on the window "Click again to quit" after the loop,
and wait for a final click before closing the window
"""



def circToRectangle():

    win = GraphWin("Graphics Window")

    
    shape = Rectangle(Point (50 , 50) ,Point(100,100)) #first Rectangle and size
    shape.setOutline ("red")
    shape.setFill ("red")
    shape.draw (win)
    
    #Rectangle coordinates
    f = 0 #X1
    x=0 #Y1
    z = 50 #X2
    y=50 #Y2

    i =0

    while(i<10):
       
        p = win.getMouse() #loop to waits for a mouse click 
       
        if(win.getMouse):    

            rect = Rectangle(Point(f,x),Point(z,y))
            rect.setOutline("red")
            rect.setFill("red")
            rect.draw(win)

            f +=50
            z +=50 

            if(i==3):
                       
                x = 50
                y =100
                z =50
                f = 0
                
                for j in range(4):
                    if(win.getMouse()):
                        
                        i+=1
                        rect = Rectangle(Point(f,x),Point(z,y))
                        rect.setOutline("red")
                        rect.setFill("red")
                        rect.draw(win)
                        f +=50
                        z +=50

                    if(i==4):

                        f+=50
                        z+=50
            
            if(i ==7):

                x = 100
                y = 150
                z = 50
                f = 0
                

                for g in range(2):

                    if(g==0):
                        i+=1
                        rect = Rectangle(Point(f,x),Point(z,y))
                        rect.setOutline("red")
                        rect.setFill("red")
                        rect.draw(win)
                        f += 50
                        z += 50
                    
                    if(win.getMouse()):
                    
                        i+=1
                        rect = Rectangle(Point(f,x),Point(z,y))
                        rect.setOutline("red")
                        rect.setFill("red")
                        rect.draw(win)
                        f += 50
                        z += 50
                            
            i+=1 # increment loop

    Text(Point(90,80),"Click anywhere \nto close window").draw(win)
   
    if(win.getMouse()):
        win.close()

####################################################################################################################
    

"""
2.
An archery target consists of a central circle of yellow surrounded by con­
centric rings of red, blue, black and white. Each ring has the same width,
which is the same as the radius of the yellow circle. Write a program
that draws such a target. Hint: Objects drawn later will appear on top of
objects drawn earlier.
"""

def target():
    win = GraphWin()

    radius = 50
    colors=["white","black","blue","red","yellow"]

    for i in range(5):
        circle=Circle(Point(100,100),radius)
        circle.setFill(colors[i])
        circle.draw(win)
        radius -=10

    p = win.getMouse()

####################################################################################################################



"""
3.
Write a program that draws some sort of face.
"""

def smiley():
    
    win = GraphWin("smiley")
    
    circ1 = Circle(Point(100,100),70)
    circ1.setFill("yellow")
    circ1.setOutline("yellow")
    circ1.draw(win)

    circ2 = Circle(Point(100,120),40)
    circ2.setFill("black")
    circ2.setOutline("yellow")
    circ2.draw(win)

    circ3 = Circle(Point(100,115),38)
    circ3.setFill("yellow")
    circ3.setOutline("yellow")
    circ3.draw(win)

    circ4 = Circle(Point(100,80),30)
    circ4.setFill("yellow")
    circ4.setOutline("yellow")
    circ4.draw(win)

    circ5 = Circle(Point(75,85),10)
    circ5.setFill("black")
    circ5.setOutline("yellow")
    circ5.draw(win)

    circ6 = Circle(Point(125,85),10)
    circ6.setFill("black")
    circ6.setOutline("yellow")
    circ6.draw(win)

    p = win.getMouse()

####################################################################################################################

"""
4.
write a program that draws a winter scene with a Christmas tree and a
snowman.
"""

def winterScene():

    win = GraphWin("narnia0",600,400)


    #create a list of a circles representing snowflakes. 
    
    flake = "flake"#first part of key for appointing memory to a snowflake
    it = 0#second part
    rowCount=0
    wiggle = True

    #coordinates for circles
    x = 20
    y = 20

    for i in range(4):

        if(wiggle==True):
            y +=20
            x +=5
            for i in range(15):
                
                thatFlake = flake+str(it)#concat to form one key word
                thatFlake= Circle(Point(x,y),3)#create circle
                thatFlake.setOutline("white")
                thatFlake.setFill("white")
                thatFlake.draw(win)
                x+=50
                it+=1 #change second part to create different key work

            wiggle=False
            x=20



        if(wiggle==False):
            y+=10
            x-=17

            for i in range(15):
                thatFlake = flake+str(it)
                thatFlake= Circle(Point(x,y),3)
                thatFlake.setOutline("white")
                thatFlake.setFill("white")
                thatFlake.draw(win)
                x += 50
                it+=1

            wiggle=True
            x=20


        
    #tree

    line = Line(Point(100,200),Point(100,400))
    line.draw(win)
    
    triangle = Polygon(Point(100,200),Point(150,350),Point(50,350))
    triangle.setFill("green")
    triangle.draw(win)

    #crown
    star = Polygon(Point(100,180),Point(107,190),Point(120,190),Point(110,197),Point(115,210),Point(100,200),
    Point(85,210),Point(90,197),Point(80,190),Point(93,190),Point(100,180))
    star.setFill("gold")
    star.draw(win)

    #tree balls

    b1=Circle(Point(110,230),5)
    b1.setFill("red")
    b1.draw(win)

    b2=Circle(Point(105,250),5)
    b2.setFill("yellow")
    b2.draw(win)

    b3=Circle(Point(90,285),5)
    b3.setFill("purple")
    b3.draw(win)

    b4=Circle(Point(90,320),5)
    b4.setFill("red")
    b4.draw(win)

    b5=Circle(Point(120,340),5)
    b5.setFill("red")
    b5.draw(win)

    b6=Circle(Point(115,300),5)
    b6.setFill("purple")
    b6.draw(win)


    #snowman

    #body

    lower=Circle(Point(450,340),60)
    lower.setFill("white")
    lower.draw(win)
    
    middle=Circle(Point(450,240),40)
    middle.setFill("white")
    middle.draw(win)

    top=Circle(Point(450,168),32)
    top.setFill("white")
    top.draw(win)

    #buttons

    bt1=Circle(Point(450,330),5)
    bt1.setFill("black")
    bt1.draw(win)

    bt2=Circle(Point(450,290),5)
    bt2.setFill("black")
    bt2.draw(win)

    bt3=Circle(Point(450,250),5)
    bt3.setFill("black")
    bt3.draw(win)

    bt4=Circle(Point(450,210),5)
    bt4.setFill("black")
    bt4.draw(win)

    #face

    #mouth
    mouth = Circle(Point(450,173),15)
    mouth.setFill("black")
    mouth.setOutline("white")
    mouth.draw(win)

    mouthC = Circle(Point(450,168),13)
    mouthC.setFill("white")
    mouthC.setOutline("white")
    mouthC.draw(win)
    
    #eyes
    eyeR = Circle(Point(460,155),3)
    eyeR.setFill("black")
    eyeR.draw(win)

    eyeL = Circle(Point(440,155),3)
    eyeL.setFill("black")
    eyeL.draw(win)

    #arms

    left=Line(Point(410,240),Point(370,220))
    left.draw(win)

    right=Line(Point(490,240),Point(530,220))
    right.draw(win)

    p = win.getMouse()

####################################################################################################################


"""
TODO 5.
"""
####################################################################################################################

"""
6.

Modify the graphical future value program so that the input (principal and
APR) also are done in a graphical fashion using Entry objects.
"""

def futval () :

    win = GraphWin("",400,350)
    rect = Rectangle(Point(2,2),Point(99,25))
    rect.draw(win)
    rect2 = Rectangle(Point(99,2),Point(198,25))
    rect2.draw(win)
    years = Text(Point(48,13),"years")
    years.draw(win)
    value = Text(Point(150,13),"value")
    value.draw(win)

    print ("This program calculates the future value")
    print ("of a certain number of years of a yearly fixed-investment.")
        
    #apreciation label
    aprL=Text(Point(250,100),"Appreciation").draw(win)

    #apreciation entry widget
    aprE=Entry(Point(350,100),7)
    aprE.setText("0.0")
    aprE.draw(win)

    #principal label
    principalL=Text(Point(250,50),"Principal").draw(win)

    #principal entry widget
    principalE=Entry(Point(350,50),7)
    principalE.setText("0.0")
    principalE.draw(win)

    win.getMouse()

    principal = principalE.getText() #save user principal in principal var

    apr = aprE.getText() #save user appreciation in apr 

    
    addition = 1 # for to hold a character in string name so the string can be changed after assigning it to a variable in the list
    myRectangles = [] # list to hold all the bars which will hold the to calculating values 

    #create bars
    for i in range(20):
       
       
       string = "rect"+str(addition)
       addition +=1
       myRectangles.append(string)

    y = 27 # coordinate 
    index = 19 #last el of myRectangles[]

    #Calculate apreciation

    for i in range(11):

        if(i==0):

            #Create the bars to hold the value
            myRectangles[i] = Rectangle(Point(2,y),Point(99,y+25))
            myRectangles[index] = Rectangle(Point(99,y),Point(198,y+25))
            
            #Draw them on the window
            myRectangles[i].draw(win)
            myRectangles[index].draw(win)

            # save years and accumalated wealth for that year
            years=Text(Point(85,y+11),i)
            values=Text(Point(150,y+11),"$"+"%.2f"%round(float(principal),2))
            
            # draw them on the screen
            values.draw(win)
            years.draw(win)

        if(i>0):

            #Create the bars to hold the value
            myRectangles[i] = Rectangle(Point(2,y),Point(99,y+25))
            myRectangles[index] = Rectangle(Point(99,y),Point(198,y+25))
            
            #Draw them on the window
            myRectangles[i].draw(win)
            myRectangles[index].draw(win)

            #years and accumalated wealth for that year
            years = Text(Point(85,y+11),i)
            principal = float(principal) *(1+float(apr)/100)

            values = Text(Point(150,y+11),"$"+"%.2f"%round(float(principal),2))

            #Draw objects on the window
            values.draw(win)
            years.draw(win)
        


        index -=1 # decrement last element of the list 
        y +=25 #increase the coordinate7
    
    win.getMouse()

    win.close()

####################################################################################################################
"""
7. Circle Intersection.
Write a program that computes the intersection of a circle with a hori­
zontal line and displays the information textually and graphically.
Input: Radius of the circle and they-intercept of the line.
Output: Draw a circle centered at ( 0, 0 ) with the given radius in a window
with coordinates running from -10,-10 to 10,10.
Draw a horizontal line across the window with the given y-intercept.
Draw the two points of intersection in red.
Print out the x values of the points of intersection.
Formula: x =
±
y' r2 - y2
"""


def yCircInter():

    win=GraphWin("",400,400)
    y=Line(Point(130,30),Point(130,230))
    x=Line(Point(30,130),Point(230,130))
    x.draw(win)
    y.draw(win)

    #coordinate system
    xMAX=Text(Point(240,130),"10").draw(win)
    xMIN=Text(Point(16,130),"-10").draw(win)
    yMAX=Text(Point(130,19),"10").draw(win)
    yMIN=Text(Point(127,240),"-10").draw(win)
    origin=Text(Point(122,140),"0").draw(win)

    #radius
    r=Text(Point(330,150),"radius:").draw(win)
    rE=Entry(Point(330,175),7)
    rE.setText("0.0")
    rE.draw(win)

    #y-Coordinate
    y=Text(Point(330,70),"y-Intercept:").draw(win)
    yE=Entry(Point(330,95),7)
    yE.setText("0.0")
    yE.draw(win)

    win.getMouse()

    #save user input and convert to float

    a=yE.getText()
    a=float(a)
    b=rE.getText()
    b=float(b)

    Circ=Circle(Point(130,130),b*10).draw(win)

    win.getMouse()

    lin=Line(Point(16,130-a*10),Point(240,130-a*10)).draw(win)
    
    xl=Circle(Point(130-sqrt(((b*10)**2)-((a*10)**2)),130-a*10),3)
    xl.setFill("red")
    xr=Circle(Point(130+sqrt(((b*10)**2)-((a*10)**2)),130-a*10),3)
    xr.setFill("red")

    xl.draw(win)
    xr.draw(win)

    less=round(-sqrt(((b*10)**2)-((a*10)**2)),2)
    less=str(less)
    greater=round(+sqrt(((b*10)**2)-((a*10)**2)),2)
    greater=str(greater)

    lab=Text(Point(150,330),"The Intersection at < 0 = "+less).draw(win)
    lab2=Text(Point(150,360),"The Intersection at > 0 = "+greater).draw(win)

    win.getMouse()

####################################################################################################################
"""
8. Line Segment Information.
This program allows the user to draw a line segment and then displays
some graphical and textual information about the line segment.
Input: Two mouse clicks for the end points of the line segment.
Output: Draw the midpoint of the segment in cyan.
Draw the line.
Print the length and the slope of the line.
Formulas:
dx = x2 - x1
dy = Y2 - Yl
slope = dy / dx
length = J dx 2 + d y 2
"""


def lineSegment():

    

    win=GraphWin("click on two places",400,400)

    #wait for two user mouseclicks
    fir=win.getMouse()
    sec=win.getMouse()

    #save their x and y coordinates
    x1=fir.getX()
    y1=fir.getY()
    x2=sec.getX()
    y2=sec.getY()

    #convert for a point in the middle of the line segment
    p1=(x2+x1)/2
    p2=(y2+y1)/2

    #draw the line
    lin=Line(Point(x1,y1),Point(x2,y2)).draw(win)
    
    #draw the middle point
    cir=Circle(Point(p1,p2),3)
    cir.setFill("cyan")
    cir.draw(win)

    dx=x2-x1
    dy=y2-y1

    #calculate the slope and length
    slope=dy/dx
    length=sqrt(dx**2+dy**2)

    print(slope)
    print(length)



    win.getMouse()

####################################################################################################################

"""
9. Rectangle Information.
This program displays information about a rectangle drawn by the user.
Input: Two mouse clicks for the opposite comers of a rectangle.
Output: Draw the rectangle.
Print the perimeter and area of the rectangle.
Formulas:
area = (length) (width)
perimeter = 2(length + width)
"""


def rectInfo():

    

    win=GraphWin("click on two places",400,400)

    #wait for two user mouseclicks
    fir=win.getMouse()
    sec=win.getMouse()

    #save their x and y coordinates
    x1=fir.getX()
    y1=fir.getY()
    x2=sec.getX()
    y2=sec.getY()

    dx=x2-x1
    dy=y2-y1

    if(dx<0):
        dx*=-1
    if(dy<0):
        dy*=-1

    area = dx*dy
    perimeter=(dx*dy)*2

    rect=Rectangle(Point(x1,y1),Point(x2,y2)).draw(win)

    print("Area = " + str("%.0f"%area))
    print("Perimeter = " + str("%.0f"%perimeter))

    win.getMouse()

####################################################################################################################

"""
10. Triangle Information.
Same as the previous problem, but with three clicks for the vertices of
a triangle.
Formulas: For perimeter, see length from the Line Segment problem.
area = Js(s - a) (s - b) (s - c ) where a, b, and c are the lengths of
the sides and s
= a+�+c .
"""



def triangleInfo():

    win=GraphWin("Click on three different places",800,600)

    #anticipate three mousclicks
    fir=win.getMouse()
    sec=win.getMouse()
    third=win.getMouse()

    #save their coordinates
    x1=fir.getX()
    y1=fir.getY()
    x2=sec.getX()
    y2=sec.getY()
    x3=third.getX()
    y3=third.getY()

    #draw the triangle
    lin1=Line(Point(x1,y1),Point(x2,y2)).draw(win)
    lin2=Line(Point(x2,y2),Point(x3,y3)).draw(win)
    lin3=Line(Point(x1,y1),Point(x3,y3)).draw(win)

    #calculate the lengths of the sides
    dx1=x3-x2
    dy1=y3-y2
    dx2=x2-x1
    dy2=y2-y1
    dx3=x3-x1
    dy3=y3-y1

    #sides
    a=sqrt(dx1**2+dy1**2)
    b=sqrt(dx2**2+dy2**2)
    c=sqrt(dx3**2+dy3**2)

    perimeter=a+b+c
    s=perimeter/2
    area=sqrt(s*(s-a)*(s-b)*(s-c))

    print("The perimeter is "+str("%.2f"%perimeter))
    print("The area is " +str("%.2f"%area))
    
    win.getMouse()

####################################################################################################################

"""
1 1. Five-click House.
You are to write a program that allows the user to draw a simple house
using five mouse clicks. The first two clicks will be the opposite corners of
the rectangular frame of the house. The third click will indicate the center
of the top edge of a rectangular door. The door should have a total width
that is � of the width of the house frame. The sides of the door should
extend from the corners of the top down to the bottom of the frame. The
fourth click will indicate the center of a square window. The window is
half as wide as the door. The last click will indicate the peak of the roof.
The edges of the roof will extend from the point at the peak to the corners
of the top edge of the house frame.
"""

def clickHouse():

    win=GraphWin("Click five times to make a house",800,600)
    
    #mouseclicks for the walls of the house
    fir=win.getMouse()
    sec=win.getMouse()

    x1=fir.getX()
    y1=fir.getY()
    x2=sec.getX()
    y2=sec.getY()

    #draw the walls with the given mouse coordinates
    walls=Rectangle(Point(x1,y1),Point(x2,y2)).draw(win)

    #get the house width and use it to calculate the doorWidth(1/5houseWidth)
    hWidth=x2-x1

    if(hWidth<0): # if the second mouseclick is on the left side x2-x1 becomes negative: alternative to this if statement would be to go in the init class and make adjustments there
        hWidth*=-1

    dWidth=hWidth/5  

    while(True):

        third=win.getMouse()
        x3=third.getX()
        y3=third.getY()
        #checking if the third click puts the door in the conveinments of the walls of the house


        if(x3-dWidth/2>=x1 and x3+dWidth/2<=x2 and y3<y1 and y3>y2 #lower left was first click
        or x3-dWidth/2>=x1 and x3+dWidth/2<=x2 and y3<y2 and y3>y1 # upper left was first click
        or x3+dWidth/2<=x1 and x3-dWidth>=x2 and y3<y1 and y3>y2 #lower right 
        or x3+dWidth/2<=x1 and x3-dWidth>=x2 and y3>y1 and y3<y2): #upper right
                
            #the measurements for the window
            winWidth=dWidth/2

            #save the lowest click's y as a value for the lower door corner coordinate 
            lowDCorner=0
            if(y2>y1):
                lowDCorner=y2
            else:
                lowDCorner=y1
                    
                #draw The door
            lin1=Line(Point(x3-dWidth/2,y3),Point(x3+dWidth/2,y3)).draw(win)
            lin2=Line(Point(x3-dWidth/2,y3),Point(x3-dWidth/2,lowDCorner)).draw(win)
            lin3=Line(Point(x3+dWidth/2,y3),Point(x3+dWidth/2,lowDCorner)).draw(win)
            break
        print("The door has to fit in the house")

        
    # window

    while(True):

            
        fourth=win.getMouse()
        x4=fourth.getX()
        y4=fourth.getY()


        if(x4+winWidth/2<x2 and x4-winWidth/2>x1 and y4+winWidth/2<y2 and y4-winWidth/2>y1 
        or x4+winWidth/2<x2 and x4-winWidth/2>x1 and y4-winWidth/2>y2 and y4+winWidth/2<y1 
        or x4+winWidth/2<x1 and x4-winWidth/2>x2 and y4-winWidth/2>y2 and y4+winWidth/2<y1 
        or x4+winWidth/2<x1 and x4-winWidth/2>x2 and y4-winWidth/2>y1 and y4+winWidth/2<y2): #the user clicked somewhere between the walls of the house
                
                    
            if(y4<y3 or y4+winWidth/2>=y3 and x4-winWidth/2>x3+dWidth/2 or y4+winWidth/2>=3 and x4+winWidth/2<x3-dWidth/2): # and not on the door
                window=Rectangle(Point(x4-winWidth/2,y4-winWidth/2),Point(x4+winWidth/2,y4+winWidth/2)).draw(win)
                break
        print("The window has to be on the house and not on the door")
    # Roof

    while(True):

        fifth=win.getMouse()
        x5=fifth.getX()
        y5=fifth.getY()

        #check the first and last click coordinates to check which one is higher then the last click has to be higher than that
        if(y1<=y2 and y5<y1):
            p=Point(x2,y1)
            side1=Line(Point(x5,y5),Point(x2,y1)).draw(win)
            side2=Line(Point(x5,y5),Point(x1,y1)).draw(win)
            break

        elif(y1>y2 and y5<y2):

            p=Point(x1,y2)
            side1=Line(Point(x5,y5),Point(x1,y2)).draw(win)
            side2=Line(Point(x5,y5),Point(x2,y2)).draw(win)
            break
        print("You have to put the roof on top of the walls")


    
    win.getMouse()





