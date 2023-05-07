# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waiting_room_student.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1040, 681)
        Form.setStyleSheet("background-color:#2C2F33;")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 70, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.camera_frame = QtWidgets.QFrame(Form)
        self.camera_frame.setGeometry(QtCore.QRect(250, 230, 491, 490))
        self.camera_frame.setStyleSheet("QFrame{\n"
"    border: 0px solid black;\n"
"}")
        self.camera_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera_frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.camera_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 170, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Waiting room"))
        self.label_4.setText(_translate("Form", "Tip: adjust your camera, and get ready for the test"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())