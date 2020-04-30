#include "ros/ros.h"              
#include "std_msgs/Float32MultiArray.h"    
#include <sstream>
#include "std_msgs/Header.h"

#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>
/// @ package mocap_fake.cpp
/// This node computes fake mocap data

int main(int argc, char **argv) 
{
    ros::init(argc, argv, "mocap_fake");   

    ros::NodeHandle  n;  

/// Fake mocap data Publisher ont the topic ('fake_data_mocap')
    ros::Publisher markers_coordinates = n.advertise<std_msgs::Float32MultiArray>("fake_data_mocap",1);

     while(ros::ok()) {                   ///fake data are always pushed on the topic while the node is active

      std_msgs::Float32MultiArray array;   ///define type of data Float32MultiArray

      array.data.push_back(0.0);           ///array.data.push_back(0.0); array.data.push_back(0.0); array.data.push_back(0.0);      
      array.data.push_back(0.0);
      array.data.push_back(0.0);
      
/// 
 /// Publishing fake mocap data (all values settled to zero)
     markers_coordinates.publish(array);   
       
     }

return 0;

}

    