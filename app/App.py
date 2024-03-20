import os
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QInputDialog, QMessageBox
from config import db_loc
from dialogs.DatabaseMenu import DatabaseMenu


class PasswordManagerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.db_folder = db_loc
        self.current_db = None
        self.passwords = None
        self._databases = self.load_databases()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Manager')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Main menu widgets
        menu_layout = QVBoxLayout()
        menu_label = QLabel('Password Manager')
        menu_layout.addWidget(menu_label)

        create_db_button = QPushButton('Create new password database')
        create_db_button.clicked.connect(self.create_db_clicked)
        menu_layout.addWidget(create_db_button)

        start_db_button = QPushButton('Start with an existing database')
        start_db_button.clicked.connect(self.start_db_clicked)
        menu_layout.addWidget(start_db_button)

        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.close)
        menu_layout.addWidget(exit_button)

        layout.addLayout(menu_layout)

        self.setLayout(layout)
        self.show()

    def load_databases(self):
        return [f for f in os.listdir(self.db_folder) if f.endswith('.txt')]

    def create_db_clicked(self):
        db_name, ok = QInputDialog.getText(self, 'Create Database', 'Enter the name of the database:')
        if ok and db_name:
            open(os.path.join(self.db_folder, db_name + '.txt'), 'w').close()
            QMessageBox.information(self, 'Success', 'New database created.')
            self._databases = self.load_databases()

    def start_db_clicked(self):
        if not self._databases:
            QMessageBox.warning(self, 'Error', 'No existing databases found.')
            return

        db_name, ok = QInputDialog.getItem(self, 'Select Database', 'Choose a database:', self._databases, 0, False)
        if ok and db_name:
            self.current_db = db_name
            self.passwords = self.load_passwords()
            self.show_db_menu()

    def load_passwords(self):
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
        with open(os.path.join(self.db_folder, self.current_db), 'w') as file:
            for label, (username, password, note) in self.passwords.items():
                file.write(f'{username}:{password}:{label}:{note}\n')

    def show_db_menu(self):
        db_menu = DatabaseMenu(self.current_db, self.passwords)
        db_menu.exec()
