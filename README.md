# An architecture to build a multimodal dataset for gesture recognition
This project consist in two software architectures, one that allows to easily acquire data from the three available sensors (i.e. Kinect, Smartwatch and MOCAP) in order to build a multimodal dataset and the other one is to visualize the data stored.
The dataset will be built for 5 types of gesture, namely pouring, drinking, sitting down, standing up and walking, using the sensors mentioned above.

## Authors
* Francesco Porta: francy857@gmail.com
* Davide Piccinini: piccio98dp@gmail.com
* Sara Romano: sara.romano.15@gmail.com
* Aurora Bertino: au1698@icloud.com
* Silvana Andrea Civiletto:

## Architecture of the System
The “Gesture Sequence Generator” module is the implementation of the server of a service-client
pattern; the “Experimenter GUI” represents all the graphical part of the architecture (divided into “Configuration UI”, which contains the management of the recording’s configuration, and
“Communication with User UI”, where the user can control the recording and where images and
time elapsed are displayed); the three “Sensor Modules” collect data from the sensors (MOCAP,
Smartwatch and Kinect) and when they receive the signals from the Experimenter_GUI, they
publish datas in a topics (one for each type of message); the three “Record Modules” read data
from the topics published by the Sensor Modules and record them into a Rosbags; the
“Conversion and Segmentation” module is commissioned to convert the data from “rosbag” to
“csv” format, to assign certain labels to it and to segment them.

<p align="center"> 
<img src="https://github.com/FraPorta/Itslit/blob/master/ExperimenterDiagram.jpg?raw=true">
</p>

## Contents of the repository
In this section we will explain the repository's content.

### Dependence
This folder contains 3 packages: "mocap_optitrack", "kinect_aux-indigo", "openni_camera-indigo-devel".
"mocap_optitrack" is a package developed for ROS Indigo. It is cloned by the repository https://github.com/ACarfi/SOFAR and it publishes markers's position on the topic '/markers_coo'. It should be launched with the command "mocap.launch" before the experiment starts to collect real mocap data.

### Files
This is the folder in which the files created with the application will be stored.

### Pictures
This folder contains the several images that need to be displayed in the GUI in order to concisely communicate to the user what gesture he/she has to perform at a given time.

### Launch
This folder contains two launchfiles: one executes the whole application and the other one executes the nodes which mimic the hardware's functioning.

### Msg

### Src
This folder contains all the nodes that make up the main program: "GUI_node" initializes the GUI and deals with the logic behind the graphical elements, which makes the user navigate between windows, write personal informations, select which sensors to use, and so on; the "gestures_nodes" implements the server which manages the request for a random gesture sequence; the "fake_node_imu" creates fake simulated data from the Smartwatch; the "Smartwatch_node" manages data from Smartwatch sensor: it saves data when it is required by user; the "Recorder_IMU" saves data Imu into a Rosbag; the "fake_node_pc" create fake simulated data from the Kinect; the "kinect_node" manages data from Kinect sensor: it saves data when it is required by user; the "Recorder_PC" saves data PointCloud2 into a Rosbag; the "mocap_fake" creates fake simulated data from the Mocap; the "Mocap_node" manages data from Mocap sensor: it saves data when it is required by user; the "Recorder_mocap" saves Mocap data into a Rosbag. 
In addition to these 2 files, there's also the following folder.

### Lib
This folder contains 2 important sub-folders, "Tools" and "Windows".

### Tools
This folder contains code which is needed in bigger programs: "gesture_sequence_client" implements the class to istantiate the client side of the service-client pattern; "startmsg_publisher" implements the class to create the publisher side of a publish-subscribe pattern.

### Windows
This folder contains the code which encapsulates both the windows and their elements, which are istantiated in "GUI_node": here lies the code for the configuration window, the recording/communication with user window and the several tutorial windows.
The code consists in classes created using "Qt5Designer" a program which lets you build up a graphical user interface by dragging components onto a window: we end up with a ".ui" file, which is then converted to python code.

### Srv
This folder contains the simple ".srv" file that encodes the request-response structure of the service-client pattern.


## Installation
The first thing to do, after having cloned the repository in the Ros workspace, is to build the package and install in order to make the ‘msg’ and ‘srv’ files executable, using the following commands in the workspace:
    
    ```
    catkin_make
    catkin_make install
    ```

Then it is necessary to install a Ros related Python library (this passage may not be required if the pc on which the modules will be installed has already other Ros projects developed with Python 3). 
    
    ```
	sudo apt-update
	sudo apt install python3-pip
    sudo apt-get install python3-yaml	
    sudo pip3 install rospkg catkin-pkg 
    pip3 install --user pyqt5
	sudo apt-get install python3-pyqt5
    ```

To run the system:
    
    ```
    roslaunch multimodal_dataset_creation fake_nodes.launch
    roslaunch multimodal_dataset_creation experimenter_GUI.launch
    ```

# Rqt_graph
<p align="center"> 
<img src="https://github.com/FraPorta/Itslit/blob/master/rqt.png?raw=true">
</p>

### Modules
* "Experimenter_GUI" Module
* "Gesture Sequence Generator" Module
* "Fake Imu" Module
* "Smartwatch" Module
* "Fake PointCloud2" Module
* "Kinect" Module
* "Recorder Imu" Module
* "Recorder PC" Module
* "Recorder Mocap" Module
* "mocap fake" Module
* "Mocap node" Module
* "Conversion and Segmentation" Module
	
## Report

The report was added to the Google Drive link shared on Slack.
