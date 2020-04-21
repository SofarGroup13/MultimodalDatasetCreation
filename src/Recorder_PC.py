#! /usr/bin/env python

import rosbag
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2


class RecorderPC(object):
    def init(self):

        self.data = PointCloud2()
        self.flag_start=False
        rospy.Subscriber('/kinect_data', PointCloud2, self.callback)

    def callback(self,data):
        self.data = data
        self.flag_start = True

    def run(self):
        self.init()
        while True:
            try:
                if self.flag_start:
                    bag = rosbag.Bag('dati_PC.bag', 'w')
                    try:
                        co = PointCloud2()

                        bag.write('/kinect_data', co)
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
