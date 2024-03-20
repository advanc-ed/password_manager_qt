import os
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QMessageBox, QInputDialog
from dialogs.CustomDialog import PasswordEntryDialog


class DatabaseMenu(QDialog):
    def __init__(self, db_name, passwords):
        super().__init__()

        self.db_name = db_name
        self.passwords = passwords

        self.setWindowTitle(f'Password Manager | {db_name}')
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        label = QLabel('Main Menu')
        layout.addWidget(label)

        show_button = QPushButton('Show existing passwords')
        show_button.clicked.connect(self.show_passwords)
        layout.addWidget(show_button)

        add_button = QPushButton('Add new password')
        add_button.clicked.connect(self.add_password)
        layout.addWidget(add_button)

        delete_button = QPushButton('Delete an existing password')
        delete_button.clicked.connect(self.delete_password)
        layout.addWidget(delete_button)

        update_button = QPushButton('Update an existing password')
        update_button.clicked.connect(self.update_password)
        layout.addWidget(update_button)

        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.setLayout(layout)

    def show_passwords(self):
        if not self.passwords:
            QMessageBox.information(self, 'Info', 'No passwords stored in this database.')
            return

        password_labels = list(self.passwords.keys())
        selected_label, ok = QInputDialog.getItem(self, 'Select Password', 'Choose a password label:', password_labels,
                                                  0, False)
        if ok and selected_label:
            username, password, note = self.passwords[selected_label]
            QMessageBox.information(self, 'Stored Password',
                                    f'Label: {selected_label}\n' +
                                    f'Username: {username}\n' +
                                    f'Password: {password}\n' +
                                    f'Note: {note}')

    def read_password_from_user(self):
        dialog = PasswordEntryDialog(self)
        if dialog.exec():
            return dialog.get_data()

        return None

    def add_password(self):
        username, password, label, note = self.read_password_from_user()
        if username and password and label and note:
            self.passwords[label] = (username, password, note)
            self.save_passwords()
            QMessageBox.information(self, 'Success', 'Password added.')

    def delete_password(self):
        if not self.passwords:
            QMessageBox.information(self, 'Info', 'No passwords stored in this database.')
            return

        password_labels = list(self.passwords.keys())
        selected_label, ok = QInputDialog.getItem(self, 'Delete Password', 'Choose a password label to delete:',
                                                  password_labels, 0, False)
        if ok and selected_label:
            del self.passwords[selected_label]
            self.save_passwords()
            QMessageBox.information(self, 'Success', 'Password deleted.')

    def update_password(self):
        if not self.passwords:
            QMessageBox.information(self, 'Info', 'No passwords stored in this database.')
            return

        password_labels = list(self.passwords.keys())
        selected_label, ok = QInputDialog.getItem(self, 'Update Password', 'Choose a password label to update:',
                                                  password_labels, 0, False)
        if ok and selected_label:
            username, password, label, note = self.read_password_from_user()
            if username and password and label and note:
                self.passwords.pop(selected_label)
                self.passwords[label] = (username, password, note)
                self.save_passwords()
                QMessageBox.information(self, 'Success', 'Password updated.')

    def save_passwords(self):
        with open(os.path.join('db', self.db_name), 'w') as file:
            for label, (username, password, note) in self.passwords.items():
                file.write(f'{username}:{password}:{label}:{note}\n')
