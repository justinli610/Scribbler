from myro import *

initialize("com6")

class Robot:
	#initialTurn: 0 for forward, 1 for going left, -1 for going forward for beside the obstacle and 2 for going right
    initialTurn = 0
    initialTurnTime = 0
    restart= False

    #values for turning at optimal speed
    turningValue = 1
    turningTime = 0.75

    #values for extra moving forward optimal amount to get body of robot past obstacle
    extraValue= 1
    extraTime= 1

    #for general driving forward power
    driveValue = 1.0

    #distance sensitivity for sensors
    sideDistance = 400
    frontDistance = 1000


    #for moving the robot the distance forward equivalent to the length of the robot
    #this is because the sensors are located on the front of the robot
    def moveExtraBitForward(self):
        forward(self.extraValue, self.extraTime)

    #moves robot forward while using front sensor and stops when too close
    def moveForwardDetectFront(self):

        while not(self.frontTooClose()):
            motors(self.driveValue, self.driveValue)
        initialTurn = True
        stop()

    #moves robot forward while using right sensor and stops when too close
    def moveForwardDetectRight(self, turnVal):
        while not(self.rightClear()):
            motors(self.driveValue, self.driveValue)
            if self.frontTooClose():
                self.restart=True
                stop()
                return
            if self.initialTurn:
                self.initialTurnTime+=1
        if self.initialTurn:
            initialTurn = False
        self.moveExtraBitForward()
        stop()

    #move forward the original distance travelled to the left of the object
    def moveForwardSetTime(self):
        while self.initialTurnTime>0:
            motors(self.driveValue, self.driveValue)
            self.initialTurnTime-=1
            if self.frontTooClose():
                stop()
                return
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
        if turn == 0:
			#keep moving forward and detecting objects in the front
			moveForwardDetectFront (test)
			turn = 1
			
		#enter this loop when detecting the right side things are important
		else if abs(turn) == 1:
			#keep moving forward and increase the timer ONLY IF turn = +1
			
			#keep detecting objects on the right
			if moveForwardDetectRight:
				#turn right
				if turn = 1:
					turn = 2
				if turn = -1:
					turn = 2
		else if turn == 2:
			#keep moving forward and decrease the timer
			if (timer < 0)
				#turn left
				turn = 0
            
main()