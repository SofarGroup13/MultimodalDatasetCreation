#! /usr/bin/env python3.5
import rosbag, os, rospkg, csv, sys
from std_msgs.msg import Header, String, Float32MultiArray
from sensor_msgs.msg import PointCloud2, Imu

## Verify the correctness of input arguments
if (len(sys.argv) == 2): 
     bagFolder = sys.argv[1]
else:
     print(sys.argv)
     print("invalid number of argument")
     sys.exit(1) 

filesName = ['dati_PC', 'gesture_sequence', 'point', 'dati_IMU']

## Access to rosbag
for fileName in filesName: 
    bag = rosbag.Bag(bagFolder + "/" + fileName + ".bag")
    csvName = bagFolder + "/" + fileName + ".csv" ## Creation of new csv file for each topic
    if not(os.path.isfile(csvName)):
        with open(csvName, 'w+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter = ',')
            firstIteration = True
        	for topic, msg, t in bag.read_messages(): ## Recovery of topic list from rosbag

                    values = []
if fileName == 'dati_PC':   
                        if firstIteration:
                            header = ['ros_seconds', 'ros_nanoseconds', 'height',  'width']
                            filewriter.writerow(header)       
                            firstIteration = False      
                        values.append(msg.header.stamp.secs)
                        values.append(msg.header.stamp.nsecs)
                        values.append(int(msg.header.frame_id))
			values.append(int(msg.height)) 
                        values.append(int(msg.width))
if fileName == 'dati_IMU':   
                        if firstIteration:
                            header = ['ros_seconds', 'ros_nanoseconds', 'android_millis', 'angular_vel_x', 'angular_vel_y', 'angular_vel_z', 					       'linear_acc_x', 'linear_acc_y', 'linear_acc_z']
                            filewriter.writerow(header)       
                            firstIteration = False      
                        values.append(msg.header.stamp.secs)
                        values.append(msg.header.stamp.nsecs)
                        values.append(int(msg.header.frame_id))
                        values.append(msg.angular_velocity.x)
                        values.append(msg.angular_velocity.y)
                        values.append(msg.angular_velocity.z)
                        values.append(msg.linear_acceleration.x)
                        values.append(msg.linear_acceleration.y)
                        values.append(msg.linear_acceleration.z)
if fileName == 'point':   
                        if firstIteration:
                            header = ['ros_seconds', 'ros_nanoseconds', 'data_offset']
                            filewriter.writerow(header)       
                            firstIteration = False      
                        values.append(msg.header.stamp.secs)
                        values.append(msg.header.stamp.nsecs)
                        values.append(int(msg.header.frame_id))
                        values.append(msg.data_offset)
                        
elif fileName == 'gesture_sequence': 
                        if firstIteration:
                            header = ['ros_seconds', 'ros_nanoseconds', 'gesture_name']
                            filewriter.writerow(header)       
                            firstIteration = False   
                        values.append(msg.stamp.secs)
                        values.append(msg.stamp.nsecs)
                        values.append(msg.frame_id)
filewriter.writerow(values)
           
bag.close()
