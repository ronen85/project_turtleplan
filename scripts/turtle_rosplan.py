#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
import rosplan_dispatch_msgs.msg
import rosplan_knowledge_msgs.srv
from diagnostic_msgs.msg import KeyValue
from move_base_msgs.msg import *
import actionlib

waypoints = {'a1': [0  , 0],   'a2': [0  , -2], 'a3': [0  , -4],
             'b1': [3.6, 0.7], 'b2': [3.6, -2], 'b3': [3.6, -4.7],
			 'c1': [7  , 0],   'c2': [7  , -2], 'c3': [7  , -4]}

def callback(msg):
	print 'callback initiate\n', '\n'*5
	# initiate action feedback variable
	feedBack = rosplan_dispatch_msgs.msg.ActionFeedback()
	# grab the action name
	feedBack.action_id = msg.action_id
	feedBack.status = "action enabled"
	# initial action feedback update
	action_feedback_pub.publish(feedBack)
	# start move_to command
	if msg.name == 'goto_waypoint':
		for p in msg.parameters:
			print 'the p key is: ', p.key
			print 'the p value is: ', p.value
			if p.key == 'v':
				robot = p.value
			elif p.key == 'from':
				from_wp = p.value
			elif p.key == 'to':
				to_wp = p.value
		[x_cord, y_cord] = waypoints[to_wp]
		print 'x_cord, y_cord are: ', x_cord, y_cord
		simple_move_client(x_cord, y_cord, robot)
		# robotControl.robotMoveTo(from_wp, to_wp, robot)
		print '\n'*3
	# update and publish feedback variable
	feedBack = rosplan_dispatch_msgs.msg.ActionFeedback()
	feedBack.action_id = msg.action_id
	feedBack.status = "action achieved"
	action_feedback_pub.publish(feedBack)

def simple_move_client(x_pos = 0.0, y_pos = 0.0, robot = ''):
	print 'client initiate...'
	# initiate client varaiable
	print 'wait for movebase node: ', robot + '/move_base'
	client = actionlib.SimpleActionClient(robot + '/move_base', MoveBaseAction)
	print 'client is online !'
	# initiate goal varaiable
	goal = MoveBaseGoal()
	# set goal
	goal.target_pose.pose.position.x = x_pos
	goal.target_pose.pose.position.y = y_pos
	goal.target_pose.pose.orientation.w = 1.0
	goal.target_pose.header.frame_id = robot + '_tf/map'
	goal.target_pose.header.stamp = rospy.Time.now()
	# Waits until the action server is online
	client.wait_for_server()
	# send goal to client
	client.send_goal(goal)
	# wait for result
	client.wait_for_result()
	# print result
	print client.get_result()
	print 'DONE'

# initiate node
rospy.init_node("turtle_rosplan_interface")
# publish action feedback to /kcl_rosplan/action_feedback topic
action_feedback_pub = rospy.Publisher('/kcl_rosplan/action_feedback', rosplan_dispatch_msgs.msg.ActionFeedback, queue_size=10)
rospy.wait_for_service('/kcl_rosplan/update_knowledge_base')
# call to service /update_knowledge_base
update_kb = rospy.ServiceProxy('/kcl_rosplan/update_knowledge_base', rosplan_knowledge_msgs.srv.KnowledgeUpdateService)
# subscribe to action_dispatch server
rospy.Subscriber("/kcl_rosplan/action_dispatch", rosplan_dispatch_msgs.msg.ActionDispatch, callback)
# loop over ...
rospy.spin()
