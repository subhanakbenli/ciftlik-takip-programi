# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\suakb\supi\bionluk\çiftlik takip (bionluk tuba hanım)\ciftlik-takip-programi\ui_design\AnaSayfa.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Anasayfa_MainWindow(object):
    def setupUi(self, Anasayfa_MainWindow):
        Anasayfa_MainWindow.setObjectName("Anasayfa_MainWindow")
        Anasayfa_MainWindow.resize(1201, 610)
        Anasayfa_MainWindow.setMinimumSize(QtCore.QSize(0, 25))
        Anasayfa_MainWindow.setStyleSheet("/*\n"
"Ubuntu Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 01/10/2021 (dd/mm/yyyy), 15:18.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Ubuntu.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:rgb(211, 248, 243);\n"
"}\n"
"QCheckBox {\n"
"    padding:2px;\n"
"}\n"
"QCheckBox:hover {\n"
"    border:1px solid rgb(255,150,60);\n"
"    border-radius:4px;\n"
"    padding: 1px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border:1px solid rgb(246, 134, 86);\n"
"    border-radius:4px;\n"
"      background-color:rgb(246, 134, 86)\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-width:1px solid rgb(246, 134, 86);\n"
"    border-radius:4px;\n"
"      background-color:rgb(255,255,255);\n"
"}\n"
"QColorDialog {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QComboBox {\n"
"    color:rgb(81,72,65);\n"
"    background: #ffffff;\n"
"}\n"
"QComboBox:editable {\n"
"    selection-color:rgb(81,72,65);\n"
"    selection-background-color: #ffffff;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    selection-color: #ffffff;\n"
"    selection-background-color: rgb(246, 134, 86);\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color:  #1e1d23;    \n"
"}\n"
"QDateTimeEdit, QDateEdit, QDoubleSpinBox, QFontComboBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QDialog {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"\n"
"QLabel,QLineEdit {\n"
"    color:rgb(17,17,17);\n"
"}\n"
"QLineEdit {\n"
"    background-color:rgb(255,255,255);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QMenuBar {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item {\n"
"    padding-top:4px;\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    padding-top:2px;\n"
"    padding-left:2px;\n"
"    padding-right:2px;\n"
"    border-top-width:2px;\n"
"    border-left-width:2px;\n"
"    border-right-width:2px;\n"
"    border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"    border-style:solid;\n"
"    background-color:rgb(65,64,59);\n"
"    border-top-color: rgb(47,47,44);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"}\n"
"QMenu {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenu::item {\n"
"    color:rgb(223,219,210);\n"
"    padding:4px 10px 4px 20px;\n"
"}\n"
"QMenu::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border-style:solid;\n"
"    border-width:3px;\n"
"    padding:4px 7px 4px 17px;\n"
"    border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border: 1px solid transparent;\n"
"    color:rgb(17,17,17);\n"
"    selection-background-color:rgb(236,116,64);\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px inset rgb(150,150,150); \n"
"    border-radius: 10px;\n"
"    background-color:rgb(221,221,219);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border:1px solid;\n"
"    border-radius:8px;\n"
"    border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(65,64,59);\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-bottom-color: rgb(150,150,150);\n"
"    border-right-color: rgb(165,165,165);\n"
"    border-left-color: rgb(165,165,165);\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:default{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-width: 1px;\n"
"    border-top-color: rgba(255,150,60,200);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-bottom-color: rgba(200,70,20,200);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"    color:rgb(174,167,159);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 255));\n"
"}\n"
"QRadioButton {\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgba(246, 134, 86, 255);\n"
"    color: #a9b7c6;\n"
"    background-color:rgba(246, 134, 86, 255);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(246, 134, 86);\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QScrollArea {\n"
"    color: white;\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QSlider::groove {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal, QSlider::add-page:vertical {\n"
"     background: white;\n"
"}\n"
"QSlider::sub-page:horizontal, QSlider::sub-page:vertical {\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QStatusBar, QSpinBox {\n"
"    color:rgb(81,72,65);\n"
"}\n"
"QSpinBox {\n"
"    background-color: #ffffff;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"      border: 1px solid rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-left-radius: 7px;\n"
"      border-top-right-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"      border: 1px solid rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"      border: 1px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"      border-bottom-left-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    border: 1px transparent grey;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"     background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"} \n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid;\n"
"    border-color: rgb(207,207,207);\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-bottom-right-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"      border: 1px solid grey;\n"
"      border-bottom-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"      border: 1px solid rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"      border: 1px solid rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-left-radius: 7px;\n"
"      border-top-right-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"     height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border: 1px solid rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"    border: 1px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"      border: 1px transparent grey;\n"
"      border-bottom-left-radius: 3px;\n"
"      border-bottom-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"    border-color: rgb(180,180,180);\n"
"    background-color:rgb(247,246,246);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"    padding-bottom:2px;\n"
"    padding-top:2px;\n"
"    color:rgb(81,72,65);\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(221,218,217,255), stop:1 rgba(240,239,238,255));\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-left-color: rgb(180,180,180);\n"
"    border-right-color: rgb(180,180,180);\n"
"    border-bottom-color: transparent;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      background-color:rgb(247,246,246);\n"
"      margin-left: 0px;\n"
"      margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:transparent;\n"
"    color:rgb(17,17,17);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QTimeEdit, QToolBox, QToolBox::tab, QToolBox::tab:selected {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Anasayfa_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 1)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uygunHayvanListele_pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uygunHayvanListele_pushButton.sizePolicy().hasHeightForWidth())
        self.uygunHayvanListele_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.uygunHayvanListele_pushButton.setFont(font)
        self.uygunHayvanListele_pushButton.setStyleSheet("background-color:rgb(255, 196, 255)")
        self.uygunHayvanListele_pushButton.setObjectName("uygunHayvanListele_pushButton")
        self.horizontalLayout.addWidget(self.uygunHayvanListele_pushButton)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.butunHayvanlariListele_pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butunHayvanlariListele_pushButton.sizePolicy().hasHeightForWidth())
        self.butunHayvanlariListele_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.butunHayvanlariListele_pushButton.setFont(font)
        self.butunHayvanlariListele_pushButton.setStyleSheet("background-color:rgb(145, 196, 65)")
        self.butunHayvanlariListele_pushButton.setObjectName("butunHayvanlariListele_pushButton")
        self.horizontalLayout.addWidget(self.butunHayvanlariListele_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.icerde_checkBox = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.icerde_checkBox.setFont(font)
        self.icerde_checkBox.setChecked(True)
        self.icerde_checkBox.setObjectName("icerde_checkBox")
        self.horizontalLayout_8.addWidget(self.icerde_checkBox)
        self.disarida_checkBox = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.disarida_checkBox.setFont(font)
        self.disarida_checkBox.setChecked(True)
        self.disarida_checkBox.setObjectName("disarida_checkBox")
        self.horizontalLayout_8.addWidget(self.disarida_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.disi_checkBox = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.disi_checkBox.setFont(font)
        self.disi_checkBox.setChecked(True)
        self.disi_checkBox.setObjectName("disi_checkBox")
        self.horizontalLayout_9.addWidget(self.disi_checkBox)
        self.erkek_checkBox = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.erkek_checkBox.setFont(font)
        self.erkek_checkBox.setChecked(True)
        self.erkek_checkBox.setObjectName("erkek_checkBox")
        self.horizontalLayout_9.addWidget(self.erkek_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.kimlikNo_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kimlikNo_lineEdit.sizePolicy().hasHeightForWidth())
        self.kimlikNo_lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kimlikNo_lineEdit.setFont(font)
        self.kimlikNo_lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.kimlikNo_lineEdit.setInputMask("")
        self.kimlikNo_lineEdit.setObjectName("kimlikNo_lineEdit")
        self.horizontalLayout_3.addWidget(self.kimlikNo_lineEdit)
        self.kimlikNoAra_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kimlikNoAra_pushButton.sizePolicy().hasHeightForWidth())
        self.kimlikNoAra_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.kimlikNoAra_pushButton.setFont(font)
        self.kimlikNoAra_pushButton.setStyleSheet("background-color:rgb(189, 255, 200)")
        self.kimlikNoAra_pushButton.setObjectName("kimlikNoAra_pushButton")
        self.horizontalLayout_3.addWidget(self.kimlikNoAra_pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.QrOkut_giris = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QrOkut_giris.sizePolicy().hasHeightForWidth())
        self.QrOkut_giris.setSizePolicy(sizePolicy)
        self.QrOkut_giris.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.QrOkut_giris.setFont(font)
        self.QrOkut_giris.setStyleSheet("background-color:rgb(45, 246, 65)")
        self.QrOkut_giris.setObjectName("QrOkut_giris")
        self.horizontalLayout_6.addWidget(self.QrOkut_giris)
        self.QrOkut_cikis = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QrOkut_cikis.sizePolicy().hasHeightForWidth())
        self.QrOkut_cikis.setSizePolicy(sizePolicy)
        self.QrOkut_cikis.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.QrOkut_cikis.setFont(font)
        self.QrOkut_cikis.setStyleSheet("background-color:rgb(245, 66, 45)")
        self.QrOkut_cikis.setObjectName("QrOkut_cikis")
        self.horizontalLayout_6.addWidget(self.QrOkut_cikis)
        spacerItem2 = QtWidgets.QSpacerItem(25, 45, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.hayvanEkle_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hayvanEkle_pushButton.sizePolicy().hasHeightForWidth())
        self.hayvanEkle_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.hayvanEkle_pushButton.setFont(font)
        self.hayvanEkle_pushButton.setStyleSheet("background-color:rgb(245, 196, 155)")
        self.hayvanEkle_pushButton.setObjectName("hayvanEkle_pushButton")
        self.horizontalLayout_6.addWidget(self.hayvanEkle_pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(2, 4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(145)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(27)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 3)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        Anasayfa_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Anasayfa_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 25))
        self.menubar.setObjectName("menubar")
        Anasayfa_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Anasayfa_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Anasayfa_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Anasayfa_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Anasayfa_MainWindow)

    def retranslateUi(self, Anasayfa_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Anasayfa_MainWindow.setWindowTitle(_translate("Anasayfa_MainWindow", "Çiftlik Takip Programı"))
        self.uygunHayvanListele_pushButton.setText(_translate("Anasayfa_MainWindow", "Uygun \n"
"Hayvanları Listele"))
        self.butunHayvanlariListele_pushButton.setText(_translate("Anasayfa_MainWindow", "Bütün Hayvanları Listele"))
        self.icerde_checkBox.setText(_translate("Anasayfa_MainWindow", "İçerde"))
        self.disarida_checkBox.setText(_translate("Anasayfa_MainWindow", "Dışarıda"))
        self.disi_checkBox.setText(_translate("Anasayfa_MainWindow", "Dişi"))
        self.erkek_checkBox.setText(_translate("Anasayfa_MainWindow", "Erkek"))
        self.label_5.setText(_translate("Anasayfa_MainWindow", "Kimlik No:"))
        self.kimlikNoAra_pushButton.setText(_translate("Anasayfa_MainWindow", "Kimlik No ile Ara"))
        self.QrOkut_giris.setText(_translate("Anasayfa_MainWindow", "Giriş"))
        self.QrOkut_cikis.setText(_translate("Anasayfa_MainWindow", "Çıkış"))
        self.hayvanEkle_pushButton.setText(_translate("Anasayfa_MainWindow", "Hayvan Ekle"))
        self.groupBox_2.setTitle(_translate("Anasayfa_MainWindow", "Hayvanlar"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Anasayfa_MainWindow", "Kimlik No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Anasayfa_MainWindow", "Cins"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Anasayfa_MainWindow", "Cinsiyet"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Anasayfa_MainWindow", "Doğum Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Anasayfa_MainWindow", "Ağırlık "))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Anasayfa_MainWindow", "Sağlık"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Anasayfa_MainWindow", "Konum"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Anasayfa_MainWindow", "Sil"))