#!/usr/bin/env python

import sys
import roslib
import rospy

# Brings in the SimpleActionClient
import actionlib

from move_base_msgs.msg import *

def simple_move_client(x_pos = 0.0, y_pos = 0.0, robot = ''):
    rospy.init_node(robot + 'simple_move')
    client = actionlib.SimpleActionClient(robot + 'move_base', MoveBaseAction)
    # create goal
    goal = MoveBaseGoal()
    #set goal
    goal.target_pose.pose.position.x = x_pos
    goal.target_pose.pose.position.y = y_pos
    goal.target_pose.pose.orientation.w = 1.0
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()
    # send goal to client
    client.send_goal(goal)
    # finish
    client.wait_for_result()
    # print result
    print client.get_result()
    print 'DONEEE'

def robotMoveTo(from_wp, to_wp, robot):
    print 'robotMoveTo success'*3
    robot = ''
    # rospy.init_node(robot + 'simple_move')
    client = actionlib.SimpleActionClient(robot + 'move_base', MoveBaseAction)
    # create goal
    x_pos = 0.5
    y_pos = 0.5
    goal = MoveBaseGoal()
    goal.target_pose.pose.position.x = x_pos
    goal.target_pose.pose.position.y = y_pos
    goal.target_pose.pose.orientation.w = 1.0
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()
    # send goal to client
    client.send_goal(goal)
    # finish
    client.wait_for_result()
    # print result
    print client.get_result()
    print 'robotMoveTo done'*3

if __name__ == '__main__':
    try:
        simple_move_client(0.5, 0.5)
    except rospy.ROSInterruptException:
        print "Keyboard Interrupt"
