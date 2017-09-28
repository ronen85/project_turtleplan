#!/bin/bash

# add rob-a as an object
rosservice call /kcl_rosplan/update_knowledge_base "update_type: 0
knowledge:
  knowledge_type: 0
  instance_type: 'robot'
  instance_name: 'rob-a'
  attribute_name: ''
  function_value: 0.0";

# add a1 as an object
rosservice call /kcl_rosplan/update_knowledge_base "update_type: 0
knowledge:
  knowledge_type: 0
  instance_type: 'waypoint'
  instance_name: 'a1'
  attribute_name: ''
  function_value: 0.0";

# add a2 as an object
rosservice call /kcl_rosplan/update_knowledge_base "update_type: 0
knowledge:
  knowledge_type: 0
  instance_type: 'waypoint'
  instance_name: 'a2'
  attribute_name: ''
  function_value: 0.0";

# add fact : a1 a2 are connected
rosservice call /kcl_rosplan/update_knowledge_base "update_type: 0
knowledge:
  knowledge_type: 1
  instance_type: ''
  instance_name: ''
  attribute_name: 'connected'
  values:
  - {key: 'from', value: 'a1'}
  - {key: 'to', value: 'a2'}
  function_value: 0.0";

# add fact : a2 a1 are connected
rosservice call /kcl_rosplan/update_knowledge_base "update_type: 0
knowledge:
  knowledge_type: 1
  instance_type: ''
  instance_name: ''
  attribute_name: 'connected'
  values:
  - {key: 'from', value: 'a2'}
  - {key: 'to', value: 'a1'}
  function_value: 0.0";

# add fact (robot_at rob-a a1)
rosservice call /kcl_rosplan/update_knowledge_base "update_type: 0
knowledge:
  knowledge_type: 1
  instance_type: ''
  instance_name: ''
  attribute_name: 'robot_at'
  values:
  - {key: 'v', value: 'rob-a'}
  - {key: 'wp', value: 'a1'}
  function_value: 0.0";

# add fact (free a2)
rosservice call /kcl_rosplan/update_knowledge_base "update_type: 0
knowledge:
  knowledge_type: 1
  instance_type: ''
  instance_name: ''
  attribute_name: 'free'
  values:
  - {key: 'wp', value: 'a2'}
  function_value: 0.0";

# add goal (robot_at rob-a a2)
rosservice call /kcl_rosplan/update_knowledge_base "update_type: 1
knowledge:
  knowledge_type: 1
  instance_type: ''
  instance_name: ''
  attribute_name: 'robot_at'
  values:
  - {key: 'v', value: 'rob-a'}
  - {key: 'wp', value: 'a2'}
  function_value: 0.0"
