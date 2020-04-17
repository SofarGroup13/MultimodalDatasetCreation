#! /usr/bin/env python3.5
import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Header


def callback1(data):
    data.data

class Fromsmart(object):
    def init(self):
        self.update_rate = 100
        self.data = Imu()
        self.dataPublished = False

        self.pub_imu = rospy.Publisher('/imu_data', Imu, queue_size= 1 )
        rospy.Subscriber('/smartwatch_status', Header, callback1)
        rospy.Subscriber('/inertial', Imu, self.callbackImu)



    def callbackImu(self,data):
            self.data = data
            self.dataPublished = True

    def run(self):
        self.init()
        r = rospy.Rate(self.update_rate)
        while True:
            try:
                if self.dataPublished:
                    self.pub_imu.publish(self.data)
                    self.dataPublished =False
            except KeyboardInterrupt:
                break

def main():
    rospy.init_node('smartdata', disable_signals=True)
    smartdata = Fromsmart()
    smartdata.run()

if __name__ == '__main__':
    main()
