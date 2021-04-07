# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dateConverter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import jalali
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWindow, QIntValidator




def close():
    sys.exit(app.exec_())


def maximize():
    if self.isMaximized():
        self.showNormal()
    else:
        self.showMaximized()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 616)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.MainLayout.setContentsMargins(10, 10, 10, 10)
        self.MainLayout.setSpacing(0)
        self.MainLayout.setObjectName("MainLayout")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(64, 0, 128, 255), stop:1 rgba(0, 0, 128, 255));\n"
"border-radius: 10px;")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.MainFrame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color: none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_btns = QtWidgets.QFrame(self.title_bar)
        self.frame_btns.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(245, 71, 71);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(245, 71, 71, 150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_4.addWidget(self.btn_close)
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(254, 188, 69);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(254, 188, 69, 150);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_4.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(50, 196, 50);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 196, 50, 150);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_4.addWidget(self.btn_maximize)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(49, 206, 185);")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.title_bar)
        self.content_bar = QtWidgets.QFrame(self.MainFrame)
        self.content_bar.setStyleSheet("background-color: none;")
        self.content_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.content_bar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content_bar)
        self.stackedWidget.setStyleSheet("background-color: none;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content_home = QtWidgets.QFrame(self.page_home)
        self.frame_content_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_home.setObjectName("frame_content_home")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_content_home)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_inputs = QtWidgets.QFrame(self.frame_content_home)
        self.frame_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inputs.setObjectName("frame_inputs")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_inputs)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_circle_1 = QtWidgets.QFrame(self.frame_inputs)
        self.frame_circle_1.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_circle_1.setMaximumSize(QtCore.QSize(250, 250))
        self.frame_circle_1.setStyleSheet("QFrame {\n"
"    border: 5px solid rgb(52, 203, 178);\n"
"    border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid rgb(66, 91, 107);\n"
"}")
        self.frame_circle_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle_1.setObjectName("frame_circle_1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_circle_1)
        self.verticalLayout_5.setContentsMargins(20, 50, 20, 70)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_circle_1)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_circle_1)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.onlyInt = QIntValidator()
        self.edt_year = QtWidgets.QLineEdit(self.frame_circle_1)
        self.edt_year.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edt_year.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(52, 203, 178);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(66, 91, 107);\n"
"}")
        self.edt_year.setInputMask("")
        self.edt_year.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_year.setObjectName("edt_year")
        self.edt_year.setValidator(self.onlyInt)
        self.verticalLayout_5.addWidget(self.edt_year)
        self.horizontalLayout_5.addWidget(self.frame_circle_1)
        self.frame_circle_2 = QtWidgets.QFrame(self.frame_inputs)
        self.frame_circle_2.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_circle_2.setMaximumSize(QtCore.QSize(250, 250))
        self.frame_circle_2.setStyleSheet("QFrame {\n"
"    border: 5px solid rgb(52, 203, 178);\n"
"    border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid rgb(66, 91, 107);\n"
"}")
        self.frame_circle_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle_2.setObjectName("frame_circle_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_circle_2)
        self.verticalLayout_6.setContentsMargins(20, 50, 20, 70)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frame_circle_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_circle_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.edt_month = QtWidgets.QLineEdit(self.frame_circle_2)
        self.edt_month.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edt_month.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(52, 203, 178);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(66, 91, 107);\n"
"}")
        self.edt_month.setInputMask("")
        self.edt_month.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_month.setObjectName("edt_month")
        self.edt_month.setValidator(self.onlyInt)
        self.verticalLayout_6.addWidget(self.edt_month)
        self.horizontalLayout_5.addWidget(self.frame_circle_2)
        self.frame_circle_3 = QtWidgets.QFrame(self.frame_inputs)
        self.frame_circle_3.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_circle_3.setMaximumSize(QtCore.QSize(250, 250))
        self.frame_circle_3.setStyleSheet("QFrame {\n"
"    border: 5px solid rgb(52, 203, 178);\n"
"    border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid rgb(66, 91, 107);\n"
"}")
        self.frame_circle_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle_3.setObjectName("frame_circle_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_circle_3)
        self.verticalLayout_7.setContentsMargins(20, 50, 20, 70)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_circle_3)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_circle_3)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.edt_day = QtWidgets.QLineEdit(self.frame_circle_3)
        self.edt_day.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edt_day.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(52, 203, 178);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(66, 91, 107);\n"
"}")
        self.edt_day.setInputMask("")
        self.edt_day.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_day.setObjectName("edt_day")
        self.edt_day.setValidator(self.onlyInt)
        self.verticalLayout_7.addWidget(self.edt_day)
        self.horizontalLayout_5.addWidget(self.frame_circle_3)
        self.verticalLayout_8.addWidget(self.frame_inputs)
        self.frame_output = QtWidgets.QFrame(self.frame_content_home)
        self.frame_output.setStyleSheet("")
        self.frame_output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_output.setObjectName("frame_output")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_output)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_details = QtWidgets.QFrame(self.frame_output)
        self.frame_details.setStyleSheet("QFrame {\n"
"    border: 0.5px solid rgb(52, 203, 178);"
"}")
        self.frame_details.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_details.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_details.setObjectName("frame_details")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_details)
        self.verticalLayout_9.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_year = QtWidgets.QLabel(self.frame_details)
        self.label_year.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_year.setFont(font)
        self.label_year.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.label_year.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_year.setObjectName("label_year")
        self.verticalLayout_9.addWidget(self.label_year)
        self.label_month = QtWidgets.QLabel(self.frame_details)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_month.setFont(font)
        self.label_month.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.label_month.setObjectName("label_month")
        self.verticalLayout_9.addWidget(self.label_month)
        self.label_day = QtWidgets.QLabel(self.frame_details)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_day.setFont(font)
        self.label_day.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.label_day.setObjectName("label_day")
        self.verticalLayout_9.addWidget(self.label_day)
        self.label_dow = QtWidgets.QLabel(self.frame_details)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_dow.setFont(font)
        self.label_dow.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.label_dow.setObjectName("label_dow")
        self.verticalLayout_9.addWidget(self.label_dow)
        self.horizontalLayout_6.addWidget(self.frame_details)
        self.frame_works = QtWidgets.QFrame(self.frame_output)
        self.frame_works.setStyleSheet("")
        self.frame_works.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_works.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_works.setObjectName("frame_works")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_works)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame = QtWidgets.QFrame(self.frame_works)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioButton_jtg = QtWidgets.QRadioButton(self.frame)
        self.radioButton_jtg.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.radioButton_jtg.setChecked(True)
        self.radioButton_jtg.setObjectName("radioButton_jtg")
        self.horizontalLayout_7.addWidget(self.radioButton_jtg)
        self.radioButton_gtj = QtWidgets.QRadioButton(self.frame)
        self.radioButton_gtj.setStyleSheet("border: none;\n"
"color: rgb(54, 202, 172);")
        self.radioButton_gtj.setObjectName("radioButton_gtj")
        self.horizontalLayout_7.addWidget(self.radioButton_gtj)
        self.verticalLayout_10.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_works)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setContentsMargins(25, 0, 25, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_clc = QtWidgets.QPushButton(self.frame_2)
        self.btn_clc.setMaximumSize(QtCore.QSize(150, 30))
        self.btn_clc.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(254, 188, 69);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(254, 188, 69, 150);\n"
"}")
        self.btn_clc.setObjectName("btn_clc")
        self.horizontalLayout_8.addWidget(self.btn_clc)
        self.verticalLayout_10.addWidget(self.frame_2)
        self.horizontalLayout_6.addWidget(self.frame_works)
        self.verticalLayout_8.addWidget(self.frame_output)
        self.verticalLayout_4.addWidget(self.frame_content_home)
        self.stackedWidget.addWidget(self.page_home)
        self.page_credits = QtWidgets.QWidget()
        self.page_credits.setObjectName("page_credits")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_credits)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_content_credits = QtWidgets.QFrame(self.page_credits)
        self.frame_content_credits.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_credits.setObjectName("frame_content_credits")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_content_credits)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_3 = QtWidgets.QFrame(self.frame_content_credits)
        self.frame_3.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(212, 212, 212);\n"
"background-color: rgb(0, 0, 100);\n"
"border-radius: 20px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_13.addWidget(self.label_7)
        self.verticalLayout_11.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(self.frame_content_credits)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(49, 206, 185);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_11.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_content_credits)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(49, 206, 185);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_content_credits)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(49, 206, 185);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.verticalLayout_12.addWidget(self.frame_content_credits)
        self.stackedWidget.addWidget(self.page_credits)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.content_bar)
        self.credits_bar = QtWidgets.QFrame(self.MainFrame)
        self.credits_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.credits_bar.setStyleSheet("background-color: none;")
        self.credits_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_bar.setObjectName("credits_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_lable_credits = QtWidgets.QFrame(self.credits_bar)
        self.frame_lable_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lable_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lable_credits.setObjectName("frame_lable_credits")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_lable_credits)
        self.horizontalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_credits = QtWidgets.QLabel(self.frame_lable_credits)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(128, 102, 168);")
        self.label_credits.setObjectName("label_credits")
        self.horizontalLayout_3.addWidget(self.label_credits)
        self.horizontalLayout_2.addWidget(self.frame_lable_credits)
        self.frame_grip = QtWidgets.QFrame(self.credits_bar)
        self.frame_grip.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setStyleSheet("padding: 5px;")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_grip)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.btn_help = QtWidgets.QPushButton(self.frame_grip)
        self.btn_help.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_help.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_help.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(120, 90, 162);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 90, 162, 150);\n"
"}")
        self.btn_help.setText("")
        self.btn_help.setObjectName("btn_help")
        self.verticalLayout_14.addWidget(self.btn_help)
        self.horizontalLayout_2.addWidget(self.frame_grip)
        self.verticalLayout.addWidget(self.credits_bar)
        self.MainLayout.addWidget(self.MainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_clc.clicked.connect(self.calc)
        self.btn_close.clicked.connect(close)
        self.btn_maximize.clicked.connect(self.maximized)
        self.btn_minimize.clicked.connect(MainWindow.showMinimized)
        self.btn_help.clicked.connect(self.help_page)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Date Converter"))
        self.label.setText(_translate("MainWindow", "ENTER YEAR"))
        self.label_2.setText(_translate("MainWindow", "Example: 1980 OR 1399"))
        self.label_3.setText(_translate("MainWindow", "ENTER MONTH"))
        self.label_4.setText(_translate("MainWindow", "Example: 5"))
        self.label_5.setText(_translate("MainWindow", "ENTER DAY"))
        self.label_6.setText(_translate("MainWindow", "Example: 3"))
        self.label_year.setText(_translate("MainWindow", "Year:"))
        self.label_month.setText(_translate("MainWindow", "Month:"))
        self.label_day.setText(_translate("MainWindow", "Day:"))
        self.label_dow.setText(_translate("MainWindow", "DoW:"))
        self.radioButton_jtg.setText(_translate("MainWindow", " Jalali to Gregorian"))
        self.radioButton_gtj.setText(_translate("MainWindow", " Gregorian to Jalali"))
        self.btn_clc.setText(_translate("MainWindow", "Calculate"))
        self.label_7.setText(_translate("MainWindow", "\"If you control the code, you control the world.\""))
        self.label_8.setText(_translate("MainWindow", "Iranian Calendar (Jalali Calendar)\n"
"The Iranian calendar (also known as Persian calendar or the Jalaali Calendar) is a solar calendar currently used\n"
"in Iran and Afghanistan. It is observation-based, rather than rule-based, beginning each year on the vernal equinox\n"
"as precisely determined by astronomical observations from Tehran. "))
        self.label_9.setText(_translate("MainWindow", "Gregorian Calendar\n"
"The Gregorian calendar is the calendar that is used nearly everywhere in the world. A modification of the Julian\n"
"calendar, it was first proposed by the Neapolitan doctor Aloysius Lilius, and was decreed by Pope Gregory XIII, for\n"
"whom it was named, on 24 February 1582. "))
        self.label_10.setText(_translate("MainWindow", "Developer: Kia Hamedi\n"
"Email: Kia.arta9793@gmail.com\n"
"Website: www.kiahamedi.ir\n"
"Github: https://github.com/kiahamedi"))
        self.label_credits.setText(_translate("MainWindow", "By: Kia Hamedi"))

    def maximized(self):
        if self.windowState() & Qt.WindowMaximized:
            self.showNormal()
        else:
            self.showMaximized()

    def help_page(self):
        if self.stackedWidget.currentIndex() == 0:
            self.stackedWidget.setCurrentIndex(1)
        elif self.stackedWidget.currentIndex() == 1:
            self.stackedWidget.setCurrentIndex(0)

    def calc(self):
        year = self.edt_year.text()
        month = self.edt_month.text()
        day = self.edt_day.text()
        if year and month and day:
            if self.radioButton_jtg.isChecked():
                months = ['January','February','March','April','May','June','July','August','September','October','November','December']
                DayL = ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']
                newd = jalali.Persian((int(year), int(month), int(day))).gregorian_tuple()
                self.label_year.setText("Year:            " + str(newd[0]))
                self.label_month.setText("Month:            " + str(newd[1]) + " / "+ months[int(str(newd[1]))-1])
                self.label_day.setText("Day:            " + str(newd[2]))
                self.label_dow.setText("DoW:            " + str(DayL[datetime.date(newd[0],newd[1],newd[2]).weekday()]))
            elif self.radioButton_gtj.isChecked():
                months = ['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand']
                DayL = ['Do Shanbe','Se Shanbe','Chahar Shanbe','Panj Shanbe','Jome','Shanbe','Yek Shanbe']
                newd = jalali.Gregorian((int(year), int(month), int(day))).persian_tuple()
                self.label_year.setText("Year:            " + str(newd[0]))
                self.label_month.setText("Month:            " + str(newd[1]) + " / "+ months[int(str(newd[1]))-1])
                self.label_day.setText("Day:            " + str(newd[2]))
                self.label_dow.setText("DoW:             " + str(DayL[datetime.date(int(year),int(month),int(day)).weekday()]))

 

class MyApplication(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())
    sys.exit(app.exec_())

