import rospy
from std_msgs.msg import Header

## class StartMsg_Publisher
#
class StartMsg_Publisher:
    ## The constructor
    #  @param self The object pointer
    #  @param topic The topic onto which the message will be published
    def __init__(self, topic):
        self.topic = topic
        self.seq = 0
        self.message = Header()

        self.publisher = rospy.Publisher(self.topic, Header)

    ## function publish
    #  @param self The object pointer
    #  @param msg_string The message to be published onto the topic
    def publish(self, msg_string):
        self.message = Header()
        self.message.seq = self.seq
        self.message.stamp = rospy.Time.now()
        self.message.frame_id = msg_string

        self.publisher.publish(self.message)

        self.seq = self.seq + 1