#! /usr/bin/env python3.5
import rospy
import random
from random import choice
from multimodal_dataset_creation.srv import GestureSequence, GestureSequenceResponse

## function gesture_generator
#  Generate a random gesture sequence 
#  @param req The request value(num_of_gestures)
def gesture_generator(req):
        n = req.num_of_gestures
        response = []

        for index in range(n):
            if index < 5:
                if index==0:
                    response.append(random.randint(0,4))
                else:
                    response.append(choice([i for i in range(0,5) if i not in response]))
            else:
                response.append(random.randint(0,4))
        ##print(response)
        return GestureSequenceResponse(response)
    

if __name__ == "__main__":
    rospy.init_node('gesture_sequence_generator')
    s = rospy.Service('gesture_sequence_generator', GestureSequence, gesture_generator)
    rospy.spin()