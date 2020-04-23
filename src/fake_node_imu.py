#! /usr/bin/env python3.5

import rospy
from sensor_msgs.msg import Imu


class FakeImu(object):
        def init(self):
            self.update_rate = 100 #frequency

            self.pub_imu = rospy.Publisher('/fake_data_Imu', Imu, queue_size= 1 )

        #Create a new FakedataImu object and fill in in its contents
            self.fake_imu = Imu()

        #Fill in the header information
            self.fake_imu.header.stamp = rospy.Time.now()
            self.fake_imu.header.frame_id = 'distance_sensor_frame'

        #Fill in the sensor data all 0
            self.fake_imu.orientation_covariance[0] = 0
            self.fake_imu.orientation_covariance[1] = 0
            self.fake_imu.orientation_covariance[2] = 0
            self.fake_imu.orientation_covariance[3] = 0

            self.fake_imu.orientation_covariance[0] = 0
            self.fake_imu.orientation_covariance[1] = 0
            self.fake_imu.orientation_covariance[2] = 0

            self.fake_imu.linear_acceleration_covariance[0] = 0
            self.fake_imu.linear_acceleration_covariance[1] = 0
            self.fake_imu.linear_acceleration_covariance[2] = 0

        def run(self):
            self.init()
            r = rospy.Rate(self.update_rate)
            while not rospy.is_shutdown():
                try:
                    self.pub_imu.publish(self.fake_imu) #publish data on topic

                except KeyboardInterrupt:
                    break

def main():
            rospy.init_node('fakeimudata', disable_signals=True) #create node
            fakeimudata = FakeImu()
            fakeimudata.run()

if __name__ == '__main__':
    main()
