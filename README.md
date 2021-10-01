# Vichesta-Robonauts

The GitHub Repository for Vichesta'21 by Team Robonauts

## Run the simulation

- Clone this repository in the `src` folder of your catkin workspace.
- Inside your workspace folder, run `catkin build`.
- Open a terminal and run the following command to start the simulation:
  ```
  roslaunch takshak all.launch
  ```
- Open a new terminal and run the following command:
  ```
  rosrun takshak move.py
  ```
  
## Features in our approach:
- Bot can run autonomously in any environment, because it takes a static map made by implementing SLAM on the environment, generates global and local costmaps, get the required path from Navfn global planner and DWA local planner prevents collisions.
- We haven't hard coded the coloured boxes, aruco codes and coloured gates, instead, the approach is generalized. The order of coloured boxes, aruco markers and coloured gates can vary, and still the bot will get correct results.


### Exernal ROS Packages used:
- ROS Navigation Stack https://github.com/ros-planning/navigation.git </br>
- cmvision https://github.com/teshanshanuka/cmvision.git
- cv_bridge https://github.com/ros-perception/vision_opencv.git
