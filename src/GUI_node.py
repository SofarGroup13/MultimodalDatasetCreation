#! /usr/bin/env python3.5
import sys, rospy, PyQt5
from PyQt5 import QtWidgets
from lib.Windows.configuration_Window import Ui_Configuration_Window


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.startConfigurationWindow()

    def startConfigurationWindow(self):
        self.configuration_Window = Ui_Configuration_Window()
        self.configuration_Widget = QtWidgets.QWidget()
        self.configuration_Window.setupUi(self.configuration_Widget)
        self.configuration_Widget.show()
        self.configuration_Widget.setWindowTitle("Configuration")

        

if __name__ == '__main__':
    rospy.init_node('experimenter_GUI', disable_signals=True)

    app = PyQt5.QtWidgets.QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())
