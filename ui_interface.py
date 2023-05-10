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
                                 "#cardinfo1,#cardinfo2,#cardinfo3{\n"
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
                                 "#lineEdit,#lineEdit_1,#lineEdit_2,#lineEdit_3,#lineEdit_4,#lineEdit_5,#lineEdit_6{\n"
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
            self.label.__dict__[cardCar_2].setText(QCoreApplication.translate("MainWindow", f"{dataSet['prix_location_par_jour']}\u00a3/Day", None))
            self.label.__dict__[cardCar_1].setText(QCoreApplication.translate("MainWindow", f"{dataSet['marque']} {dataSet['modele']}", None))
            self.__dict__[favoriteBtn].setToolTip(QCoreApplication.translate("MainWindow", u"Add", None))


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
        self.label_11 = QLabel(self.page_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.verticalLayout_18.addWidget(self.label_11)
        self.mainPages.addWidget(self.page_8)


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
            label.setText(QCoreApplication.translate("MainWindow", f"{dataSet['marque']} {dataSet['modele']}", None))

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
            label_26.setText(QCoreApplication.translate("MainWindow", f"{dataSet['disponibilite']}", None))

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
            label_marque.setText(QCoreApplication.translate("MainWindow", u"Marque", None))
            label_dash.setText(QCoreApplication.translate("MainWindow", u"-", None))
            label_hp_marque.setText(QCoreApplication.translate("MainWindow", f"{dataSet['marque']}", None))

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
            label1.setText(QCoreApplication.translate("MainWindow", u"Mod\u00e8le", None))
            label2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            label3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['modele']}", None))
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
            label1.setText(QCoreApplication.translate("MainWindow", u"Type de carburant", None))
            label2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            label3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['type_de_carburant']}", None))
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
            labelcarspec5_1.setText(QCoreApplication.translate("MainWindow", u"Nombre de places", None))
            labelcarspec5_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            labelcarspec5_3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['nombre_de_places']}", None))

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

            labelcarspec7_1.setText(QCoreApplication.translate("MainWindow", u"Prix de location par jour", None))
            labelcarspec7_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            labelcarspec7_3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['prix_location_par_jour']}", None))

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
            labelcarspec6_1.setText(QCoreApplication.translate("MainWindow", u"Disponibilit\u00e9", None))
            labelcarspec6_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
            labelcarspec6_3.setText(QCoreApplication.translate("MainWindow", f"{dataSet['disponibilite']}", None))

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
        self.SeeMore_1.clicked.connect(lambda: self.mainPages.setCurrentIndex(int(3)))
        self.SeeMore_2.clicked.connect(lambda: self.mainPages.setCurrentIndex(int(4)))
        self.SeeMore_3.clicked.connect(lambda: self.mainPages.setCurrentIndex(int(5)))
        self.SeeMore_4.clicked.connect(lambda: self.mainPages.setCurrentIndex(int(6)))
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
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Reports", None))

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

