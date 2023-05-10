import datetime
import sys
import os
from PySide2 import *
from PySide2 import QtWidgets
from Custom_Widgets.Widgets import *
from ui_interface import *
import json
from users import *
from cars import *
from dataBaseLogin import *
import mysql.connector
import hashlib
import pyautogui
user = User()
car=Car()
class MainWindow(PySide2.QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #####################
        loadJsonStyle(self, self.ui)
        #####################
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_database_for_updates)
        self.timer.start(1000)  # Check for updates every second
        self.last_update_time = datetime.datetime.now()
        self.db = Database()
        #####################
        self.restore_button = getattr(self.ui, "restoreBtn")
        self.restore_button.clicked.connect(self.restore_or_maximize_window)
        # EXPAND CENTER MENU SIZE
        self.ui.settingBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        # CLOSE CENTER MENU SIZE
        self.ui.closeCenterMenu.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())
        # EXPAND RIGHT MENU SIZE
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        # CLOSE RIGHT MENU SIZE
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())
        # CLOSE NOTIFICATION SIZE
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
        self.ui.homeBtn.clicked.connect(self.checkButtonGroup)
        self.ui.dataBtn.clicked.connect(self.checkButtonGroup)
        self.ui.reportBtn.clicked.connect(self.checkButtonGroup)
        self.ui.deleteAllBtn.clicked.connect(self.deletAll)
        self.ui.valideBtn.clicked.connect(self.save)
        self.show()



    with open('config.json', 'r') as f:
        config = json.load(f)
        username = config['user']

    print(username)
    ############ START QPushButtonGroup##########################
    def checkButtonGroup(self):
        btn = self.sender()
        group = btn.group
        groupBtns = getattr(self, "group_btns_" + str(group))
        active = getattr(self, "group_active_" + str(group))
        notActive = getattr(self, "group_not_active_" + str(group))

        for x in groupBtns:
            if not x == btn:
                x.setStyleSheet(notActive)
                x.active = False

        btn.setStyleSheet(active)
        btn.active = True
    def save(self):
        if self.ui.lineEdit.text() =='' and self.ui.lineEdit_2.text() =='' and self.ui.lineEdit_3.text() =='' and self.ui.lineEdit_4.text()=='' and self.ui.lineEdit_5.text() =='' and self.ui.lineEdit_6.text() =='':
            return
        if self.ui.lineEdit.text() != '':
            nomEtPrenom = self.ui.lineEdit.text().split()
            nom = nomEtPrenom[0]
            prenom = nomEtPrenom[1]
            user.change_nom_prenom(username, nom, prenom)
            self.ui.label_39.setText(QCoreApplication.translate("MainWindow", f"{self.ui.lineEdit.text()}", None))
            self.ui.label_39.repaint()
            self.ui.lineEdit.setText('')
        if self.ui.lineEdit_2.text() != '':
            user.change_numero_telephone(username, self.ui.lineEdit_2.text())
            self.ui.label_41.setText(QCoreApplication.translate("MainWindow", f"{self.ui.lineEdit_2.text()}", None))
            self.ui.label_41.repaint()
            self.ui.lineEdit_2.setText('')
        if self.ui.lineEdit_3.text() != '' :
            user.change_email(username, self.ui.lineEdit_3.text())
            self.ui.label_43.setText(QCoreApplication.translate("MainWindow", f"{self.ui.lineEdit_3.text()}", None))
            self.ui.label_43.repaint()
            self.ui.lineEdit_3.setText('')
        if self.ui.lineEdit_4.text() == '' and self.ui.lineEdit_5.text() != '':
            pyautogui.alert("Entrez votre ancien mot de passe!!")
        if self.ui.lineEdit_4.text() != '' and self.ui.lineEdit_5.text() == '':
            pyautogui.alert("Entrez votre nouveau mot de passe!!")
        if  self.ui.lineEdit_4.text() != '' and self.ui.lineEdit_5.text() != '':
            dataUser = user.get_user(username)
            hashed_password = hashlib.sha256(self.ui.lineEdit_4.text().encode('utf-8')).hexdigest()
            hashed_new_password = hashlib.sha256(self.ui.lineEdit_5.text().encode('utf-8')).hexdigest()
            if dataUser['password'] == hashed_password:
                user.change_password_without_hashing(username,hashed_new_password)
                self.ui.lineEdit_4.setText('')
                self.ui.lineEdit_5.setText('')
            else :
                pyautogui.alert("Entrez votre ancien mot de passe n'est pas correct")
        if self.ui.lineEdit_6.text() != '':
            if self.ui.lineEdit_6.text() == '0000':
                user.change_user_type(username,'admin')

            elif self.ui.lineEdit_6.text() == '1111':
                user.change_user_type(username, 'user')
            else:
                return

    def deletAll(self):
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_4.setText('')
        self.ui.lineEdit_5.setText('')
        self.ui.lineEdit_6.setText('')

    def check_database_for_updates(self):
        # Retrieve new data from your MySQL database using the Database instance
        self.db.execute('SELECT * FROM users WHERE added_at > %s', (self.last_update_time,))
        new_data = self.db.cursor.fetchall()

        if new_data:
            # Update your PyQt application with the new data
            # ...

            # Set the last update time to the current time
            self.last_update_time = datetime.datetime.now()

        # Commit changes to the database using the Database instance
        self.db.commit()
    ###############Function Generate Car########################

    ############ END QPushButtonGroup##########################
    def restore_or_maximize_window(self):
        if self.windowState() == Qt.WindowMaximized:
            self.setWindowState(Qt.WindowNoState)
            self.ui.restoreBtn.setIcon(QtGui.QIcon(":/icons/icons/square.svg"))
        else:
            self.setWindowState(Qt.WindowMaximized)
            self.ui.restoreBtn.setIcon(QtGui.QIcon(":/icons/icons/copy.svg"))
        self.activateWindow()
        ####################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

