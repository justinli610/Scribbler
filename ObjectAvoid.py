from myro import *

initialize("com6")

#To Do
'''
Put filter on Sensors to give better parameterization of distance
Set turning in intervals to help with clearing the obstacle
--> Replace 'turning time'
Need to get final path 20 degrees from exiting straight
'''

class Robot:
    initialTurn = False
    initialTurnTime = 0
    restart= False

    #values for turning at optimal speed
    turningValue = 0.5
    turningTime = 1.38

    #values for extra moving forward optimal amount to get body of robot past obstacle
    extraValue= 0.5
    extraTime= 1.8

    #for general driving forward power
    driveValue = 0.5

    #distance sensitivity for sensors
    sideDistance = 0
    frontDistance = 1090


    #for moving the robot the distance forward equivalent to the length of the robot
    #this is because the sensors are located on the front of the robot
    def moveExtraBitForward(self):
        forward(self.extraValue, self.extraTime)

    #moves robot forward while using front sensor and stops when too close
    def moveForwardDetectFront(self):
        values = [False, False, False] #assigns all the values to be false
        count = 0
        values[count] = self.frontTooClose() #
        count += 1
		#the loop will run until all the values becomes True
        while not(values[0] and values[1] and values[2]):
            motors(self.driveValue, self.driveValue)
            values[count] = self.frontTooClose()
            count += 1

            if count > 2:
                count = 0
            print "%r %r %r" % (values[0], values[1], values[2])

        #self.moveExtraBitForward()
		#tells the program that the initial turn has been executed
        initialTurn = True
        stop()

    #moves robot forward while using right sensor and stops when too close
    def moveForwardDetectRight(self):
        values = [False, False, False, False, False]
        count = 0
        values[count] = self.rightClear()
        count += 1

        while not(values[0] and values[1] and values[2] and values[3] and values[4]):
            motors(self.driveValue, self.driveValue)
            values[count] = self.rightClear()
            count += 1

            if count > 4:
                count = 0
            if self.initialTurn:
                self.initialTurnTime+=1
        if self.initialTurn:
            initialTurn = False
        #self.moveExtraBitForward()
        stop()

    #move forward the original distance travelled to the left of the object
    def moveForwardSetTime(self):
        while self.initialTurnTime*4>0:
            motors(self.driveValue, self.driveValue)
            self.initialTurnTime-=1
            """if self.frontTooClose():
                stop()
                return"""
        stop()

    #detects distance from closest object in front
    def frontTooClose(self):
        dist = getObstacle('middle')
        print "Front: %d" % dist
        if dist>self.frontDistance:
            return True

    #detects distance from closest object to the right
    def rightClear(self):
        print "Right: %d" % getObstacle('right')
        if getObstacle('right')<=self.sideDistance:
            return True

#This function is used to keep detecting objects on the right so that the robot knows when it can turn right.
def checkContinue(): # True if clear
    time = currentTime()

    #Turn to right
    turnRight(0.5, 0.7)

    total = 0
    #Measure a bunch of values and check if they're good
    for x in xrange(0, 10):
        total += getObstacle('right')

    print total / 10

    if total / 10 > 500:
        flag = False # Obstacle present, repeat
    else:
        flag = True

    #Turn back to left
    turnLeft(0.5, 0.7)

    return (currentTime() - time, flag) #time that has elapsed

def sensorTest():
    front = getObstacle('middle')
    right = getObstacle('right')
    left = getObstacle('left')
    print "Front sensor: %d\t Right sensor: %d\tLeft sensor: %d" % (front,right,left)

def main():
    setName("Paula")
    test=Robot()
    startTime = currentTime()
    totalTime = 0
    while True:
		#keeps moving front until it detects something
        test.moveForwardDetectFront()
		#turns left when it detects something
        turnLeft(test.turningValue,test.turningTime)
        flag = False #tells the program that the robot is in the process of moving around the obstacle
		
		#runs the loop when the robot needs to keep track of time
        while not flag:
            forward(0.5, 0.6)
            (time, flag) = checkContinue()
            totalTime -= time;

        totalTime += currentTime() - startTime

        test.moveExtraBitForward()

        turnRight(test.turningValue, test.turningTime)
        # Side of box
        test.moveExtraBitForward()
        flag = False
        while not flag:
            forward(0.5, 0.6)
            (time, flag) = checkContinue()
        test.moveExtraBitForward()
        turnRight(test.turningValue,test.turningTime + 0.1)

        #final side
        #test.moveExtraBitForward()

        startTime = currentTime()

        while currentTime() < startTime + totalTime:
            forward(0.5, 0.1)

        turnLeft(test.turningValue, test.turningTime)

        """for x in xrange(0,2):
            test.moveForwardDetectRight()
            test.moveExtraBitForward()
            turnRight(test.turningValue,test.turningTime)
            test.moveExtraBitForward()
        test.moveForwardSetTime()
        turnLeft(test.turningValue,test.turningTime)"""
            
main()
