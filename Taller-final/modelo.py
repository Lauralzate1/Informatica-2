import json


class Model:
    def __init__(self, data_file='data.json'):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {'pacientes': []}
            self.save_data()

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def authenticate(self, username, password):
        return username == 'admin123' and password == 'contrasena123'

    def add_paciente(self, paciente):
        if any(p['id'] == paciente['id'] for p in self.data['pacientes']):
            return False
        self.data['pacientes'].append(paciente)
        self.save_data()
        return True

    def delete_paciente(self, patient_id):
        self.data['pacientes'] = [
            p for p in self.data['pacientes'] if p['id'] != patient_id]
        self.save_data()

    def search_pacientes(self, name_prefix):
        name_prefix = name_prefix.lower()
        return [p for p in self.data['pacientes'] if p['nombre'].lower().startswith(name_prefix)]
