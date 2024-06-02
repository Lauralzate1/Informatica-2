from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton
from modelo import Model
from vista import LoginView, MainView


class Controller:
    def __init__(self):
        self.model = Model()
        self.login_view = LoginView()
        self.main_view = MainView()

        self.login_view.login_button.clicked.connect(self.handle_login)
        self.main_view.add_button.clicked.connect(self.handle_add_paciente)
        self.main_view.search_button.clicked.connect(self.handle_search)

        self.main_view.logout_button.clicked.connect(self.handle_logout)

    def show_login(self):
        self.login_view.show()

    def handle_login(self):
        username = self.login_view.user_input.text()
        password = self.login_view.pass_input.text()
        if self.model.authenticate(username, password):
            self.login_view.close()
            self.main_view.show()
        else:
            self.login_view.show_error('Usuario o contraseña incorrectos')

    def handle_logout(self):
        self.main_view.close()
        self.show_login()

    def handle_add_paciente(self):
        paciente = {
            'nombre': self.main_view.nombre_input.text(),
            'apellido': self.main_view.apellido_input.text(),
            'edad': self.main_view.edad_input.text(),
            'id': self.main_view.id_input.text()
        }
        if self.model.add_paciente(paciente):
            self.main_view.show_message('Paciente agregado exitosamente')
        else:
            self.main_view.show_error('La identificación ya existe')

    def handle_search(self):
        name_prefix = self.main_view.search_input.text()
        pacientes = self.model.search_pacientes(name_prefix)
        self.main_view.table.setRowCount(len(pacientes))
        for row, paciente in enumerate(pacientes):
            self.main_view.table.setItem(
                row, 0, QTableWidgetItem(paciente['id']))
            self.main_view.table.setItem(
                row, 1, QTableWidgetItem(paciente['nombre']))
            self.main_view.table.setItem(
                row, 2, QTableWidgetItem(paciente['apellido']))
            self.main_view.table.setItem(
                row, 3, QTableWidgetItem(paciente['edad']))

            delete_button = QPushButton('Eliminar')
            delete_button.clicked.connect(
                lambda _, pid=paciente['id']: self.handle_delete(pid))
            self.main_view.table.setCellWidget(row, 4, delete_button)

    def handle_delete(self, paciente_id):
        self.model.delete_paciente(paciente_id)
        self.handle_search()
