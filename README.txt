1. source /opt/ros/humble/setup.bash
2. colcon build
3. source install/setup.bash
4.ros2 run student_comm subscriber 2>&1 | tee sub.log
/ ros2 run student_comm publisher 2>&1 | tee pub.log

5.cat pub.log pub.log > log.txt