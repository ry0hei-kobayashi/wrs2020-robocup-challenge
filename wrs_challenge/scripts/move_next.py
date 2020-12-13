#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import sys
import math
rospy.init_node('move')
import utils
import time



if __name__=='__main__':


    try:
        utils.move_head_tilt(-0.5)
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
        utils.move_hand(1)

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
        utils.move_base_goal(0, 0, 0)
        time.sleep(2)
    except:
        rospy.logerr('fail to move')
        sys.exit()
        
    try:
        utils.move_base_goal(0.85, 4.0, 0)
        utils.move_base_goal(0.85, 4.0, 180)
    except:
        rospy.logerr('fail to move')
        sys.exit()