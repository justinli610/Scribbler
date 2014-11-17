from myro import *
from WriteAlphabet import *

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
drawWord("a dog")
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
