# Assignemnt_RT_2

This assignment of the Research Track 2 course aims to control an autonomous robot that wanders into an unknown map, equipped with a laser scanner and knowing its odometry, and it is divided into three parts:
1. In the first part, it is necessary to document the code of the third       assignment of Research Track 1 course, using essentially Doxygen or Sphinx.   
2. In the second part we have to create a Jupyter notebook, starting from the third assignment of the Research Track 1 course, to replace the user interface hence, to control the robot in the three modalities.
3. In the third part we address statistical studies between my first assignment of Research Track 1 and the one from the professor's, through specific tests.


Installing and running
----------------------

First of all is necessary to clone this repository in the 'src' folder of the ROS workspace, compile it using 'catkin_make'.
After downloading and building the environment, make the ' .py ' file executable with the command:

```bash
$ chmod +x <name_of_the_script>.py
```

To run the simulation use the following command in three different terminal:

```bash
$ roslaunch final_assignment simulation_gmapping.launch
```

```bash
$ roslaunch final_assignment move_base.launch
```

```bash
$ roslaunch a_assignment3 a_launch.launch
```

In the Jupyter notebook page run all the cells of yur repository and now you can see the robot starts to move in the environment.



1.FIRST PART OF RT2
---------

For this part, I use Sphinx since I used Python to write the code of my last assignment, so I commented out every function I implemented in my code, adding an intro for every file.


Structure of the code
---------
 
The code have the script ' a_launch.launch ' which contain ' controller.py ', where you can find the functions to manage each user choice, and ' case_2.py '.

There are 4 type of choices:

1. if the user select the first choice, he must enter X and Y coordinates with which the robot can move towards a defined position; moreover the code is able to show a message which inform the user if the target is achieved or not

2. if the user select the second choice, the code called the function ' teleop_twist_keyboard ' which is the main responsible of the robot's moves

3. if the user select the third choice, the code called the function ' teleop_twist_keyboard ' which is the main responsible of the robot's moves, plus the collision handler which allow to the robot to avoid obstacles and proceed along the path smoothly

4. in the last choice, the user simply close the whole program.



2.SECOND PART OF RT2
---------

For this part, I use the Jupyter Notebook, which is an open source application used to create documents and to share it.
The aim of using this app is create buttons, for example:

-First
If first button is pushed, this function contains two buttons for x and y starting from a specified value and can be increased or decreased from the user. Accordingly a new button will appear 'send X and Y', once pressed a new function will called getting the new values of X and Y as inputs and sending them to the robot using the client server.

-Second 
If second button is pushed, other 4 buttons will appear responsible of the guidance of the robot containing the 'up' 'down' 'left' and 'right' buttons which will accordingly call a new function responsible of the velocity of the robot.

-Third
The third button will do the same job as the second but a check box will be displayed in a way that will launch the file responsible of the avoidance of the obstacles.

Moreover, two visualisers were included to track the path of the robot and the laserscan.

3.THIRD PART OF RT2
---------

For the last part, we address statistical studies between my first code of RT1 and the one given by the professor. 
I take 22 samples in which I study:
- the running time of one lap
- how many times the robot went in the wrong direction
- how many times the robot crashed 
At the end, this sampling is necessary to calculate the T-test and the Chi-Square test.


Timing of robot
---------

The timing of each laps is obtained computing the T-test of both robots and comparing them to get a conclusion.
In this case, only one of this two hypothesis may be accepted, so:

H_0 = The two robots perform in the same way

H_a = The professor's robot is faster than mine

After seeing the results, and after comparing them with the TTtable  I can discard the first option since the time calculate is grater than the one in the table.


Wrong directions of robot
---------

The wrong direction takes into account all those times the robot takes a wrong turn,after crabing and leaving a token behind, and then gets back on the right track independently. 
Also in this case, only one of this two hypothesis may be accepted, so:

H_0 = The two robots perform in the same way

H_a = The professor's robot drive better than mine

After seeing the results, and after comparing them with the TTtable  I can discard the first option since the time calculate is grater than the one in the table.


The robot crashed or not
---------

To complete this test is necessary to see the Chi-square test.
Also in this case, only one of this two hypothesis may be accepted, so:

H_0 = The two robots perform in the same way

H_a = The professor's robot is better than mine

After seeing the results, I can discard the second option since the summation is a value between 0.1 and 0.2 ( = 0,1039).






