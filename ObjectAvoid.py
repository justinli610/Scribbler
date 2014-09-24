from myro import *

initialize("comX")

initialTurn = false
initialTurnTime = 0
restart = false

#values for turning at optimal speed
turningValue = 1
turningTime = 1

#values for extra moving forward optimal amount to get body of robot past obstacle
extraValue = 1
extraTime = 1

#for general driving forward power
driveValue = 1.0

#distance sensitivity for sensors
sideDistance = 100
frontDistance = 50


#for moving the robot the distance forward equivalent to the length of the robot
#this is because the sensors are located on the front of the robot
def moveExtraBitForward():
    forward(extraValue, extraTime)
    
#moves robot forward while using front sensor and stops when too close
def moveForwardDetectFront():
    while !frontTooClose():
        motors(driveValue, driveValue)
    moveExtraBitForward()
    initialTurn = true
    stop()

#moves robot forward while using right sensor and stops when too close
def moveForwardDetectRight():
    while !rightClear():
        motors(driveValue, driveValue)
        if frontTooClose():
            restart=true
            stop()
            return
        if initialTurn:
            initialTurnTime++
    if initialTurn:
        initialTurn = false
    moveExtraBitForward()
    stop()

#move forward the original distance travelled to the left of the object
def moveForwardSetTime():
    while initialTurnTime>0:
        motors(driveValue, driveValue)
        initialTurnTime--
        if frontTooClose():
            stop()
            return
    stop()
        
#detects distance from closest object in front
def frontTooClose():
    if getObstacle('middle')<frontDistance:
        return true

#detects distance from closest object to the right
def rightClear():
    if getObstacle('right')>sideDistance
        return true

def main():
    setName("Paula")
    while true:
        moveForwardDetectFront()
        turnLeft(turningValue,turningTime)
        for x in xrange(0,2):
            moveForwardDetectRight()
            if restart:
                restart = false
                continue
            turnRight(turningValue,turningTime)
        moveForwardSetTime()
        turnLeft(turningValue,turningTime)
            
main()