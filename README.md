# :curly_loop: cubic-traj-gen

- Code developed by Kaviraj Gosaye, QMUL
- Student ID: 220575371
- Package Name : ar_week8_test

## :loudspeaker: Disclaimer

This repository is part of the deliverables for my MSc AI degree. Unauthorized reproduction of this project, including for plagiarism or any form of academic dishonesty, is strictly prohibited. The content is intended to showcase my skills and may be used for reference purposes only with proper attribution.

### :scroll: Description: 
This ROS package will automatically generate point-to-point cubic trajectories connecting pairs of randomly generated points

## :running: Commands to run package:

1. Unzip package ar_week8_test into the 'src' folder of the root directory of your catkin workspace.

2. Launch a terminal for ROS

3. Execute the following to setup environment variables: source /opt/ros/noetic/setup.bash

4. Build package (in root directory): catkin_make

5. Source the workspace: source devel/setup.bash

6. Execute the command to run the package: roslaunch ar_week8_test cubic_traj_gen.launch

>Running the step 6 will start the nodes and service and rqt_graph and rqt_plot GUI will automatically open.

- Select the topics trajPos, trajVel and trajAcc in rqt_plot to visualize the values. 
- Select Nodes/Topics(active) and click on refresh in rqt_graph to visualize the nodes and topics

## :computer: Tech and Versions:
1. Ubuntu 20.04.6 - focal
2. ROS Noetic
3. catkin
4. rqt
5. Python 3.8.10


## :open_file_folder: Package Structure:
<img src = './ros-pkg-structure.png' alt='package-structure' width='500' height='500'>

## :electric_plug: Communication Flow:
<img src = './ros-communication-flow.png' alt='package-structure' width='700' height='500'>
