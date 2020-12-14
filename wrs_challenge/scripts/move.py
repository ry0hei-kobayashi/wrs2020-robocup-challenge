#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import sys
import math
rospy.init_node('move')
import utils
import time
import moveit_commander
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped

import matplotlib.pyplot as plt
import rospy
import tf
from utils import *
#rospy.init_node("arm")
#rospy.init_node("recognition")

from ipywidgets import interact
from geometry_msgs.msg import PoseStamped


if __name__=='__main__':


    try:
        #utils.move_base_goal(0, 0, 0)
        utils.move_head_tilt(-0.5)
        utils.put_object("e_lego_duplo", 0.4, 0.0, 0.0)
        utils.move_hand(1.0)
        utils.move_wholebody_ik(0.45, -0.05, 0.1, 180, 0, 0)
        utils.move_hand(0.0)
        utils.move_arm_init()

    except:
        rospy.logerr('fail to init')
        sys.exit()

    try:
        utils.move_base_goal(1.8, -0.1, -90)
        utils.move_arm_neutral()
        utils.move_hand(1)
        time.sleep(2)
        utils.move_hand(0)
        utils.move_arm_init()

    except:
        rospy.logerr('fail to init')
        sys.exit()

    try:
        utils.move_arm_init()
        utils.move_base_goal(1, 0.5, 90)
    except:
        rospy.logerr('failed to move')
        sys.exit()

    try:
        
        utils.move_arm_neutral()
        utils.move_head_tilt(-1)
        utils.move_hand(1)
       
      

        utils.get_object_list()
       
        utils.move_wholebody_ik(0.9, 1.5, 0.2, 180, 0, 90)
        utils.move_wholebody_ik(0.9, 1.5, 0.08, 180, 0, 90)

        utils.move_hand(0)
        utils.move_arm_neutral()
    except:
        rospy.logerr('fail to grasp')
        sys.exit()


    try:
        utils.move_arm_init()
        utils.move_base_goal(1.8, -0.1, -90)
        utils.move_arm_neutral()
        
        utils.move_hand(1)
        time.sleep(2)
        utils.move_hand(0)
        utils.move_arm_init()

    except:
        rospy.logerr('fail to move')
        sys.exit()
    
    try:
        utils.move_base_goal(0.85, 4.0, 180)

    except:
        rospy.logerr('fail to move')
        sys.exit()

    try:
        utils.delete_object("e_lego_duplo")
        utils.move_base_goal(0, 0, 0)
    except:
        print("first_state")
        sys.exit()