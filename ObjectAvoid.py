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
    turningValue = 1
    turningTime = 0.73

    #values for extra moving forward optimal amount to get body of robot past obstacle
    extraValue= 1
    extraTime= 1

    #for general driving forward power
    driveValue = 0.5

    #distance sensitivity for sensors
    sideDistance = 0
    frontDistance = 1050


    #for moving the robot the distance forward equivalent to the length of the robot
    #this is because the sensors are located on the front of the robot
    def moveExtraBitForward(self):
        forward(self.extraValue, self.extraTime)

    #moves robot forward while using front sensor and stops when too close
    def moveForwardDetectFront(self):
        values = [False, False, False]
        count = 0
        values[count] = self.frontTooClose()
        count += 1
        while not(values[0] and values[1] and values[2]):
            motors(self.driveValue, self.driveValue)
            values[count] = self.frontTooClose()
            count += 1

            if count > 2:
                count = 0

        #self.moveExtraBitForward()
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
        print "Front: %d" % getObstacle('middle')
        if getObstacle('middle')>self.frontDistance:
            return True

    #detects distance from closest object to the right
    def rightClear(self):
        print "Right: %d" % getObstacle('right')
        if getObstacle('right')<=self.sideDistance:
            return True

def sensorTest():
    front = getObstacle('middle')
    right = getObstacle('right')
    left = getObstacle('left')
    print "Front sensor: %d\t Right sensor: %d\tLeft sensor: %d" % (front,right,left)

def main():
    setName("Paula")
    test=Robot()
    while True:
        test.moveForwardDetectFront()
        turnLeft(test.turningValue,test.turningTime)
        for x in xrange(0,2):
            test.moveForwardDetectRight()
            """if test.restart:
                test.restart = False
                continue"""
            test.moveExtraBitForward()
            turnRight(test.turningValue,test.turningTime)
            test.moveExtraBitForward()
        test.moveForwardSetTime()
        turnLeft(test.turningValue,test.turningTime)
            
main()
