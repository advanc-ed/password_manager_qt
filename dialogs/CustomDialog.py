from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QPushButton

class PasswordEntryDialog(QDialog):
    """Dialog for entering a new password."""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Password Entry Dialog')
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        # Username input
        self.username_label = QLabel('Username:')
        self.username_edit = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)

        # Password input
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)

        # Label input
        self.label_label = QLabel('Label:')
        self.label_edit = QLineEdit()
        layout.addWidget(self.label_label)
        layout.addWidget(self.label_edit)

        # Note input
        self.note_label = QLabel('Note:')
        self.note_edit = QLineEdit()
        layout.addWidget(self.note_label)
        layout.addWidget(self.note_edit)

        # Buttons layout
        button_layout = QHBoxLayout()
        add_button = QPushButton('Add')
        add_button.clicked.connect(self.accept)
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(add_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_data(self):
        """Get entered password data."""
        return self.username_edit.text(), self.password_edit.text(), self.label_edit.text(), self.note_edit.text()
