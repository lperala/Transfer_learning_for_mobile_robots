# Transfer_learning_for_mobile_robots

This page contains files created for Bachelor's Thesis on Transfer_learning_for_mobile_robots

# Pre-requisites
* Ubuntu 20.04 LTS
* ROS Kinetic
* Python >=3.0

# Instructions
To install all the dependencies needed for this project, follow these steps:

1. Set up ROS: 
http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment

2. Launch the Turlebot3 in Gazebo environment:
https://automaticaddison.com/how-to-launch-the-turtlebot3-simulation-with-ros/#gazebo

3. Install OpenAI for ROS by following this tutorial:
http://wiki.ros.org/openai_ros/TurtleBot2%20with%20openai_ros
You can replace everything that says turtlebot2 with turtlebot3. 
Create your own task environment according to section 2.4 in the link above. Use the file found from our Github as the task environment: turtlebot3_task.py

# File Description
| File/Folder Name | Description |
| --- | --- |
| blender_models | Blender models used to create Gazebo environments |
| graafit | Learning graphs as .png files and learning data as .txt files |
| my_turtlebot3_openai_example | Main source files used by ROS |
| worlds | Gazebo environments created from the Blender models |
| turtlebot3_task.py | Task environment for qlearning  |

# Terminal commands
Initiate Gazebo environment, launch file name depends on the world that is launched:

>roslaunch turtlebot3_gazebo <LAUNCH_FILE_NAME>.launch

Start training the Turtlebot with OpenAI:

>roslaunch my_turtlebot3_openai_example start_training.launch

The learning curve can be plotted in real-time by using ROS rqt-multiplot:

>roslaunch rqt_multiplot rqt_multiplot

Run LiDAR spoofing script:

>python3 coordinated_laser_spoof.py
