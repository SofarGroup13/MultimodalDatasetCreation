#! /usr/bin/env python
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2

HEADER = Header(frame_id='/sample_frame')

#pointcloud2
FIELDS = [
#(x,y,z)
PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),

#(RGB)
PointField(name='rgb', offset=12, datatype=PointField.UINT32, count=1),

PointField(name='my_field1', offset=16, datatype=PointField.FLOAT32, count=1),
PointField(name='my_field2', offset=20, datatype=PointField.FLOAT32, count=1),
]

#Publish
POINTS = [

#[x, y, z, rgb, my_fiel1, my_field2]
[0.3, 0.0, 0.0, 0xff0000, 0.5, 1.2],
[0.0, 0.3, 0.0, 0x00ff00, 1.8, 0.0],
[0.0, 0.0, 0.3, 0x0000ff, 0.9, 0.4],
]

class CustomPointCloud(object):
    def __init__(self):
        rospy.init_node('fake_node_pc')
        self.publisher = rospy.Publisher('custom_point_cloud', PointCloud2, queue_size=1)

    def publish_points(self):
        point_cloud = pc2.create_cloud(HEADER, FIELDS, POINTS)
        r = rospy.Rate(1)
        while not rospy.is_shutdown():
            self.publisher.publish(point_cloud)
            r.sleep()

def main():
    try:
        custom_point_cloud = CustomPointCloud()
        custom_point_cloud.publish_points()
    except rospy.ROSInterruptException:
        pass

if __name__=='__main__':
    main()
