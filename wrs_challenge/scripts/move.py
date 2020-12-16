#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import sys
import math
rospy.init_node('move')
#from utils import *

import utils
import time
import moveit_commander
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped

#import cv2
import matplotlib.pyplot as plt
from utils import *
#rospy.init_node("arm")

import tf
#from utils import *
#rospy.init_node("recognition")
#from ipywidgets import interact


if __name__=='__main__':

    try:
	    
	    rgbd = RGBD()
	    
	    utils.put_object("e_lego_duplo", 0.4, 0.0, 0.0)
	    utils.move_head_tilt(-1)
	    
	    image_data = rgbd.get_image()
	    plt.imshow(image_data)
	    image_data.shape
	    #image_data[0][0]
	    
	    points_data = rgbd.get_points()
	    plt.imshow(points_data['z'])
	    points_data['z'].shape
	   # points_data['z'][0][0]
	    
	    h_image = rgbd.get_h_image()
	    plt.imshow(h_image)
	    
	
	    #from ipywidgets import interact
		
	    #def f(lower = 0, upper = 255):
    	#        yellow_region = (h_image > lower) & (h_image < upper)
    	#        plt.imshow(yellow_region)
	
        #    interact(f, lower=(0, 255, 5), upper=(0, 255, 5))
	    

    
	    rgbd.set_h(110,160)       
	    region = rgbd.get_region()
	    plt.imshow(region)
	    rgbd.get_xyz()
	    rgbd.set_coordinate_name("lego")
	    trans = get_relative_coordinate("map", "lego")
	    x = trans.translation.x
	    y = trans.translation.y
	    x, y

	    utils.move_hand(1)
	    utils.move_wholebody_ik(x, y, 0.1, 180, 0, 0)
	    utils.move_hand(0)
	    utils.move_arm_init()

    except:
        rospy.logerr('fail to init 0')
        sys.exit()

    try:
        utils.move_base_goal(1.8, -0.1, -90)
    except:
        rospy.logerr('fail to move')
        sys.exit()
    
    #try:
	#utils.move_head_tilt(-0.5)
        #utils.put_object("e_lego_duplo", 0.4, 0.0, 0.0)
        #utils.move_hand(1.0)
        #utils.move_wholebody_ik(0.45, -0.05, 0.1, 180, 0, 0)
        #utils.move_hand(0.0)
        #utils.move_arm_init()

    #except:
        #rospy.logerr('fail to init')
        #sys.exit()


    try:
	    target_joints = {'arm_flex_joint': 0.0, 'arm_lift_joint': 0.0, 'arm_roll_joint': 0.0, 		'head_pan_joint': 0.0, 'head_tilt_joint': 0.0, 'wrist_flex_joint': 0.0, 'wrist_roll_joint': 0.0}
	    utils.arm.go(target_joints,wait=True)
	    utils.arm.stop()
	    utils.arm.clear_pose_targets()
	    utils.move_arm_neutral()
    
    except:
        rospy.logerr('fail to move')
        sys.exit()
    
    try:
        utils.move_arm_neutral()
        utils.move_hand(1)
        time.sleep(2)
        utils.move_hand(0)
        utils.move_arm_init()

    except:
        rospy.logerr('fail to init')
        sys.exit()

    try:
        utils.move_base_goal(1, 0.5, 90)
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
    except:
        rospy.logerr('fail to move')
        sys.exit()

    try:
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
        #utils.delete_object("e_lego_duplo")
        utils.move_base_goal(0, 0, 0)
    except:
        
        sys.exit()
