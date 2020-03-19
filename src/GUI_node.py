## @package GUI_node.py
#  This module shows the interface of the architecture whith the configuration and the recording windows
#
import sys, rospy, PyQt5
from PyQt5 import QtWidgets
from lib.Windows.configuration_Window import Ui_Configuration_Window
from lib.Windows.recording_Window import Ui_Recording_Window

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
        self.show()
        
    ## goToRecording function
    #  function that shows the configuration window
    #  @param self The object pointer.
    def goToRecording(self):
        ## function 
        self.recording_Window = Ui_Recording_Window()
        self.recording_Widget = QtWidgets.QWidget()
        self.recording_Window.setupUi(self.recording_Widget)
        self.recording_Widget.setWindowTitle("Recording")
        self.setCentralWidget(self.recording_Widget)

        # setting the GoBack button to go back to the configuration window if clicked
        self.recording_Window.GoBack_Button.clicked.connect(self.startConfigurationWindow)
        self.show()



if __name__ == '__main__':
    rospy.init_node('experimenter_GUI', disable_signals=True)

    app = PyQt5.QtWidgets.QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())
