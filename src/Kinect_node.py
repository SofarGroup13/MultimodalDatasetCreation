#!/usr/bin/env python3.5
import rospy

#introduction of type of data from kinect we are interested
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header

def callback2(data):
    data.data

class FromKinect(object):
    #init
    def init(self):
        self.update_rate = 30   #Frequency (Hz) (640x480 pixels)@depends on the used FromKinect
        self.data = PointCloud2() #type of data
        self.flagstart = False
        #publish on a topic the interested data
        self.pub_imu = rospy.Publisher('/kinect_data', PointCloud2, queue_size= 10 )
        rospy.Subscriber('/kinect_status', Header, callback2)
        rospy.Subscriber('/camera/depth/points', PointCloud2, self.callbackkin)

    def callbackkin(self,data):
        self.data = data
        self.flagstart = True

    #starting
    def run(self):
        self.init()
        r = rospy.Rate(self.update_rate)
        while True:
            try:
                if self.flagstart:
                    self.pub_kinect.publish(self.data)
                    self.selfstart =False
            except KeyboardInterrupt:
                break
#create node
def main():
    rospy.init_node('kinectdata', disable_signals=True)
    kinectdata = FromKinect()
    kinectdata.run()

if __name__ == '__main__':
    main()
