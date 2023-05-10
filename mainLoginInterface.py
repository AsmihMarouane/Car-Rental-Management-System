import sys

########################################################################
# IMPORT GUI FILE
from ui_loginSignupInerface import *
########################################################################
from Custom_Widgets.Widgets import *
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(PySide2.QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #########################################################################################
        self.signinBtn.clicked.connect(lambda: self.loginSignup.setCurrentWidget(self.pageLogin))
        self.createNewAccBtn.clicked.connect(lambda: self.loginSignup.setCurrentWidget(self.pageSignUp))

        # SHOW WINDOW
        #######################################################################
        self.show()
        ########################################################################

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(Form)
    Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    Form.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################