#!/usr/bin/env python


# load node with rosrun ...

import rospy
from std_msgs.msg import Empty
import rosplan_dispatch_msgs.msg
import rosplan_knowledge_msgs.srv
from diagnostic_msgs.msg import KeyValue
from move_base_msgs.msg import *
import actionlib
import robotControl

rospy.init_node("turtle_rosplan_interface")
# publish action feedback to /kcl_rosplan/action_feedback topic
action_feedback_pub = rospy.Publisher('/kcl_rosplan/action_feedback', rosplan_dispatch_msgs.msg.ActionFeedback, queue_size=10)
rospy.wait_for_service('/kcl_rosplan/update_knowledge_base')
# call to service /update_knowledge_base
update_kb = rospy.ServiceProxy('/kcl_rosplan/update_knowledge_base', rosplan_knowledge_msgs.srv.KnowledgeUpdateService)

def callback(msg):
	# rn : initiate action feedback variable
	feedBack = rosplan_dispatch_msgs.msg.ActionFeedback()
	# grab the action name
	feedBack.action_id = msg.action_id
	feedBack.status = "action enabled"
	action_feedback_pub.publish(feedBack)
	if msg.name == 'goto_waypoint':
		print '\ncallback success !!!!\n'
		for p in msg.parameters:
			print 'the p key is: ', p.key
			print 'the p value is: ', p.value
			if p.key == 'v':
				robot = p.value
			elif p.key == 'from':
				from_wp = p.value
			elif p.key == 'to':
				to_wp = p.value
		robotControl.robotMoveTo(from_wp, to_wp, robot)
		print '\n'*3


	feedBack = rosplan_dispatch_msgs.msg.ActionFeedback()
	feedBack.action_id = msg.action_id
	feedBack.status = "action achieved"
	action_feedback_pub.publish(feedBack)

def simple_move():
	print 'simple move online\n' * 5
	rospy.init_node('simple_move')
	sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )
	goal = MoveBaseGoal()
	goal.target_pose.pose.position.x = 1.0
	goal.target_pose.pose.orientation.w = 1.0
	goal.target_pose.header.frame_id = 'first_move'
	goal.target_pose.header.stamp = rospy.Time.now()

	#start listner
	sac.wait_for_server()

	#send goal
	sac.send_goal(goal)

	#finish
	sac.wait_for_result()

	#print result
	print sac.get_result()


rospy.Subscriber("/kcl_rosplan/action_dispatch", rosplan_dispatch_msgs.msg.ActionDispatch, callback)

rospy.spin()
