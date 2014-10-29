Scribbler
=========
SE 101 Group Project

##Introduction
The Scribbler robot group project exists in order to introduce the first year Software Engineering at University of Waterloo to working with hardware limitations in real life. The Myro Scribbler bot is equipped with extremely terrible hardware, which makes it the perfect piece of hardware for prospective software engineers to work with.
  Initially the objective of our team is to write a program that will make the robot avoid obstacles with the help of its terrible sensors. After this initial demo, we will start working towards our main project: A text-speech and speech-text program.

##Obstacle Avoidance
###Initial conditions
The robot is set on the floor with a box and/or other obstacles in its path.
###Objective
The robot must avoid the hitting the obstacle by moving around it.
###Requirements
While avoiding the obstacle the robot must remain within 2-5 cm (1-2 inches) of the object, furthermore the
robot should return to its original route after successfully avoiding the object. That is, the robot may not
touch the object nor may it deviate too much from its course.
###First Demo Grading
For tests (1)-(3), there is 1 mark for staying within the specified distance from the obstacle and 1 mark for
returning to within 20° of the original trajectory.
###Program Structure

####List of Variables

* initialTurn

   stores a boolean value to represent whether the robot has turned at the beginning, this helps the robot to keep moving forward without worrying UNTIL it detects something with its front sensors
* initialTurnTime
* restart

   stores a boolean value to control the turning on and off of the robot and its connection to the program.
* turningValue
* turningTime
* extraValue
* extraTime
* driveValue
* sideDistance and frontDistance

   stores the sensitivity cap for the sensors

####List of Functions

* moveForwardDetectFront ()

   As the name suggests, the robot moves forward and looks out for objects with the front sensor. It contains an array of booleans named values. All the values of this array is initiated to False. Each  of these elements are used to track whether the front sensor detects everything. Although using one value instead of an array of three element SHOULD have been enough, the terribly inconsistent sensor on the Myrobot are too unpredictable, so we are using three values instead of one.  
   When all the values are False, i.e. the function frontTooClose keeps returning False, the robot will keep moving. We are making the robot move by sending in the driveValue to the motors() function in a loop (which keeps running until ALL the values are True). Moreover, in each loop, the frontTooClose() values are stored alternatively in the three elements of value. When the loop is finally broken (as all of the elements become True), it sets the initialTurn variable to True and stops the function.
	
* checkContinue()

   This function implements our algorithm to keep detecting objects on the right. The robot moves a bit, turns slightly right, uses the sensors, and if the sensors detect anything, it turns back to its original orientation, and keeps moving. This loop continues until the sensors don't detect anything. At that point, the object turns right.


####The main()

The main starts off by setting a name for the robot and instantiating a new Robot object labelled test. To keep track of the starting time, the startTime variable is used and it stores the currentTime() return value. To keep track of the total time elapsed, the totalTime is initiated with a value of 0.  
The next part runs an infinite loop in steps. At first the robot moves forward until it detects anything in the front. After that function stops, the robot turns left. Then a new boolean variable is introduced, named flag, which keeps track of whether the robot need to keep track of its movement time. Basically, flag becomes False whenever the robot is in the process of moving around the obstacle.

	
##Contributors
* Justin Li
* David Zhang
* Leonardo Shao
* Sadman Kazi
* Tammy Liu
* Shan Phylim
 
