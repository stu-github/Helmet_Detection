# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1409, 1146)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.author_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.author_label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.author_label_2.setFont(font)
        self.author_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.author_label_2.setObjectName("author_label_2")
        self.verticalLayout_3.addWidget(self.author_label_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.author_label = QtWidgets.QLabel(self.centralwidget)
        self.author_label.setMinimumSize(QtCore.QSize(200, 30))
        self.author_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.author_label.setFont(font)
        self.author_label.setStyleSheet("QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox, \n"
"QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog {\n"
"    background-color: #222222;\n"
"    color: #BBBBBB;\n"
"    font-family: \"Calibri\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}")
        self.author_label.setAlignment(QtCore.Qt.AlignCenter)
        self.author_label.setObjectName("author_label")
        self.horizontalLayout_7.addWidget(self.author_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(1300, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_video_widget = QVideoWidget(self.groupBox)
        self.input_video_widget.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.input_video_widget.setFont(font)
        self.input_video_widget.setObjectName("input_video_widget")
        self.verticalLayout.addWidget(self.input_video_widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.predict_progressBar = QtWidgets.QProgressBar(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.predict_progressBar.setFont(font)
        self.predict_progressBar.setProperty("value", 0)
        self.predict_progressBar.setObjectName("predict_progressBar")
        self.horizontalLayout_2.addWidget(self.predict_progressBar)
        self.fps_label = QtWidgets.QLabel(self.groupBox)
        self.fps_label.setMinimumSize(QtCore.QSize(0, 0))
        self.fps_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.fps_label.setFont(font)
        self.fps_label.setObjectName("fps_label")
        self.horizontalLayout_2.addWidget(self.fps_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_media_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.import_media_pushButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.import_media_pushButton.setFont(font)
        self.import_media_pushButton.setStyleSheet("QPushButton{\n"
"    background-color:#2828FF;\n"
"    color:#ffffff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#FFFFFF;\n"
"    background:#9393FF;\n"
"}\n"
"")
        self.import_media_pushButton.setObjectName("import_media_pushButton")
        self.horizontalLayout.addWidget(self.import_media_pushButton)
        self.start_predict_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.start_predict_pushButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.start_predict_pushButton.setFont(font)
        self.start_predict_pushButton.setStyleSheet("QPushButton{\n"
"    background-color:#16A085;\n"
"    color:#ffffff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#FFFFFF;\n"
"    background:#2EE1C1;\n"
"}\n"
"")
        self.start_predict_pushButton.setObjectName("start_predict_pushButton")
        self.horizontalLayout.addWidget(self.start_predict_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.output_video_widget = QVideoWidget(self.groupBox_2)
        self.output_video_widget.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.output_video_widget.setFont(font)
        self.output_video_widget.setObjectName("output_video_widget")
        self.verticalLayout_2.addWidget(self.output_video_widget)
        self.open_predict_file_pushButton = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.open_predict_file_pushButton.setFont(font)
        self.open_predict_file_pushButton.setObjectName("open_predict_file_pushButton")
        self.verticalLayout_2.addWidget(self.open_predict_file_pushButton)
        self.verticalLayout_3.addWidget(self.splitter)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.video_horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.video_horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.video_horizontalSlider.setFont(font)
        self.video_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.video_horizontalSlider.setObjectName("video_horizontalSlider")
        self.horizontalLayout_4.addWidget(self.video_horizontalSlider)
        self.video_percent_label = QtWidgets.QLabel(self.centralwidget)
        self.video_percent_label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.video_percent_label.setFont(font)
        self.video_percent_label.setObjectName("video_percent_label")
        self.horizontalLayout_4.addWidget(self.video_percent_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.play_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.play_pushButton.setMinimumSize(QtCore.QSize(0, 25))
        self.play_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.play_pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pushButton.setIcon(icon)
        self.play_pushButton.setObjectName("play_pushButton")
        self.horizontalLayout_3.addWidget(self.play_pushButton)
        self.pause_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pause_pushButton.setMinimumSize(QtCore.QSize(0, 25))
        self.pause_pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pause_pushButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_pushButton.setIcon(icon1)
        self.pause_pushButton.setObjectName("pause_pushButton")
        self.horizontalLayout_3.addWidget(self.pause_pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.predict_info_plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.predict_info_plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.predict_info_plainTextEdit.setFont(font)
        self.predict_info_plainTextEdit.setObjectName("predict_info_plainTextEdit")
        self.horizontalLayout_6.addWidget(self.predict_info_plainTextEdit)
        self.horizontalLayout_5.addWidget(self.groupBox_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gpu_info_chart = QChartView(self.centralwidget)
        self.gpu_info_chart.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.gpu_info_chart.setFont(font)
        self.gpu_info_chart.setObjectName("gpu_info_chart")
        self.verticalLayout_3.addWidget(self.gpu_info_chart)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1409, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.author_label_2.setText(_translate("MainWindow", "Intelligent Monitoring System of Construction Site"))
        self.author_label.setText(_translate("MainWindow", "Product by: HinGwenWoong"))
        self.groupBox.setTitle(_translate("MainWindow", "Input Media"))
        self.label.setText(_translate("MainWindow", "Processing:"))
        self.fps_label.setText(_translate("MainWindow", "(FPS)"))
        self.import_media_pushButton.setStatusTip(_translate("MainWindow", "Import video to predict"))
        self.import_media_pushButton.setText(_translate("MainWindow", "Import"))
        self.start_predict_pushButton.setStatusTip(_translate("MainWindow", "Predict the vedio"))
        self.start_predict_pushButton.setText(_translate("MainWindow", "Predict"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output Media"))
        self.open_predict_file_pushButton.setText(_translate("MainWindow", "Open in Browser"))
        self.video_percent_label.setText(_translate("MainWindow", "0 %"))
        self.play_pushButton.setText(_translate("MainWindow", "Play"))
        self.pause_pushButton.setText(_translate("MainWindow", "Pause"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Predict Info:"))
from PyQt5.QtChart import QChartView
from PyQt5.QtMultimediaWidgets import QVideoWidget
