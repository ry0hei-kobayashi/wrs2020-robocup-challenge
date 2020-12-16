#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import sys
import math

rospy.init_node('move')
import utils

from sensor_msgs.msg import LaserScan

#class Laser():

    #def __init__(self):
	#laser = Laser()
        # レーザースキャンのサブスクライバのコールバックに_laser_cbメソッドを登録
        #self._laser_sub = rospy.Subscriber('/hsrb/base_scan',
	#					LaserScan, self._laser_cb)
        #self._scan_data = laser.get_date()

   # def _laser_cb(self, msg):
        # レーザスキャンのコールバック関数
    #    self._scan_data = msg

    #def get_data(self):
     #   return self._scan_data

#import matplotlib.pyplot as plt
#import rospy
#import tf
#from utils import *
#rospy.init_node("recognition")
#rgbd = RGBD()

#image_data = rgbd.get_image()
#plt.imshow(image_data)
#image_data.shape
#image_data[0][0]
#points_data = rgbd.get_points()
#plt.imshow(points_data['z'])
#points_data['z'].shape
#points_data['z'][0][0]
#h_image = rgbd.get_h_image()
#plt.imshow(h_image)

#from ipywidgets import interact

#def f(lower = 0, upper = 255):
#    yellow_region = (h_image > lower) & (h_image < upper)
#    plt.imshow(yellow_region)

#interact(f, lower=(0, 255, 5), upper=(0, 255, 5))

#rgbd.set_h(130, 140)

#region = rgbd.get_region()
#plt.imshow(region)
#rgbd.get_xyz()
#rgbd.set_coordinate_name("lego")

#trans = get_relative_coordinate("map", "lego")
#x = trans.translation.x
#y = trans.translation.y
#x, y

#move_hand(1)

#move_wholebody_ik(x, y, 0.1, 180, 0, 0)
#move_hand(0)
#move_arm_init()




if __name__=='__main__':

    try:
        # 視線を少し下げる
        utils.move_head_tilt(-0.4)
    except:
        rospy.logerr('fail to init')
        sys.exit()

    try:
        # 移動姿勢
        utils.move_arm_init()
        # 長テーブルの前に移動
        utils.move_base_goal(1, 0.5, 90)
    except:
        rospy.logerr('fail to move')
        sys.exit()

    try:
        # 把持用初期姿勢に遷移
        utils.move_arm_neutral()
        # 手を開く
        utils.move_hand(1)
        # 手を伸す
        utils.move_wholebody_ik(0.9, 1.5, 0.2, 180, 0, 90)
        # 手を下げる
        utils.move_wholebody_ik(0.9, 1.5, 0.08, 180, 0, 90)
        # 手を閉じる
        utils.move_hand(0)
        # 把持用初期姿勢に遷移
        utils.move_arm_neutral()
    except:
        rospy.logerr('fail to grasp')
        sys.exit()

    try:
        # 移動姿勢
        utils.move_arm_init()
        # トレーの前に移動
       # utils.move_base_goal(1.8, -0.1, -90)
        # 手を前に動かす
        utils.move_arm_neutral()
        # 手を開く
        utils.move_hand(1)
    except:
        rospy.logerr('fail to move')
        sys.exit()
