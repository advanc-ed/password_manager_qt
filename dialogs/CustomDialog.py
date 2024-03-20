from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QPushButton


class PasswordEntryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Password Entry Dialog')
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        self.username_label = QLabel('Username:')
        self.username_edit = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)

        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)

        self.label_label = QLabel('Label:')
        self.label_edit = QLineEdit()
        layout.addWidget(self.label_label)
        layout.addWidget(self.label_edit)

        self.note_label = QLabel('Note:')
        self.note_edit = QLineEdit()
        layout.addWidget(self.note_label)
        layout.addWidget(self.note_edit)

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
        return self.username_edit.text(), self.password_edit.text(), self.label_edit.text(), self.note_edit.text()

