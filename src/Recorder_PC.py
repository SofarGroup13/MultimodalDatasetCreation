#! /usr/bin/env python

#This node is created for recording all data from Kinect in a Rosbag.


import rosbag
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2


class RecorderPC(object):
    #initialization
    def init(self):

        self.data = PointCloud2()
        self.flag_start=False
        rospy.Subscriber('/kinect_data', PointCloud2, self.callback) #subscriber to topic published by Kinect_node

    def callback(self,data):
        self.data = data
        self.flag_start = True

    def run(self):
        self.init()
        while True:
            try:
                if self.flag_start: #this bool is acrived when the topic has datas
                    bag = rosbag.Bag('dati_PC.bag', 'w') #creation of rosbag
                    try:
                        co = PointCloud2()

                        bag.write('/kinect_data', co) #write data in a rosbag 
                    finally:
                        bag.close()
            except KeyboardInterrupt:
                break

def main():
    rospy.init_node('recordPC', disable_signals = True)
    recordPC = RecorderPC()
    recordPC.run()

if __name__ == '__main__':
    main()
