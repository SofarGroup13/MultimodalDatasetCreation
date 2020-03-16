# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configurationGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 650)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 971, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())

        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.titleConfigurationLabel = QtWidgets.QLabel(self.page)
        self.titleConfigurationLabel.setGeometry(QtCore.QRect(380, 10, 240, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleConfigurationLabel.sizePolicy().hasHeightForWidth())

        self.titleConfigurationLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.titleConfigurationLabel.setFont(font)
        self.titleConfigurationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleConfigurationLabel.setObjectName("titleConfigurationLabel")

        self.startButton = QtWidgets.QPushButton(self.page)
        self.startButton.setGeometry(QtCore.QRect(420, 470, 160, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")

        self.personDataFrame = QtWidgets.QFrame(self.page)
        self.personDataFrame.setGeometry(QtCore.QRect(30, 70, 221, 291))
        self.personDataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.personDataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.personDataFrame.setObjectName("personDataFrame")

        self.nameLabel = QtWidgets.QLabel(self.personDataFrame)
        self.nameLabel.setGeometry(QtCore.QRect(30, 20, 58, 14))
        self.nameLabel.setObjectName("nameLabel")

        self.ageLabel = QtWidgets.QLabel(self.personDataFrame)
        self.ageLabel.setGeometry(QtCore.QRect(30, 70, 31, 16))
        self.ageLabel.setObjectName("ageLabel")

        self.genderLabel = QtWidgets.QLabel(self.personDataFrame)
        self.genderLabel.setGeometry(QtCore.QRect(30, 120, 58, 14))
        self.genderLabel.setObjectName("genderLabel")

        self.heightLabel = QtWidgets.QLabel(self.personDataFrame)
        self.heightLabel.setGeometry(QtCore.QRect(30, 170, 58, 14))
        self.heightLabel.setObjectName("heightLabel")

        self.weightLabel = QtWidgets.QLabel(self.personDataFrame)
        self.weightLabel.setGeometry(QtCore.QRect(30, 220, 58, 14))
        self.weightLabel.setObjectName("weightLabel")

        self.nameEdit = QtWidgets.QLineEdit(self.personDataFrame)
        self.nameEdit.setGeometry(QtCore.QRect(30, 40, 113, 24))
        self.nameEdit.setObjectName("nameEdit")

        self.ageEdit = QtWidgets.QLineEdit(self.personDataFrame)
        self.ageEdit.setGeometry(QtCore.QRect(30, 90, 113, 24))
        self.ageEdit.setObjectName("ageEdit")

        self.heightEdit = QtWidgets.QLineEdit(self.personDataFrame)
        self.heightEdit.setGeometry(QtCore.QRect(30, 190, 113, 24))
        self.heightEdit.setObjectName("heightEdit")

        self.weightEdit = QtWidgets.QLineEdit(self.personDataFrame)
        self.weightEdit.setGeometry(QtCore.QRect(30, 240, 113, 24))
        self.weightEdit.setObjectName("weightEdit")
        
        self.genderBox = QtWidgets.QComboBox(self.personDataFrame)
        self.genderBox.setGeometry(QtCore.QRect(30, 140, 78, 24))
        self.genderBox.setObjectName("genderBox")
        self.genderBox.addItem("")
        self.genderBox.addItem("")
        self.genderBox.addItem("")

        self.gesturesFrame = QtWidgets.QFrame(self.page)
        self.gesturesFrame.setGeometry(QtCore.QRect(350, 70, 221, 291))
        self.gesturesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gesturesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gesturesFrame.setObjectName("gesturesFrame")

        self.nGesturesLabel = QtWidgets.QLabel(self.gesturesFrame)
        self.nGesturesLabel.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.nGesturesLabel.setObjectName("nGesturesLabel")

        self.nGesturesEdit = QtWidgets.QLineEdit(self.gesturesFrame)
        self.nGesturesEdit.setGeometry(QtCore.QRect(30, 40, 113, 24))
        self.nGesturesEdit.setObjectName("nGesturesEdit")

        self.label = QtWidgets.QLabel(self.gesturesFrame)
        self.label.setGeometry(QtCore.QRect(30, 70, 71, 16))
        self.label.setObjectName("label")

        self.gesture1Box = QtWidgets.QComboBox(self.gesturesFrame)
        self.gesture1Box.setGeometry(QtCore.QRect(30, 90, 78, 24))
        self.gesture1Box.setObjectName("gesture1Box")
        self.gesture1Box.addItem("")
        self.gesture1Box.addItem("")
        self.gesture1Box.addItem("")
        self.gesture1Box.addItem("")
        self.gesture1Box.addItem("")
        self.gesture1Box.addItem("")

        self.firstLabel = QtWidgets.QLabel(self.gesturesFrame)
        self.firstLabel.setGeometry(QtCore.QRect(0, 95, 21, 16))
        self.firstLabel.setObjectName("firstLabel")

        self.gesture2Box = QtWidgets.QComboBox(self.gesturesFrame)
        self.gesture2Box.setGeometry(QtCore.QRect(30, 120, 78, 24))
        self.gesture2Box.setObjectName("gesture2Box")
        self.gesture2Box.addItem("")
        self.gesture2Box.addItem("")
        self.gesture2Box.addItem("")
        self.gesture2Box.addItem("")
        self.gesture2Box.addItem("")
        self.gesture2Box.addItem("")

        self.gesture5Box = QtWidgets.QComboBox(self.gesturesFrame)
        self.gesture5Box.setGeometry(QtCore.QRect(30, 210, 78, 24))
        self.gesture5Box.setObjectName("gesture5Box")

        self.gesture5Box.addItem("")
        self.gesture5Box.addItem("")
        self.gesture5Box.addItem("")
        self.gesture5Box.addItem("")
        self.gesture5Box.addItem("")
        self.gesture5Box.addItem("")

        self.gesture4Box = QtWidgets.QComboBox(self.gesturesFrame)
        self.gesture4Box.setGeometry(QtCore.QRect(30, 180, 78, 24))
        self.gesture4Box.setObjectName("gesture4Box")
        self.gesture4Box.addItem("")
        self.gesture4Box.addItem("")
        self.gesture4Box.addItem("")
        self.gesture4Box.addItem("")
        self.gesture4Box.addItem("")
        self.gesture4Box.addItem("")

        self.gesture3Box = QtWidgets.QComboBox(self.gesturesFrame)
        self.gesture3Box.setGeometry(QtCore.QRect(30, 150, 78, 24))
        self.gesture3Box.setObjectName("gesture3Box")
        self.gesture3Box.addItem("")
        self.gesture3Box.addItem("")
        self.gesture3Box.addItem("")
        self.gesture3Box.addItem("")
        self.gesture3Box.addItem("")
        self.gesture3Box.addItem("")

        self.secondLabel = QtWidgets.QLabel(self.gesturesFrame)
        self.secondLabel.setGeometry(QtCore.QRect(0, 125, 21, 16))
        self.secondLabel.setObjectName("secondLabel")

        self.thirdLabel = QtWidgets.QLabel(self.gesturesFrame)
        self.thirdLabel.setGeometry(QtCore.QRect(0, 155, 21, 16))
        self.thirdLabel.setObjectName("thirdLabel")

        self.fourthLabel = QtWidgets.QLabel(self.gesturesFrame)
        self.fourthLabel.setGeometry(QtCore.QRect(0, 185, 21, 16))
        self.fourthLabel.setObjectName("fourthLabel")

        self.fifthLabel = QtWidgets.QLabel(self.gesturesFrame)
        self.fifthLabel.setGeometry(QtCore.QRect(0, 215, 21, 16))
        self.fifthLabel.setObjectName("fifthLabel")

        self.casualCheckBox = QtWidgets.QCheckBox(self.gesturesFrame)
        self.casualCheckBox.setGeometry(QtCore.QRect(30, 240, 141, 21))
        self.casualCheckBox.setObjectName("casualCheckBox")

        self.sensorsFrame = QtWidgets.QFrame(self.page)
        self.sensorsFrame.setGeometry(QtCore.QRect(680, 70, 221, 291))
        self.sensorsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sensorsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sensorsFrame.setObjectName("sensorsFrame")

        self.sensorsLabel = QtWidgets.QLabel(self.sensorsFrame)
        self.sensorsLabel.setGeometry(QtCore.QRect(30, 20, 81, 16))
        self.sensorsLabel.setObjectName("sensorsLabel")
        
        self.kinectCheckBox = QtWidgets.QCheckBox(self.sensorsFrame)
        self.kinectCheckBox.setGeometry(QtCore.QRect(30, 40, 71, 21))
        self.kinectCheckBox.setObjectName("kinectCheckBox")

        self.MOCAPCheckBox = QtWidgets.QCheckBox(self.sensorsFrame)
        self.MOCAPCheckBox.setGeometry(QtCore.QRect(30, 60, 81, 21))
        self.MOCAPCheckBox.setObjectName("MOCAPCheckBox")

        self.smartwatchCheckBox = QtWidgets.QCheckBox(self.sensorsFrame)
        self.smartwatchCheckBox.setGeometry(QtCore.QRect(30, 80, 111, 21))
        self.smartwatchCheckBox.setObjectName("smartwatchCheckBox")

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.Recording_Label = QtWidgets.QLabel(self.page_2)
        self.Recording_Label.setGeometry(QtCore.QRect(380, 10, 240, 40))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)

        self.Recording_Label.setFont(font)
        self.Recording_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Recording_Label.setObjectName("Recording_Label")

        self.Countdown_Label = QtWidgets.QLabel(self.page_2)
        self.Countdown_Label.setGeometry(QtCore.QRect(440, 70, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Countdown_Label.setFont(font)
        self.Countdown_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Countdown_Label.setObjectName("Countdown_Label")

        self.Display_Image_Label = QtWidgets.QLabel(self.page_2)
        self.Display_Image_Label.setGeometry(QtCore.QRect(300, 180, 400, 300))
        self.Display_Image_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Display_Image_Label.setText("")
        self.Display_Image_Label.setPixmap(QtGui.QPixmap("../../../../Downloads/Blurring_Cat.jpeg"))
        self.Display_Image_Label.setScaledContents(True)
        self.Display_Image_Label.setObjectName("Display_Image_Label")

        self.Time_Progress = QtWidgets.QProgressBar(self.page_2)
        self.Time_Progress.setGeometry(QtCore.QRect(220, 510, 640, 30))
        self.Time_Progress.setProperty("value", 0)
        self.Time_Progress.setObjectName("Time_Progress")

        self.Time_Elapsed_Label = QtWidgets.QLabel(self.page_2)
        self.Time_Elapsed_Label.setGeometry(QtCore.QRect(375, 560, 250, 40))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Time_Elapsed_Label.setFont(font)
        self.Time_Elapsed_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Time_Elapsed_Label.setObjectName("Time_Elapsed_Label")

        self.PlayStop_Button = QtWidgets.QPushButton(self.page_2)
        self.PlayStop_Button.setGeometry(QtCore.QRect(100, 510, 100, 30))
        self.PlayStop_Button.setObjectName("PlayStop_Button")

        self.GoBack_Button = QtWidgets.QPushButton(self.page_2)
        self.GoBack_Button.setGeometry(QtCore.QRect(40, 20, 100, 30))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.GoBack_Button.setFont(font)
        self.GoBack_Button.setObjectName("GoBack_Button")
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Change page when clicking start button
        self.startButton.clicked.connect(self.startButtonAction)

        # Go back to the first page when clicking Go Back button
        self.GoBack_Button.clicked.connect(self.goBackButtonAction)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def startButtonAction(self, MainWindow):
        self.stackedWidget.setCurrentIndex(1)

    def goBackButtonAction(self,MainWindow):
        self.stackedWidget.setCurrentIndex(0)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Experimenter GUI"))
        self.titleConfigurationLabel.setText(_translate("MainWindow", "Configuration"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.ageLabel.setText(_translate("MainWindow", "Age"))
        self.genderLabel.setText(_translate("MainWindow", "Gender"))
        self.heightLabel.setText(_translate("MainWindow", "Height"))
        self.weightLabel.setText(_translate("MainWindow", "Weight"))
        self.genderBox.setItemText(0, _translate("MainWindow", "M"))
        self.genderBox.setItemText(1, _translate("MainWindow", "F"))
        self.genderBox.setItemText(2, _translate("MainWindow", "Other"))
        self.nGesturesLabel.setText(_translate("MainWindow", "Number of Gestures"))
        self.label.setText(_translate("MainWindow", "Gestures"))
        self.gesture1Box.setItemText(0, _translate("MainWindow", "None"))
        self.gesture1Box.setItemText(1, _translate("MainWindow", "Drinking"))
        self.gesture1Box.setItemText(2, _translate("MainWindow", "Pouring"))
        self.gesture1Box.setItemText(3, _translate("MainWindow", "Sitting Down"))
        self.gesture1Box.setItemText(4, _translate("MainWindow", "Standing Up"))
        self.gesture1Box.setItemText(5, _translate("MainWindow", "Walking"))
        self.firstLabel.setText(_translate("MainWindow", "1st"))
        self.gesture2Box.setItemText(0, _translate("MainWindow", "None"))
        self.gesture2Box.setItemText(1, _translate("MainWindow", "Drinking"))
        self.gesture2Box.setItemText(2, _translate("MainWindow", "Pouring"))
        self.gesture2Box.setItemText(3, _translate("MainWindow", "Sitting Down"))
        self.gesture2Box.setItemText(4, _translate("MainWindow", "Standing Up"))
        self.gesture2Box.setItemText(5, _translate("MainWindow", "Walking"))
        self.gesture5Box.setItemText(0, _translate("MainWindow", "None"))
        self.gesture5Box.setItemText(1, _translate("MainWindow", "Drinking"))
        self.gesture5Box.setItemText(2, _translate("MainWindow", "Pouring"))
        self.gesture5Box.setItemText(3, _translate("MainWindow", "Sitting Down"))
        self.gesture5Box.setItemText(4, _translate("MainWindow", "Standing Up"))
        self.gesture5Box.setItemText(5, _translate("MainWindow", "Walking"))
        self.gesture4Box.setItemText(0, _translate("MainWindow", "None"))
        self.gesture4Box.setItemText(1, _translate("MainWindow", "Drinking"))
        self.gesture4Box.setItemText(2, _translate("MainWindow", "Pouring"))
        self.gesture4Box.setItemText(3, _translate("MainWindow", "Sitting Down"))
        self.gesture4Box.setItemText(4, _translate("MainWindow", "Standing Up"))
        self.gesture4Box.setItemText(5, _translate("MainWindow", "Walking"))
        self.gesture3Box.setItemText(0, _translate("MainWindow", "None"))
        self.gesture3Box.setItemText(1, _translate("MainWindow", "Drinking"))
        self.gesture3Box.setItemText(2, _translate("MainWindow", "Pouring"))
        self.gesture3Box.setItemText(3, _translate("MainWindow", "Sitting Down"))
        self.gesture3Box.setItemText(4, _translate("MainWindow", "Standing Up"))
        self.gesture3Box.setItemText(5, _translate("MainWindow", "Walking"))
        self.secondLabel.setText(_translate("MainWindow", "2nd"))
        self.thirdLabel.setText(_translate("MainWindow", "3rd"))
        self.fourthLabel.setText(_translate("MainWindow", "4th"))
        self.fifthLabel.setText(_translate("MainWindow", "5th"))
        self.casualCheckBox.setText(_translate("MainWindow", "Casual Sequence"))
        self.sensorsLabel.setText(_translate("MainWindow", "Sensors Used"))
        self.kinectCheckBox.setText(_translate("MainWindow", "Kinect"))
        self.MOCAPCheckBox.setText(_translate("MainWindow", "MOCAP"))
        self.smartwatchCheckBox.setText(_translate("MainWindow", "Smartwatch"))
        self.Recording_Label.setText(_translate("MainWindow", "Recording"))
        self.Countdown_Label.setText(_translate("MainWindow", "10"))
        self.Time_Elapsed_Label.setText(_translate("MainWindow", "Time elapsed is 0:00/0:00"))
        self.PlayStop_Button.setText(_translate("MainWindow", "Play"))
        self.GoBack_Button.setText(_translate("MainWindow", "Go back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
