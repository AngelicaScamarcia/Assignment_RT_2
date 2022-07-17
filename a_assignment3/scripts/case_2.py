#! /usr/bin/env python

"""
.. module:: case_2
   :platform: Unix
   :synopsis: Python code to let the user drive the robot
.. moduleauthor:: Angelica Scamarcia <s5290802@studenti.unige.it>

Service:
    /kb_input

This node implements the lauching of:
   case 2. the user can drive the robot as he wants without any constraints
   case 3. the user drives the robot with the collision control, that is able to avoid the user to hit obstacles.
"""

import rospy
from a_assignment3.srv import Kb_input	
import os   

def manage(req):
    """
    Function called case 2 and case 3 
    
    Args:
        *request(float64 x, float64 y)* coming from the move_base_msgs
    
    The choice of the user passes to the `os` to launch the chosen launch file
    """
    #read the request and then the function chose to call case 2 or 3
    if req.kb_case == 1:
       #call the launcher for case 3 (keyboard teleop)
       os.system("roslaunch a_assignment3 case_2.launch") 
       
    elif req.kb_case == 2:
        #call keyboard teleop and obstacle avoidance 
        print("call teleop twist keyboard")
        #call the launcher for case 3
        os.system("roslaunch a_assignment3 case_3.launch")
    
    else:
        print("wrong input")
    
    return 0         
   
   
def input_keyboard_server():  
    """
    Function that describes the node `keyboard_controller` to the user.
    
    It calls the service handler to manage the `kb_input` service, taking the values from the `manage` function.
    """
    # define some information about the node 
    print("keyboard controlling for robot")
    #initialize the node
    rospy.init_node('keyboard_controller')
    
    #call server service 
    service = rospy.Service('kb_input', Kb_input , manage)
    print("service ready")
    rospy.spin()

#main
if __name__=="__main__":
    input_keyboard_server()
