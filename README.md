# ROS2 + Gazebo Robotic Arm Project

### Preferred specs: 
* Ubuntu 24.04 64-bit (bare metal, VM, or WSL)
* Quad core Intel i5 or equivalent
* 4-8GB of ram or more
* Dedicated GPU with at least 1GB VRAM (Highly reccomended)

**Instructions to install ROS2 deb packages on Ubuntu (Make sure you have ROS2 Jazzy installed)**  
LINK: [ROS2 Jazzy Installation](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)

**Install the build tool for ROS2**
```bash
sudo apt install python3-colcon-common-extensions
```

**Install Gazebo**
```bash
sudo apt-get install ros-${ROS_DISTRO}-ros-gz
```

**Run this command on every new shell to have access to ROS 2 commands**
```bash
source /opt/ros/jazzy/setup.bash
```
**Or copy/paste this line into your CLI, everytime you open a new shell this command will run automatically** 
```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```

**Run this command inside the workspace directory to compile the workspace packages**
```bash
colcon build
```

**Run this command inside the workspace directory to make ROS aware of the newly compiled packages**
```bash
source install/setup.bash
```

**Run this command inside the workspace directory to launch packages**
```bash
ros2 launch [package-name] [launch-file.py]
```
