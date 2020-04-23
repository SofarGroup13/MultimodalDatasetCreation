#! /usr/bin/env python3.5
import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Header
#from multimodal_dataset_creation.msg import FakeImu1 #import fake_msg


#defining node
class Fromsmart(object):
    def init(self):
        #data from GUI_node
        self.data1 = Header()
        self.flagstart =False
        #frequency
        self.update_rate = 100
        #data frum Smartwatch
        self.data = Imu()
        self.dataPublished = False

        self.pub_imu = rospy.Publisher('/imu_data', Imu, queue_size= 1 )
        rospy.Subscriber('/smartwatch_status', Header, self.callback1)

        #rospy.Subscriber('/inertial', Imu, self.callbackImu)
        rospy.Subscriber('/fake_data_Imu', Imu, self.callbackImu)

    def callback1(self,data):
        self.data1 = data
        self.flagstart = True


    def callbackImu(self,data):
        self.data = data

        self.dataPublished = True #active bool

    def run(self):
        self.init()
        r = rospy.Rate(self.update_rate)
        while True:
            try:
                #if self.dataPublished and self.flagstart:

                    self.pub_imu.publish(self.data) #publish data from /fake_data_imu to topic /imu_data
                    self.dataPublished =False #disable bool
            except KeyboardInterrupt:
                break

def main():
    rospy.init_node('smartdata', disable_signals=True) #create node
    smartdata = Fromsmart()
    smartdata.run()

if __name__ == '__main__':
    main()
