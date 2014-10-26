from myro import *

initialize("com6")

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
    sideDistance = 400
    frontDistance = 1100


    #for moving the robot the distance forward equivalent to the length of the robot
    #this is because the sensors are located on the front of the robot
    def moveExtraBitForward(self):
        forward(self.extraValue, self.extraTime)

    #moves robot forward while using front sensor and stops when too close
    def moveForwardDetectFront(self):
        values = [0, 0, 0]
        while not(self.frontTooClose()):
            motors(self.driveValue, self.driveValue)

        #self.moveExtraBitForward()
        initialTurn = True
        stop()

    #moves robot forward while using right sensor and stops when too close
    def moveForwardDetectRight(self):
        while not(self.rightClear()):
            motors(self.driveValue, self.driveValue)
            """if self.frontTooClose():
                self.restart=True
                stop()
                return"""
            if self.initialTurn:
                self.initialTurnTime+=1
        if self.initialTurn:
            initialTurn = False
        self.moveExtraBitForward()
        stop()

    #move forward the original distance travelled to the left of the object
    def moveForwardSetTime(self):
        while self.initialTurnTime*2>0:
            motors(self.driveValue, self.driveValue)
            self.initialTurnTime-=1
            """if self.frontTooClose():
                stop()
                return"""
        stop()

    #detects distance from closest object in front
    def frontTooClose(self):
        print "Front: %d\n" % getObstacle('middle')
        if getObstacle('middle')>self.frontDistance:
            return True

    #detects distance from closest object to the right
    def rightClear(self):
        if getObstacle('right')>self.sideDistance:
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
