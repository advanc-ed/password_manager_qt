import sys
from PyQt6.QtWidgets import QApplication
from app.App import PasswordManagerApp

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Initialize the Qt application.
    password_manager = PasswordManagerApp()  # Create an instance of the PasswordManagerApp.
    sys.exit(app.exec())  # Run the application's event loop and handle exit status.
