#! /usr/bin/env python3.5
import rosbag, os, rospkg, csv, sys
from std_msgs.msg import Header, String
from sensor_msgs.msg import PointCloud2

if (len(sys.argv) > 2):
    print(sys.argv)
    print("invalid number of argument")
    sys.exit(1)
else:
    bagFolder = sys.argv[1]

filesName = ['pointclod2', 'info', 'gestures']

for fileName in filesName:
    bag = rosbag.Bag(bagFolder + "/" + fileName + ".bag")
    csvName = bagFolder + "/" + fileName + ".csv"
    if not(os.path.isfile(csvName)):
        with open(csvName, 'w+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter = ',')
            firstIteration = True
            if fileName != 'info':
                for topic, msg, t in bag.read_messages():
                    values = []
if fileName == 'pointcloud2':   
                        if firstIteration:
                            header = ['ros_seconds', 'ros_nanoseconds', 'height',  'width']
                            filewriter.writerow(header)       
                            firstIteration = False      
                        values.append(msg.header.stamp.secs)
                        values.append(msg.header.stamp.nsecs)
                        values.append(int(msg.header.frame_id))
			values.append(int(msg.height)) #informarsi se immettere le variabili lungo x e y
                        values.append(int(msg.width))
                    elif fileName == 'gestures': #cambiare il blocco, modificando la logica: sapere quanti frame al sec prende il kinect e dunque calcolare ogni quanto frame mettere l'identificatore della gesture (vedi labeling)
                        if firstIteration:
                            header = ['ros_seconds', 'ros_nanoseconds', 'gesture_name']
                            filewriter.writerow(header)       
                            firstIteration = False   
                        values.append(msg.stamp.secs)
                        values.append(msg.stamp.nsecs)
                        values.append(msg.frame_id)
                    filewriter.writerow(values)
            else:#non fare 
                for topic, msg, t in bag.read_messages(topics =['/name']): 
                    values = ['name']
                    values.append(msg.frame_id)
                    filewriter.writerow(values)
                for topic, msg, t in bag.read_messages(topics =['/surname']):#cambiare con num.gestures, ma aspettare l'esatta dicitura da Davide
                    values = ['surname']
                    values.append(msg.frame_id)
                    filewriter.writerow(values)
                for topic, msg, t in bag.read_messages(topics =['/age']):
                    values = ['age']
                    values.append(msg.frame_id)
                    filewriter.writerow(values)
                for topic, msg, t in bag.read_messages(topics =['/gender']):
                    values = ['gender']
                    values.append(msg.frame_id)
                    filewriter.writerow(values)    
                for topic, msg, t in bag.read_messages(topics =['/sensors']):
                    values = ['sensors']
                    values.append(msg.frame_id)      
                    filewriter.writerow(values)      
    bag.close()
