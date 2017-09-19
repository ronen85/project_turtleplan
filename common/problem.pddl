(define (problem turtlebot_demo_task)

(:domain turtlebot_demo)

(:objects
    kenny - robot
    wp0 wp1 - waypoint
)
(:init
    (connected wp0 wp1)
    (connected wp1 wp0)
    (robot_at kenny wp0)
    (= (distance wp0 wp1) 2)
    (= (distance wp0 wp1) 2)
)

(:goal (and
    (visited wp1)
    (robot_at kenny wp0)        
)))
