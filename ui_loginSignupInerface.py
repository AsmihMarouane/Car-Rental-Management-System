# -*- coding: utf-8 -*-
import PySide2
################################################################################
## Form generated from reading UI file 'loginSignupInterfaceJfeIjt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Custom_Widgets.Widgets import QCustomStackedWidget
from dataBaseLogin import *
from users import *
import pyautogui
import os
import subprocess
import ressourceLogin_rc
import json
import re
from PyQt5.QtGui import QRegExpValidator
users=User()
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(623, 558)
        Form.setStyleSheet(u"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 700, 700))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(700, 700))
        self.widget.setMaximumSize(QSize(700, 700))
        self.widget.setStyleSheet(u"QPushButton#loginBtn,#signupBtn{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#loginBtn:hover,#signupBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 112, 226));\n"
"}\n"
"QPushButton#loginBtn:pressed,#signupBtn:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"QPushButton#createNewAccBtn{\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#createNewAccBtn:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color:rgba(91, 88, 53, 255);\n"
"}\n"
"QPushButton#signinBtn{\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#signinBtn:pressed{\n"
"	padding-left:5px;\n"
"	paddin"
                        "g-top:5px;\n"
"	color:rgba(91, 88, 53, 255);\n"
"}")
        self.loginSignup = QCustomStackedWidget(self.widget)
        self.loginSignup.setObjectName(u"loginSignup")
        self.loginSignup.setGeometry(QRect(0, 0, 800, 800))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loginSignup.sizePolicy().hasHeightForWidth())
        self.loginSignup.setSizePolicy(sizePolicy1)
        self.loginSignup.setMinimumSize(QSize(800, 800))
        self.loginSignup.setMaximumSize(QSize(800, 800))
        self.pageLogin = QWidget()
        self.pageLogin.setObjectName(u"pageLogin")
        sizePolicy1.setHeightForWidth(self.pageLogin.sizePolicy().hasHeightForWidth())
        self.pageLogin.setSizePolicy(sizePolicy1)
        self.pageLogin.setMinimumSize(QSize(800, 800))
        self.pageLogin.setMaximumSize(QSize(800, 800))
        self.pageLogin.setStyleSheet(u"")
        self.label_6 = QLabel(self.pageLogin)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 30, 280, 430))
        self.label_6.setStyleSheet(u"border-image: url(:/images/ULD60viV.png);\n"
"border-top-left-radius:50px;")
        self.label_7 = QLabel(self.pageLogin)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 30, 280, 430))
        self.label_7.setStyleSheet(u"background-color:rgba(255, 255, 255, 60);\n"
"border-top-left-radius:50px;")
        self.label_8 = QLabel(self.pageLogin)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(270, 30, 240, 430))
        self.label_8.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-bottom-right-radius:50px;")
        self.label_9 = QLabel(self.pageLogin)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(331, 80, 90, 40))
        self.label_9.setMinimumSize(QSize(90, 40))
        self.label_9.setMaximumSize(QSize(90, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color:rgba(0, 0, 0, 200)")
        self.lineEdit_3 = QLineEdit(self.pageLogin)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(295, 150, 190, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_4 = QLineEdit(self.pageLogin)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(295, 215, 190, 40))
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.loginBtn = QPushButton(self.pageLogin)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(295, 295, 190, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.loginBtn.setFont(font2)
        self.loginBtn.setAutoDefault(False)
        self.horizontalLayoutWidget_2 = QWidget(self.pageLogin)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(300, 340, 181, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color:rgba(0, 0, 0, 210)")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.createNewAccBtn = QPushButton(self.horizontalLayoutWidget_2)
        self.createNewAccBtn.setObjectName(u"createNewAccBtn")
        self.createNewAccBtn.setMinimumSize(QSize(30, 30))
        self.createNewAccBtn.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icons/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.createNewAccBtn.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.createNewAccBtn)

        self.horizontalLayoutWidget = QWidget(self.pageLogin)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(448, 10, 61, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minimiseBtn = QPushButton(self.horizontalLayoutWidget)
        self.minimiseBtn.setObjectName(u"minimiseBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimiseBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.minimiseBtn, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.closeBtn = QPushButton(self.horizontalLayoutWidget)
        self.closeBtn.setObjectName(u"closeBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.closeBtn, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.loginSignup.addWidget(self.pageLogin)
        self.pageSignUp = QWidget()
        self.pageSignUp.setObjectName(u"pageSignUp")
        self.label_11 = QLabel(self.pageSignUp)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 30, 280, 430))
        self.label_11.setStyleSheet(u"border-image: url(:/images/ULD60viV.png);\n"
"border-top-left-radius:50px;\n"
"")
        self.label_12 = QLabel(self.pageSignUp)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 30, 280, 430))
        self.label_12.setStyleSheet(u"background-color:rgba(255, 255, 255, 60);\n"
"border-top-left-radius:50px;")
        self.label_13 = QLabel(self.pageSignUp)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(270, 30, 240, 430))
        self.label_13.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-bottom-right-radius:50px;")
        self.lineEdit_5 = QLineEdit(self.pageSignUp)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(295, 150, 190, 40))
        self.lineEdit_5.setFont(font1)
        self.lineEdit_5.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.label_14 = QLabel(self.pageSignUp)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(340, 80, 120, 40))
        self.label_14.setMinimumSize(QSize(120, 40))
        self.label_14.setMaximumSize(QSize(120, 40))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"color:rgba(0, 0, 0, 200)")
        self.lineEdit_6 = QLineEdit(self.pageSignUp)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(295, 210, 190, 40))
        self.lineEdit_6.setFont(font1)
        self.lineEdit_6.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_7 = QLineEdit(self.pageSignUp)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(295, 270, 190, 40))
        self.lineEdit_7.setFont(font1)
        self.lineEdit_7.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_7.setEchoMode(QLineEdit.Password)
        self.signupBtn = QPushButton(self.pageSignUp)
        self.signupBtn.setObjectName(u"signupBtn")
        self.signupBtn.setGeometry(QRect(295, 330, 190, 40))
        self.signupBtn.setFont(font2)
        self.horizontalLayoutWidget_3 = QWidget(self.pageSignUp)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(280, 390, 221, 52))
        self.verticalLayout = QVBoxLayout(self.horizontalLayoutWidget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.horizontalLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color:rgba(0, 0, 0, 210)")

        self.verticalLayout.addWidget(self.label_15)

        self.signinBtn = QPushButton(self.horizontalLayoutWidget_3)
        self.signinBtn.setObjectName(u"signinBtn")
        self.signinBtn.setMinimumSize(QSize(30, 30))
        self.signinBtn.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.signinBtn.setIcon(icon3)

        self.verticalLayout.addWidget(self.signinBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.loginSignup.addWidget(self.pageSignUp)

        self.retranslateUi(Form)

        self.loginSignup.setCurrentIndex(0)
        self.signinBtn.clicked.connect(lambda: self.loginSignup.setCurrentWidget(self.pageLogin))
        self.createNewAccBtn.clicked.connect(lambda: self.loginSignup.setCurrentWidget(self.pageSignUp))
        self.closeBtn.clicked.connect(Form.close)
        self.minimiseBtn.clicked.connect(Form.showMinimized)
        QMetaObject.connectSlotsByName(Form)
    # setupUi
        users.create_table()
        self.signupBtn.clicked.connect(self.checker)
        self.loginBtn.clicked.connect(self.loginUser)


    def checker(self):
        regexUser = re.compile(r'^[a-zA-Z0-9]{8,}$')
        matchUser = regexUser.match(self.lineEdit_5.text())
        regexPassword = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$')
        matchPassword = regexPassword.match(self.lineEdit_7.text())
        regexEmail = re.compile(r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$')
        matchEmail = regexEmail.match(self.lineEdit_6.text())
        if matchUser and matchPassword and matchEmail:
            self.createUser()
        elif not matchUser:
            pyautogui.alert("Le nom d'utilisateur nécessite au moins 8 caractères. ")
        elif not matchPassword:
            pyautogui.alert("The password must contain at least one lowercase letter, one uppercase letter, one number, one special character, and be at least 8 characters long. Example: Abc123!@#")
        elif not matchEmail:
            pyautogui.alert("Email invalide")
    def createUser(self):
        username=self.lineEdit_5.text()
        if users.login_exist(username):
            users.add_user(self.lineEdit_5.text(), self.lineEdit_7.text(), self.lineEdit_6.text())
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            pyautogui.alert("Votre compte a été créé avec succès ! Vous pouvez maintenant vous connecter en utilisant vos identifiants de connexion. Si vous avez des problèmes pour vous connecter, veuillez contacter notre équipe d'assistance. Merci d'avoir choisi notre service.")
        else:
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            pyautogui.alert("Username already exists. Please choose a different one.")
    def loginUser(self):
        if self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
            username = self.lineEdit_3.text()
            password = self.lineEdit_4.text()
            if users.verify_login(username, password):
                # Login successful, open main interface
                user = username
                with open('config.json', 'w') as f:
                    json.dump({'user': user}, f)
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                pyautogui.alert("Login successful!")
                os.system('python ./main.py')
            else:
                # Login failed, display error message
                self.lineEdit_4.setText("")
                pyautogui.alert('Invalid login information')


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"Log In", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_3.setToolTip(QCoreApplication.translate("Form", u"User Name", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"  User Name", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_4.setToolTip(QCoreApplication.translate("Form", u"Password", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"  Password", None))
#if QT_CONFIG(tooltip)
        self.loginBtn.setToolTip(QCoreApplication.translate("Form", u"Login", None))
#endif // QT_CONFIG(tooltip)
        self.loginBtn.setText(QCoreApplication.translate("Form", u"L o g I n", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Create New Account :", None))
#if QT_CONFIG(tooltip)
        self.createNewAccBtn.setToolTip(QCoreApplication.translate("Form", u"Create Account", None))
#endif // QT_CONFIG(tooltip)
        self.createNewAccBtn.setText("")
        self.minimiseBtn.setText("")
        self.closeBtn.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_5.setToolTip(QCoreApplication.translate("Form", u"Add User Name", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"  User Name", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Sign Up", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_6.setToolTip(QCoreApplication.translate("Form", u"Add Email", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"  Email", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_7.setToolTip(QCoreApplication.translate("Form", u"Add Password", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Form", u"  Password", None))
#if QT_CONFIG(tooltip)
        self.signupBtn.setToolTip(QCoreApplication.translate("Form", u"Signup", None))
#endif // QT_CONFIG(tooltip)
        self.signupBtn.setText(QCoreApplication.translate("Form", u"S i g n U p", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"You already have an account please Sign in :", None))
#if QT_CONFIG(tooltip)
        self.signinBtn.setToolTip(QCoreApplication.translate("Form", u"Login", None))
#endif // QT_CONFIG(tooltip)
        self.signinBtn.setText("")
    # retranslateUi