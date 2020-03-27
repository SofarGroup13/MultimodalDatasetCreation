import rospy
from multimodal_dataset_creation.srv import GestureSequence

class Gesture_Sequence_Service:
    def __init__(self):
        srv = rospy.Service("gesture_sequence_generator",GestureSequence,requireGesture)
        rospy.spin()

    #def requireGesture(self):
       

