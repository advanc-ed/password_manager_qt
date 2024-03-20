import sys
from PyQt5.QtWidgets import QApplication
from app.app import PasswordManagerApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    password_manager = PasswordManagerApp()
    sys.exit(app.exec_())
