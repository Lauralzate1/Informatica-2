from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)


class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.user_label = QLabel('Usuario:')
        self.user_input = QLineEdit()
        self.pass_label = QLabel('Contraseña:')
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Log In')

        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)


class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.add_paciente_layout = QHBoxLayout()

        self.nombre_label = QLabel('Nombre:')
        self.nombre_input = QLineEdit()
        self.apellido_label = QLabel('Apellido:')
        self.apellido_input = QLineEdit()
        self.edad_label = QLabel('Edad:')
        self.edad_input = QLineEdit()
        self.id_label = QLabel('Identificación:')
        self.id_input = QLineEdit()

        self.add_button = QPushButton('Agregar Paciente')
        self.logout_button = QPushButton('Log Out')

        self.add_paciente_layout.addWidget(self.nombre_label)
        self.add_paciente_layout.addWidget(self.nombre_input)
        self.add_paciente_layout.addWidget(self.apellido_label)
        self.add_paciente_layout.addWidget(self.apellido_input)
        self.add_paciente_layout.addWidget(self.edad_label)
        self.add_paciente_layout.addWidget(self.edad_input)
        self.add_paciente_layout.addWidget(self.id_label)
        self.add_paciente_layout.addWidget(self.id_input)
        self.add_paciente_layout.addWidget(self.add_button)
        self.add_paciente_layout.addWidget(self.logout_button)

        self.search_layout = QHBoxLayout()

        self.search_label = QLabel('Buscar:')
        self.search_input = QLineEdit()
        self.search_button = QPushButton('Buscar')

        self.search_layout.addWidget(self.search_label)
        self.search_layout.addWidget(self.search_input)
        self.search_layout.addWidget(self.search_button)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ['ID', 'Nombre', 'Apellido', 'Edad', 'Acciones'])

        layout.addLayout(self.add_paciente_layout)
        layout.addLayout(self.search_layout)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', message)

    def show_message(self, message):
        QMessageBox.information(self, 'Información', message)
