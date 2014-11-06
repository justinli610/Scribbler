from myro import *

initialize("com6")

def drawWord(a):
    for i in xrange(len(a)):
        drawLetter(a[i])

def drawLetter(arg):    #include other letters
    if (arg == 'a'):
        a()
        return
    if (arg == 'c'):
        c()
        return
    if (arg == 't'):
        t()
        return
    return
'''
move(translate, rotate)
First param: 1, forward, -1, backwards, fullspeed
Second param: 1, left, -1, right, fullspeed
'''
def arc(degrees,radius = 1):    #may need to change function to implement different radii
    print ("Arc: " + str(degrees))
    #speed = 0.2
    #moveTime = 0.035;#Tweek this value so that it turns the correct amount
    speed = 0.3
    moveTime = 0.0232
    if (degrees >= 0):
        move(speed,speed/radius)        '''try changing to motors(left speed?, right speed?) +stop()'''
    else:
        move(speed,-speed/radius)
    print(abs(degrees)*moveTime)
    wait(abs(degrees)*moveTime)
    move(0,0)
    wait(0.3)#Let the robot wheels recover

def line(length):
    print ("Line: " + str(length))
    #speed = 0.3
    #moveTime = 0.75#Tweek this value so that it turns the correct amount
    speed = 0.5
    moveTime = 0.5
    if (length >= 0):
        forward(speed,length*moveTime)
    else:
        backward(speed,abs(length)*moveTime)
    wait(0.3)#Let the robot wheels recover

def turn(degrees):
    print ("Turn: " + str(degrees))
    #speed = 0.2
    #turnTime = 0.0348;
    speed = 0.3
    turnTime = 0.0255
    if degrees > 0:#Left turn, CCW
        turnLeft(speed, degrees*turnTime)
    else:#Right turn, CW
        turnRight(speed, abs(degrees)*turnTime)
    wait(0.3)#Let the robot wheels recover

'''
Always move line(3) after drawing the letter to make space for the next letter
'''

#Draws an a
#Also includes the return movements to the baseline
def a():
    line(3)#To clear more space for the circle
    arc(360)#Break up the movements because bug with angles > 400
    arc(90)
    turn(180)
    line(2)
    turn(90)
    line(3)

def b():    #test
    turn(90)
    line(3)
    turn(180)
    line(2)
    arc(360)
    turn(180)
    line(1)
    turn(90)
    line(3)

def c():
    turn(180)
    arc(-180)
    turn(180)
    arc(180)
    line(3)

def d():    #test
    line(3)
    arc(360)
    arc(90)
    turn(90)
    line(3)
    turn(180)
    line(3)
    turn(90)
    line(3)

def e():    #test
    line(3)
    turn(180)
    arc(-270)
    turn(-90)
    line(2)
    turn(90)
    arc(100)
    arc(-10)
    line(4)

def f():    #test
    turn(90)
    line(5)
    arc(180)
    turn(180)
    arc(-180)
    line(-1)
    turn(90)
    line(2)
    line(-4)
    line(2)
    turn(90)
    line(4)
    turn(90)
    line(3)
def g(): #test
    line(3)
    arc(360)
    arc(90)
    turn(180)
    line(4)
    arc(-180)
    turn(180)
    arc(180)
    line(-2)
    turn(90)
    line(3)
def h():#test
    turn(90)
    line(5)
    line(-3)
    arc(-180)
    line(2)
    rotate(90)
    line(3)
def i():#test
    turn(90)
    line(3)
    turn(-90)
    arc(360,0.5)    #change function to use different radii
    turn(-90)
    line(3)
    turn(90)
    line(3)
def j():#test
    turn(90)
    line(3)
    turn(-90)
    arc(360,0.5)    #change function to use different radii
    turn(-90)
    line(5)
    arc(-180)
    turn(180)
    arc(180)
    line(2)
    turn(-90)
    line(3)
def k():#test
    turn(90)
    line(5)
    line(-3)
    turn(-45)
    line(2)
    line(-2)
    turn(-90)
    line(2)
    turn(45)
    line(3)
def l():#test
    turn(90)
    line(5)
    line(-5)
    turn(-90)
    line(3)
def m():#test
    turn(90)
    line(3)
    arc(-180)
    line(3)
    turn(180)
    line(3)
    arc(-180)
    line(3)
    turn(-90)
    line(3)
def n():#test
    turn(90)
    line(3)
    arc(-180)
    line(3)
    turn(-90)
    line(3)
def o():#test
    line(3)
    arc(360)
    line(3)
def p():
    turn(-90)
    line(2)
    line(-5)
    line(1)
    arc(360)
    line(2)
    turn(90)
    line(3)
def q():#test
    line(3)
    arc(360)
    arc(90)
    line(2)
    line(-5)
    turn(-45)
    line(2)
    line(-2)
    turn(45)
    line(2)
    turn(-90)
    line(3)
def r():#test
    turn(90)
    line(3)
    line(-1)
    arc(-180)
    turn(180)
    arc(180)
    line(2)
    turn(90)
    line(3)
def s():#test   currently improportionally big, so if arc() can be changed to accomodate radii, then change s()
    line(3)
    turn(180)
    arc(-90)
    turn(180)
    arc(270)
    arc(-270)
    turn(180)
    arc(270)
    arc(-180)
    turn(180)
    line(3)
def t():
    turn(90)
    line(5)
    line(-1)
    turn(90)
    line(1)
    line(-2)
    line(1)
    turn(90)
    line(4)
    turn(90)
    line(3)
def u():#test
    line(3)
    turn(180)
    arc(-90)
    line(2)
    turn(180)
    line(2)
    arc(180)
    line(2)
    turn(180)
    line(3)
    turn(90)
    line(3)
def v():#test
    line(3)
    turn(110)
    line(2)
    line(-2)
    turn(-40)
    line(2)
    line(-2)
    turn(-70)
    line(3)
def w():#test
    line(3)
    turn(110)
    line(2)
    line(-2)
    turn(-40)
    line(2)
    turn(-140)
    line(2)
    turn(140)
    line(2)
    line(-2)
    turn(-70)
    line(3)
def x():#test
    turn(60)
    line(2)
    line(-1)
    turn(40)
    line(1)
    line(-2)
    turn(-110)
    line(3)
def y():#test
    line(3)
    turn(110)
    line(2)
    line(-2)
    turn(-40)
    line(2)
    line(-4)
    line(2)
    turn(-60)
    line(3)
def z():#test
    line(3)
    turn(90)
    line(0.5)
    turn(90)
    line(1.5)   #might be weird
    turn(-135)
    line(2)
    turn(135)
    line(1.5)
    line(-1.5)
    turn(45)
    line(2)
    turn(135)
    line(1.5)
    turn(-90)
    line(0.5)
    turn(90)
    line(3)
def space():
    line(3)
    
    

#arc(360)
#turn(360)
#a()
#c()
#t()
drawWord("cat")

#So you don't have to reconnect everytime
'''
while True:
    pass
    '''
