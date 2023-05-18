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
from PySide2.QtGui import QPixmap, QPixmapCache
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
        self.ui.submitBtn.clicked.connect(self.add_new_cars_from_table)
        self.ui.refreshCarBtn.clicked.connect(self.Show_Cras)
        self.ui.clearBtn.clicked.connect(self.clear_add_new_car)
        self.ui.addImageBtn.clicked.connect(self.getImage)
        self.ui.searchBtn.clicked.connect(self.search_cars)
        self.ui.deleteCarBtn.clicked.connect(self.delete_rows)
        self.ui.updateCarBtn.clicked.connect(self.update_Qtable_database)
        self.ui.checkoutPanierBtn.clicked.connect(lambda:self.ui.mainPages.setCurrentIndex(5))
        self.ui.checkoutPanierBtn.clicked.connect(self.checkout)
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
                self.ui.label_45.setText(QCoreApplication.translate("MainWindow", f"admin", None))
                self.ui.label_45.repaint()
                self.ui.lineEdit_6.setText('')

            elif self.ui.lineEdit_6.text() == '1111':
                user.change_user_type(username, 'user')
                self.ui.label_45.setText(QCoreApplication.translate("MainWindow", f"user", None))
                self.ui.label_45.repaint()
                self.ui.lineEdit_6.setText('')
            else:
                return

    def deletAll(self):
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_4.setText('')
        self.ui.lineEdit_5.setText('')
        self.ui.lineEdit_6.setText('')

    def checkout(self):
        dataSet=car.get_car(1)
        self.ui.label_72.setText(QCoreApplication.translate("MainWindow", f"{dataSet['brand']} {dataSet['model']}", None))
        self.ui.label_72.repaint()
        self.ui.label_71.setPixmap(QPixmap(f":/image/{dataSet['image']}"))
        self.ui.label_71.repaint()
        self.ui.label_76.setText(QCoreApplication.translate("MainWindow", f"{dataSet['daily_rental_price']}  $", None))
        self.ui.label_76.repaint()

    def Show_Cras(self):
        data = car.get_all_car()
        if data:
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.ui.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row_position)

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.jpg *.gif *.png)")
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.ui.label_61.setPixmap(QPixmap(pixmap))

    def add_new_cars_from_table(self):
        registration_number=self.ui.lineEdit_14.text()
        # Check if the car already exists in the database
        query = "SELECT COUNT(*) FROM cars WHERE registration_number = %s"
        values = (registration_number,)
        self.db.execute(query, values)
        result = self.db.cursor.fetchone()
        # If the car does not exist in the database, add it
        if result[0] == 0:
            marque = self.ui.lineEdit_8.text()
            modele = self.ui.lineEdit_9.text()
            image = ""
            carburant = self.ui.comboBox_4.currentText()
            nombre_de_places = self.ui.comboBox_5.currentText()
            transmission = self.ui.comboBox_6.currentText()
            prix_location_par_jour = self.ui.lineEdit_13.text()
            disponibilite = self.ui.comboBox_7.currentText()
            car.add_car_to_database(registration_number,marque, modele, image, carburant, nombre_de_places, transmission,prix_location_par_jour, disponibilite)
            pyautogui.alert("Car added successfully!")
            self.ui.lineEdit_8.setText("")
            self.ui.lineEdit_9.setText("")
            self.ui.lineEdit_13.setText("")
            self.ui.lineEdit_14.setText("")
        else:
            pyautogui.alert("Car already exists in the database!")
            self.ui.lineEdit_14.setText("")
            self.ui.lineEdit_8.setText("")
            self.ui.lineEdit_9.setText("")
            self.ui.lineEdit_13.setText("")

    def clear_add_new_car(self):
        self.ui.lineEdit_8.setText("")
        self.ui.lineEdit_9.setText("")
        self.ui.lineEdit_13.setText("")
        self.ui.lineEdit_14.setText("")


    def delete_rows(self):
        selected_rows = self.ui.tableWidget.selectionModel().selectedRows()
        if len(selected_rows) == 0:
            QMessageBox.warning(self, "No Rows Selected", "Please select rows to delete.")
            return

        confirm = QMessageBox.question(self, "Confirm Deletion", "Are you sure you want to delete the selected row(s)?",QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            for row in selected_rows:
                # Get the primary key (assuming it's in the first column)
                registration_number = self.ui.tableWidget.item(row.row(), 0)
                if registration_number is not None:
                    registrationNumber = registration_number.text()
                    # Delete the record from MySQL
                    car.delete(registrationNumber)
                    self.ui.tableWidget.removeRow(row.row())


    def update_Qtable_database(self):
        try:
            selected_row = self.ui.tableWidget.currentRow()
            if selected_row != -1:
                registration_number = self.ui.tableWidget.item(selected_row, 0).text()
                brand = self.ui.tableWidget.item(selected_row, 1).text()
                model = self.ui.tableWidget.item(selected_row, 2).text()
                image = self.ui.tableWidget.item(selected_row, 3).text()
                fuel_type = self.ui.tableWidget.item(selected_row, 4).text()
                number_of_seats = self.ui.tableWidget.item(selected_row, 5).text()
                transmission = self.ui.tableWidget.item(selected_row, 6).text()
                daily_rental_price = self.ui.tableWidget.item(selected_row, 7).text()
                availability = self.ui.tableWidget.item(selected_row, 8).text()

                # Query the database to retrieve the existing row with the registration number
                dataSet = car.get_car_with_registration_number(registration_number)

                # Check if any values have changed
                if (
                        dataSet[1] != brand or
                        dataSet[2] != model or
                        dataSet[3] != image or
                        dataSet[4] != fuel_type or
                        dataSet[5] != number_of_seats or
                        dataSet[6] != transmission or
                        dataSet[7] != daily_rental_price or
                        dataSet[8] != availability
                ):
                    # Update the row in the QTableWidget with the values from the database
                    car.set_car(registration_number, brand, model, image, fuel_type, number_of_seats, transmission, daily_rental_price, availability)
                    # Display a notification message
                    QMessageBox.information(None, "Notification",f"Updated values for registration number {registration_number}.")


        except Exception as e:
            # Handle any exceptions that might occur
            QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")

    def search_cars(self):
        brand = self.ui.lineEdit_7.text().lower()
        fuel = self.ui.comboBox.currentText().lower()
        transmission = self.ui.comboBox_2.currentText().lower()
        availability = self.ui.comboBox_3.currentText().lower()

        # Loop through each row in the table
        for row in range(self.ui.tableWidget.rowCount()):
            table_brand_item = self.ui.tableWidget.item(row, 1)
            table_model_item = self.ui.tableWidget.item(row, 2)
            table_fuel_item = self.ui.tableWidget.item(row, 4)
            table_transmission_item = self.ui.tableWidget.item(row, 6)
            table_availability_item = self.ui.tableWidget.item(row, 8)

            # Check if the items are not None before accessing text()
            if (
                    table_brand_item is None or
                    table_model_item is None or
                    table_fuel_item is None or
                    table_transmission_item is None or
                    table_availability_item is None
            ):
                continue

            table_brand = table_brand_item.text().lower()
            table_model = table_model_item.text().lower()
            table_fuel = table_fuel_item.text().lower()
            table_transmission = table_transmission_item.text().lower()
            table_availability = table_availability_item.text().lower()

            # Check if the brand matches (if it's not empty)
            brand_match = not brand or (brand and brand == table_brand)
            # Check if the model matches (if it's not empty)
            model_match = not brand or (brand and brand == table_model)
            # Check if the fuel type matches (if it's not empty)
            fuel_match = not fuel or (fuel and fuel == table_fuel)
            # Check if the transmission matches (if it's not empty)
            transmission_match = not transmission or (transmission and transmission == table_transmission)
            # Check if the availability matches (if it's not empty)
            availability_match = not availability or (availability and availability == table_availability)

            # If all criteria match, show the row
            if (
                    brand_match and model_match and fuel_match and
                    transmission_match and availability_match
            ):
                self.ui.tableWidget.setRowHidden(row, False)
            # Otherwise, hide the row
            else:
                self.ui.tableWidget.setRowHidden(row, True)

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

