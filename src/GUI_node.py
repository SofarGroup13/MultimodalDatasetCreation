#! /usr/bin/env python3.5
## @package GUI_node.py
#  This module shows the interface of the architecture whith the configuration and the recording windows
#
import sys, rospy, PyQt5, collections, time, math, os
from datetime import datetime
from PyQt5 import QtWidgets, QtGui
from lib.Windows.configuration_Window import Ui_Configuration_Window
from lib.Windows.recording_Window import Ui_Recording_Window
from lib.Tools.startmsg_publisher import StartMsg_Publisher
from lib.Tools.gesture_sequence_client import Gesture_Sequence_Client

## class MainWindow
#   
# 
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(892, 600)

        ## Create three topics in order to communicate the start/stop command to the sensors
        self.kinectPublisher = StartMsg_Publisher("/kinect_status")
        self.smartwatchPublisher = StartMsg_Publisher("/smartwatch_status")
        self.mocapPublisher = StartMsg_Publisher("/mocap_status")

        ## Variable needed to notify when the stop button is clicked in order to stop the recording
        self.stopSignal = False

        ## Variable to store the total recording time in seconds
        self.totalTime = 0

        ## Directory where all the current recording related files will be saved
        self.recordingDirectory = ""

        ## List to store the gesture sequence to be performed
        self.completeGestureSequence = []

        ## Initialize the configuration window (later it will be the tutorial 1)
        self.startConfigurationWindow()

    ## function startConfigurationWindow 
    #  Function that shows the configuration window
    #  @param self The object pointer
    def startConfigurationWindow(self):
        self.configuration_Window = Ui_Configuration_Window()
        self.configuration_Widget = QtWidgets.QWidget()
        self.configuration_Window.setupUi(self.configuration_Widget)
        self.configuration_Widget.setWindowTitle("Configuration")
        self.setCentralWidget(self.configuration_Widget)

        ## Go to the recording page when the Go To Recording button is clicked
        self.configuration_Window.Go_To_Recording_Button.clicked.connect(self.goToRecording)

        ## Manage the mutually exclusive choice of the gesture sequence
        self.configuration_Window.Casual_Sequence_Check.stateChanged.connect(self.selectCasualSequence)

        self.show()


    ## function selectCasualSequence 
    #  Management of the mutual exclusion between choosing a random sequence or a predefined one
    #  @param self The object pointer.
    def selectCasualSequence(self):
        if self.configuration_Window.Casual_Sequence_Check.isChecked():
            self.configuration_Window.Gestures_Number_Edit.setEnabled(True)
            self.configuration_Window.First_Gesture_Selection.setEnabled(False)
            self.configuration_Window.Second_Gesture_Selection.setEnabled(False)
            self.configuration_Window.Third_Gesture_Selection.setEnabled(False)
            self.configuration_Window.Fourth_Gesture_Selection.setEnabled(False)
            self.configuration_Window.Fifth_Gesture_Selection.setEnabled(False)

        else:
            self.configuration_Window.Gestures_Number_Edit.setEnabled(False)
            self.configuration_Window.First_Gesture_Selection.setEnabled(True)
            self.configuration_Window.Second_Gesture_Selection.setEnabled(True)
            self.configuration_Window.Third_Gesture_Selection.setEnabled(True)
            self.configuration_Window.Fourth_Gesture_Selection.setEnabled(True)
            self.configuration_Window.Fifth_Gesture_Selection.setEnabled(True)
            
        
    ## function goToRecording
    #  Function that shows the recording window
    #  @param self The object pointer
    def goToRecording(self):

        ## Store temporarily the personal informations in a list
        self.savePersonalInfo()

        ## Save the sensors check boxes values for further use
        self.useKinect = self.configuration_Window.Kinect_Sensor_Check.isChecked()
        self.useSmartwatch = self.configuration_Window.Smartwatch_Sensor_Check.isChecked()
        self.useMOCAP = self.configuration_Window.MOCAP_Sensor_Check.isChecked()

        ## If the user wants a casual sequence, call the service
        if self.configuration_Window.Casual_Sequence_Check.isChecked():
            self.completeGestureSequence = self.askGestureSequence().gesture_sequence

            ## Compute the total recording time (we assume that every gesture will be performed for 30 seconds)
            self.totalTime = 30 * len(self.completeGestureSequence)
        else:
            ## Obtain the sequence from the combo boxes and create the integer array
            self.firstGesture = self.configuration_Window.First_Gesture_Selection.currentIndex()
            self.secondGesture = self.configuration_Window.Second_Gesture_Selection.currentIndex()
            self.thirdGesture = self.configuration_Window.Third_Gesture_Selection.currentIndex()
            self.fourthGesture = self.configuration_Window.Fourth_Gesture_Selection.currentIndex()
            self.fifthGesture = self.configuration_Window.Fifth_Gesture_Selection.currentIndex()

            self.completeGestureSequence = [self.firstGesture, self.secondGesture, self.thirdGesture, self.fourthGesture, self.fifthGesture]

            ## If the user has set one or more combo boxes to "None" we have to remove their values
            if 5 in self.completeGestureSequence:
                self.completeGestureSequence.remove(5)

                ## If the user has set all combo boxes to "None" we default to a sequence containing only one gesture
                if len(self.completeGestureSequence) == 0:
                    self.completeGestureSequence = [0]

            ## Compute the total recording time (we assume that every gesture will be performed for 30 seconds)
            self.totalTime = 30 * len(self.completeGestureSequence)

        ## Check
        print(self.completeGestureSequence)

        ## Initialize recording window
        self.recording_Window = Ui_Recording_Window()
        self.recording_Widget = QtWidgets.QWidget()
        self.recording_Window.setupUi(self.recording_Widget)
        self.recording_Widget.setWindowTitle("Recording")
        self.setCentralWidget(self.recording_Widget)

        ## Set the total time label accordingly
        self.recording_Window.Total_Time_Label.setText("/" + str(math.floor(self.totalTime / 60)) + ":" + str(self.totalTime % 60))

        ## Set a welcoming image
        self.recording_Window.Gesture_Image_Label.setPixmap(QtGui.QPixmap("pictures/Hello.jpg"))

        ## Setting the GoBack button to go back to the configuration window if clicked
        self.recording_Window.GoBack_Button.clicked.connect(self.startConfigurationWindow)

        ## When the PlayStop button is pressed the countdown is started
        self.recording_Window.PlayStop_Button.clicked.connect(self.startCountdown)

        self.show()

    ## function savePersonalInfo 
    #  Function that save the personal informations temporarily before saving them into a file
    #  @param self The object pointer.
    def savePersonalInfo(self):
        self.info_Tuple = collections.namedtuple("Personal_Info",['name','surname','age','gender','height','weight'])
        self.personal_Info = self.info_Tuple(\
            self.configuration_Window.Name_Edit.text(),\
            self.configuration_Window.Surname_Edit.text(),\
            self.configuration_Window.Age_Edit.text(),\
            self.configuration_Window.Gender_Selection.currentText(),\
            self.configuration_Window.Height_Edit.text(),\
            self.configuration_Window.Weight_Edit.text()) 

    ## askGestureSequence method
    #  Makes a request to the service to get the random gesture sequence
    #  @param self The object pointer
    def askGestureSequence(self):
        self.gesture_sequence_client = Gesture_Sequence_Client(int(self.configuration_Window.Gestures_Number_Edit.text()))
        return self.gesture_sequence_client.gesture_sequence

    ## function startCountdown
    #  Function called when the play button is clicked to start the countdown before the recording starts
    #  @param self The object pointer
    def startCountdown(self):
        ## Change the play button to stop button and set it as disabled
        self.recording_Window.PlayStop_Button.setText("Stop")
        self.recording_Window.PlayStop_Button.setEnabled(False)

        ## Create the recording folder
        self.createRecordingFolder()

        ## Create and fill in the personal informations file 
        self.personalInfoFilepath = os.path.join(self.recordingDirectory, "Personal_Informations.txt")
        
        ## Check
        print(self.personalInfoFilepath)

        self.pinfoFile = open(self.personalInfoFilepath, 'w')
        self.lines = ["Name is: " + self.personal_Info.name + "\n", 
                      "Surname is: " + self.personal_Info.surname + "\n", 
                      "Age is: " + self.personal_Info.age + "\n",
                      "Gender is: " + self.personal_Info.gender + "\n",
                      "Height is: " + self.personal_Info.height + "\n",
                      "Weight is: " + self.personal_Info.weight + "\n"]
        self.pinfoFile.writelines(self.lines)
        self.pinfoFile.close()

        ## Show the countdown onto the screen
        self.recording_Window.Countdown_Value_Label.setText("10")
        time.sleep(1)
        self.recording_Window.Countdown_Value_Label.setText("9")
        time.sleep(1)
        self.recording_Window.Countdown_Value_Label.setText("8")
        time.sleep(1)
        self.recording_Window.Countdown_Value_Label.setText("7")
        time.sleep(1)
        self.recording_Window.Countdown_Value_Label.setText("6")
        time.sleep(1)
        self.recording_Window.Countdown_Value_Label.setText("5")
        time.sleep(1)
        self.recording_Window.Countdown_Value_Label.setText("4")
        time.sleep(1)
        self.recording_Window.Countdown_Value_Label.setText("3")
        time.sleep(1)
        self.recording_Window.Countdown_Value_Label.setText("2")
        time.sleep(1)
        self.recording_Window.Countdown_Value_Label.setText("1")
        time.sleep(1)

        ## Clear the labels
        self.recording_Window.Countdown_Value_Label.setText("")
        self.recording_Window.Countdown_Title_Label.setText("")

        ## If all the check boxes are unchecked use as default sensor the Kinect
        if not self.useKinect and not self.useSmartwatch and not self.useMOCAP:
            ## Create the file to contain the kinect data
            self.kinectFilepath = os.path.join(self.recordingDirectory, "Kinect_Data.txt")
            self.kinectData = open(self.kinectFilepath, 'w')
            self.kinectData.close()

            ## Publish the start command for the kinect (check if "1" is ok)
            self.kinectPublisher.publish("1")
        else: 
            ## Publish the start commmands onto the correct topics and create files accordingly
            if self.useKinect:
                ## Create the file to contain the kinect data
                self.kinectFilepath = os.path.join(self.recordingDirectory, "Kinect_Data.txt")
                self.kinectData = open(self.kinectFilepath, 'w')
                self.kinectData.close()

                ## Publish the start command for the kinect
                self.kinectPublisher.publish("1")

            if self.useSmartwatch:
                ## Create the file to contain the smartwatch data
                self.smartwatchFilepath = os.path.join(self.recordingDirectory, "Smartwatch_Data.txt")
                self.smartwatchData = open(self.smartwatchFilepath, 'w')
                self.smartwatchData.close()

                ## Publish the start command for the smartwatch
                self.smartwatchPublisher.publish("1")

            if self.useMOCAP:
                ## Create the file to contain the MOCAP data
                self.mocapFilepath = os.path.join(self.recordingDirectory, "MOCAP_Data.txt")
                self.mocapData = open(self.mocapFilepath, 'w')
                self.mocapData.close()

                ## Publish the start command for the MOCAP
                self.mocapPublisher.publish("1")

        ## Set the stop button to be enabled and connect to it the stopRecording function
        self.recording_Window.PlayStop_Button.clicked.connect(self.stopRecording)
        self.recording_Window.PlayStop_Button.setEnabled(True)

        ## Execute the userFeedback function
        self.userFeedback()

    ## function createRecordingFolder
    #  Function that creates the current recording folder
    #  @param self The object pointer
    def createRecordingFolder(self):
        ## Build up the folder path such that we can't get dupes
        self.workingDirectory = os.path.dirname(os.path.abspath(__file__))
        print(self.workingDirectory)
        self.parentDirectory = os.path.dirname(self.workingDirectory)
        self.now = datetime.now()
        self.folderName = self.now.strftime("%m_%d_%Y_%H-%M-%S")
        self.recordingDirectory = os.path.join(self.parentDirectory, "files", self.folderName)

        ## Check
        print(self.recordingDirectory)

        ## If the directory doesn't already exist then create it
        if not os.path.exists(self.recordingDirectory):
            os.mkdir(self.recordingDirectory)
        else:
            print(self.recordingDirectory + " already exists.")

    ## function stopRecording
    #  Function that is called when the user presses the stop button to stop the recording before the predefined time
    #  @param self The object pointer
    def stopRecording(self):
        ## Set the stopSignal to true to stop the userFeedback function
        self.stopSignal = True

        ## Stop the sensors from sending other data
        self.kinectPublisher.publish("0")
        self.smartwatchPublisher.publish("0")
        self.mocapPublisher.publish("0")

    ## function userFeedback
    #  Function that deals with updating the current time and updating images
    #  @param self The object pointer
    def userFeedback(self):
        self.currentTime = 0
        self.currentMinutes = 0
        self.currentSeconds = 0

        ## Show the image of the first gesture to be performed
        self.updateImage(0)

        while not self.stopSignal and (self.currentTime != self.totalTime):
            ## Increment the current time by 1 (second) and compute the minutes and seconds elapsed
            self.currentTime = self.currentTime + 1
            self.currentMinutes = math.floor(self.currentTime / 60)
            self.currentSeconds = self.currentTime % 60

            ## Show the time progress in the label and in the progress bar
            self.recording_Window.Time_Elapsed_ProgressBar.setProperty("value", round((self.currentTime / self.totalTime) * 100))
            self.recording_Window.Current_Time_Label.setText(str(self.currentMinutes) + ":" + str(self.currentSeconds))

            ## If a multiple of 30 seconds has passed, update the image shown with the next one
            if (self.currentTime % 30) == 0:
                self.updateImage(int(self.currentTime / 30))

            time.sleep(1)

        self.stopSignal = False

        ## Disable the PlayStop button, set the progress bar to the maximum value and update the current time
        self.recording_Window.PlayStop_Button.setEnabled(False)
        self.recording_Window.Time_Elapsed_ProgressBar.setProperty("value", 100)
        self.recording_Window.Current_Time_Label.setText(self.recording_Window.Total_Time_Label.text())

        ## Notify that the recording has finished (how? maybe show an image with written "recording has finished")

    ## function updateImage
    #  Function that updates the image to be shown to the user
    #  @param self The object pointer
    #  @param gesturePosition The position in the array of the gesture whose image must be shown
    def updateImage(self, gesturePosition):
        ## Obtain which gesture in the sequence we have to show
        self.currentGesture = self.completeGestureSequence[gesturePosition]

        ## Show the corresponding image
        if self.currentGesture == 0:
            self.recording_Window.Gesture_Image_Label.setPixmap(QtGui.QPixmap("pictures/Drinking.jpg"))
        elif self.currentGesture == 1:
            self.recording_Window.Gesture_Image_Label.setPixmap(QtGui.QPixmap("pictures/Pouring.jpg"))
        elif self.currentGesture == 2:
            self.recording_Window.Gesture_Image_Label.setPixmap(QtGui.QPixmap("pictures/Sitting_Down.jpg"))
        elif self.currentGesture == 3:
            self.recording_Window.Gesture_Image_Label.setPixmap(QtGui.QPixmap("pictures/Standing_Up.jpg"))
        elif self.currentGesture == 4:
            self.recording_Window.Gesture_Image_Label.setPixmap(QtGui.QPixmap("pictures/Walking.jpg"))
        else:
            print("Something went wrong.")


if __name__ == '__main__':
    rospy.init_node('experimenter_GUI', disable_signals=True)

    app = PyQt5.QtWidgets.QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())
