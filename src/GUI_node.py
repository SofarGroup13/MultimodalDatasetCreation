#! /usr/bin/env python3.5
## @package GUI_node.py
#  This module shows the interface of the architecture whith the configuration and the recording windows
#
import sys, rospy, PyQt5, collections
from PyQt5 import QtWidgets
from lib.Windows.configuration_Window import Ui_Configuration_Window
from lib.Windows.recording_Window import Ui_Recording_Window
from lib.Tools.startmsg_publisher import StartMsg_Publisher
from lib.Tools.gesture_sequence_service import Gesture_Sequence_Service

## class MainWindow
#   
# 
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(892, 600)
        self.startConfigurationWindow()

    ## startConfigurationWindow function
    #  function that shows the configuration window
    #  @param self The object pointer.
    def startConfigurationWindow(self):
        self.configuration_Window = Ui_Configuration_Window()
        self.configuration_Widget = QtWidgets.QWidget()
        self.configuration_Window.setupUi(self.configuration_Widget)
        self.configuration_Widget.setWindowTitle("Configuration")
        self.setCentralWidget(self.configuration_Widget)

        # go to the recording page whem clicking the Go To Recording button
        self.configuration_Window.Go_To_Recording_Button.clicked.connect(self.goToRecording)

        # enable the Num_of_Gestures EditBox
        self.configuration_Window.Casual_Sequence_Check.stateChanged.connect(self.selectCasualSequence)

        self.show()


    ## selectCasualSequence function
    #  manage the click on the casual_Check_Box
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
            
        
    ## goToRecording function
    #  function that shows the recording window
    #  @param self The object pointer.
    def goToRecording(self):

        # store temporarly info in a list
        self.savePersonalInfo()

        # initialize recording window
        self.recording_Window = Ui_Recording_Window()
        self.recording_Widget = QtWidgets.QWidget()
        self.recording_Window.setupUi(self.recording_Widget)
        self.recording_Widget.setWindowTitle("Recording")
        self.setCentralWidget(self.recording_Widget)

        # setting the GoBack button to go back to the configuration window if clicked
        self.recording_Window.GoBack_Button.clicked.connect(self.startConfigurationWindow)
        self.show()

    ## savePersonalInfo function
    #  function that save the personal informations temporarly before saving them into a file
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




if __name__ == '__main__':
    rospy.init_node('experimenter_GUI', disable_signals=True)

    app = PyQt5.QtWidgets.QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())
