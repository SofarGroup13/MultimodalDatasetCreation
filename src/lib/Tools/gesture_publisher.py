import os
import rosbag
import sys
from multimodal_dataset_creation.msg import IntList

# class Gesture_Bag
#   Stores the gesture sequence in a rosbag


class Gesture_Bag:
    # The constructor
    #  @param self The object pointer
    #  @param sequence The sequence of gestures to be stored in the bag
    def __init__(self, sequence, folder):
        self.folder = folder
        self.sequence = sequence
        self.bag = rosbag.Bag(
            (os.path.join(self.folder, 'gesture_sequence.bag')), 'w')
        self.publish(self.sequence)

    def publish(self, sequence):
        
        self.list = IntList()
        self.list.data = sequence[0]
        self.list.t = sequence[1]

        self.bag.write('/gesture_sequence', self.list)
