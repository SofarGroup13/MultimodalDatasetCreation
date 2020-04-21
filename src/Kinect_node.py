#!/usr/bin/env python3.5
import rospy

#introduction of type of data from kinect we are interested
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header
import sensor_msgs.point_cloud2 as pc2



class Kinect(object):
    #init
    def init(self):

        self.data1 = Header()
        self.flag = False



        self.flagstart = False
        self.update_rate = 30   #Frequency (Hz) (640x480 pixels)@depends on the used FromKinect
        self.data = PointCloud2() #type of data
        #publish on a topic the interested data
        self.pub = rospy.Publisher('/kinect_data', PointCloud2, queue_size= 10 )
        rospy.Subscriber('/kinect_status', Header, self.callback2)
        #rospy.Subscriber('/camera/depth/points', PointCloud2, self.callbackkin)


        rospy.Subscriber('/custom_point_cloud', PointCloud2, self.callbackkin)

    def callback2(self, data1):
        self.data1=data
        self.flag = True

    def callbackkin(self,point_cloud):
        for point in pc2.read_points(point_cloud):
            rospy.logwarn("x, y, z: %.1f, %.1f, %.1f" % (point[0], point[1], point[2]))
            rospy.logwarn("my field 1: %f" %(point[4]))
            rospy.logwarn("my field 2: %f" %(point[5]))
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
    rospy.init_node('kinectdata', disable_signals=True)
    kinectdata = Kinect()
    kinectdata.run()

if __name__ == '__main__':
    main()
