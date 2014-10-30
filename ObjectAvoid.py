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
    #values for turning at optimal speed
    turningValue = 0.5
    turningTime = 1.38

    #values for extra moving forward optimal amount to get body of robot past obstacle
    extraValue= 0.58
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
        values[count] = self.frontTooClose()
        count += 1
		#the loop will run until all the values becomes True
        while not(values[0] and values[1] and values[2]):
            motors(self.driveValue, self.driveValue)
            values[count] = self.frontTooClose()
            count += 1

            if count > 2:
                count = 0
            print "%r %r %r" % (values[0], values[1], values[2])
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

    #Turn slightly right
    turnRight(0.5, 0.7)

    total = 0
    #Measure the right sensor value ten times
    for x in xrange(0, 10):
        total += getObstacle('right')
	#calculate the average of the ten values
    print total / 10
	#if the average is greater than 500
    if total / 10 > 500:
        flag = False #then Obstacle present
	#else flag becomes true, telling the robot that there is nothing on its right
	else:
        flag = True

    #Turn back to left after the checking is done
    turnLeft(0.5, 0.7)
	#return the flag (as the loop is outside the function) and the time elapsed to do the checking
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
		#keeps moving front until it detects something and then turns left
        test.moveForwardDetectFront()
        turnLeft(test.turningValue,test.turningTime)
		
		#First part of the 'moving around the box'
        flag = False #tells the program that the robot is in the process of moving around the obstacle
		
		#runs the loop when the robot needs to keep track of time
        while not flag:
            forward(0.5, 0.6)
            (time, flag) = checkContinue() 
            totalTime -= time;
		#loop breaks when the right sensors detect that there is nothing on the right
		#totalTime stores the actual time the robot spent moving, later used to move back to its position
        totalTime += currentTime() - startTime 
		
		#move the extra bit forward and then turnRight
        test.moveExtraBitForward()
        turnRight(test.turningValue, test.turningTime)
		
        # Side of box
        test.moveExtraBitForward()
		#do the same thing as the previous section without keeping track of time
        flag = False
        while not flag:
            forward(0.5, 0.6)
            (time, flag) = checkContinue()
        test.moveExtraBitForward()
        turnRight(test.turningValue,test.turningTime + 0.1)

        #final side
        startTime = currentTime()
		#moves until the tracked time is up
        while currentTime() < startTime + totalTime:
            forward(0.5, 0.1)
		
		#turns left after the robot gets to where it was.
        turnLeft(test.turningValue, test.turningTime)
            
main()
