from myro import *
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
    arc(360 + 30)#Break up the movements because bug with angles > 400
    arc(90)
    turn(180)
    line(-1)
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
    space()
def c():
    space()
    turn(180)
    arc(-210)
    turn(180)
    arc(270)
    turn(180)
    arc(-60)
    turn(180)
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
    arc(-270-20)
    turn(-90)
    line(1.8)
    turn(90)
    arc(140)
    turn(180)
    arc(-40)
    turn(180)
    space()
def f():
    space()
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
    space()
    arc(360 + 30)
    arc(90)
    line(0.7)
    turn(180)
    line(3)
    arc(-140)
    turn(180)
    arc(140)
    line(1.4)
    turn(-90)
    space()
def h():
    turn(90)
    line(4)
    line(-3)
    arc(-180)
    line(1)
    turn(90)
    space()
def i():
    turn(90)
    line(1.5)
    turn(180)
    line(1.5)
    turn(90)
    space()
def j():
    space()
    turn(90)
    line(1.5)
    turn(180)
    line(3)
    arc(-140)
    turn(180)
    arc(140)
    line(1.5)
    turn(-90)
    space()
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
def m():
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
def n():
    turn(90)
    line(1.5)
    line(-0.5)
    arc(-180)
    line(1)
    turn(90)
    space()
def o():
    space()
    arc(360+25)
    space()
def p():
    turn(90)
    line(2)
    line(-1)
    arc(-360-25)
    line(-3)
    line(2)
    turn(-90)
    space()
    space()
def q():
    space()
    arc(360+25)
    arc(90)
    line(0.5)
    line(-3)
    turn(-45)
    line(1.5)
    line(-1.5)
    turn(45)
    line(2)
    turn(-90)
    space()
def r():
    turn(90)
    line(1.5)
    line(-0.5)
    arc(-140)
    turn(180)
    arc(140)
    line(1)
    turn(90)
    space()
    space()
def s(): #finetune
    space()
    turn(180)
    arc(-90)
    turn(180)
    arc(270)
    arc(-260)
    turn(180)
    arc(260)
    arc(-180)
    turn(180)
    space()
def t():
    space()
    turn(90)
    line(3)
    line(-1)
    turn(90)
    line(0.9)
    line(-0.9)
    line(-0.7)
    line(1)
    turn(90)
    line(2)
    turn(90)
    space()
def u():
    space()
    turn(180)
    arc(-95)
    line(0.75)
    turn(180)
    line(0.75)
    arc(95)
    arc(95)
    line(0.75)
    turn(180)
    line(1.75)
    turn(90)
    space()
def v():
    space()
    turn(110)
    line(2)
    line(-1.8)
    turn(-65)
    line(2)
    line(-1.8)
    turn(-70)
    space()
def w():#finetune
    space()
    turn(110)
    line(2)
    line(-1.8)
    turn(-65)
    line(2)
    turn(-120)
    line(2)
    turn(110)
    line(2)
    line(-1.8)
    turn(-70)
    space()
def x():
    turn(50)
    line(2)
    line(-0.8)
    turn(80)
    line(1)
    line(-1.8)
    turn(-130)
    space()
def y():
    space()
    turn(107)
    line(2)
    line(-1.8)
    turn(-58)
    line(2)
    line(-4)
    line(2.2)
    turn(-68)
    space()
def z():
    space()
    space()
    turn(90)
    line(0.1)
    turn(90)
    line(2)   #might be weird
    turn(-135)
    line(2.5)
    turn(135)
    line(2)
    line(-1.8)
    turn(40)
    line(2.5)
    turn(135)
    line(2)
    turn(-90)
    line(0.1)
    turn(90)
    space()
def space():
    line(1)
