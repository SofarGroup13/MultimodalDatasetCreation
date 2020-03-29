import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

## class Ui_Configuration_Window
#  This class contains the configuration window design
class Ui_Configuration_Window(PyQt5.QtWidgets.QWidget):
    def setupUi(self, Configuration_Window):
        Configuration_Window.setObjectName("Configuration_Window")
        Configuration_Window.resize(900, 600)

        ## Label that contains the window's title
        self.Configuration_Title = QtWidgets.QLabel(Configuration_Window)
        self.Configuration_Title.setGeometry(QtCore.QRect(325, 0, 250, 50))

        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Configuration_Title.setFont(font)

        self.Configuration_Title.setFrameShape(QtWidgets.QFrame.Panel)
        self.Configuration_Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Configuration_Title.setLineWidth(4)

        self.Configuration_Title.setScaledContents(False)
        self.Configuration_Title.setAlignment(QtCore.Qt.AlignCenter)

        self.Configuration_Title.setObjectName("Configuration_Title")

        ## Button that makes you go to the recording window
        self.Go_To_Recording_Button = QtWidgets.QPushButton(Configuration_Window)
        self.Go_To_Recording_Button.setGeometry(QtCore.QRect(325, 550, 250, 40))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Go_To_Recording_Button.setFont(font)

        self.Go_To_Recording_Button.setObjectName("Go_To_Recording_Button")

        ## Sub-layout to contain the options for the gesture sequence selection
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Configuration_Window)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(300, 60, 341, 469))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.Gesture_Sequence_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Gesture_Sequence_Layout.setContentsMargins(0, 0, 0, 0)
        self.Gesture_Sequence_Layout.setObjectName("Gesture_Sequence_Layout")

        ## Label that contains the gesture sequence selection sub-layout's title
        self.Gesture_Sequence_Options_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Gesture_Sequence_Options_Label.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Gesture_Sequence_Options_Label.sizePolicy().hasHeightForWidth())
        self.Gesture_Sequence_Options_Label.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Gesture_Sequence_Options_Label.setFont(font)

        self.Gesture_Sequence_Options_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Gesture_Sequence_Options_Label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.Gesture_Sequence_Options_Label.setObjectName("Gesture_Sequence_Options_Label")

        ## Add the label to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Gesture_Sequence_Options_Label)

        ## Check-box the user ticks to select if he/she wants to request a casual sequence
        self.Casual_Sequence_Check = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Casual_Sequence_Check.sizePolicy().hasHeightForWidth())
        self.Casual_Sequence_Check.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.Casual_Sequence_Check.setFont(font)

        self.Casual_Sequence_Check.setObjectName("Casual_Sequence_Check")

        ## Add the check-box to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Casual_Sequence_Check)

        ## Label that contains a string to specify the content of the following line edit
        self.Gestures_Number_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.Gestures_Number_Label.setFont(font)

        self.Gestures_Number_Label.setObjectName("Gestures_Number_Label")

        ## Add the label to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Gestures_Number_Label)

        ## Line edit into which the user writes the number of gestures to be contained in the casual sequence
        self.Gestures_Number_Edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Gestures_Number_Edit.setEnabled(False)
        self.Gestures_Number_Edit.setObjectName("Gestures_Number_Edit")

        ## Add the line edit to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Gestures_Number_Edit)

        ## Simple label the contains "or"
        self.Or_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Or_Label.setFont(font)

        self.Or_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.Or_Label.setObjectName("Or_Label")

        ## Add the label to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Or_Label)

        ## Label that contains a string to specify the content of the following combo box
        self.First_Gesture_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.First_Gesture_Label.setFont(font)

        self.First_Gesture_Label.setObjectName("First_Gesture_Label")

        ## Add the label to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.First_Gesture_Label)

        ## Combo box to allow the user to select the first gesture to perform
        self.First_Gesture_Selection = QtWidgets.QComboBox(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.First_Gesture_Selection.setFont(font)

        self.First_Gesture_Selection.setObjectName("First_Gesture_Selection")

        self.First_Gesture_Selection.addItem("")
        self.First_Gesture_Selection.addItem("")
        self.First_Gesture_Selection.addItem("")
        self.First_Gesture_Selection.addItem("")
        self.First_Gesture_Selection.addItem("")
        self.First_Gesture_Selection.addItem("")

        ## Add the combo box to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.First_Gesture_Selection)

        ## Label that contains a string to specify the content of the following combo box
        self.Second_Gesture_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.Second_Gesture_Label.setFont(font)

        self.Second_Gesture_Label.setObjectName("Second_Gesture_Label")

        ## Add the label to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Second_Gesture_Label)

        ## Combo box to allow the user to select the second gesture to perform
        self.Second_Gesture_Selection = QtWidgets.QComboBox(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.Second_Gesture_Selection.setFont(font)

        self.Second_Gesture_Selection.setObjectName("Second_Gesture_Selection")

        self.Second_Gesture_Selection.addItem("")
        self.Second_Gesture_Selection.addItem("")
        self.Second_Gesture_Selection.addItem("")
        self.Second_Gesture_Selection.addItem("")
        self.Second_Gesture_Selection.addItem("")
        self.Second_Gesture_Selection.addItem("")

        ## Add the combo box to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Second_Gesture_Selection)

        ## Label that contains a string to specify the content of the following combo box
        self.Third_Gesture_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.Third_Gesture_Label.setFont(font)

        self.Third_Gesture_Label.setObjectName("Third_Gesture_Label")

        ## Add the label to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Third_Gesture_Label)

        ## Combo box to allow the user to select the third gesture to perform
        self.Third_Gesture_Selection = QtWidgets.QComboBox(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.Third_Gesture_Selection.setFont(font)

        self.Third_Gesture_Selection.setObjectName("Third_Gesture_Selection")

        self.Third_Gesture_Selection.addItem("")
        self.Third_Gesture_Selection.addItem("")
        self.Third_Gesture_Selection.addItem("")
        self.Third_Gesture_Selection.addItem("")
        self.Third_Gesture_Selection.addItem("")
        self.Third_Gesture_Selection.addItem("")

        ## Add the combo box to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Third_Gesture_Selection)

        ## Label that contains a string to specify the content of the following combo box
        self.Fourth_Gesture_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.Fourth_Gesture_Label.setFont(font)

        self.Fourth_Gesture_Label.setObjectName("Fourth_Gesture_Label")

        ## Add the label to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Fourth_Gesture_Label)

        ## Combo box to allow the user to select the fourth gesture to perform
        self.Fourth_Gesture_Selection = QtWidgets.QComboBox(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.Fourth_Gesture_Selection.setFont(font)

        self.Fourth_Gesture_Selection.setObjectName("Fourth_Gesture_Selection")

        self.Fourth_Gesture_Selection.addItem("")
        self.Fourth_Gesture_Selection.addItem("")
        self.Fourth_Gesture_Selection.addItem("")
        self.Fourth_Gesture_Selection.addItem("")
        self.Fourth_Gesture_Selection.addItem("")
        self.Fourth_Gesture_Selection.addItem("")

        ## Add the combo box to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Fourth_Gesture_Selection)

        ## Label that contains a string to specify the content of the following combo box
        self.Fifth_Gesture_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.Fifth_Gesture_Label.setFont(font)

        self.Fifth_Gesture_Label.setObjectName("Fifth_Gesture_Label")

        ## Add the label to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Fifth_Gesture_Label)

        ## Combo box to allow the user to select the fifth gesture to perform
        self.Fifth_Gesture_Selection = QtWidgets.QComboBox(self.verticalLayoutWidget_2)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.Fifth_Gesture_Selection.setFont(font)

        self.Fifth_Gesture_Selection.setObjectName("Fifth_Gesture_Selection")

        self.Fifth_Gesture_Selection.addItem("")
        self.Fifth_Gesture_Selection.addItem("")
        self.Fifth_Gesture_Selection.addItem("")
        self.Fifth_Gesture_Selection.addItem("")
        self.Fifth_Gesture_Selection.addItem("")
        self.Fifth_Gesture_Selection.addItem("")

        ## Add the combo box to the sub-layout
        self.Gesture_Sequence_Layout.addWidget(self.Fifth_Gesture_Selection)

        ## Sub-layout to contain the personal informations 
        self.verticalLayoutWidget = QtWidgets.QWidget(Configuration_Window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 261, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.Personal_Info_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Personal_Info_Layout.setContentsMargins(0, 0, 0, 0)
        self.Personal_Info_Layout.setSpacing(5)
        self.Personal_Info_Layout.setObjectName("Personal_Info_Layout")

        ## Label that contains the personal informations sub-layout's title 
        self.Personal_Info_Label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Personal_Info_Label.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Personal_Info_Label.setFont(font)

        self.Personal_Info_Label.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.Personal_Info_Label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.Personal_Info_Label.setObjectName("Personal_Info_Label")

        ## Add the label to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Personal_Info_Label)

        ## Label that contains a string to specify the content of the following line edit
        self.Name_Label = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Name_Label.setFont(font)

        self.Name_Label.setObjectName("Name_Label")

        ## Add the label to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Name_Label)

        ## Line edit into which the user writes his/her name
        self.Name_Edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Name_Edit.setObjectName("Name_Edit")

        ## Add the line edit to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Name_Edit)

        ## Label that contains a string to specify the content of the following line edit
        self.Surname_Label = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Surname_Label.setFont(font)

        self.Surname_Label.setObjectName("Surname_Label")

        ## Add the label to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Surname_Label)

        ## Line edit into which the user writes his/her surname
        self.Surname_Edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Surname_Edit.setObjectName("Surname_Edit")

        ## Add the line edit to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Surname_Edit)

        ## Label that contains a string to specify the content of the following line edit
        self.Age_Label = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Age_Label.setFont(font)

        self.Age_Label.setObjectName("Age_Label")

        ## Add the label to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Age_Label)

        ## Line edit into which the user writes his/her age
        self.Age_Edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Age_Edit.setObjectName("Age_Edit")

        ## Add the line edit to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Age_Edit)

        ## Label that contains a string to specify the content of the following combo box
        self.Gender_Label = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Gender_Label.setFont(font)

        self.Gender_Label.setObjectName("Gender_Label")

        ## Add the label to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Gender_Label)

        ## Combo box that allows the user to choose his/her gender
        self.Gender_Selection = QtWidgets.QComboBox(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.Gender_Selection.setFont(font)

        self.Gender_Selection.setEditable(False)

        self.Gender_Selection.setObjectName("Gender_Selection")

        self.Gender_Selection.addItem("")
        self.Gender_Selection.addItem("")
        self.Gender_Selection.addItem("")

        ## Add the combo box to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Gender_Selection)

        ## Label that contains a string to specify the content of the following line edit
        self.Height_Label = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Height_Label.setFont(font)
        
        self.Height_Label.setObjectName("Height_Label")

        ## Add the label to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Height_Label)

        ## Line edit into which the user writes his/her height
        self.Height_Edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Height_Edit.setObjectName("Height_Edit")

        ## Add the line edit to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Height_Edit)

        ## Label that contains a string to specify the content of the following line edit
        self.Weight_Label = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Weight_Label.setFont(font)

        self.Weight_Label.setObjectName("Weight_Label")

        ## Add the label to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Weight_Label)

        ## Line edit into which the user writes his/her weight
        self.Weight_Edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Weight_Edit.setObjectName("Weight_Edit")

        ## Add the line edit to the sub-layout
        self.Personal_Info_Layout.addWidget(self.Weight_Edit)

        ## Bring the following elements into the foreground
        self.Name_Label.raise_()
        self.Surname_Label.raise_()
        self.Age_Label.raise_()
        self.Gender_Label.raise_()
        self.Height_Label.raise_()
        self.Weight_Label.raise_()
        self.Personal_Info_Label.raise_()
        self.Age_Edit.raise_()
        self.Gender_Selection.raise_()
        self.Height_Edit.raise_()
        self.Name_Edit.raise_()
        self.Surname_Edit.raise_()
        self.Weight_Edit.raise_()

        ## Sub-layout to contain the check boxes used to select which sensors to utilize
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Configuration_Window)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(660, 150, 221, 251))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.Sensor_Options_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Sensor_Options_Layout.setContentsMargins(0, 0, 0, 0)
        self.Sensor_Options_Layout.setSpacing(10)
        self.Sensor_Options_Layout.setObjectName("Sensor_Options_Layout")

        ## Label that contains the sensors options sub-layout's title
        self.Sensors_Options_Label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Sensors_Options_Label.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Sensors_Options_Label.setFont(font)

        self.Sensors_Options_Label.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.Sensors_Options_Label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.Sensors_Options_Label.setObjectName("Sensors_Options_Label")

        ## Add the label to the sub-layout
        self.Sensor_Options_Layout.addWidget(self.Sensors_Options_Label)

        ## Check box used to implement the Kinect sensor
        self.Kinect_Sensor_Check = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Kinect_Sensor_Check.sizePolicy().hasHeightForWidth())
        self.Kinect_Sensor_Check.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Kinect_Sensor_Check.setFont(font)

        self.Kinect_Sensor_Check.setObjectName("Kinect_Sensor_Check")

        ## Add the check box to the sub-layout
        self.Sensor_Options_Layout.addWidget(self.Kinect_Sensor_Check)

        ## Check box used to implement the MOCAP sensor
        self.MOCAP_Sensor_Check = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MOCAP_Sensor_Check.sizePolicy().hasHeightForWidth())
        self.MOCAP_Sensor_Check.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.MOCAP_Sensor_Check.setFont(font)

        self.MOCAP_Sensor_Check.setObjectName("MOCAP_Sensor_Check")

        ## Add the check box to the sub-layout
        self.Sensor_Options_Layout.addWidget(self.MOCAP_Sensor_Check)

        ## Check box used to implement the smartwatch sensor
        self.Smartwatch_Sensor_Check = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Smartwatch_Sensor_Check.sizePolicy().hasHeightForWidth())
        self.Smartwatch_Sensor_Check.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.Smartwatch_Sensor_Check.setFont(font)

        self.Smartwatch_Sensor_Check.setObjectName("Smartwatch_Sensor_Check")

        ## Add the check box to the sub-layout
        self.Sensor_Options_Layout.addWidget(self.Smartwatch_Sensor_Check)

        ## A simple frame that encapsulates all the personal informations related elements
        self.Personal_Info_Frame = QtWidgets.QFrame(Configuration_Window)
        self.Personal_Info_Frame.setGeometry(QtCore.QRect(15, 85, 271, 421))
        self.Personal_Info_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Personal_Info_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Personal_Info_Frame.setLineWidth(2)
        self.Personal_Info_Frame.setObjectName("Personal_Info_Frame")

        ## A simple frame that encapsulates all the gesture sequence options related elements
        self.Gesture_Sequence_Frame = QtWidgets.QFrame(Configuration_Window)
        self.Gesture_Sequence_Frame.setGeometry(QtCore.QRect(295, 55, 351, 480))
        self.Gesture_Sequence_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Gesture_Sequence_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Gesture_Sequence_Frame.setLineWidth(2)
        self.Gesture_Sequence_Frame.setObjectName("Gesture_Sequence_Frame")

        ## A simple frame that encapsulates all the sensors options related elements
        self.Sensors_Options_Frame = QtWidgets.QFrame(Configuration_Window)
        self.Sensors_Options_Frame.setGeometry(QtCore.QRect(655, 145, 231, 261))
        self.Sensors_Options_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Sensors_Options_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Sensors_Options_Frame.setLineWidth(2)
        self.Sensors_Options_Frame.setObjectName("Sensors_Options_Frame")

        ## Bring the following elements into the foreground
        self.Sensors_Options_Frame.raise_()
        self.Personal_Info_Frame.raise_()
        self.Gesture_Sequence_Frame.raise_()
        self.Configuration_Title.raise_()
        self.Go_To_Recording_Button.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()

        self.retranslateUi(Configuration_Window)
        QtCore.QMetaObject.connectSlotsByName(Configuration_Window)

    ## function retranslateUi
    #  Adds text to the window's elements
    #  @param self The object pointer
    #  @param Configuration_Window The window whose elements's text must be modified
    def retranslateUi(self, Configuration_Window):
        _translate = QtCore.QCoreApplication.translate
        Configuration_Window.setWindowTitle(_translate("Configuration_Window", "Form"))
        self.Configuration_Title.setText(_translate("Configuration_Window", "Configuration"))
        self.Go_To_Recording_Button.setText(_translate("Configuration_Window", "Go to Recording"))
        self.Gesture_Sequence_Options_Label.setText(_translate("Configuration_Window", "Gesture Sequence Options"))
        self.Casual_Sequence_Check.setText(_translate("Configuration_Window", "Casual Sequence"))
        self.Gestures_Number_Label.setText(_translate("Configuration_Window", "Number of Gestures:"))
        self.Or_Label.setText(_translate("Configuration_Window", "OR"))
        self.First_Gesture_Label.setText(_translate("Configuration_Window", "1st Gesture:"))
        self.First_Gesture_Selection.setItemText(0, _translate("Configuration_Window", "Drinking"))
        self.First_Gesture_Selection.setItemText(1, _translate("Configuration_Window", "Pouring"))
        self.First_Gesture_Selection.setItemText(2, _translate("Configuration_Window", "Sitting Down"))
        self.First_Gesture_Selection.setItemText(3, _translate("Configuration_Window", "Standing Up"))
        self.First_Gesture_Selection.setItemText(4, _translate("Configuration_Window", "Walking"))
        self.First_Gesture_Selection.setItemText(5, _translate("Configuration_Window", "None"))
        self.Second_Gesture_Label.setText(_translate("Configuration_Window", "2nd Gesture:"))
        self.Second_Gesture_Selection.setItemText(0, _translate("Configuration_Window", "Drinking"))
        self.Second_Gesture_Selection.setItemText(1, _translate("Configuration_Window", "Pouring"))
        self.Second_Gesture_Selection.setItemText(2, _translate("Configuration_Window", "Sitting Down"))
        self.Second_Gesture_Selection.setItemText(3, _translate("Configuration_Window", "Standing Up"))
        self.Second_Gesture_Selection.setItemText(4, _translate("Configuration_Window", "Walking"))
        self.Second_Gesture_Selection.setItemText(5, _translate("Configuration_Window", "None"))
        self.Third_Gesture_Label.setText(_translate("Configuration_Window", "3rd Gesture:"))
        self.Third_Gesture_Selection.setItemText(0, _translate("Configuration_Window", "Drinking"))
        self.Third_Gesture_Selection.setItemText(1, _translate("Configuration_Window", "Pouring"))
        self.Third_Gesture_Selection.setItemText(2, _translate("Configuration_Window", "Sitting Down"))
        self.Third_Gesture_Selection.setItemText(3, _translate("Configuration_Window", "Standing Up"))
        self.Third_Gesture_Selection.setItemText(4, _translate("Configuration_Window", "Walking"))
        self.Third_Gesture_Selection.setItemText(5, _translate("Configuration_Window", "None"))
        self.Fourth_Gesture_Label.setText(_translate("Configuration_Window", "4th Gesture:"))
        self.Fourth_Gesture_Selection.setItemText(0, _translate("Configuration_Window", "Drinking"))
        self.Fourth_Gesture_Selection.setItemText(1, _translate("Configuration_Window", "Pouring"))
        self.Fourth_Gesture_Selection.setItemText(2, _translate("Configuration_Window", "Sitting Down"))
        self.Fourth_Gesture_Selection.setItemText(3, _translate("Configuration_Window", "Standing Up"))
        self.Fourth_Gesture_Selection.setItemText(4, _translate("Configuration_Window", "Walking"))
        self.Fourth_Gesture_Selection.setItemText(5, _translate("Configuration_Window", "None"))
        self.Fifth_Gesture_Label.setText(_translate("Configuration_Window", "5th Gesture:"))
        self.Fifth_Gesture_Selection.setItemText(0, _translate("Configuration_Window", "Drinking"))
        self.Fifth_Gesture_Selection.setItemText(1, _translate("Configuration_Window", "Pouring"))
        self.Fifth_Gesture_Selection.setItemText(2, _translate("Configuration_Window", "Sitting Down"))
        self.Fifth_Gesture_Selection.setItemText(3, _translate("Configuration_Window", "Standing Up"))
        self.Fifth_Gesture_Selection.setItemText(4, _translate("Configuration_Window", "Walking"))
        self.Fifth_Gesture_Selection.setItemText(5, _translate("Configuration_Window", "None"))
        self.Personal_Info_Label.setText(_translate("Configuration_Window", "Personal Informations"))
        self.Name_Label.setText(_translate("Configuration_Window", "Name:"))
        self.Surname_Label.setText(_translate("Configuration_Window", "Surname:"))
        self.Age_Label.setText(_translate("Configuration_Window", "Age:"))
        self.Gender_Label.setText(_translate("Configuration_Window", "Gender:"))
        self.Gender_Selection.setItemText(0, _translate("Configuration_Window", "Male"))
        self.Gender_Selection.setItemText(1, _translate("Configuration_Window", "Female"))
        self.Gender_Selection.setItemText(2, _translate("Configuration_Window", "Other"))
        self.Height_Label.setText(_translate("Configuration_Window", "Height:"))
        self.Weight_Label.setText(_translate("Configuration_Window", "Weight:"))
        self.Sensors_Options_Label.setText(_translate("Configuration_Window", "Sensors Options"))
        self.Kinect_Sensor_Check.setText(_translate("Configuration_Window", "Kinect Sensor"))
        self.MOCAP_Sensor_Check.setText(_translate("Configuration_Window", "MOCAP sensor"))
        self.Smartwatch_Sensor_Check.setText(_translate("Configuration_Window", "Smartwatch sensor"))
