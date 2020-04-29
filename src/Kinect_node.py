#!/usr/bin/env python3.5

#This node is the node capable of taking specific data (sensor_msgs/PointCloud2) from Kinect (or from the fake_node_Pc) and publish a topic with these.

import rospy
#introduction of type of data from kinect we are interested
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header
import sensor_msgs.point_cloud2 as pc2



class Kinect(object):
    #init
    def init(self):

        self.data1 = Header() #type of data from Gui_Node
        self.flag = False #Flag to active the publishing on topic for record
        self.flagstart = False
        self.update_rate = 30   #Frequency (Hz) (640x480 pixels)@depends on the used FromKinect
        self.data = PointCloud2() #type of data
        #publish on a topic the interested data
        self.pub = rospy.Publisher('/kinect_data', PointCloud2, queue_size= 10 )
        rospy.Subscriber('/kinect_status', Header, self.callback2)
        #rospy.Subscriber('/camera/depth/points', PointCloud2, self.callbackkin) #In case there is the link with the kinect and the use of OpenNi_Library
        rospy.Subscriber('/fake_data_PC', PointCloud2, self.callbackkin)

    def callback2(self, data1):
        self.data1=data1
        if self.data1.frame_id == "1":
            self.flag = True
        else:
            self.flag = False

    def callbackkin(self, data):
        #for point in pc2.read_points(point_cloud):
            #rospy.logwarn("x, y, z: %.1f, %.1f, %.1f" % (point[0], point[1], point[2]))
            #rospy.logwarn("my field 1: %f" %(point[4]))
            #rospy.logwarn("my field 2: %f" %(point[5]))
        self.data = data
        self.flagstart = True

    #starting
    def run(self):
        self.init()


        r = rospy.Rate(self.update_rate)
        while True:
            try:
                if self.flagstart and self.flag:
                    self.pub.publish(self.data)
                    self.selfstart =False
            except KeyboardInterrupt:
                break
#create node
def main():
    rospy.init_node('kinectnode', disable_signals=True)
    kinectnode = Kinect()
    kinectnode.run()

if __name__ == '__main__':
    main()
