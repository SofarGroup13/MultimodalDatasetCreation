#! /usr/bin/env python
## @package Recorder_IMU.py
#This node is created for recording all data from Smartwatch in a Rosbag.
import os, glob
import rosbag
import rospy
from sensor_msgs.msg import Imu

##class RecorderImu
class RecorderImu(object):
    def init(self):
        ##defining folder
        self.workingDirectory = os.path.dirname(os.path.abspath(__file__))
        self.parentDirectory = os.path.dirname(self.workingDirectory)
        self.filesDirectory = os.path.join(self.parentDirectory,"files")

        self.data = Imu() #define type of rosmessage
        self.flag_start = False
        ##subscriber to a topic 'imu_data'
        rospy.Subscriber('/imu_data', Imu, self.callback) #subscriber to topic from smartwatch node
    ##function for callback
    def callback(self,data):
        self.data = data
        self.flag_start = True

    def run(self):
        self.init()
        while True:
            try:
                if self.flag_start:
                    ##saving bag into a defined folder
                    self.folder_path = max(glob.glob(os.path.join(self.filesDirectory, '*/')), key=os.path.getmtime)
                    ##creation rosbag
                    bag = rosbag.Bag((os.path.join(self.folder_path,'dati_IMU.bag')), 'w') #creation rosbag
                    try:
                        pt = Imu()
                        ##writing into a rosbag
                        bag.write('/imu_data', pt) #write imu data on rosbag
                    finally:
                        bag.close() #close rosbag
                        self.flag_start = False
            except KeyboardInterrupt:
                break
##cration node
def main():
    rospy.init_node('recordIMU', disable_signals= True) #create node
    recordIMU = RecorderImu()
    recordIMU.run()

if __name__=='__main__':
    main()
