from myro import *

initialize("com6")

def drawWord(a):
    for i in xrange(len(a)):
        drawLetter(a[i])

def drawLetter(arg):
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
def arc(degrees,radius = 1):
    print ("Arc: " + str(degrees))
    #speed = 0.2
    #moveTime = 0.035;#Tweek this value so that it turns the correct amount
    speed = 0.3
    moveTime = 0.0232
    if (degrees >= 0):
        move(speed,speed/radius)
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
    line(3)
    turn(90)
    line(3)         #slightly too far

def c():
    turn(180)
    arc(-180)
    turn(180)
    arc(180)
    line(3)

def t():
    turn(90)
    line(5)         #needs to be further
    line(-1)
    turn(90)
    line(1)
    line(-2)
    line(1)
    turn(90)
    line(4)
    turn(90)
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