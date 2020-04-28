import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

## class Ui_RecordingTutorial_Window
#  This class contains the recording tutorial window design
class Ui_RecordingTutorial_Window(object):
    def setupUi(self, RecordingTutorial_Window):
        RecordingTutorial_Window.setObjectName("RecordingTutorial_Window")
        RecordingTutorial_Window.resize(900, 600)

        ## Label containing the window's title
        self.RecordingTutorial_Title_Label = QtWidgets.QLabel(RecordingTutorial_Window)
        self.RecordingTutorial_Title_Label.setGeometry(QtCore.QRect(300, 20, 300, 50))

        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.RecordingTutorial_Title_Label.setFont(font)

        self.RecordingTutorial_Title_Label.setFrameShape(QtWidgets.QFrame.Panel)
        self.RecordingTutorial_Title_Label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RecordingTutorial_Title_Label.setLineWidth(4)

        self.RecordingTutorial_Title_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.RecordingTutorial_Title_Label.setObjectName("RecordingTutorial_Title_Label")

        ## Label that contains the informative text to display to the user
        self.RecordingTutorial_Text_Label = QtWidgets.QLabel(RecordingTutorial_Window)
        self.RecordingTutorial_Text_Label.setGeometry(QtCore.QRect(100, 100, 700, 400))

        font = QtGui.QFont()
        font.setPointSize(18)
        self.RecordingTutorial_Text_Label.setFont(font)

        self.RecordingTutorial_Text_Label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.RecordingTutorial_Text_Label.setWordWrap(True)

        self.RecordingTutorial_Text_Label.setObjectName("RecordingTutorial_Text_Label")

        ## Button to finish the tutorial
        self.Continue_Button = QtWidgets.QPushButton(RecordingTutorial_Window)
        self.Continue_Button.setGeometry(QtCore.QRect(375, 520, 150, 40))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Continue_Button.setFont(font)

        self.Continue_Button.setObjectName("Continue_Button")

        self.retranslateUi(RecordingTutorial_Window)
        QtCore.QMetaObject.connectSlotsByName(RecordingTutorial_Window)

    ## function retranslateUi
    #  Adds text to the window's elements
    #  @param self The object pointer
    #  @param RecordingTutorial_Window The window whose elements's text must be modified
    def retranslateUi(self, RecordingTutorial_Window):
        _translate = QtCore.QCoreApplication.translate
        RecordingTutorial_Window.setWindowTitle(_translate("RecordingTutorial_Window", "Form"))
        self.RecordingTutorial_Title_Label.setText(_translate("RecordingTutorial_Window", "Recording tutorial"))
        self.RecordingTutorial_Text_Label.setText(_translate("RecordingTutorial_Window", "<html><head/><body><p>In the <span style=\" font-style:italic;\">Recording Window</span>, you initially have two options: either you go back to the <span style=\" font-style:italic;\">Configuration Window</span> or you click the <span style=\" font-style:italic;\">&quot;Play&quot; button</span>, which will trigger a <span style=\" font-weight:600;\">10-second countdown</span>.</p><p><br/></p><p>At the end of it, the recording will start and the image corresponding to the gesture to perform will be displayed: images will be updated <span style=\" font-weight:600;\">every 30 seconds</span>.</p><p><br/></p><p>When the recording has started you can manually stop it with the <span style=\" font-style:italic;\">&quot;Stop&quot; button</span>.</p></body></html>"))
        self.Continue_Button.setText(_translate("RecordingTutorial_Window", "Ok, I got it!"))