from myro import *
import speech
import time

initialize("com6")

def drawWord(a):
    for i in xrange(len(a)):
        drawLetter(a[i])

def drawLetter(arg):    #include other letters
    if (arg == 'a'):
        a()
        return
    if (arg == 'b'):
        b()
        return
    if (arg == 'c'):
        c()
        return
    if (arg == 'd'):
        d()
        return
    if (arg == 'e'):
        e()
        return
    if (arg == 'f'):
        f()
        return
    if (arg == 't'):
        t()
        return
    if (arg == 's'):
        s()
        return
    return
'''
move(translate, rotate)
First param: 1, forward, -1, backwards, fullspeed
Second param: 1, left, -1, right, fullspeed
'''
'''def arc(degrees,radius = 1):    #may need to change function to implement different radii
    print ("Arc: " + str(degrees))
    #speed = 0.2
    #moveTime = 0.035;#Tweek this value so that it turns the correct amount
    speed = 0.3
    moveTime = 0.0232
    if (degrees >= 0):
        move(speed,speed/radius)       #try changing to motors(left speed?, right speed?) +stop()
    else:
        move(speed,-speed/radius)
    print(abs(degrees)*moveTime)
    wait(abs(degrees)*moveTime)
    move(0,0)
    wait(0.3)#Let the robot wheels recover
'''
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

#Small turn (e.g. for 's')
def arc(degrees):
    print ("Turn: " + str(degrees))
    #speed = 0.2
    #turnTime = 0.0348;
    speed = 0.2
    turnPower = 0.4 *degrees/abs(degrees)
    move(speed, turnPower)
    """if degrees > 0:#Left turn, CCW
        turnPower = degrees*time
    else:#Right turn, CW
        turnPower = abs(degrees)*time"""

    while timeRemaining(.0165*abs(degrees)):
        i = 0
    move(0, 0)
    wait(0.3)#Let the robot wheels recover

'''
Always move line(3) after drawing the letter to make space for the next letter
'''

#Draws an a
#Also includes the return movements to the baseline
def a():
    space()#To clear more space for the circle
    arc(360)#Break up the movements because bug with angles > 400
    arc(90)
    turn(180)
    line(2)
    turn(90)
    space()

def b():
    turn(90)
    line(4)
    turn(180)
    line(3)
    arc(360 + 30)
    line(1)
    turn(90)
    space()

def c():
    turn(180)
    arc(-180)
    turn(180)
    arc(180)
    space()

def d():
    space()
    arc(360+30)
    arc(90)
    line(3)
    turn(180)
    line(4)
    turn(90)
    space()

def e():    #finetune
    space()
    turn(180)
    arc(-270-10)
    turn(-90)
    line(1.8)
    turn(90)
    arc(140)
    turn(180)
    arc(-40)
    turn(180)
    space()

def f():
    turn(90)
    line(3)
    arc(-90)
    turn(180)
    arc(90)
    line(0.7)
    turn(90)
    line(0.9)
    line(-0.6)
    line(-0.7)
    line(0.7)
    turn(-90)
    line(2.3)
    turn(90)
    space()
def g():
    line(3)
    arc(360 + 30)
    arc(90)
    line(0.7)
    turn(180)
    line(3)
    arc(-180)
    turn(180)
    arc(180+20)
    line(1.4)
    turn(-90)
    line(3)
def h():
    turn(90)
    line(4)
    line(-3)
    arc(-180)
    line(1)
    turn(90)
    space()
def i():#test
    turn(90)
    line(1)
    turn(-90)
    arc(360,0.5)    #change function to use different radii
    turn(-90)
    line(3)
    turn(90)
    space()
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
def k():
    turn(90)
    line(3)
    line(-2)
    turn(-45)
    line(2)
    line(-1.5)
    turn(-90)
    line(1.5)
    turn(45)
    space()
def l():
    turn(90)
    line(3)
    line(-3)
    turn(-90)
    space()
def m():#finetune
    turn(90)
    line(1.5)
    line(-0.5)
    arc(-180)
    line(1)
    turn(180)
    line(1)
    arc(-180)
    line(1)
    turn(90)
    space()
def n():#finetune
    turn(90)
    line(1.5)
    line(-0.5)
    arc(-180)
    line(1)
    turn(90)
    space()
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
def s():
    line(3)
    turn(180)
    arc(-90)
    turn(180)
    arc(270)
    arc(-260)
    turn(180)
    arc(260)
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
    line(2)

m()
n()
#arc(360)
#turn(360)
#a()
#c()
#t()
#drawWord("e")
'''
phrase = speech.input()
print phrase
drawWord (phrase)

def callback(phrase, listener):
    if phrase == "stop":
        listener.stoplistening()
    drawWord(phrase)

listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)
#So you don't have to reconnect everytime

#So you don't have to reconnect everytime
'''
'''
while True:
    pass
    '''
