import os
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QInputDialog, QMessageBox
from config import db_loc
from dialogs.DatabaseMenu import DatabaseMenu


class PasswordManagerApp(QWidget):
    """Main application window for the Password Manager."""

    def __init__(self):
        super().__init__()

        # Initialize attributes
        self.db_folder = db_loc
        self.current_db = None
        self.passwords = None
        self._databases = self.load_databases()  # Load existing databases

        self.initUI()  # Initialize the user interface

    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle('Password Manager')  # Set window title
        self.setGeometry(100, 100, 400, 300)  # Set window geometry

        layout = QVBoxLayout()  # Create a vertical layout for widgets

        # Main menu widgets
        menu_layout = QVBoxLayout()
        menu_label = QLabel('Password Manager')
        menu_layout.addWidget(menu_label)

        # Buttons for creating new database, starting with existing database, and exiting
        create_db_button = QPushButton('Create new password database')
        create_db_button.clicked.connect(self.create_db_clicked)
        menu_layout.addWidget(create_db_button)

        start_db_button = QPushButton('Start with an existing database')
        start_db_button.clicked.connect(self.start_db_clicked)
        menu_layout.addWidget(start_db_button)

        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.close)
        menu_layout.addWidget(exit_button)

        layout.addLayout(menu_layout)  # Add menu layout to main layout

        self.setLayout(layout)  # Set the main layout
        self.show()  # Show the widget

    def load_databases(self):
        """Load existing databases."""
        return [f for f in os.listdir(self.db_folder) if f.endswith('.txt')]

    def create_db_clicked(self):
        """Handle the 'Create new password database' button click."""
        db_name, ok = QInputDialog.getText(self, 'Create Database', 'Enter the name of the database:')
        if ok and db_name:
            open(os.path.join(self.db_folder, db_name + '.txt'), 'w').close()  # Create new database file
            QMessageBox.information(self, 'Success', 'New database created.')
            self._databases = self.load_databases()  # Reload the list of databases

    def start_db_clicked(self):
        """Handle the 'Start with an existing database' button click."""
        if not self._databases:
            QMessageBox.warning(self, 'Error', 'No existing databases found.')
            return

        db_name, ok = QInputDialog.getItem(self, 'Select Database', 'Choose a database:', self._databases, 0, False)
        if ok and db_name:
            self.current_db = db_name
            self.passwords = self.load_passwords()
            self.show_db_menu()

    def load_passwords(self):
        """Load passwords from the selected database."""
        passwords = {}
        db_loc = os.path.join(self.db_folder, self.current_db)
        if os.path.exists(db_loc):
            with open(db_loc, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(':')
                    if len(parts) >= 4:
                        username, password, label, note = parts[:4]
                        passwords[label] = (username, password, note)
        return passwords

    def save_passwords(self):
        """Save passwords to the selected database."""
        with open(os.path.join(self.db_folder, self.current_db), 'w') as file:
            for label, (username, password, note) in self.passwords.items():
                file.write(f'{username}:{password}:{label}:{note}\n')

    def show_db_menu(self):
        """Show the database menu dialog."""
        db_menu = DatabaseMenu(self.current_db, self.passwords)
        db_menu.exec()
