import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

## class Ui_Recording_Window
#  This class contains the recording window design
class Ui_Recording_Window(object):
    def setupUi(self, Recording_Window):
        Recording_Window.setObjectName("Recording_Window")
        Recording_Window.resize(892, 600)

        ## Label containing the window's title
        self.Recording_Title = QtWidgets.QLabel(Recording_Window)
        self.Recording_Title.setGeometry(QtCore.QRect(325, 0, 250, 50))

        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Recording_Title.setFont(font)

        self.Recording_Title.setFrameShape(QtWidgets.QFrame.Panel)
        self.Recording_Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Recording_Title.setLineWidth(4)

        self.Recording_Title.setAlignment(QtCore.Qt.AlignCenter)

        self.Recording_Title.setObjectName("Recording_Title")

        ## Button used to come back to the configuration window
        self.GoBack_Button = QtWidgets.QPushButton(Recording_Window)
        self.GoBack_Button.setGeometry(QtCore.QRect(20, 20, 100, 50))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.GoBack_Button.setFont(font)

        self.GoBack_Button.setObjectName("GoBack_Button")

        ## Layout to contain the two countdown labels
        self.verticalLayoutWidget = QtWidgets.QWidget(Recording_Window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 70, 160, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.Countdown_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Countdown_Layout.setContentsMargins(0, 0, 0, 0)
        self.Countdown_Layout.setObjectName("Countdown_Layout")

        ## Simple title label
        self.Countdown_Title_Label = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.Countdown_Title_Label.setFont(font)

        self.Countdown_Title_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.Countdown_Title_Label.setObjectName("Countdown_Title_Label")

        ## Add the title to the layout
        self.Countdown_Layout.addWidget(self.Countdown_Title_Label)

        ## Label that stores the countdown value
        self.Countdown_Value_Label = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Countdown_Value_Label.setFont(font)

        self.Countdown_Value_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.Countdown_Value_Label.setObjectName("Countdown_Value_Label")

        ## Add the label to the layout
        self.Countdown_Layout.addWidget(self.Countdown_Value_Label)

        ## Label that will display the images corresponding to the gesture to perform
        self.Gesture_Image_Label = QtWidgets.QLabel(Recording_Window)
        self.Gesture_Image_Label.setGeometry(QtCore.QRect(275, 180, 350, 300))

        self.Gesture_Image_Label.setFrameShape(QtWidgets.QFrame.Panel)
        self.Gesture_Image_Label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Gesture_Image_Label.setLineWidth(3)

        self.Gesture_Image_Label.setText("")
        self.Gesture_Image_Label.setScaledContents(True)

        self.Gesture_Image_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.Gesture_Image_Label.setObjectName("Gesture_Image_Label")

        ## Layout to contain the play/stop button and the progress bar representing the time elapsed 
        self.horizontalLayoutWidget = QtWidgets.QWidget(Recording_Window)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 500, 761, 34))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.Time_Progress_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Time_Progress_Layout.setContentsMargins(0, 0, 0, 0)
        self.Time_Progress_Layout.setObjectName("Time_Progress_Layout")

        ## Button that starts the countdown and then is used to stop the recording 
        self.PlayStop_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayStop_Button.sizePolicy().hasHeightForWidth())
        self.PlayStop_Button.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PlayStop_Button.setFont(font)

        self.PlayStop_Button.setObjectName("PlayStop_Button")

        ## Add the button to the layout
        self.Time_Progress_Layout.addWidget(self.PlayStop_Button)

        ## Progress bar used to show the time elapsed as a percentage bar
        self.Time_Elapsed_ProgressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_Elapsed_ProgressBar.sizePolicy().hasHeightForWidth())
        self.Time_Elapsed_ProgressBar.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(16)
        self.Time_Elapsed_ProgressBar.setFont(font)

        self.Time_Elapsed_ProgressBar.setProperty("value", 0)

        self.Time_Elapsed_ProgressBar.setObjectName("Time_Elapsed_ProgressBar")

        ## Add the progress bar to the layout
        self.Time_Progress_Layout.addWidget(self.Time_Elapsed_ProgressBar)

        ## Layout to contain the string that shows the time elapsed in a "minutes:seconds" format
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Recording_Window)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(300, 550, 301, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.Time_Elapsed_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.Time_Elapsed_Layout.setContentsMargins(0, 0, 0, 0)
        self.Time_Elapsed_Layout.setSpacing(10)
        self.Time_Elapsed_Layout.setObjectName("Time_Elapsed_Layout")

        ## Label that contains the first part of the string
        self.Time_Elapsed_Label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_Elapsed_Label.sizePolicy().hasHeightForWidth())
        self.Time_Elapsed_Label.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.Time_Elapsed_Label.setFont(font)

        self.Time_Elapsed_Label.setObjectName("Time_Elapsed_Label")

        ## Add the label to the layout
        self.Time_Elapsed_Layout.addWidget(self.Time_Elapsed_Label)

        ## Label that contains the current time, which will be updated every second
        self.Current_Time_Label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Current_Time_Label.sizePolicy().hasHeightForWidth())
        self.Current_Time_Label.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(24)
        self.Current_Time_Label.setFont(font)

        self.Current_Time_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.Current_Time_Label.setObjectName("Current_Time_Label")

        ## Add the label to the layout
        self.Time_Elapsed_Layout.addWidget(self.Current_Time_Label)

        ## Label that contains the total duration of the recording
        self.Total_Time_Label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Total_Time_Label.sizePolicy().hasHeightForWidth())
        self.Total_Time_Label.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(24)
        self.Total_Time_Label.setFont(font)

        self.Total_Time_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.Total_Time_Label.setObjectName("Total_Time_Label")

        ## Add the label to the layout
        self.Time_Elapsed_Layout.addWidget(self.Total_Time_Label)

        self.retranslateUi(Recording_Window)
        QtCore.QMetaObject.connectSlotsByName(Recording_Window)

    ## function retranslateUi
    #  Adds text to the window's elements
    #  @param self The object pointer
    #  @param Recording_Window The window whose elements's text must be modified
    def retranslateUi(self, Recording_Window):
        _translate = QtCore.QCoreApplication.translate
        Recording_Window.setWindowTitle(_translate("Recording_Window", "Form"))
        self.Recording_Title.setText(_translate("Recording_Window", "Recording"))
        self.GoBack_Button.setText(_translate("Recording_Window", "Go back"))
        self.Countdown_Title_Label.setText(_translate("Recording_Window", "Countdown:"))
        self.Countdown_Value_Label.setText(_translate("Recording_Window", ""))
        self.PlayStop_Button.setText(_translate("Recording_Window", "Play"))
        self.Time_Elapsed_Label.setText(_translate("Recording_Window", "Time elapsed is "))
        self.Current_Time_Label.setText(_translate("Recording_Window", "0:00"))
        self.Total_Time_Label.setText(_translate("Recording_Window", "/0:00"))
