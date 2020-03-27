import rospy
from std_msgs.msg import Header

class StartMsg_Publisher:
    def __init__(self, topic):
        self.topic = topic

        self.message = Header()
        self.publisher = rospy.Publisher(self.topic,Header)


    def publish(self, msg_string):
        self.message = Header()
        self.message.stamp = rospy.Time.now()
        self.message.frame_id = msg_string
        self.publisher.publish(self.message)

