#include "ros/ros.h"              
#include "std_msgs/Float32MultiArray.h"    
#include <sstream>
#include "std_msgs/Header.h"

#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>

/// This node computes fake mocap data

int main(int argc, char **argv) 
{
    ros::init(argc, argv, "mocap_fake");   

    ros::NodeHandle  n;  

/// Fake mocap data Publisher
    ros::Publisher markers_coordinates = n.advertise<std_msgs::Float32MultiArray>("fake_data_mocap",1);

     while(ros::ok()) { 

      std_msgs::Float32MultiArray array;

      array.data.push_back(0.0);       
      array.data.push_back(0.0);
      array.data.push_back(0.0);
 
 /// Publishing fake mocap data (all values settled to zero)
     markers_coordinates.publish(array);   
       
     }

return 0;

}

    