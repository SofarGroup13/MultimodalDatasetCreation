#!/usr/bin/env python3.5
##@package Mocap_node.py
##This node is the node capable of taking specific data (std_msgs.msg/Float32MultiArray) from Mocap and publish a topic with these.

import rospy
##introduction of type of data from mocap in which we are interested
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Header

## class Mocap
class Mocap(object):

    def init(self):

        self.data3 = Header()                      
        self.flag = False                           ##Flag to active the publisher on topic for record
        self.flagstart = False
        self.update_rate1 = 30                      ##Frequency (Hz), depends on the used Mocap
        self.data4 = Float32MultiArray()            
        ##publish on a topic the interested data ('/mocap_data')
        self.pub3 = rospy.Publisher('/mocap_data',Float32MultiArray, queue_size= 10 )
        ##subscribe to the topic ('/mocap_status')
        rospy.Subscriber('/mocap_status', Header, self.callback3)
        ##subscribe to the topic ('/fake_data_mocap') 
        rospy.Subscriber('/fake_data_mocap', Float32MultiArray, self.callback4)
## callback function, topic_('/mocap_status')
    def callback3(self, data3):
        self.data3=data3
        if self.data3.frame_id == "1":
            self.flag = True
        else:
            self.flag = False
## callback function, topic_('/fake_data_mocap')
    def callback4(self, data4):
        self.data4 = data4
        self.flagstart = True
   
    ##starting
    def run(self):
        self.init()


        r = rospy.Rate(self.update_rate1)
        while True:
            try:
                if self.flagstart and self.flag: ## If the node receives Header comand and fake mocap data
                    self.pub3.publish(self.data4)  ## Publish on the topic ('/mocap_data')    
                    self.selfstart =False
            except KeyboardInterrupt:
                break

##create Mocap_node
def main():
    rospy.init_node('Mocap_node', disable_signals=True)
    Mocap_node = Mocap() 
    Mocap_node.run()     

if __name__ == '__main__':
    main()
