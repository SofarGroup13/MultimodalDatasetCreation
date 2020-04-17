#! /usr/bin/env python3.5

import rosbag
import rospy
from sensor_msgs.msg import Imu
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import Point
#import pcl_ros




class Recordermodule(object):

    #initialization and subscription of the topics
    def init(self):
        self.data1 = Imu()
        self.data2 = Point()
        self.data3 = PointCloud2()
        self.flag_Mocap = False
        self.flag_Smartwatch = False
        self.flag_Kinect = False

        rospy.Subscriber('/imu_data', Imu, self.callbackSmar)
        rospy.Subscriber('/kinect_data', PointCloud2, self.callbackKin)
        rospy.Subscriber('/mocap_data', Point, self.callbackMoc)




    #callback for data from Mocap
    def callbackMoc(self, data):
        self.data2 = data2
        self.flag_Mocap = True

    #callback for data from Kinect
    def callbackKin(self, data):
        self.data3 = data3
        self.flag_Kinect = True

    #callback from data from Smarwatch
    def callbackSmar(self, data):
        self.data1 = data1
        self.flag_Smartwatch = True

    #starting
    def run(self):
        self.init()
        #creation of rosbag
        bag = rosbag.Bag('dati.bag', 'w')

        while True:
            try:

                if self.flag_Mocap and self.flag_Kinect and self.flag_Smartwatch:
#KINECT
                    co = PointCloud2()

                #initialization
                    co.x = 0
                    co.y = 0
                    co.z = 0
                    counter = 0
                    result = []
                #array che contiene le coordinate dei pointcloud
                    for point in sensor_msgs.point_cloud2.read_points(data3, skip_nans=True):

                        co.x += point[0]
                        co.y += point[1]
                        co.z += point[2]

                        result.append(point)
                        #writing on rosbag datas from Kinect
                        bag.write('result', co)

                        counter += 1

#SMARTWATCH
                    #writing on rosbag data from Smartwatch
                    bag.write('/imu_data', self.data1)

#MOCAP
                    pt = Point()
                    pt.x = 0
                    pt.y = 0
                    pt.z = 0
                    counter = 0
                    result_moc = []
                ##sincmocap

                    #for point2 in (type of message in topic from mocap).read_points(data, skin_nans=True):

                        #pt.x += point2[0]
                        #pt.y += point2[1]
                        #pt.z += point2[2]

                        #result_moc.append(point2)

                        #bag.write('result_moc', pt)

                        #counter += 1

                    self.flag_Mocap = False
                    self.flag_Kinect = False
                    self.flag_Smartwatch = False

            finally:
                bag.close()
#create node
def main():
    rospy.init_node('recorder', anonymous = True)
    recorder = Recordermodule()
    recorder.run()
    rospy.spin()

if __name__ == '__main__':
    main()
