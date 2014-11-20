from Alphabet import *
from myro import *

initialize("com6")

def drawWord(a):
    for i in xrange(len(a)):
        speak(a[i])
        drawLetter(a[i])
    speak(a)


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
    if (arg == 'g'):
        g()
        return
    if (arg == 'h'):
        h()
        return
    if (arg == 'i'):
        i()
        return
    if (arg == 'j'):
        j()
        return
    if (arg == 'k'):
        k()
        return
    if (arg == 'l'):
        l()
        return
    if (arg == 'm'):
        m()
        return
    if (arg == 'n'):
        n()
        return
    if (arg == 'o'):
        o()
        return
    if (arg == 'p'):
        p()
        return
    if (arg == 'q'):
        q()
        return
    if (arg == 'r'):
        r()
        return
    if (arg == 's'):
        s()
        return
    if (arg == 't'):
        t()
        return
    if (arg == 'u'):
        u()
        return
    if (arg == 'v'):
        v()
        return
    if (arg == 'w'):
        w()
        return
    if (arg == 'x'):
        x()
        return
    if (arg == 'y'):
        y()
        return
    if (arg == 'z'):
        z()
        return
    if (arg == ' '):
        space()
        space()
        return
    return
'''
move(translate, rotate)
First param: 1, forward, -1, backwards, fullspeed
Second param: 1, left, -1, right, fullspeed

phrase = speech.input()
print phrase
drawWord (phrase)

def callback(phrase, listener):
    if phrase == "stop":
        listener.stoplistening()
    drawWord(phrase)

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

def	returnToBase():
	beep(1, 440)
	ask("Remove drawing device and press \"OK\"")
	print ("Returning to baseline")
	turn(-90)
	while get("line")[0] == 0 or get("line")[1] == 0:
		forward(0.3, 0.5)
	stop()
	turn(90)
	
listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)

while True:
    pass
    '''
