# Vichesta-Robonauts

The GitHub Repository for Vichesta'21 by Team Robonauts

## Run the simulation

- Clone this repository/Download the Vichesta_Robonauts folder from drive [link](https://drive.google.com/drive/folders/1MSrlq-jMzMaWwUXjhpCX-cOlR_HxB57m?usp=sharing)  in the `src` folder of your catkin workspace.
- Inside your workspace folder, run `catkin build`.
- Open a terminal and run the following command to start the simulation:
  ```
  roslaunch takshak all.launch
  ```
- Open a new terminal and run the following command:
  ```
  rosrun takshak move.py
  ```
  
### NOTE:
We have tested our package on ROS Noetic, in order to run on Melodic,in spawn_marker.py and move.py, we have to replace python3 by python in the first line. ALso, after installing wxWidgets, locate the file /usr/share/cmake-3.10/Modules and replace the contents of FindwxWidgets.cmake file from this [link](https://gist.github.com/nickoe/d3c224a2587eff8ea959bc383a993520/).

  
## Features in our approach:
- Bot can run autonomously in any environment, because it takes a static map made by implementing SLAM on the environment, generates global and local costmaps, get the required path from Navfn global planner and DWA local planner prevents collisions.
- We haven't hard coded the coloured boxes, aruco codes and coloured gates, instead, the approach is generalized. The order of coloured boxes, aruco markers and coloured gates can vary, and still the bot will get correct results.


### Exernal ROS Packages and Dependencies used:
- [ROS Navigation Stack](https://github.com/ros-planning/navigation.git)
- [cmvision](https://github.com/teshanshanuka/cmvision.git)
- [cv_bridge](https://github.com/ros-perception/vision_opencv.git)
- wxWidgets (cmvision dependency)
```
sudo apt install --no-install-recommends -y \
libgtk-3-dev  \
wx3.0-headers \
libwxgtk3.0-gtk3-dev
```
