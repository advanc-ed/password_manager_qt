import sys
from PyQt6.QtWidgets import QApplication
from app.App import PasswordManagerApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    password_manager = PasswordManagerApp()
    sys.exit(app.exec())
