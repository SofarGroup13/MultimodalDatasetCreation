import os, rosbag, sys
from multimodal_dataset_creation.msg import IntList

## class Gesture_Bag
#   Stores the gesture sequence in a rosbag
class Gesture_Bag:
    ## The constructor
    #  @param self The object pointer
    #  @param sequence The sequence of gestures to be stored in the bag
    def __init__(self, sequence, folder):
        self.folder = folder 
        self.sequence = sequence
        self.publish(self.sequence)
        
    def publish(self, sequence):    
        self.bag = rosbag.Bag((os.path.join(self.folder,'gesture_sequence.bag')),'w')
        try:
            self.list = IntList()
            self.list.data = [i[0] for i in sequence]
            self.list.t = [i[1] for i in sequence]

            self.bag.write('gesture_sequence', self.list)
        finally:
            self.bag.close()
