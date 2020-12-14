#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import sys
import math
rospy.init_node('move')
import utils
import time
import moveit_commander
from geometry_msgs.msg import PoseStamped



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
        whole_body = moveit_commander.MoveGroupCommander("whole_body_light")
        whole_body.allow_replanning(True)
        whole_body.set_workspace([-3.0, -3.0, 3.0, 3.0])

        def move_wholebody_ik(x, y, z, roll, pitch, yaw) p = PoseStamped()

    # "map"座標を基準座標に指定
            p.header.frame_id = "/map"

    # エンドエフェクタの目標位置姿勢のx,y,z座標をセットします
            p.pose.position.x = x
            p.pose.position.y = y
            p.pose.position.z = z

    # オイラー角をクオータニオンに変換します
            p.pose.orientation = quaternion_from_euler(roll, pitch, yaw)

    # 目標位置姿勢をセット
            whole_body.set_pose_target(p)
            return whole_body.go()
        #utils.move_wholebody_ik(0.9, 1.5, 0.2, 180, 0, 90)
        #utils.move_wholebody_ik(0.9, 1.5, 0.08, 180, 0, 90)

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
        utils.move_base_goal(0.85, 4.0, 0)
        utils.move_base_goal(0.85, 4.0, 180)
    except:
        rospy.logerr('fail to move')
        sys.exit()
