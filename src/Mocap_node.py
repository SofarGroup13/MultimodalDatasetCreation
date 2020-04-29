#!/usr/bin/env python3.5

#This node is the node capable of taking specific data (sensor_msgs/Float32MultiArray) from Mocap and publish a topic with these.

import rospy
#introduction of type of data from mocap we are interested
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Header


class Mocap(object):

    def init(self):

        self.data3 = Header()               #type of data from Gui_Node
        self.flag = False                   #Flag to active the publishing on topic for record
        self.flagstart = False
        self.update_rate1 = 30               #Frequency (Hz)
        self.data4 = Float32MultiArray()           #type of data
        #publish on a topic the interested data
        self.pub3 = rospy.Publisher('/mocap_data',Float32MultiArray, queue_size= 10 )
        rospy.Subscriber('/mocap_status', Header, self.callback3)
        #rospy.Subscriber(mocap_fake_node) 
        rospy.Subscriber('/fake_data_mocap', Float32MultiArray, self.callback4)

    def callback3(self, data3):
        self.data3=data3
        if self.data3.frame_id == "1":
            self.flag = True
        else:
            self.flag = False

    def callback4(self, data4):
        self.data4 = data4
        self.flagstart = True
   
    #starting
    def run(self):
        self.init()


        r = rospy.Rate(self.update_rate1)
        while True:
            try:
                if self.flagstart and self.flag:
                    self.pub.publish(self.data4)
                    self.selfstart =False
            except KeyboardInterrupt:
                break

#create node
def main():
    rospy.init_node('Mocap_node', disable_signals=True)
    Mocap_node = Mocap()
    Mocap_node.run()

if __name__ == '__main__':
    main()
