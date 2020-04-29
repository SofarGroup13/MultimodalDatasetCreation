#include "ros/ros.h"              
#include "std_msgs/Float32MultiArray.h"    
#include <sstream>
#include "std_msgs/Header.h"

#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>

// This node compute fake mocap data

int main(int argc, char **argv) 
{
    ros::init(argc, argv, "mocap_fake");   

    ros::NodeHandle  n;  
    ros::Publisher markers_coordinates = n.advertise<std_msgs::Float32MultiArray>("/mocap_data",1);
    

     while(ros::ok()) { 

      std_msgs::Float32MultiArray array;

      array.data.push_back(0.0);       
      array.data.push_back(0.0);
      array.data.push_back(0.0);
 
     markers_coordinates.publish(array);
       
     }

return 0;

}















