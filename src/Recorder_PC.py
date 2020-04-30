#! /usr/bin/env python
## @package Recorder_PC.py
#This node is created for recording all datas from Kinect in a Rosbag.

import os, glob
import rosbag
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

##class RecorderPC
class RecorderPC(object):
    #initialization
    def init(self):
        ##defining folder
        self.workingDirectory = os.path.dirname(os.path.abspath(__file__))
        self.parentDirectory = os.path.dirname(self.workingDirectory)
        self.filesDirectory = os.path.join(self.parentDirectory,"files")


        self.data = PointCloud2()
        self.flag_start=False
        ##subscriber to the topic with data PC
        rospy.Subscriber('/kinect_data', PointCloud2, self.callback) #subscriber to topic published by Kinect_node
        ##function for callback
    def callback(self,data):
        self.data = data
        self.flag_start = True

    def run(self):
        self.init()
        while True:
            try:
                if self.flag_start: #this bool is acrived when the topic has data
                    ##saving rosbag into a defined folder
                    self.folder_path = max(glob.glob(os.path.join(self.filesDirectory, '*/')), key=os.path.getmtime)
                    ##creation rosbag
                    bag1 = rosbag.Bag((os.path.join(self.folder_path,'dati_PC.bag')), 'w') #creation of rosbag
                    try:
                        co = PointCloud2()
                        ##writing into a rosbag
                        bag1.write('/kinect_data', co) #write data in a rosbag
                    finally:
                        bag1.close()
                        self.flag_start = False
            except KeyboardInterrupt:
                break
##creation node
def main():
    rospy.init_node('recordPC', disable_signals = True)
    recordPC = RecorderPC()
    recordPC.run()

if __name__ == '__main__':
    main()
