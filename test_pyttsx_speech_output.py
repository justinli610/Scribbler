import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 80)

voices = engine.getProperty('voices')

print len(voices)#Number of different voices in the system

voices2 = voices[62:63]#Limit range of voices to test. Doesn't include ending index

#Further testing of the voice chosen
#~ print "Using voice:", repr(voice)
#~ engine.setProperty('voice', voice.id)    
#~ engine.say("?")

for voice in voices2:
    print "Using voice:", repr(voice)
    engine.setProperty('voice', voice.id)
    
    engine.say("I hope that this program is good enough?")
    '''
    engine.say("A B C D E F G H I J K L M")
    engine.say("N O P Q R S T U V W X Y Z")
    engine.say("0 1 2 3 4 5 6 7 8 9")
    engine.say("Sunday Monday Tuesday Wednesday Thursday Friday Saturday")
    engine.say("Violet Indigo Blue Green Yellow Orange Red")
    engine.say("Apple Banana Cherry Date Guava")
    '''
engine.runAndWait()#Prevents further processes until all the queue of audio is output

print "HERE!"#prints after all of the queued output is played
