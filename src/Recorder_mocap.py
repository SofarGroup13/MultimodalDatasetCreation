#! /usr/bin/env python
##@package Recorder_mocap.py
##This node is created for recording all datas from Mocap in a Rosbag.
import os, glob
import rosbag
import rospy
from std_msgs.msg import Float32MultiArray

##class RecorderMocap
class RecorderMocap(object):
    def init(self):

        self.workingDirectory = os.path.dirname(os.path.abspath(__file__))
        self.parentDirectory = os.path.dirname(self.workingDirectory)
        self.filesDirectory = os.path.join(self.parentDirectory,"files")

        self.data = Float32MultiArray()      ##define the type of message Float32MultiArray()
        self.flag_start = False               
        rospy.Subscriber('/mocap_data', Float32MultiArray, self.callback) ##subscribe to the topic ('/mocap_data')
## callback function, topic_('/mocap_data')
    def callback(self,data):
        self.data = data
        self.flag_start = True
##starting
    def run(self):
        self.init()
        while True:
            try:
                if self.flag_start:   ##if the node receives data on the topic ('/mocap_data')
                    self.folder_path = max(glob.glob(os.path.join(self.filesDirectory, '*/')), key=os.path.getmtime)
                    bag3 = rosbag.Bag((os.path.join(self.folder_path,'mocap_bag.bag')), 'w')  ##create rosbag 'mocap_bag.bag'.
                    try:
                        pt = Float32MultiArray()
                        
                        bag3.write('/mocap_data', pt)    ##write mocap data from topic ('/mocap_data') into the rosbag
                    finally:
                        bag3.close()                     ##close rosbag
                        self.flag_start = False
            except KeyboardInterrupt:
                break

def main():
    rospy.init_node('Recorder_mocap', disable_signals= True)  ##create node Recorder_mocap
    Recorder_mocap = RecorderMocap()
    Recorder_mocap.run()

if __name__=='__main__':
    main()