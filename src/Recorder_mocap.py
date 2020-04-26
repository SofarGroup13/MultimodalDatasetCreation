#! /usr/bin/env python

#This node is created for recording all datas from mocap Optitrack in a Rosbag.

import rosbag
import rospy
from std_msgs.msg import Float32MultiArray


class RecorderMocap(object):
    def init(self):

        self.data = Float32MultiArray  
        self.flag_start = False
        rospy.Subscriber('/mocap_data', Float32MultiArray, self.callback) 

    def callback(self,data):
        self.data = data
        self.flag_start = True

    def run(self):
        self.init()
        while True:
            try:
                if self.flag_start:
                    bag = rosbag.Bag('mocap_data.bag', 'w')  #creation rosbag
                    try:
                        pt = Imu()

                        bag.write('/mocap_data', pt) #write imu data on rosbag
                    finally:
                        bag.close()    #close rosbag
            except KeyboardInterrupt:
                break

def main():
    rospy.init_node('Recordermocap', disable_signals= True)  #create node
    Recorder_mocap = RecorderMocap()
    Recorder_mocap .run()

if __name__=='__main__':
    main()