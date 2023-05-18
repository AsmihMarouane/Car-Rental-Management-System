from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget
from users import *
import mysql.connector
import json
import resources_rc
from cars import *

with open('config.json', 'r') as f:
    config = json.load(f)
    username = config['user']

user = User(username)
dataUser = user.get_user(username)

car=Car()

print(dataUser)
print(dataUser['user_type'])


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(937, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"*{\n"
                                 "border:none;\n"
                                 "background-color:transparent;\n"
                                 "background:transparent;\n"
                                 "padding:0;\n"
                                 "margin:0;\n"
                                 "color:#fff;\n"
                                 "}\n"
                                 "#centralwidget{\n"
                                 "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.663636 rgba(44, 47, 72, 255), stop:1 rgba(140, 131, 131, 255))\n"
                                 "}\n"
                                 "#leftMenuSubContainer{\n"
                                 "background-color:#1d203e;\n"
                                 "}\n"
                                 "#leftMenuSubContainer,QPushButton{\n"
                                 "text-align:left;\n"
                                 "padding:5px 10px;\n"
                                 "border-top-left-radius:10px;\n"
                                 "border-bottom-left-radius:10px;\n"
                                 "}\n"
                                 "#centerMenuSubContainer,#rightMenuSubContainer{\n"
                                 "	background-color:#2C2F48;\n"
                                 "}\n"
                                 "#frame_4,#frame_8,#popupNotificationSubContainer{\n"
                                 "background-color:#1D203E;\n"
                                 "border-radius:10px;\n"
                                 "}\n"
                                 "#headerContainer,#footerContainer{\n"
                                 "background-color:#2C2F48;\n"
                                 "}\n"

                                 "#card1,#card2,#card3{\n"
                                 "background-color:#1D203E;\n"
                                 "border-radius:10px;\n"
                                 "}\n"
                                 "#cardinfo1,#cardinfo2,#cardinfo3,#cardinfo4{\n"
                                 "background-color:#1D203E;\n"
                                 "border-radius:10px;\n"
                                 "}\n"
                                 "#cardCar1,#cardCar2,#cardCar3,#cardCar4,#cardCar5,#cardCar6,#cardCar7,#cardCar8,#cardCar9,#cardCar10,#cardCar11,#cardCar12,#cardCar13,#cardCar14,#cardCar15,#cardCar16,#cardCar17,#cardCar18,#cardCar19,#cardCar20,#cardCar21,#cardCar22{\n"
                                 "b"
                                 "ackground-color:#1D203E;\n"
                                 "border-radius:10px;\n"
                                 "}\n"
                                 "#carSpec1,#carSpec2,#carSpec3,#carSpec4,#carSpec5,#carSpec6,#carSpec7,#carSpec8,#carSpec9,#carSpec10,#carSpec11,#carSpec12,#carSpec13,#carSpec14,#carSpec15,#carSpec16,#carSpec17,#carSpec18,#carSpec19,#carSpec20{\n"
                                 "background-color:#1D203E;\n"
                                 "border-radius:10px;\n"
                                 "}\n"
                                 "#profilePicture{\n"
                                 "}\n"
                                 "#lineEdit,#lineEdit_1,#lineEdit_2,#lineEdit_3,#lineEdit_4,#lineEdit_5,#lineEdit_6,#lineEdit_7,#tableWidget,#lineEdit_8,#lineEdit_9,#lineEdit_10,#lineEdit_11,#lineEdit_12,#lineEdit_13,#lineEdit_14{\n"
                                 "	background-color:rgb(255, 255, 255);\n"
                                 "	color:rgb(121, 121, 121);\n"
                                 "	border-radius:5px;\n"
                                 "}\n"
                                 "#deleteAllBtn:pressed,#valideBtn:pressed{\n"
                                 "	padding-left:5px;\n"
                                 "	padding-top:5px;\n"
                                 "	background-color:rgba(150, 123, 111, 255);\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_25 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame_3)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"background-color: #1f232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon2)
        self.dataBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.reportBtn = QPushButton(self.frame_2)
        self.reportBtn.setObjectName(u"reportBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reportBtn.setIcon(icon3)
        self.reportBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.reportBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingBtn = QPushButton(self.frame)
        self.settingBtn.setObjectName(u"settingBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon4)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingBtn)

        self.infoBtn = QPushButton(self.frame)
        self.infoBtn.setObjectName(u"infoBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame)
        self.helpBtn.setObjectName(u"helpBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout_25.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.closeCenterMenu = QPushButton(self.frame_4)
        self.closeCenterMenu.setObjectName(u"closeCenterMenu")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenu.setIcon(icon7)
        self.closeCenterMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.closeCenterMenu, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        font = QFont()
        font.setPointSize(13)
        self.centerMenuPages.setFont(font)
        self.centerMenuPages.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.centerMenuPages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(13)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.page_3)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout_25.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        sizePolicy2.setHeightForWidth(self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy2)
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(150, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QSize(100, 40))
        self.label_5.setPixmap(QPixmap(u":/image/1.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon8)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn, 0, Qt.AlignHCenter)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon9)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon10)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon11)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon13)

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy3)
        self.mainBodyContent.setMinimumSize(QSize(594, 562))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        sizePolicy.setHeightForWidth(self.mainPages.sizePolicy().hasHeightForWidth())
        self.mainPages.setSizePolicy(sizePolicy)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_16 = QVBoxLayout(self.page_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.Home = QLabel(self.page_6)
        self.Home.setObjectName(u"Home")
        self.Home.setFont(font1)
        self.Home.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.Home, 0, Qt.AlignTop)

        self.cardsFrame = QWidget(self.page_6)
        self.cardsFrame.setObjectName(u"cardsFrame")
        self.horizontalLayout_13 = QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.card2 = QFrame(self.cardsFrame)
        self.card2.setObjectName(u"card2")
        self.card2.setMaximumSize(QSize(250, 250))
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.card2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_12 = QFrame(self.card2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_20.setFont(font3)

        self.horizontalLayout_15.addWidget(self.label_20)

        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(40, 40))
        self.label_15.setPixmap(QPixmap(u":/icons/icons/sidebar.svg"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_15, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_21.addWidget(self.frame_12)

        self.label_17 = QLabel(self.card2)
        self.label_17.setObjectName(u"label_17")
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_17.setFont(font4)

        self.verticalLayout_21.addWidget(self.label_17, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_13.addWidget(self.card2)

        self.card3 = QFrame(self.cardsFrame)
        self.card3.setObjectName(u"card3")
        self.card3.setMaximumSize(QSize(250, 250))
        self.card3.setFrameShape(QFrame.StyledPanel)
        self.card3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.card3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_13 = QFrame(self.card3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.horizontalLayout_16.addWidget(self.label_21)

        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(40, 40))
        self.label_18.setPixmap(QPixmap(u":/icons/icons/shopping-bag.svg"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_18, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.frame_13)

        self.label_19 = QLabel(self.card3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)

        self.verticalLayout_23.addWidget(self.label_19, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_13.addWidget(self.card3)


        self.verticalLayout_16.addWidget(self.cardsFrame, 0, Qt.AlignTop)

        self.cardsFrameInfo = QWidget(self.page_6)
        self.cardsFrameInfo.setObjectName(u"cardsFrameInfo")
        self.horizontalLayout_14 = QHBoxLayout(self.cardsFrameInfo)
        self.horizontalLayout_14.setSpacing(8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.cardinfo4 = QFrame(self.cardsFrameInfo)
        self.cardinfo4.setObjectName(u"cardinfo4")
        self.cardinfo4.setFrameShape(QFrame.StyledPanel)
        self.cardinfo4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.cardinfo4)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, -1, -1, -1)
        self.printInvoiceBtn = QPushButton(self.cardinfo4)
        self.printInvoiceBtn.setObjectName(u"printInvoiceBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.printInvoiceBtn.setIcon(icon14)
        self.printInvoiceBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_51.addWidget(self.printInvoiceBtn)

        self.horizontalLayout_14.addWidget(self.cardinfo4, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.printInvoiceBtn.setText(QCoreApplication.translate("MainWindow", u"Print Invoice", None))


        self.cardinfo1 = QFrame(self.cardsFrameInfo)
        self.cardinfo1.setObjectName(u"cardinfo1")
        self.cardinfo1.setMinimumSize(QSize(0, 0))
        self.cardinfo1.setMaximumSize(QSize(150, 50))
        self.cardinfo1.setFrameShape(QFrame.StyledPanel)
        self.cardinfo1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.cardinfo1)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.topDealersBtn = QPushButton(self.cardinfo1)
        self.topDealersBtn.setObjectName(u"topDealersBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.topDealersBtn.setIcon(icon14)
        self.topDealersBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_22.addWidget(self.topDealersBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_14.addWidget(self.cardinfo1)

        self.cardinfo2 = QFrame(self.cardsFrameInfo)
        self.cardinfo2.setObjectName(u"cardinfo2")
        self.cardinfo2.setMaximumSize(QSize(150, 50))
        self.cardinfo2.setFrameShape(QFrame.StyledPanel)
        self.cardinfo2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.cardinfo2)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.plansBtn = QPushButton(self.cardinfo2)
        self.plansBtn.setObjectName(u"plansBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/sidebar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.plansBtn.setIcon(icon15)
        self.plansBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_24.addWidget(self.plansBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_14.addWidget(self.cardinfo2)

        self.cardinfo3 = QFrame(self.cardsFrameInfo)
        self.cardinfo3.setObjectName(u"cardinfo3")
        self.cardinfo3.setMaximumSize(QSize(150, 50))
        self.cardinfo3.setFrameShape(QFrame.StyledPanel)
        self.cardinfo3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.cardinfo3)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gpsTrackingBtn = QPushButton(self.cardinfo3)
        self.gpsTrackingBtn.setObjectName(u"gpsTrackingBtn")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/map-pin.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gpsTrackingBtn.setIcon(icon16)
        self.gpsTrackingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_25.addWidget(self.gpsTrackingBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_14.addWidget(self.cardinfo3)


        self.verticalLayout_16.addWidget(self.cardsFrameInfo)

        self.mainPages.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_17 = QVBoxLayout(self.page_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.page_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_10, 0, Qt.AlignTop)

        self.listOfCars = QWidget(self.page_7)
        self.listOfCars.setObjectName(u"listOfCars")
        self.verticalLayout_26 = QVBoxLayout(self.listOfCars)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.listOfCars)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 421, 1218))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.listOfCarsSub = QWidget(self.scrollAreaWidgetContents)
        self.listOfCarsSub.setObjectName(u"listOfCarsSub")
        self.listOfCarsSub.setMinimumSize(QSize(0, 1200))
        self.listOfCarsSub.setStyleSheet(u"")
        self.formLayout = QFormLayout(self.listOfCarsSub)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
    ######################################################################################################
    ##########################List Of CardsCars ##########################################################

        cars = Car()
        numberOfCars = cars.get_number_of_cars()

        for x in range(numberOfCars):
            id = x + 1
            dataSet = cars.get_car(id)
            var_name = str(id)
            cardCar = f"cardCar{var_name}"
            cardCar_1 = f"cardCar{var_name}_1"
            cardCar_2 = f"cardCar{var_name}_2"
            favoriteBtn = f"favoriteBtn_{var_name}"
            SeeMoreBtn = f"SeeMore_{var_name}"
            carImage = f"carImage_{var_name}"
            self.__dict__[cardCar] = QWidget(self.listOfCarsSub)
            self.__dict__[cardCar].setObjectName(cardCar)
            self.__dict__[cardCar].setMaximumSize(QSize(200, 200))
            self.__dict__[cardCar].setStyleSheet(u"")
            self.verticalLayout.__dict__[cardCar] = QVBoxLayout(self.__dict__[cardCar])
            self.verticalLayout.__dict__[cardCar].setSpacing(0)
            self.verticalLayout.__dict__[cardCar].setObjectName(f"verticalLayout.{cardCar}")
            self.verticalLayout.__dict__[cardCar].setContentsMargins(0, 0, 0, 0)
            self.frame.__dict__[cardCar_1] = QFrame(self.__dict__[cardCar])
            self.frame.__dict__[cardCar_1].setObjectName(f"frame{cardCar_1}")
            self.frame.__dict__[cardCar_1].setFrameShape(QFrame.StyledPanel)
            self.frame.__dict__[cardCar_1].setFrameShadow(QFrame.Raised)
            self.horizontalLayout_2.__dict__[cardCar_1] = QHBoxLayout(self.frame.__dict__[cardCar_1])
            self.horizontalLayout_2.__dict__[cardCar_1].setSpacing(0)
            self.horizontalLayout_2.__dict__[cardCar_1].setObjectName(f"horizontalLayout_2{cardCar_1}")
            self.horizontalLayout_2.__dict__[cardCar_1].setContentsMargins(0, 0, 0, 0)
            self.label.__dict__[cardCar_1] = QLabel(self.frame.__dict__[cardCar_1])
            self.label.__dict__[cardCar_1].setObjectName(f"label{cardCar_1}")
            font.__dict__[cardCar] = QFont()
            font.__dict__[cardCar].setPointSize(9)
            self.label.__dict__[cardCar_1].setFont(font.__dict__[cardCar])
            self.horizontalLayout_2.__dict__[cardCar_1].addWidget(self.label.__dict__[cardCar_1], 0,Qt.AlignHCenter | Qt.AlignVCenter)
            self.__dict__[favoriteBtn] = QPushButton(self.frame.__dict__[cardCar_1])
            self.__dict__[favoriteBtn].setObjectName(f"{favoriteBtn}")
            icon.__dict__[cardCar] = QIcon()
            icon.__dict__[cardCar].addFile(u":/icons/icons/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.__dict__[favoriteBtn].setIcon(icon.__dict__[cardCar])
            self.__dict__[favoriteBtn].setIconSize(QSize(20, 20))
            self.horizontalLayout_2.__dict__[cardCar_1].addWidget(self.__dict__[favoriteBtn], 0,Qt.AlignRight | Qt.AlignVCenter)
            self.verticalLayout.__dict__[cardCar].addWidget(self.frame.__dict__[cardCar_1], 0, Qt.AlignTop)
            self.frame.__dict__[cardCar_2] = QFrame(self.__dict__[cardCar])
            self.__dict__[carImage] = QLabel(self.__dict__[cardCar])
            self.__dict__[carImage].setObjectName(f"{carImage}")
            self.__dict__[carImage].setMaximumSize(QSize(200, 200))
            self.__dict__[carImage].setPixmap(QPixmap(f":/image/{dataSet['image']}"))
            self.__dict__[carImage].setScaledContents(True)
            self.verticalLayout.__dict__[cardCar].addWidget(self.__dict__[carImage], 0, Qt.AlignHCenter)
            self.frame.__dict__[cardCar_2].setObjectName(f"frame{cardCar_2}")
            self.frame.__dict__[cardCar_2].setFrameShape(QFrame.StyledPanel)
            self.frame.__dict__[cardCar_2].setFrameShadow(QFrame.Raised)
            self.horizontalLayout_2.__dict__[cardCar_2] = QHBoxLayout(self.frame.__dict__[cardCar_2])
            self.horizontalLayout_2.__dict__[cardCar_2].setSpacing(0)
            self.horizontalLayout_2.__dict__[cardCar_2].setObjectName(f"horizontalLayout_2{cardCar_2}")
            self.horizontalLayout_2.__dict__[cardCar_2].setContentsMargins(0, 0, 0, 0)
            self.__dict__[SeeMoreBtn] = QPushButton(self.frame.__dict__[cardCar_2])
            self.__dict__[SeeMoreBtn].setObjectName(f"{SeeMoreBtn}")
            self.__dict__[SeeMoreBtn].setMinimumSize(QSize(100, 0))
            self.__dict__[SeeMoreBtn].setMaximumSize(QSize(80, 60))
            self.horizontalLayout_2.__dict__[cardCar_2].addWidget(self.__dict__[SeeMoreBtn], 0,Qt.AlignLeft | Qt.AlignVCenter)
            self.label.__dict__[cardCar_2] = QLabel(self.frame.__dict__[cardCar_2])
            self.label.__dict__[cardCar_2].setObjectName(f"label{cardCar_2}")
            self.horizontalLayout_2.__dict__[cardCar_2].addWidget(self.label.__dict__[cardCar_2], 0,Qt.AlignRight | Qt.AlignVCenter)
            self.verticalLayout.__dict__[cardCar].addWidget(self.frame.__dict__[cardCar_2])
            self.formLayout.setWidget(x, QFormLayout.FieldRole, self.__dict__[cardCar])
            self.__dict__[SeeMoreBtn].setToolTip(QCoreApplication.translate("MainWindow", u"See More ...", None))
            self.__dict__[SeeMoreBtn].setText(QCoreApplication.translate("MainWindow", u"See More ...", None))
            self.label.__dict__[cardCar_2].setText(QCoreApplication.translate("MainWindow", f"{dataSet['daily_rental_price']}\u00a3/Day", None))
            self.label.__dict__[cardCar_1].setText(QCoreApplication.translate("MainWindow", f"{dataSet['brand']} {dataSet['model']}", None))
            self.__dict__[favoriteBtn].setToolTip(QCoreApplication.translate("MainWindow", u"Add", None))
            self.__dict__[favoriteBtn].clicked.connect(lambda:self.mainPages.setCurrentIndex(4))
            car_data = cars.get_car(1)
            self.__dict__[favoriteBtn].clicked.connect(lambda: (
                lambda dataSet: (
                    self.label_69.setText(f"{dataSet['brand']} {dataSet['model']}"),
                    self.label_69.repaint(),
                    self.carImage_4.setPixmap(QPixmap(f":/image/{dataSet['image']}")),
                    self.carImage_4.repaint()
                )
            )(car_data))


        ###############################END####################################################################
    ######################################################################################################
        self.verticalLayout_27.addWidget(self.listOfCarsSub)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_26.addWidget(self.scrollArea)
        self.verticalLayout_17.addWidget(self.listOfCars)



        self.mainPages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_18 = QVBoxLayout(self.page_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_30 = QFrame(self.page_8)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_30)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pushButton = QPushButton(self.frame_31)
        self.pushButton.setObjectName(u"pushButton")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon18)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.pushButton, 0, Qt.AlignLeft | Qt.AlignVCenter)

        self.label_8 = QLabel(self.frame_31)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_26.addWidget(self.label_8, 0, Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_47.addWidget(self.frame_31, 0, Qt.AlignTop)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_7 = QLineEdit(self.frame_33)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(50, 25))
        self.lineEdit_7.setStyleSheet(u"")

        self.horizontalLayout_30.addWidget(self.lineEdit_7)

        self.label_58 = QLabel(self.frame_33)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_30.addWidget(self.label_58)

        self.comboBox = QComboBox(self.frame_33)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_30.addWidget(self.comboBox)

        self.label_59 = QLabel(self.frame_33)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_30.addWidget(self.label_59)

        self.comboBox_2 = QComboBox(self.frame_33)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_30.addWidget(self.comboBox_2)

        self.label_11 = QLabel(self.frame_33)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_30.addWidget(self.label_11)

        self.comboBox_3 = QComboBox(self.frame_33)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_30.addWidget(self.comboBox_3)

        self.searchBtn = QPushButton(self.frame_33)
        self.searchBtn.setObjectName(u"searchBtn")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon19)

        self.horizontalLayout_30.addWidget(self.searchBtn, 0, Qt.AlignRight | Qt.AlignVCenter)

        self.verticalLayout_47.addWidget(self.frame_33)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.tableWidget = QTableWidget(self.frame_32)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"color:rgb(126, 126, 126)")

        self.horizontalLayout_29.addWidget(self.tableWidget)

        self.verticalLayout_47.addWidget(self.frame_32)

        self.verticalLayout_18.addWidget(self.frame_30)

        self.frame_34 = QFrame(self.page_8)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.refreshCarBtn = QPushButton(self.frame_34)
        self.refreshCarBtn.setObjectName(u"refreshCarBtn")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/refresh-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshCarBtn.setIcon(icon20)

        self.horizontalLayout_31.addWidget(self.refreshCarBtn)

        self.addCarBtn = QPushButton(self.frame_34)
        self.addCarBtn.setObjectName(u"addCarBtn")
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/corner-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addCarBtn.setIcon(icon21)

        self.horizontalLayout_31.addWidget(self.addCarBtn)

        self.updateCarBtn = QPushButton(self.frame_34)
        self.updateCarBtn.setObjectName(u"updateCarBtn")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/code.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.updateCarBtn.setIcon(icon22)

        self.horizontalLayout_31.addWidget(self.updateCarBtn)

        self.deleteCarBtn = QPushButton(self.frame_34)
        self.deleteCarBtn.setObjectName(u"deleteCarBtn")
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteCarBtn.setIcon(icon23)

        self.horizontalLayout_31.addWidget(self.deleteCarBtn)

        self.verticalLayout_18.addWidget(self.frame_34)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Page Admin", None))
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter car Brand", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Fuel Type", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"gasoline", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"diesel", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"electric", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"hybrid", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"ethanol", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"hydrogen", None))

        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Transmission", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"manual", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"automatic", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"CVT", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Availability", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Available", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Unavailable", None))

        self.searchBtn.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Registration number", None));
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Brand", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Model", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Fuel type", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Number of seats", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Transmission", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Rental price/Day", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Availability", None));
        self.refreshCarBtn.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        self.addCarBtn.setText(QCoreApplication.translate("MainWindow", u"ADD NEW CAR", None))
        self.updateCarBtn.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.deleteCarBtn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.addCarBtn.clicked.connect(lambda:self.mainPages.setCurrentIndex(3))

        self.mainPages.addWidget(self.page_8)

        ##############Page Add New Car##############################################################

        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_52 = QVBoxLayout(self.page_9)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.frame_36 = QFrame(self.page_9)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 50))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.frame_36)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font)

        self.horizontalLayout_40.addWidget(self.label_60, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_5 = QPushButton(self.frame_36)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon25)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_40.addWidget(self.pushButton_5, 0, Qt.AlignRight | Qt.AlignTop)
        self.verticalLayout_52.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.page_9)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_61 = QLabel(self.frame_37)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(300, 16777215))
        self.label_61.setPixmap(QPixmap(u":/image/151.png"))
        self.label_61.setScaledContents(True)

        self.horizontalLayout_41.addWidget(self.label_61, 0, Qt.AlignLeft | Qt.AlignTop)

        self.addImageBtn = QPushButton(self.frame_37)
        self.addImageBtn.setObjectName(u"addImageBtn")
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        self.addImageBtn.setFont(font6)
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons/upload-cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addImageBtn.setIcon(icon26)
        self.addImageBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_41.addWidget(self.addImageBtn)

        self.verticalLayout_52.addWidget(self.frame_37, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.frame_38 = QFrame(self.page_9)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_38)
        self.verticalLayout_48.setSpacing(20)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(10, 20, 10, 10)
        self.frame_53 = QFrame(self.frame_38)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_48.setSpacing(30)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.frame_53)
        self.label_77.setObjectName(u"label_77")
        font7 = QFont()
        font7.setPointSize(10)
        self.label_77.setFont(font7)

        self.horizontalLayout_48.addWidget(self.label_77)

        self.lineEdit_14 = QLineEdit(self.frame_53)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_48.addWidget(self.lineEdit_14)

        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Registration number :", None))

        self.verticalLayout_48.addWidget(self.frame_53)

        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_34.setSpacing(30)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.frame_39)
        self.label_62.setObjectName(u"label_62")
        font7 = QFont()
        font7.setPointSize(10)
        self.label_62.setFont(font7)

        self.horizontalLayout_34.addWidget(self.label_62, 0, Qt.AlignLeft | Qt.AlignVCenter)

        self.lineEdit_8 = QLineEdit(self.frame_39)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_34.addWidget(self.lineEdit_8)

        self.verticalLayout_48.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_36.setSpacing(30)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.frame_40)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font7)

        self.horizontalLayout_36.addWidget(self.label_63)

        self.lineEdit_9 = QLineEdit(self.frame_40)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_36.addWidget(self.lineEdit_9)

        self.verticalLayout_48.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_38)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_35.setSpacing(30)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.frame_41)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font7)

        self.horizontalLayout_35.addWidget(self.label_64)

        self.comboBox_4 = QComboBox(self.frame_41)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMaximumSize(QSize(200, 16777215))
        self.comboBox_4.setFont(font7)

        self.horizontalLayout_35.addWidget(self.comboBox_4)

        self.verticalLayout_48.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_38)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_37.setSpacing(30)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.frame_42)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font7)

        self.horizontalLayout_37.addWidget(self.label_65)

        self.comboBox_5 = QComboBox(self.frame_42)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMaximumSize(QSize(200, 16777215))
        self.comboBox_5.setFont(font7)

        self.horizontalLayout_37.addWidget(self.comboBox_5)

        self.verticalLayout_48.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_38)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_38.setSpacing(30)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.frame_43)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font7)

        self.horizontalLayout_38.addWidget(self.label_66)

        self.comboBox_6 = QComboBox(self.frame_43)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMaximumSize(QSize(200, 16777215))
        self.comboBox_6.setFont(font7)

        self.horizontalLayout_38.addWidget(self.comboBox_6)

        self.verticalLayout_48.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_38)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_39.setSpacing(30)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.frame_44)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font7)

        self.horizontalLayout_39.addWidget(self.label_67)

        self.lineEdit_13 = QLineEdit(self.frame_44)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_39.addWidget(self.lineEdit_13)

        self.verticalLayout_48.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_38)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_33.setSpacing(30)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.frame_45)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font7)

        self.horizontalLayout_33.addWidget(self.label_68)

        self.comboBox_7 = QComboBox(self.frame_45)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMaximumSize(QSize(200, 16777215))
        self.comboBox_7.setFont(font7)

        self.horizontalLayout_33.addWidget(self.comboBox_7)

        self.verticalLayout_48.addWidget(self.frame_45)

        self.verticalLayout_52.addWidget(self.frame_38)

        self.frame_46 = QFrame(self.page_9)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.submitBtn = QPushButton(self.frame_46)
        self.submitBtn.setObjectName(u"submitBtn")
        icon27 = QIcon()
        icon27.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.submitBtn.setIcon(icon27)

        self.horizontalLayout_42.addWidget(self.submitBtn, 0, Qt.AlignRight)

        self.clearBtn = QPushButton(self.frame_46)
        self.clearBtn.setObjectName(u"clearBtn")
        icon28 = QIcon()
        icon28.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clearBtn.setIcon(icon28)

        self.horizontalLayout_42.addWidget(self.clearBtn)

        self.verticalLayout_52.addWidget(self.frame_46, 0, Qt.AlignBottom)
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Back To Page Admin", None))
        self.pushButton_5.setText("")
        self.label_61.setText("")
        self.addImageBtn.setText(QCoreApplication.translate("MainWindow", u"Add image", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Brand :", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Model :", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Fuel type :", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"gasoline", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"diesel", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"electric", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"hybrid", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"ethanol", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"hydrogen", None))

        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Number of seats :", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_5.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_5.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_5.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_5.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_5.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_5.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_5.setItemText(13, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_5.setItemText(14, QCoreApplication.translate("MainWindow", u"14", None))

        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Transmission :", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"manual", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"automatic", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"CVT", None))

        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Rental price per day :", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Availability :", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"rented", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"Unavailable", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"Available", None))

        self.submitBtn.setText(QCoreApplication.translate("MainWindow", u"S UBMIT", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"CLEAR ALL", None))

        self.pushButton_5.clicked.connect(lambda:self.mainPages.setCurrentIndex(2))

        self.mainPages.addWidget(self.page_9)

        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_53 = QVBoxLayout(self.page_10)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.scrollArea_2 = QScrollArea(self.page_10)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.listOfPanierCars = QWidget()
        self.listOfPanierCars.setObjectName(u"listOfPanierCars")
        self.listOfPanierCars.setGeometry(QRect(0, 0, 438, 585))
        self.cardCarChechOut1 = QWidget(self.listOfPanierCars)
        self.cardCarChechOut1.setObjectName(u"cardCarChechOut1")
        self.cardCarChechOut1.setGeometry(QRect(10, 30, 180, 180))
        self.cardCarChechOut1.setMaximumSize(QSize(180, 180))
        self.cardCarChechOut1.setStyleSheet(u"")
        self.verticalLayout_49 = QVBoxLayout(self.cardCarChechOut1)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.cardCarChechOut1)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.frame_47)
        self.label_69.setObjectName(u"label_69")
        font5 = QFont()
        font5.setPointSize(9)
        self.label_69.setFont(font5)

        self.horizontalLayout_43.addWidget(self.label_69, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Name Of Car", None))

        self.favoriteBtn_5 = QPushButton(self.frame_47)
        self.favoriteBtn_5.setObjectName(u"favoriteBtn_5")
        self.favoriteBtn_5.setIcon(icon18)
        self.favoriteBtn_5.setIconSize(QSize(20, 20))

        self.horizontalLayout_43.addWidget(self.favoriteBtn_5, 0, Qt.AlignRight | Qt.AlignVCenter)

        self.verticalLayout_49.addWidget(self.frame_47, 0, Qt.AlignTop)

        self.carImage_4 = QLabel(self.cardCarChechOut1)
        self.carImage_4.setObjectName(u"carImage_4")
        self.carImage_4.setMaximumSize(QSize(200, 200))
        self.carImage_4.setPixmap(QPixmap(u":/image/151.png"))
        self.carImage_4.setScaledContents(True)

        self.verticalLayout_49.addWidget(self.carImage_4, 0, Qt.AlignHCenter)

        self.frame_48 = QFrame(self.cardCarChechOut1)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.checkoutPanierBtn = QPushButton(self.frame_48)
        self.checkoutPanierBtn.setObjectName(u"checkoutPanierBtn")
        self.checkoutPanierBtn.setMinimumSize(QSize(100, 0))
        self.checkoutPanierBtn.setMaximumSize(QSize(80, 60))
        icon29 = QIcon()
        icon29.addFile(u":/icons/icons/credit-card.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.checkoutPanierBtn.setIcon(icon29)
        self.checkoutPanierBtn.setIconSize(QSize(20, 20))

        self.checkoutPanierBtn.setText(QCoreApplication.translate("MainWindow", u"CheckOut", None))

        self.horizontalLayout_44.addWidget(self.checkoutPanierBtn, 0, Qt.AlignLeft | Qt.AlignVCenter)

        self.label_70 = QLabel(self.frame_48)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"500\u00a3/Day", None))

        self.horizontalLayout_44.addWidget(self.label_70, 0, Qt.AlignRight | Qt.AlignVCenter)

        self.verticalLayout_49.addWidget(self.frame_48)

        self.scrollArea_2.setWidget(self.listOfPanierCars)

        self.verticalLayout_53.addWidget(self.scrollArea_2)

        self.mainPages.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_54 = QVBoxLayout(self.page_11)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_49 = QFrame(self.page_11)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_49)
        self.verticalLayout_50.setSpacing(15)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_71 = QLabel(self.frame_49)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setPixmap(QPixmap(u":/image/151.png"))
        self.label_71.setScaledContents(True)

        self.verticalLayout_50.addWidget(self.label_71, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_72 = QLabel(self.frame_49)
        self.label_72.setObjectName(u"label_72")
        font8 = QFont()
        font8.setPointSize(11)
        self.label_72.setFont(font8)

        self.verticalLayout_50.addWidget(self.label_72, 0, Qt.AlignHCenter)

        self.verticalLayout_54.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.page_11)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.frame_50)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font8)

        self.horizontalLayout_45.addWidget(self.label_73, 0, Qt.AlignHCenter)

        self.dateTimeEdit = QDateTimeEdit(self.frame_50)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setFont(font8)

        self.horizontalLayout_45.addWidget(self.dateTimeEdit)

        self.verticalLayout_54.addWidget(self.frame_50, 0, Qt.AlignVCenter)

        self.frame_51 = QFrame(self.page_11)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.frame_51)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font8)

        self.horizontalLayout_46.addWidget(self.label_74, 0, Qt.AlignHCenter)

        self.dateTimeEdit_2 = QDateTimeEdit(self.frame_51)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setFont(font8)

        self.horizontalLayout_46.addWidget(self.dateTimeEdit_2)

        self.verticalLayout_54.addWidget(self.frame_51, 0, Qt.AlignVCenter)

        self.frame_52 = QFrame(self.page_11)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_47.setSpacing(50)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, -1, 50, -1)
        self.label_75 = QLabel(self.frame_52)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font8)

        self.horizontalLayout_47.addWidget(self.label_75, 0, Qt.AlignRight | Qt.AlignVCenter)

        self.label_76 = QLabel(self.frame_52)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font8)

        self.horizontalLayout_47.addWidget(self.label_76, 0, Qt.AlignHCenter)

        self.verticalLayout_54.addWidget(self.frame_52, 0, Qt.AlignRight)

        self.checkOutBtn = QPushButton(self.page_11)
        self.checkOutBtn.setObjectName(u"checkOutBtn")
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/code.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.checkOutBtn.setIcon(icon23)

        self.verticalLayout_54.addWidget(self.checkOutBtn, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Name Of Car", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Pickup Date :", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Return Date :", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Amount :", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"- $", None))
        self.checkOutBtn.setText(QCoreApplication.translate("MainWindow", u"CHECK OUT", None))

        self.mainPages.addWidget(self.page_11)

        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_55 = QVBoxLayout(self.page_12)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_78 = QLabel(self.page_12)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font)

        self.verticalLayout_55.addWidget(self.label_78, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Page Report", None))

        self.mainPages.addWidget(self.page_12)


    ####################################################################################################
    #############################Page Cars##############################################################
        for x in range(1, 5):
            var_name = str(x)
            id = f"p_{var_name}"
            car = f"car{id}"
            dataSet = cars.get_car(x)



            # create a new widget and set its object name
            pageCar = QWidget()
            setattr(self, f"{id}", pageCar)
            pageCar.setObjectName(id)

            # create a new layout for the widget and set its properties
            verticalLayout = QVBoxLayout(pageCar)
            verticalLayout.setSpacing(0)
            verticalLayout.setObjectName(f"verticalLayout_{var_name}")
            verticalLayout.setContentsMargins(0, 0, 0, 0)

            # create a new widget and set its object name and size policy
            carWidget = QWidget(pageCar)
            setattr(self, car, carWidget)
            carWidget.setObjectName(car)
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(carWidget.sizePolicy().hasHeightForWidth())
            carWidget.setSizePolicy(sizePolicy)

            # create a new layout for the car widget and set its properties
            carLayout = QVBoxLayout(carWidget)
            carLayout.setSpacing(0)
            carLayout.setObjectName(f"verticalLayout_{var_name}")
            carLayout.setContentsMargins(0, 0, 0, 0)

            # create a new frame for the car widget and set its properties
            carFrame = QFrame(carWidget)
            carFrame.setObjectName(f"frame_{var_name}")
            carFrame.setFrameShape(QFrame.StyledPanel)
            carFrame.setFrameShadow(QFrame.Raised)

            # create a new layout for the frame and set its properties
            frameLayout = QHBoxLayout(carFrame)
            frameLayout.setSpacing(0)
            frameLayout.setObjectName(f"horizontalLayout_{var_name}")
            frameLayout.setContentsMargins(0, 0, 0, 0)

            # create a new label for the car name and set its properties
            label = QLabel(carFrame)
            label.setObjectName(f"label_{var_name}")
            font = QFont()
            font.setPointSize(9)
            label.setFont(font)
            label.setText(QCoreApplication.translate("MainWindow", f"{dataSet['brand']} {dataSet['model']}", None))

            # add the label to the frame layout
            frameLayout.addWidget(label, 0, Qt.AlignLeft | Qt.AlignVCenter)

            # create a new button for adding the car to favorites and set its properties
            button = QPushButton(carFrame)
            button.setObjectName(f"favoriteBtn_{var_name}")
            icon = QIcon()
            icon.addFile(u":/icons/icons/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon)
            button.setIconSize(QSize(20, 20))
            button.setToolTip(QCoreApplication.translate("MainWindow", u"Add", None))
            button.setText("")

            # add the button to the frame layout
            frameLayout.addWidget(button, 0, Qt.AlignRight | Qt.AlignVCenter)

            # add the frame to the car layout
            carLayout.addWidget(carFrame)

            # add the car widget to the page layout
            verticalLayout.addWidget(carWidget)

            # Create a new frame and set its properties
            frame_name = f"frame_{id}"
            frame = QFrame(getattr(self, car))
            setattr(self, frame_name, frame)
            frame.setObjectName(frame_name)
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setFrameShadow(QFrame.Raised)

            # Create a new vertical layout and add it to the frame
            layout_name = f"layout_{id}"
            layout = QVBoxLayout(frame)
            setattr(self, layout_name, layout)
            layout.setSpacing(10)
            layout.setObjectName(layout_name)
            layout.setContentsMargins(0, 0, 0, 10)

            # Create a new label for "Dispo/Not Dispo" and add it to the layout
            label_26_name = f"label_26_{id}"
            label_26 = QLabel(frame)
            setattr(self, label_26_name, label_26)
            label_26.setObjectName(label_26_name)
            layout.addWidget(label_26, 0, Qt.AlignHCenter)
            label_26.setText(QCoreApplication.translate("MainWindow", f"{dataSet['availability']}", None))

            # Create a new label for the car image and add it to the layout
            label_28_name = f"label_28_{id}"
            label_28 = QLabel(frame)
            setattr(self, label_28_name, label_28)
            label_28.setObjectName(label_28_name)
            label_28.setMaximumSize(QSize(400, 400))
            label_28.setPixmap(QPixmap(f"{dataSet['image']}"))
            label_28.setScaledContents(True)
            layout.addWidget(label_28, 0, Qt.AlignHCenter)

            # Create a new label for the car specs and add it to the layout
            label_29_name = f"label_29_{id}"
            label_29 = QLabel(frame)
            setattr(self, label_29_name, label_29)
            label_29.setObjectName(label_29_name)
            font6 = QFont()
            font6.setBold(True)
            font6.setWeight(75)
            label_29.setFont(font6)
            layout.addWidget(label_29)
            label_29.setText(QCoreApplication.translate("MainWindow", u"Car Specs", None))

            verticalLayout.addWidget(frame)
            ##########################Carspec1###########################################
            # create frame
            frame = QFrame(getattr(self, car))
            setattr(self, f"frame_{var_name}", frame)
            frame.setObjectName(f"frame_{var_name}")
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setFrameShadow(QFrame.Raised)

            # create horizontal layout
            h_layout = QHBoxLayout(frame)
            h_layout.setSpacing(25)
            h_layout.setObjectName(f"horizontalLayout_{var_name}")
            h_layout.setContentsMargins(0, 0, 0, 0)

            # create car specs frame
            car_spec = QFrame(frame)
            setattr(self, f"carSpec{var_name}", car_spec)
            car_spec.setObjectName(f"carSpec{var_name}")
            car_spec.setStyleSheet(u"background-color:#1D203E;\n""border-radius:10px;\n")
            car_spec.setFrameShape(QFrame.StyledPanel)
            car_spec.setFrameShadow(QFrame.Raised)

            # create vertical layout
            v_layout = QVBoxLayout(car_spec)
            v_layout.setObjectName(f"verticalLayout_{var_name}")

            # create marque label
            label_marque = QLabel(car_spec)
            setattr(self, f"label_marque{var_name}", label_marque)
            label_marque.setObjectName(f"label_marque{var_name}")
            label_marque.setMaximumSize(QSize(200, 50))
            label_marque.setFont(font4)
            label_marque.setAlignment(Qt.AlignCenter)
            v_layout.addWidget(label_marque, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # create dash label
            label_dash = QLabel(car_spec)
            setattr(self, f"label_dash{var_name}", label_dash)
            label_dash.setObjectName(f"label_dash{var_name}")
            font7 = QFont()
            font7.setPointSize(12)
            font7.setBold(True)
            font7.setWeight(75)
            label_dash.setFont(font7)
            v_layout.addWidget(label_dash, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # create hp label
            label_hp_marque = QLabel(car_spec)
            setattr(self, f"label_hp_marque{var_name}", label_hp_marque)
            label_hp_marque.setObjectName(f"label_hp_marque{var_name}")
            label_hp_marque.setFont(font6)
            v_layout.addWidget(label_hp_marque, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # add car spec frame to horizontal layout
            h_layout.addWidget(car_spec)

            # set label texts
            label_marque.setText(QCoreApplication.translate("MainWindow", u"Brand", None))
            label_dash.setText(QCoreApplication.translate("MainWindow", u"-", None))
            label_hp_marque.setText(QCoreApplication.translate("MainWindow", f"{dataSet['brand']}", None))

#######################create carspec2###############################################################
            # create new QFrame object and set its properties
            car_spec2 = QFrame(frame)
            setattr(self, f"carSpec2{var_name}", car_spec2)
            car_spec2.setObjectName(f"carSpec{var_name}")
            car_spec2.setStyleSheet(u"background-color:#1D203E;\n""border-radius:10px;\n")
            car_spec2.setFrameShape(QFrame.StyledPanel)
            car_spec2.setFrameShadow(QFrame.Raised)

            # create new QVBoxLayout object for the new QFrame
            verticalLayout_carspec_2 = QVBoxLayout(car_spec2)
            verticalLayout_carspec_2.setObjectName(f"verticalLayout_carspec_2_{id}")

            # create new QLabel objects for the new QFrame and set their properties
            label1 = QLabel(car_spec2)
            label1.setObjectName(f"label_{id}_1")
            label1.setMaximumSize(QSize(200, 50))
            label1.setFont(font4)
            label1.setAlignment(Qt.AlignCenter)
            verticalLayout_carspec_2.addWidget(label1, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            label2 = QLabel(car_spec2)
            label2.setObjectName(f"label_{id}_2")
            label2.setFont(font7)
            verticalLayout_carspec_2.addWidget(label2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            label3 = QLabel(car_spec2)
            label3.setObjectName(f"label_{id}_3")
            label3.setFont(font6)
            verticalLayout_carspec_2.addWidget(label3, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # set the text for the new QLabel objects
            label1.setText(QCoreApplication.translate("MainWindow", u"Model", None))
            label2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            label3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['model']}", None))
            # add the new QFrame to the existing horizontalLayout
            h_layout.addWidget(car_spec2)
##############################Create carspec3##########################################################
            # create new QFrame object and set its properties
            car_spec3 = QFrame(frame)
            setattr(self, f"carSpec2{var_name}", car_spec3)
            car_spec3.setObjectName(f"carSpec{var_name}")
            car_spec3.setStyleSheet(u"background-color:#1D203E;\n""border-radius:10px;\n")
            car_spec3.setFrameShape(QFrame.StyledPanel)
            car_spec3.setFrameShadow(QFrame.Raised)

            # create new QVBoxLayout object for the new QFrame
            verticalLayout_carspec_3 = QVBoxLayout(car_spec3)
            verticalLayout_carspec_3.setObjectName(f"verticalLayout_carspec_3_{id}")

            # create new QLabel objects for the new QFrame and set their properties
            label1 = QLabel(car_spec3)
            label1.setObjectName(f"label_{id}_1")
            label1.setMaximumSize(QSize(200, 50))
            label1.setFont(font4)
            label1.setAlignment(Qt.AlignCenter)
            verticalLayout_carspec_3.addWidget(label1, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            label2 = QLabel(car_spec3)
            label2.setObjectName(f"label_{id}_2")
            label2.setFont(font7)
            verticalLayout_carspec_3.addWidget(label2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            label3 = QLabel(car_spec3)
            label3.setObjectName(f"label_{id}_3")
            label3.setFont(font6)
            verticalLayout_carspec_3.addWidget(label3, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # set the text for the new QLabel objects
            label1.setText(QCoreApplication.translate("MainWindow", u"Fuel Type", None))
            label2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            label3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['fuel_type']}", None))
            # add the new QFrame to the existing horizontalLayout
            h_layout.addWidget(car_spec3)

            ###############add carspec1-2-3  to frame ###########################
            #layout.addWidget(frame)

######################################Create Frame25##########################################################

            # Create the frame and set its properties
            Frame25 = QFrame(pageCar)
            Frame25.setObjectName(f"frame_25_{var_name}")
            Frame25.setFrameShape(QFrame.StyledPanel)
            Frame25.setFrameShadow(QFrame.Raised)

            # Create a new vertical layout and add it to the frame
            v_layout_frame25 = QVBoxLayout(Frame25)
            v_layout_frame25.setObjectName(f"v_layout_frame25_{var_name}")
            v_layout_frame25.setContentsMargins(0, 0, 0, 0)

            # Create the frame and set its properties
            Frame26 = QFrame(Frame25)
            Frame26.setObjectName(f"frame_26_{var_name}")
            Frame26.setFrameShape(QFrame.StyledPanel)
            Frame26.setFrameShadow(QFrame.Raised)

            # Create a new horizental layout and add it to the frame
            h_layout_frame25 = QVBoxLayout(Frame26)
            h_layout_frame25.setObjectName(f"v_layout_frame25_{var_name}")

            # create new QFrame object and set its properties
            car_spec5 = QFrame(Frame26)
            setattr(self, f"carSpec5{var_name}", car_spec5)
            car_spec5.setObjectName(f"carSpec5{var_name}")
            car_spec5.setStyleSheet(u"background-color:#1D203E;\n""border-radius:10px;\n")
            car_spec5.setMaximumSize(QSize(200, 100))
            car_spec5.setFrameShape(QFrame.StyledPanel)
            car_spec5.setFrameShadow(QFrame.Raised)

            # Create a new vertical layout and add it to the frame
            v_layout_frame26 = QVBoxLayout(car_spec5)
            v_layout_frame26.setObjectName(f"v_layout_frame26_{var_name}")
            v_layout_frame26.setContentsMargins(0, 0, 0, 0)

            # create new QLabel objects for the new QFrame and set their properties
            labelcarspec5_1 = QLabel(car_spec5)
            labelcarspec5_1.setObjectName(f"label_{id}_carspec5_1")
            labelcarspec5_1.setMaximumSize(QSize(200, 50))
            labelcarspec5_1.setFont(font4)
            labelcarspec5_1.setAlignment(Qt.AlignCenter)
            v_layout_frame26.addWidget(labelcarspec5_1, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            labelcarspec5_2 = QLabel(car_spec5)
            labelcarspec5_2.setObjectName(f"label_{id}_carspec5_2")
            labelcarspec5_2.setFont(font7)
            v_layout_frame26.addWidget(labelcarspec5_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            labelcarspec5_3 = QLabel(car_spec5)
            labelcarspec5_3.setObjectName(f"label_{id}_carspec5_3")
            labelcarspec5_3.setFont(font6)
            v_layout_frame26.addWidget(labelcarspec5_3, 0, Qt.AlignHCenter | Qt.AlignVCenter)
            labelcarspec5_1.setText(QCoreApplication.translate("MainWindow", u"Number Of Seats", None))
            labelcarspec5_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            labelcarspec5_3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['number_of_seats']}", None))

            h_layout_frame25.addWidget(car_spec5)

###############################create carspec4############################################################
            # create new QFrame object and set its properties
            car_spec4 = QFrame(Frame26)
            setattr(self, f"carSpec4{var_name}", car_spec4)
            car_spec4.setObjectName(f"carSpec4{var_name}")
            car_spec4.setStyleSheet(u"background-color:#1D203E;\n""border-radius:10px;\n")
            car_spec4.setMaximumSize(QSize(200, 100))
            car_spec4.setFrameShape(QFrame.StyledPanel)
            car_spec4.setFrameShadow(QFrame.Raised)

            # Create a new vertical layout and add it to the frame
            v_layout_frame27 = QVBoxLayout(car_spec4)
            v_layout_frame27.setObjectName(f"v_layout_frame27_{var_name}")
            v_layout_frame27.setContentsMargins(0, 0, 0, 0)

            # create new QLabel objects for the new QFrame and set their properties
            labelcarspec4_1 = QLabel(car_spec5)
            labelcarspec4_1.setObjectName(f"label_{id}_carspec4_1")
            labelcarspec4_1.setMaximumSize(QSize(200, 50))
            labelcarspec4_1.setFont(font4)
            labelcarspec4_1.setAlignment(Qt.AlignCenter)

            v_layout_frame27.addWidget(labelcarspec4_1, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # create new QLabel objects for the new QFrame and set their properties
            labelcarspec4_2 = QLabel(car_spec5)
            labelcarspec4_2.setObjectName(f"label_{id}_carspec4_2")
            labelcarspec4_2.setFont(font7)

            v_layout_frame27.addWidget(labelcarspec4_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # create new QLabel objects for the new QFrame and set their properties
            labelcarspec4_3 = QLabel(car_spec5)
            labelcarspec4_3.setObjectName(f"label_{id}_carspec4_3")
            labelcarspec4_3.setFont(font6)

            v_layout_frame27.addWidget(labelcarspec4_3, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            labelcarspec4_1.setText(QCoreApplication.translate("MainWindow", u"Transmission", None))
            labelcarspec4_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            labelcarspec4_3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['transmission']}", None))

            h_layout_frame25.addWidget(car_spec4)
            v_layout_frame25.addWidget(Frame26)
            verticalLayout.addWidget(Frame26)
###############################################################################################################
            # Create the frame and set its properties
            Frame27 = QFrame(Frame25)
            Frame27.setObjectName(f"frame_27_{var_name}")
            Frame27.setFrameShape(QFrame.StyledPanel)
            Frame27.setFrameShadow(QFrame.Raised)

            # Create a new horizental layout and add it to the frame
            h_layout_frame27 = QVBoxLayout(Frame27)
            h_layout_frame27.setObjectName(f"v_layout_frame27_{var_name}")

            # create new QFrame object and set its properties
            car_spec7 = QFrame(Frame27)
            setattr(self, f"carSpec7{var_name}", car_spec7)
            car_spec7.setObjectName(f"carSpec7{var_name}")
            car_spec7.setMaximumSize(QSize(200, 100))
            car_spec7.setStyleSheet(u"background-color:#1D203E;\n""border-radius:10px;\n")
            car_spec7.setFrameShape(QFrame.StyledPanel)
            car_spec7.setFrameShadow(QFrame.Raised)

            # Create a new vertical layout and add it to the frame
            v_layout_frame28 = QVBoxLayout(car_spec7)
            v_layout_frame28.setObjectName(f"v_layout_frame28_{var_name}")
            v_layout_frame28.setContentsMargins(0, 0, 0, 0)

            # create new QLabel objects for the new QFrame and set their properties
            labelcarspec7_1 = QLabel(car_spec7)
            labelcarspec7_1.setObjectName(f"label_{id}_carspec7_1")
            labelcarspec7_1.setMaximumSize(QSize(200, 50))
            labelcarspec7_1.setFont(font4)
            labelcarspec7_1.setAlignment(Qt.AlignCenter)

            v_layout_frame28.addWidget(labelcarspec7_1, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # create new QLabel objects for the new QFrame and set their properties
            labelcarspec7_2 = QLabel(car_spec7)
            labelcarspec7_2.setObjectName(f"label_{id}_carspec7_2")
            labelcarspec7_2.setFont(font7)

            v_layout_frame28.addWidget(labelcarspec7_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # create new QLabel objects for the new QFrame and set their properties
            labelcarspec7_3 = QLabel(car_spec7)
            labelcarspec7_3.setObjectName(f"label_{id}_carspec7_3")
            labelcarspec7_3.setFont(font6)

            v_layout_frame28.addWidget(labelcarspec7_3, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            labelcarspec7_1.setText(QCoreApplication.translate("MainWindow", u"Daily Rental Price", None))
            labelcarspec7_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            labelcarspec7_3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['daily_rental_price']}", None))

            h_layout_frame27.addWidget(car_spec7)
#########################create carspec6#######################################################################

            # create new QFrame object and set its properties

            car_spec6 = QFrame(Frame27)
            setattr(self, f"carSpec6{var_name}", car_spec6)
            car_spec6.setObjectName(f"carSpec6{var_name}")
            car_spec6.setStyleSheet(u"background-color:#1D203E;\n""border-radius:10px;\n")
            car_spec6.setMaximumSize(QSize(200, 100))
            car_spec6.setFrameShape(QFrame.StyledPanel)
            car_spec6.setFrameShadow(QFrame.Raised)

            # Create a new vertical layout and add it to the frame
            v_layout_frame29 = QVBoxLayout(car_spec6)
            v_layout_frame29.setObjectName(f"v_layout_frame29_{var_name}")
            v_layout_frame29.setContentsMargins(0, 0, 0, 0)

            # create new QLabel objects for the new QFrame and set their properties
            labelcarspec6_1 = QLabel(car_spec6)
            labelcarspec6_1.setObjectName(f"label_{id}_carspec6_1")
            labelcarspec6_1.setMaximumSize(QSize(200, 50))
            labelcarspec6_1.setFont(font4)
            labelcarspec6_1.setAlignment(Qt.AlignCenter)

            v_layout_frame29.addWidget(labelcarspec6_1, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # create new QLabel objects for the new QFrame and set their properties
            labelcarspec6_2 = QLabel(car_spec6)
            labelcarspec6_2.setObjectName(f"label_{id}_carspec6_2")
            labelcarspec6_2.setFont(font7)

            v_layout_frame29.addWidget(labelcarspec7_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            # create new QLabel objects for the new QFrame and set their properties
            labelcarspec6_3 = QLabel(car_spec6)
            labelcarspec6_3.setObjectName(f"label_{id}_carspec6_3")
            labelcarspec6_3.setFont(font6)

            v_layout_frame29.addWidget(labelcarspec6_3, 0, Qt.AlignHCenter | Qt.AlignVCenter)
            labelcarspec6_1.setText(QCoreApplication.translate("MainWindow", u"Availability\u00e9", None))
            labelcarspec6_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            labelcarspec6_3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['availability']}", None))

            h_layout_frame27.addWidget(car_spec6)

            v_layout_frame25.addWidget(Frame25)

            layout.addWidget(frame)
            ###########LastLine#######################
            self.mainPages.addWidget(getattr(self, id))
###########################ENDPageOfCar#############################################################
#####################################################################################################

        self.verticalLayout_15.addWidget(self.mainPages)
        self.horizontalLayout_8.addWidget(self.mainContentsContainer)
        #######################################################################################################
        self.SeeMore_1.clicked.connect(lambda: self.mainPages.setCurrentIndex(int(7)))
        self.SeeMore_2.clicked.connect(lambda: self.mainPages.setCurrentIndex(int(8)))
        self.SeeMore_3.clicked.connect(lambda: self.mainPages.setCurrentIndex(int(9)))
        self.SeeMore_4.clicked.connect(lambda: self.mainPages.setCurrentIndex(int(10)))
        ##########################################################################################################################
        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(200, 544))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon7)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.page_4)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_37 = QVBoxLayout(self.widget)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 0, 20, 0)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(100, 100))
        self.label_7.setStyleSheet(u"")
        self.label_7.setPixmap(QPixmap(u":/icons/kisspng-circle-area-angle-point-black-and-white-round-frame-5a7b862e56f5a6.5838409715180447183562.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_37.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_39 = QLabel(self.widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(1920, 1080))

        self.verticalLayout_37.addWidget(self.label_39, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_22 = QFrame(self.widget)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_22)
        self.verticalLayout_43.setSpacing(10)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_22)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_43.addWidget(self.label_40, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_41 = QLabel(self.frame_22)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_43.addWidget(self.label_41, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_37.addWidget(self.frame_22, 0, Qt.AlignTop)

        self.frame_23 = QFrame(self.widget)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_23)
        self.verticalLayout_44.setSpacing(10)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_23)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_44.addWidget(self.label_42, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_43 = QLabel(self.frame_23)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_44.addWidget(self.label_43, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_37.addWidget(self.frame_23, 0, Qt.AlignTop)

        self.frame_24 = QFrame(self.widget)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_24)
        self.verticalLayout_45.setSpacing(10)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_24)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_45.addWidget(self.label_44, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_45 = QLabel(self.frame_24)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_45.addWidget(self.label_45, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_37.addWidget(self.frame_24, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.widget)

        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_28 = QFrame(self.page_5)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_28)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_28)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))

        self.verticalLayout_46.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_28)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 25))

        self.verticalLayout_46.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame_28)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 25))

        self.verticalLayout_46.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_28)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 25))
        self.lineEdit_4.setEchoMode(QLineEdit.Password)

        self.verticalLayout_46.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.frame_28)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 25))
        self.lineEdit_5.setEchoMode(QLineEdit.Password)

        self.verticalLayout_46.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.frame_28)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 25))

        self.verticalLayout_46.addWidget(self.lineEdit_6)


        self.verticalLayout_14.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.page_5)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 150))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_29)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.deleteAllBtn = QPushButton(self.frame_29)
        self.deleteAllBtn.setObjectName(u"deleteAllBtn")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteAllBtn.setIcon(icon18)
        self.deleteAllBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.deleteAllBtn, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.valideBtn = QPushButton(self.frame_29)
        self.valideBtn.setObjectName(u"valideBtn")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.valideBtn.setIcon(icon19)
        self.valideBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.valideBtn)


        self.verticalLayout_14.addWidget(self.frame_29, 0, Qt.AlignTop)

        if dataUser['user_type'] == "admin":
            self.frame_35 = QFrame(self.page_5)
            self.frame_35.setObjectName(u"frame_35")
            self.frame_35.setFrameShape(QFrame.StyledPanel)
            self.frame_35.setFrameShadow(QFrame.Raised)
            self.horizontalLayout_32 = QHBoxLayout(self.frame_35)
            self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
            self.adminBtn = QPushButton(self.frame_35)
            self.adminBtn.setObjectName(u"adminBtn")
            icon24 = QIcon()
            icon24.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.adminBtn.setIcon(icon24)
            self.horizontalLayout_32.addWidget(self.adminBtn)
            self.adminBtn.setText(QCoreApplication.translate("MainWindow", u"Page Admin", None))
            self.verticalLayout_14.addWidget(self.frame_35, 0, Qt.AlignHCenter | Qt.AlignBottom)
            self.adminBtn.clicked.connect(lambda :self.mainPages.setCurrentIndex(2))

        self.rightMenuPages.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_12 = QLabel(self.popupNotificationSubContainer)
        self.label_12.setObjectName(u"label_12")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_12.setFont(font6)

        self.verticalLayout_20.addWidget(self.label_12)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        self.closeNotificationBtn.setIcon(icon7)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_20.addWidget(self.frame_9)


        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.footerContainer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.frame_11)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)


        self.horizontalLayout_11.addWidget(self.frame_11)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.sizeGrip)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout_25.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(1)
        self.rightMenuPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"List Of Cars", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"List Of Cars", None))
#if QT_CONFIG(tooltip)
        self.reportBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.reportBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
#if QT_CONFIG(tooltip)
        self.settingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenu.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenu.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_5.setText("")
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.Home.setText(QCoreApplication.translate("MainWindow", u"Dashbord", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.label_15.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Plans", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Reservations", None))
#if QT_CONFIG(tooltip)
        self.topDealersBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Top dealers", None))
#endif // QT_CONFIG(tooltip)
        self.topDealersBtn.setText(QCoreApplication.translate("MainWindow", u"Top dealers", None))
#if QT_CONFIG(tooltip)
        self.plansBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Plans", None))
#endif // QT_CONFIG(tooltip)
        self.plansBtn.setText(QCoreApplication.translate("MainWindow", u"Plans", None))
#if QT_CONFIG(tooltip)
        self.gpsTrackingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"GPS Tracking", None))
#endif // QT_CONFIG(tooltip)
        self.gpsTrackingBtn.setText(QCoreApplication.translate("MainWindow", u"GPS Tracking", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"List of Cars :", None))


#if QT_CONFIG(tooltip)

#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Right Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_7.setText("")
        if dataUser['nom'] != "":
            self.label_39.setText(QCoreApplication.translate("MainWindow", f"{dataUser['nom']} {dataUser['prenom']}", None))
        else:
            self.label_39.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Numero de telephone :", None))
        if dataUser['telephone'] != "":
            self.label_41.setText(QCoreApplication.translate("MainWindow", f"{dataUser['telephone']}", None))
        else:
            self.label_41.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Email :", None))
        if dataUser['email'] != "":
            self.label_43.setText(QCoreApplication.translate("MainWindow", f"{dataUser['email']}", None))
        else:
            self.label_43.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Type de Compte :", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", f"{dataUser['user_type']}", None))
        # if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Entrez votre nom et pr\u00e9nom ici", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre nom et pr\u00e9nom ici", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("MainWindow", u"Entrez votre num\u00e9ro de t\u00e9l\u00e9phone ici", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre num\u00e9ro de t\u00e9l\u00e9phone ici", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_3.setToolTip(QCoreApplication.translate("MainWindow", u"Entrez votre adresse e-mail ici", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre adresse e-mail ici", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_4.setToolTip(QCoreApplication.translate("MainWindow", u"Entrez votre ancien mot de passe ici", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre ancien mot de passe ici", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_5.setToolTip(QCoreApplication.translate("MainWindow", u"Entrez votre nouveau mot de passe ici", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre nouveau mot de passe ici", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_6.setToolTip(QCoreApplication.translate("MainWindow", u"Entrez votre demande de mise \u00e0 niveau ici", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre demande de mise \u00e0 niveau ici", None))
#if QT_CONFIG(tooltip)
        self.deleteAllBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Delete All", None))
#endif // QT_CONFIG(tooltip)
        self.deleteAllBtn.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
#if QT_CONFIG(tooltip)
        self.valideBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Valide", None))
#endif // QT_CONFIG(tooltip)
        self.valideBtn.setText(QCoreApplication.translate("MainWindow", u"Valide", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Copiright Asmih", None))
    # retranslateUi

