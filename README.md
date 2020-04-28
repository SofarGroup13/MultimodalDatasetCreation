# An architecture to build a multimodal dataset for gesture recognition
This project consist in two software architectures, one that allows to easily acquire data from the three available sensors (i.e. Kinect, Smartwatch and MOCAP) in order to build a multimodal dataset and the other one is to visualize the data stored.
The dataset will be built for 5 types of gesture, namely pouring, drinking, sitting down, standing up and walking, using the sensors mentioned above.

## Authors
* Francesco Porta: francy857@gmail.com
* Davide Piccinini: piccio98dp@gmail.com
* FirstName LastName: email@email.com
* FirstName LastName: email@email.com

## Architecture of the System
Here is the dataset creation architecture: the "Experimenter_GUI" is the graphical user interface used to actively interact with the underlying program; the "Gesture Sequence Generator" module is the implementation of a service-client pattern's server; 
(COMPLETE THE FOLLOWING PART)
the three sensor modules manage the interaction between the hardware and the software; the record module ... ; the "Conversion and Segmentation" module convert the "rosbag" into "csv" format and assigns labels to the data.

<p align="center"> 
<img src="https://github.com/FraPorta/Itslit/blob/master/Experimenter_UML.png?raw=true">
</p>

## Contents of the repository
In this section we will explain the repository's content.

### Pictures
This folder contains the several images that need to be displayed in the GUI in order to concisely communicate to the user what gesture he/she has to perform at a given time.

### Launch
This folder contains the launchfile that executes the whole program.

### Src
This folder contains the 2 nodes that make up the main program: "GUI_node" initializes the GUI and deals with the logic behind the graphical elements, which makes the user navigate between windows, write personal informations, select which sensors to use, and so on; the "gestures_nodes" implements the server which manages the request for a random gesture sequence.
In addition to these 2 files, there's also the following folder.

#### Lib
This folder contains 2 important sub-folders.

##### Tools
This folder contains code which is needed in bigger programs: "gesture_sequence_client" implements the class to istantiate the client side of the service-client pattern; "startmsg_publisher" implements the class to create the publisher side of a publish-subscribe pattern.

##### Windows
This folder contains the code which encapsulates both the windows and their elements, which are istantiated in "GUI_node": here lies the code for the configuration window, the recording/communication with user window and the several tutorial windows.
The code consists in classes created using "Qt5Designer" a program which lets you build up a graphical user interface by dragging components onto a window: we end up with a ".ui" file, which is then converted to python code.

### Srv
This folder contains the simple ".srv" file that encodes the request-response structure of the service-client pattern.

## Download instructions (Keep or not?)

## Installation and System Testing (Keep or not?)
This section presents (in its sub-sections) how to install/run and test the modules. **Note that:** If all the modules have successfully completed their work and integrated everything together, then this section can present the overall **Installation and Testing** procedure for the the "whole" system, instead of having a sub-section dedicated for each module. 

Please keep in mind, **do not** include in your repository the “entire” code of the external libraries that your module may use. Hence accordingly, **describe** to the new users how they can “install” the external libraries and then **describe** how they can “install” your module that uses those libraries. Afterwhich, **describe** how to run and test your module. Finally, show **(i)** the rqt_graph generated when the module is running, **(ii)** images or links to the videos showing the working of the module (in real or in simulation).

### Module < name of the module >
	.
	.
	.
	
### Module < name of the module >
	.
	.
	.

# What else should we add?
	
## Report (To be added)

This is the link to the report: [Project 13 report]()





# Useful GitHub readme syntax

## To make bullet points

* Do this
	* Do this

## To make hyper-link

For example, making a link to [ROS tutorials](http://wiki.ros.org/ROS/Tutorials)

## To show, how to execute some commands in the terminal

    ```
    sudo apt install ros-kinetic-opencv3 #(should be already installed with previous point)
    sudo apt install ros-kinetic-opencv-apps
    ```

## To exphasize about a particular command

For example: Please do a ```catkin_make```, once you have modified your code. 

## To add image(s) or video(s)

* To embbed an image

<p align="center"> 
<img src="https://github.com/yushakareem/test-delete/blob/master/light-bulb-2-256.gif">
</p>

* To link a [video](https://youtu.be/-yOZEiHLuVU)

## References

[Concept guide.](https://guides.github.com/features/wikis/)

[Syntax guide.](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

[Link to the repository that has this readme.](https://github.com/EmaroLab/GitHub_Readme_Template)
