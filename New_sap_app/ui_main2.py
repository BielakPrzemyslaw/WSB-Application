# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_interface_2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(829, 594)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(0,0,0,0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 33))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_sap = QPushButton(self.frame)
        self.btn_sap.setObjectName(u"btn_sap")
        self.btn_sap.setMinimumSize(QSize(0, 33))
        self.btn_sap.setFont(font)
        self.btn_sap.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_sap)

        self.btn_simi = QPushButton(self.frame)
        self.btn_simi.setObjectName(u"btn_simi")
        self.btn_simi.setMinimumSize(QSize(0, 33))
        self.btn_simi.setFont(font)
        self.btn_simi.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_simi)

        self.btn_nx = QPushButton(self.frame)
        self.btn_nx.setObjectName(u"btn_nx")
        self.btn_nx.setMinimumSize(QSize(0, 33))
        self.btn_nx.setFont(font)
        self.btn_nx.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_nx)


        self.verticalLayout.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.Pages.addWidget(self.pg_home)
        self.pg_sap = QWidget()
        self.pg_sap.setObjectName(u"pg_sap")
        self.frame_2 = QFrame(self.pg_sap)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(620, 20, 141, 471))
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: black;	\n"
"	background-color: rgb(248, 248, 248);\n"
"	border-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(207, 0, 0);\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_login = QPushButton(self.frame_2)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(100, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_login)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_close = QPushButton(self.frame_2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setEnabled(True)
        self.btn_close.setMinimumSize(QSize(0, 30))
        self.btn_close.setFont(font1)
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_close)

        self.layoutWidget = QWidget(self.pg_sap)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 581, 35))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.txt_file = QLineEdit(self.layoutWidget)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setFont(font)
        self.txt_file.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_file.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.txt_file)

        self.btn_select = QPushButton(self.layoutWidget)
        self.btn_select.setObjectName(u"btn_select")
        self.btn_select.setMinimumSize(QSize(120, 33))
        font2 = QFont()
        font2.setPointSize(8)
        self.btn_select.setFont(font2)
        self.btn_select.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: black;	\n"
"	background-color: rgb(248, 248, 248);\n"
"	border-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(207, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_select)

        self.label_4 = QLabel(self.pg_sap)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 325, 561, 161))
        self.layoutWidget_2 = QWidget(self.pg_sap)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 20, 451, 35))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.txt_part_name = QLineEdit(self.layoutWidget_2)
        self.txt_part_name.setObjectName(u"txt_part_name")
        self.txt_part_name.setFont(font)
        self.txt_part_name.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_part_name.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.txt_part_name)

        self.frame_3 = QFrame(self.pg_sap)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 100, 71, 50))
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: black;	\n"
"	background-color: rgb(248, 248, 248);\n"
"	border-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(207, 0, 0);\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_export = QPushButton(self.frame_3)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setGeometry(QRect(0, 10, 71, 30))
        self.btn_export.setMinimumSize(QSize(0, 30))
        self.btn_export.setFont(font1)
        self.btn_export.setCursor(QCursor(Qt.PointingHandCursor))
        self.layoutWidget_3 = QWidget(self.pg_sap)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 170, 451, 35))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.txt_part_traveler = QLineEdit(self.layoutWidget_3)
        self.txt_part_traveler.setObjectName(u"txt_part_traveler")
        self.txt_part_traveler.setFont(font)
        self.txt_part_traveler.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_part_traveler.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.txt_part_traveler)

        self.layoutWidget_4 = QWidget(self.pg_sap)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 210, 581, 35))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.txt_file_traveler = QLineEdit(self.layoutWidget_4)
        self.txt_file_traveler.setObjectName(u"txt_file_traveler")
        self.txt_file_traveler.setFont(font)
        self.txt_file_traveler.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_file_traveler.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.txt_file_traveler)

        self.btn_select_traveler = QPushButton(self.layoutWidget_4)
        self.btn_select_traveler.setObjectName(u"btn_select_traveler")
        self.btn_select_traveler.setMinimumSize(QSize(120, 33))
        self.btn_select_traveler.setFont(font2)
        self.btn_select_traveler.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: black;	\n"
"	background-color: rgb(248, 248, 248);\n"
"	border-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(207, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_select_traveler)

        self.frame_4 = QFrame(self.pg_sap)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 250, 71, 50))
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: black;	\n"
"	background-color: rgb(248, 248, 248);\n"
"	border-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(207, 0, 0);\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btn_export_traveler = QPushButton(self.frame_4)
        self.btn_export_traveler.setObjectName(u"btn_export_traveler")
        self.btn_export_traveler.setGeometry(QRect(0, 10, 71, 30))
        self.btn_export_traveler.setMinimumSize(QSize(0, 30))
        self.btn_export_traveler.setFont(font1)
        self.btn_export_traveler.setCursor(QCursor(Qt.PointingHandCursor))
        self.Pages.addWidget(self.pg_sap)
        self.pg_simi = QWidget()
        self.pg_simi.setObjectName(u"pg_simi")
        self.layoutWidget_5 = QWidget(self.pg_simi)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 20, 451, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.txt_simi_operation_number = QLineEdit(self.layoutWidget_5)
        self.txt_simi_operation_number.setObjectName(u"txt_simi_operation_number")
        self.txt_simi_operation_number.setFont(font)
        self.txt_simi_operation_number.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_simi_operation_number.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.txt_simi_operation_number)

        self.layoutWidget_6 = QWidget(self.pg_simi)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 60, 451, 35))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.txt_simi_operation_name = QLineEdit(self.layoutWidget_6)
        self.txt_simi_operation_name.setObjectName(u"txt_simi_operation_name")
        self.txt_simi_operation_name.setFont(font)
        self.txt_simi_operation_name.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_simi_operation_name.setReadOnly(False)

        self.horizontalLayout_7.addWidget(self.txt_simi_operation_name)

        self.layoutWidget_7 = QWidget(self.pg_simi)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(10, 100, 451, 35))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.txt_simi_operation_wc = QLineEdit(self.layoutWidget_7)
        self.txt_simi_operation_wc.setObjectName(u"txt_simi_operation_wc")
        self.txt_simi_operation_wc.setFont(font)
        self.txt_simi_operation_wc.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_simi_operation_wc.setReadOnly(False)

        self.horizontalLayout_8.addWidget(self.txt_simi_operation_wc)

        self.layoutWidget_8 = QWidget(self.pg_simi)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(10, 140, 451, 35))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.txt_simi_part_number = QLineEdit(self.layoutWidget_8)
        self.txt_simi_part_number.setObjectName(u"txt_simi_part_number")
        self.txt_simi_part_number.setFont(font)
        self.txt_simi_part_number.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_simi_part_number.setReadOnly(False)

        self.horizontalLayout_9.addWidget(self.txt_simi_part_number)

        self.layoutWidget_9 = QWidget(self.pg_simi)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(10, 180, 451, 35))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.txt_simi_operation_rev = QLineEdit(self.layoutWidget_9)
        self.txt_simi_operation_rev.setObjectName(u"txt_simi_operation_rev")
        self.txt_simi_operation_rev.setFont(font)
        self.txt_simi_operation_rev.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_simi_operation_rev.setReadOnly(False)

        self.horizontalLayout_10.addWidget(self.txt_simi_operation_rev)

        self.frame_5 = QFrame(self.pg_simi)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 220, 201, 50))
        self.frame_5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: black;	\n"
"	background-color: rgb(248, 248, 248);\n"
"	border-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(207, 0, 0);\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_simi_update_operation = QPushButton(self.frame_5)
        self.btn_simi_update_operation.setObjectName(u"btn_simi_update_operation")
        self.btn_simi_update_operation.setMinimumSize(QSize(0, 30))
        self.btn_simi_update_operation.setFont(font1)
        self.btn_simi_update_operation.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_simi_update_operation)

        self.Pages.addWidget(self.pg_simi)
        self.pg_nx = QWidget()
        self.pg_nx.setObjectName(u"pg_nx")
        self.label_3 = QLabel(self.pg_nx)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 311, 31))
        self.frame_6 = QFrame(self.pg_nx)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 100, 201, 50))
        self.frame_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: black;	\n"
"	background-color: rgb(248, 248, 248);\n"
"	border-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(207, 0, 0);\n"
"\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_update_template = QPushButton(self.frame_6)
        self.btn_update_template.setObjectName(u"btn_update_template")
        self.btn_update_template.setMinimumSize(QSize(0, 30))
        self.btn_update_template.setFont(font1)
        self.btn_update_template.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.btn_update_template)

        self.layoutWidget_10 = QWidget(self.pg_nx)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(0, 70, 581, 35))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.txt_nx_file = QLineEdit(self.layoutWidget_10)
        self.txt_nx_file.setObjectName(u"txt_nx_file")
        self.txt_nx_file.setFont(font)
        self.txt_nx_file.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_nx_file.setReadOnly(False)

        self.horizontalLayout_13.addWidget(self.txt_nx_file)

        self.btn_select_2 = QPushButton(self.layoutWidget_10)
        self.btn_select_2.setObjectName(u"btn_select_2")
        self.btn_select_2.setMinimumSize(QSize(120, 33))
        self.btn_select_2.setFont(font2)
        self.btn_select_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: black;	\n"
"	background-color: rgb(248, 248, 248);\n"
"	border-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(207, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_select_2)

        self.Pages.addWidget(self.pg_nx)

        self.verticalLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_sap.setText(QCoreApplication.translate("MainWindow", u"SAP", None))
        self.btn_simi.setText(QCoreApplication.translate("MainWindow", u"SIMI", None))
        self.btn_nx.setText(QCoreApplication.translate("MainWindow", u"NX Siemens", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Home</span></p></body></html>", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"SAP Login", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"Close SAP", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select target to export folder locations", None))
        self.btn_select.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.label_4.setText("")
        self.txt_part_name.setText("")
        self.txt_part_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select part number routing to export", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.txt_part_traveler.setText("")
        self.txt_part_traveler.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select traveler number routing to export", None))
        self.txt_file_traveler.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select target to export folder locations", None))
        self.btn_select_traveler.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.btn_export_traveler.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.txt_simi_operation_number.setText("")
        self.txt_simi_operation_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Operation number", None))
        self.txt_simi_operation_name.setText("")
        self.txt_simi_operation_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Operation description", None))
        self.txt_simi_operation_wc.setText("")
        self.txt_simi_operation_wc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Works Center", None))
        self.txt_simi_part_number.setText("")
        self.txt_simi_part_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Part number", None))
        self.txt_simi_operation_rev.setText("")
        self.txt_simi_operation_rev.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Operation revision", None))
        self.btn_simi_update_operation.setText(QCoreApplication.translate("MainWindow", u"Update Operation", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">NX 2206 UPPDATE</span></p></body></html>", None))
        self.btn_update_template.setText(QCoreApplication.translate("MainWindow", u"Update template", None))
        self.txt_nx_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select target to export folder locations", None))
        self.btn_select_2.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
    # retranslateUi

