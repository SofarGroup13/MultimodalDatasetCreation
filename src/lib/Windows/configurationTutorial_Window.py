import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

## class Ui_ConfigurationTutorial_Window
#  This class contains the configuration tutorial window design
class Ui_ConfigurationTutorial_Window(object):
    def setupUi(self, ConfigurationTutorial_Window):
        ConfigurationTutorial_Window.setObjectName("ConfigurationTutorial_Window")
        ConfigurationTutorial_Window.resize(900, 600)

        ## Label containing the window's title
        self.ConfigurationTutorial_Title_Label = QtWidgets.QLabel(ConfigurationTutorial_Window)
        self.ConfigurationTutorial_Title_Label.setGeometry(QtCore.QRect(250, 20, 400, 50))

        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ConfigurationTutorial_Title_Label.setFont(font)

        self.ConfigurationTutorial_Title_Label.setFrameShape(QtWidgets.QFrame.Panel)
        self.ConfigurationTutorial_Title_Label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ConfigurationTutorial_Title_Label.setLineWidth(4)

        self.ConfigurationTutorial_Title_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.ConfigurationTutorial_Title_Label.setObjectName("ConfigurationTutorial_Title_Label")

        ## Label that contains the informative text to display to the user
        self.ConfigurationTutorialText_Label = QtWidgets.QLabel(ConfigurationTutorial_Window)
        self.ConfigurationTutorialText_Label.setGeometry(QtCore.QRect(125, 100, 300, 400))

        font = QtGui.QFont()
        font.setPointSize(17)
        self.ConfigurationTutorialText_Label.setFont(font)

        self.ConfigurationTutorialText_Label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ConfigurationTutorialText_Label.setWordWrap(True)

        self.ConfigurationTutorialText_Label.setObjectName("ConfigurationTutorialText_Label")

        ## Label that contains the image related to the informative text
        self.ConfigurationTutorialImage_Label = QtWidgets.QLabel(ConfigurationTutorial_Window)
        self.ConfigurationTutorialImage_Label.setGeometry(QtCore.QRect(475, 100, 300, 400))

        self.ConfigurationTutorialImage_Label.setText("")
        self.ConfigurationTutorialImage_Label.setPixmap(QtGui.QPixmap("../../../gui_content/pictures/Personal_Info.png"))
        self.ConfigurationTutorialImage_Label.setScaledContents(True)

        self.ConfigurationTutorialImage_Label.setObjectName("ConfigurationTutorialImage_Label")

        ## Button to advance in the tutorial
        self.Next_Button = QtWidgets.QPushButton(ConfigurationTutorial_Window)
        self.Next_Button.setGeometry(QtCore.QRect(400, 540, 100, 40))

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Next_Button.setFont(font)

        self.Next_Button.setObjectName("Next_Button")

        self.retranslateUi(ConfigurationTutorial_Window)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationTutorial_Window)

    ## function retranslateUi
    #  Adds text to the window's elements
    #  @param self The object pointer
    #  @param ConfigurationTutorial_Window The window whose elements's text must be modified
    def retranslateUi(self, ConfigurationTutorial_Window):
        _translate = QtCore.QCoreApplication.translate
        ConfigurationTutorial_Window.setWindowTitle(_translate("ConfigurationTutorial_Window", "Form"))
        self.ConfigurationTutorial_Title_Label.setText(_translate("ConfigurationTutorial_Window", "Configuration tutorial (1)"))
        self.ConfigurationTutorialText_Label.setText(_translate("ConfigurationTutorial_Window", "<html><head/><body><p>In this part you have to write the personal informations of the person <span style=\" font-style:italic;\">performing the gestures</span>, which will be saved in a &quot;txt&quot; file: <span style=\" font-weight:600;\">this isn\'t mandatory</span>, but those information might be useful. </p><p><br/></p><p>If you don\'t write anything the &quot;txt&quot; file will only contain the <span style=\" font-style:italic;\">default template</span>, which can then be modified by the user.</p></body></html>"))
        self.Next_Button.setText(_translate("ConfigurationTutorial_Window", "Next"))