from myro import *

initialize("comX")

initialTurn = false
secondTurn = false

def moveForwardDetectFront():
    while !frontTooClose():
        motors(1.0, 1.0)
    
def moveForwardDetectRight():
    while !rightClear():
        motors(1.0, 1.0)

def moveForwardDetectLeft():

def frontTooClose():
    if getObstacle('middle')<50:
        return true

def rightClear():
    if getObstacle('right')>100
        return true

def moveOuttaTheWay():
    initialTurn = true
    
def 

def main():
    setName("Paula")
    while true:
        moveForward()
        turnLeft(1,1)
        else if secondTurn
            
        else if frontTooClose():
            goingAroundObstacle = true
        else
            motors(1.0, 1.0)
            
main()