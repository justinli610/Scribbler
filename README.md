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

* turningValue and turningTime
* extraValue and extraTime
* driveValue
* sideDistance and frontDistance: stores the sensitivity cap for the sensors

####List of Functions
* **frontTooClose():** returns true if the distance of the front sensor is less that allowed frontDistance value.
   
* **rightClear():** returns true if the distance of the right sensor is less than the allowed sideDistance value.

* **moveExtraBitForward():** returns true if the distance of the right sensor is less than the allowed sideDistance value.   
   
* **moveForwardDetectFront():** As the name suggests, the robot moves forward and looks out for objects with the front sensor. It contains an array of booleans named values. All the values of this array is initiated to False. Each  of these elements are used to track whether the front sensor detects everything. Although using one value instead of an array of three element SHOULD have been enough, the terribly inconsistent sensor on the Myrobot are too unpredictable, so we are using three values instead of one.  
When all the values are False, i.e. the function frontTooClose keeps returning False, the robot will keep moving. We are making the robot move by sending in the driveValue to the motors() function in a loop (which keeps running until ALL the values are True). Moreover, in each loop, the frontTooClose() values are stored alternatively in the three elements of value. When the loop is finally broken (as all of the elements become True), it sets the initialTurn variable to True and stops the function.
	
* **checkContinue():** This function implements our algorithm to keep detecting objects on the right. The robot turns slightly right, uses the sensors, and if the sensors consistently detect something over ten frames, it turns back to its previous orientation and the program returns how much time was spent to do the checking and also return the flag as false. The flag value is returned as true when the sensors consistently detects that nothing is on the right.


####The main()

The main starts off by setting a name for the robot and instantiating a new Robot object labelled test. To keep track of the starting time, the startTime variable is used and it stores the currentTime() return value. To keep track of the total time elapsed, the totalTime is initiated with a value of 0.  

The next part runs an infinite loop in steps. At first the robot moves forward until it detects anything in the front. After that function stops, the robot turns left. Then a new boolean variable is introduced, named flag, which keeps track of whether the robot is moving along the side of the box. Basically, flag is stated to be False whenever we need to keep detecting objecs on the side. So as the robot turns left, flag becomes false and then goes into the next loop that keeps running until flag becomes true. This loop makes the robot move a little forward and keeps calling the function checkContinue() which keeps track of whether any obstacle is present on the right side of the box and returns flag as True whenever the right side of the robot is cleared. The totalTime moved by the robot is calculated after that loop ends.

The robot then moves the extra bit forward (the size of its body) so that it doesn't hit the box as it turns towards the next side of the box. The flag becomes false again and the loop continues the same way before, except this time, time is not tracked. It moves the extra bit forward and turns left again in the same way after the loop ends.

Now the robot will be moving along the final side of the box. It runs a loop that keeps track of the time and moves forward in while the loop doesn't break. The loop breaks after it runs for the same time as the previously calculated totalTime. The robot then turns left and continues in its initial path. The loop repeats.

	
##Contributors
* Justin Li
* David Zhang
* Leonardo Shao
* Sadman Kazi
* Tammy Liu
* Shan Phylim
 
