import os
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.index = len(os.listdir("yolov5/runs/detect/"))
        self.current_image_path = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_detecting_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_detecting_button.setGeometry(QtCore.QRect(550, 630, 180, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_detecting_button.setFont(font)
        self.start_detecting_button.setObjectName("start_detecting_button")
        self.start_detecting_button.setDisabled(True)
        self.load_image_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_image_button.setGeometry(QtCore.QRect(290, 570, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.load_image_button.setFont(font)
        self.load_image_button.setObjectName("load_image_button")
        self.save_image_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_image_button.setGeometry(QtCore.QRect(820, 570, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_image_button.setFont(font)
        self.save_image_button.setObjectName("save_image_button")
        self.save_image_button.setDisabled(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 50, 120, 120))
        self.label.setObjectName("label")
        self.label.setPixmap(
            QtGui.QPixmap("legoImages/orange.jpg").scaled(self.label.size(), QtCore.Qt.KeepAspectRatio))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(960, 50, 120, 120))
        self.label_2.setObjectName("label_2")
        self.label_2.setPixmap(
            QtGui.QPixmap("legoImages/white.jpg").scaled(self.label_2.size(), QtCore.Qt.KeepAspectRatio))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(770, 50, 120, 120))
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(
            QtGui.QPixmap("legoImages/black.jpg").scaled(self.label_3.size(),
                                                                                 QtCore.Qt.KeepAspectRatio))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 50, 120, 120))
        self.label_4.setObjectName("label_4")
        self.label_4.setPixmap(
            QtGui.QPixmap("legoImages/yellow.jpg").scaled(self.label_4.size(), QtCore.Qt.KeepAspectRatio))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 50, 120, 120))
        self.label_5.setObjectName("label_5")
        self.label_5.setPixmap(
            QtGui.QPixmap("legoImages/gray.jpg").scaled(self.label_5.size(), QtCore.Qt.KeepAspectRatio))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(960, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(770, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(390, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 270, 350, 280))
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("background-color: rgb(187, 189, 191)")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(730, 270, 350, 280))
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet("background-color: rgb(187, 189, 191)")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(610, 5, 61, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.functions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_detecting_button.setText(_translate("MainWindow", "Start detecting "))
        self.load_image_button.setText(_translate("MainWindow", "Load image"))
        self.save_image_button.setText(_translate("MainWindow", "Save image"))
        self.label.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", "orange"))
        self.label_7.setText(_translate("MainWindow", "yellow"))
        self.label_8.setText(_translate("MainWindow", "white"))
        self.label_9.setText(_translate("MainWindow", "black"))
        self.label_10.setText(_translate("MainWindow", "gray"))
        self.label_11.setText(_translate("MainWindow", ""))
        self.label_12.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", "Labels"))

    def functions(self):
        self.load_image_button.clicked.connect(lambda: self.load_image())
        self.save_image_button.clicked.connect(lambda: self.save_image())
        self.start_detecting_button.clicked.connect(lambda: self.detecting())

    def load_image(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.current_image_path = file_path
            print(self.current_image_path)
            pixmap = QtGui.QPixmap(file_path)
            self.label_11.setPixmap(pixmap.scaled(self.label_11.size(), QtCore.Qt.KeepAspectRatio))
            self.label_11.setStyleSheet("")
            self.start_detecting_button.setDisabled(False)

    def save_image(self):
        if self.current_image_path:
            file_dialog = QtWidgets.QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(None, "Save Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
            if file_path:
                pixmap = self.label_12.pixmap()
                pixmap.save(file_path)

    def detecting(self):
        code = 'python yolov5/detect.py --weights yolov5/best.pt --source ' + self.current_image_path
        print(code)
        subprocess.call(code, shell=True)
        self.index += 1
        file_path = "yolov5/runs/detect/exp" + str(self.index)
        file_path += "/" + os.listdir(file_path)[0]
        self.current_image_path = file_path
        print(self.current_image_path)
        pixmap = QtGui.QPixmap(file_path)
        self.label_12.setPixmap(pixmap.scaled(self.label_12.size(), QtCore.Qt.KeepAspectRatio))
        self.label_12.setStyleSheet("")
        self.save_image_button.setDisabled(False)




