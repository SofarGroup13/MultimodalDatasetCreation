#! /usr/bin/env python

#This node is created for recording all datas from Smartwatch in a Rosbag.

import rosbag
import rospy
from sensor_msgs.msg import Imu


class RecorderImu(object):
    def init(self):

        self.data = Imu() #define type of rosmessage
        self.flag_start = False
        rospy.Subscriber('/imu_data', Imu, self.callback) #subscriber to topic from smartwatch node

    def callback(self,data):
        self.data = data
        self.flag_start = True

    def run(self):
        self.init()
        while True:
            try:
                if self.flag_start:
                    bag = rosbag.Bag('dati_IMU.bag', 'w') #creation rosbag
                    try:
                        pt = Imu()

                        bag.write('/imu_data', pt) #write imu data on rosbag
                    finally:
                        bag.close() #close rosbag
            except KeyboardInterrupt:
                break

def main():
    rospy.init_node('recordIMU', disable_signals= True) #create node
    recordIMU = RecorderImu()
    recordIMU.run()

if __name__=='__main__':
    main()
