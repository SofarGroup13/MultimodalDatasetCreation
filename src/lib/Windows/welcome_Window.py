import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

## class Ui_Welcome_Window
#  This class contains the welcome window design
class Ui_Welcome_Window(object):
    def setupUi(self, Welcome_Window):
        Welcome_Window.setObjectName("Welcome_Window")
        Welcome_Window.resize(900, 600)

        ## Label containing the window's title
        self.Welcome_Title_Label = QtWidgets.QLabel(Welcome_Window)
        self.Welcome_Title_Label.setGeometry(QtCore.QRect(325, 20, 250, 50))

        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Welcome_Title_Label.setFont(font)

        self.Welcome_Title_Label.setFrameShape(QtWidgets.QFrame.Panel)
        self.Welcome_Title_Label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Welcome_Title_Label.setLineWidth(4)

        self.Welcome_Title_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.Welcome_Title_Label.setObjectName("Welcome_Title_Label")

        ## Label containing the introduction to the application text
        self.Introduction_Label = QtWidgets.QLabel(Welcome_Window)
        self.Introduction_Label.setGeometry(QtCore.QRect(50, 100, 800, 350))

        font = QtGui.QFont()
        font.setPointSize(22)
        self.Introduction_Label.setFont(font)
        
        self.Introduction_Label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Introduction_Label.setWordWrap(True)

        self.Introduction_Label.setObjectName("Introduction_Label")

        ## Button that leads to the first page of the tutorial
        self.GoToTutorial_Button = QtWidgets.QPushButton(Welcome_Window)
        self.GoToTutorial_Button.setGeometry(QtCore.QRect(200, 500, 200, 50))

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.GoToTutorial_Button.setFont(font)

        self.GoToTutorial_Button.setObjectName("GoToTutorial_Button")

        ## Button that leads directly to the configuration window
        self.SkipTutorial_Button = QtWidgets.QPushButton(Welcome_Window)
        self.SkipTutorial_Button.setGeometry(QtCore.QRect(500, 500, 200, 50))

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SkipTutorial_Button.setFont(font)

        self.SkipTutorial_Button.setObjectName("SkipTutorial_Button")

        self.retranslateUi(Welcome_Window)
        QtCore.QMetaObject.connectSlotsByName(Welcome_Window)

    ## function retranslateUi
    #  Adds text to the window's elements
    #  @param self The object pointer
    #  @param Welcome_Window The window whose elements's text must be modified
    def retranslateUi(self, Welcome_Window):
        _translate = QtCore.QCoreApplication.translate
        Welcome_Window.setWindowTitle(_translate("Welcome_Window", "Form"))
        self.Welcome_Title_Label.setText(_translate("Welcome_Window", "Welcome!"))
        self.Introduction_Label.setText(_translate("Welcome_Window", "<html><head/><body><p>This application allows you to easily create a multimodal dataset using up to three different types of sensors (Kinect, Smartwatch and MOCAP).</p><p><br/></p><p>You can now choose whether you want to see how this application works by clicking the <span style=\" font-weight:600;\">&quot;Go to tutorial&quot; button</span> or go directly to the Configuration Window by clicking the <span style=\" font-weight:600;\">&quot;Skip tutorial&quot; button</span>.</p></body></html>"))
        self.GoToTutorial_Button.setText(_translate("Welcome_Window", "Go to tutorial"))
        self.SkipTutorial_Button.setText(_translate("Welcome_Window", "Skip tutorial"))