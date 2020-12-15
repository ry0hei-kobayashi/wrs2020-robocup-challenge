
import matplotlib.pyplot as plt
#import rospyimport matplotlib.pyplot as plt
import rospy
import tf
from utils import *
rospy.init_node("recognition")


rgbd = RGBD()
utils.put_object("e_lego_duplo", 0.4, 0.0, 0.0)
utils.move_head_tilt(-1)

image_data = rgbd.get_image()
plt.imshow(image_data)
image_data.shape
image_data[0][0]

points_data = rgbd.get_points()
plt.imshow(points_data['z'])
points_data['z'].shape
points_data['z'][0][0]

h_image = rgbd.get_h_image()
plt.imshow(h_image)


from ipywidgets import interact

def f(lower = 0, upper = 255):
    yellow_region = (h_image > lower) & (h_image < upper)
    plt.imshow(yellow_region)

interact(f, lower=(0, 255, 5), upper=(0, 255, 5))



rgbd.set_h(130, 140)
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
