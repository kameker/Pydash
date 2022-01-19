from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1570, 769)
        self.NameLevelLabel = QtWidgets.QLabel(Form)
        self.NameLevelLabel.setGeometry(QtCore.QRect(480, 290, 541, 191))
        self.NameLevelLabel.setObjectName("NameLevelLabel")
        self.NameLevelLabel.setText("")
        self.RightButton = QtWidgets.QPushButton(Form)
        self.RightButton.setGeometry(QtCore.QRect(1100, 330, 121, 101))
        self.RightButton.setText("")
        self.RightButton.setObjectName("RightButton")
        self.LeftButton = QtWidgets.QPushButton(Form)
        self.LeftButton.setGeometry(QtCore.QRect(220, 340, 121, 101))
        self.LeftButton.setText("")
        self.LeftButton.setObjectName("LeftButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 580, 231, 81))
        self.pushButton_3.setObjectName("pushButton_3")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.NameLevelLabel.setText(_translate("Form", "TextLabel"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
